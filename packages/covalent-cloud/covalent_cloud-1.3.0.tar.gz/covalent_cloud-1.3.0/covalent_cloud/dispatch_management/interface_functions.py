# Copyright 2023 Agnostiq Inc.

"""Module for Covalent Cloud dispatching and related functionalities."""


from copy import deepcopy
from functools import wraps
from typing import Any, Callable, Dict, List, Optional, Union

import covalent as ct
from covalent._results_manager.result import Result
from covalent._workflow.lattice import Lattice

from covalent_cloud.function_serve.service_class import FunctionService
from covalent_cloud.service_account_interface.client import get_client
from covalent_cloud.shared.classes.exceptions import handle_error
from covalent_cloud.shared.schemas.volume import Volume

from ..shared.classes.settings import Settings, settings
from . import results_manager as rm
from .dispatch_info import DispatchInfo
from .helpers import (
    add_dispatch_info,
    fast_redispatch,
    register,
    start,
    track_redispatch,
    validate_executors,
)

API_KEY = "fake"  # pragma: allowlist secret


def cancel(
    dispatch_id: str,
    task_ids: Optional[Union[int, List[int]]] = None,
    settings: Settings = settings,
) -> None:
    """Cancel a running dispatch.

    Args:
        dispatch_id: The dispatch id of the dispatch to be cancelled.
        task_ids: Optional list of task ids to cancel. All tasks are cancelled if not provided.
        settings: The settings object to use. If None, the default settings will be used.

    """
    task_ids = [task_ids] if isinstance(task_ids, int) else (task_ids or [])
    api_client = get_client(settings=settings)
    try:
        response = api_client.put(
            f"api/v2/lattices/{dispatch_id}/cancel",
            request_options={"params": {"task_ids": task_ids}},
        )
        print(response.json().get("message"))
    except Exception as e:
        print(f"Error cancelling dispatch {dispatch_id}:\n{e}")


def dispatch(
    orig_lattice: Lattice,
    settings: Settings = settings,
    volume: Union[Volume, None] = None,
    disable_run: bool = False,
    dispatch_info: Union[DispatchInfo, Dict[str, Any], None] = None,
    tags: Union[List[str], None] = None,
) -> Callable:
    """
    Dispatches a Covalent workflow to the Covalent Cloud and returns the assigned dispatch ID.
    The dispatch function takes a Covalent workflow, also called a lattice, and sends it to the Covalent Cloud Server for execution. Once dispatched, the workflow runs on a the cloud and can be monitored using the dispatch ID in the application. The dispatch function returns a wrapper function that takes the inputs of the workflow as arguments. This wrapper function can be called to execute the workflow.

    Args:
        orig_lattice: The Covalent workflow to send to the cloud.
        settings: The settings object to use. If None, the default settings will be used.
        volume: [optional] Volume instance
        dispatch_info: [optional] DispatchInfo object to attach to a workflow - this will take priority over `tags` and other `DispatchInfo` parameters if both are provided.
        tags: [optional] List of tags to attach to a workflow - will be converted to a DispatchInfo object.

    Returns:
        A wrapper function which takes the inputs of the workflow as arguments.

    Examples:

        .. highlight:: python
        .. code-block:: python

            # define a simple lattice
            import covalent_cloud as cc
            import covalent as ct

            # create volume [optional]
            volume = cc.volume("/myvolume")

            @ct.lattice
            def my_lattice(a: int, b: int) -> int:
                return a + b

            # dispatch the lattice and get the assigned dispatch ID
            dispatch_id = cc.dispatch(my_lattice, volume=volume)(2, 3)
    """

    if isinstance(orig_lattice, FunctionService):
        raise TypeError(
            "Function services cannot be dispatched. Please use `cc.deploy()` instead."
        )

    @wraps(orig_lattice)
    def wrapper(*args, **kwargs) -> str:
        """
        Send the lattice to the dispatcher server and return
        the assigned dispatch id.

        Args:
            *args: The inputs of the workflow.
            **kwargs: The keyword arguments of the workflow.

        Returns:
            The dispatch id of the workflow.

        """

        try:

            lattice = deepcopy(orig_lattice)

            # Enabling task_packing for the build_graph call as it isn't
            # supported yet by OS covalent.
            old_task_packing = ct.get_config("sdk.task_packing")
            ct.set_config("sdk.task_packing", "true")
            lattice.build_graph(*args, **kwargs)
            ct.set_config("sdk.task_packing", old_task_packing)

            # Check that only CloudExecutors are specified.
            if settings.validate_executors and not validate_executors(lattice):
                raise ValueError("One or more electrons have invalid executors.")

            # TODO: Update register endpoint to take volume_id as a param and associate EFS to job_def
            dispatch_id = register(lattice, volume=volume, settings=settings)(*args, **kwargs)

            # The dispatch id is ALSO returned by the start function - both the register and the start function's dispatch_ids are the same
            if not disable_run:
                dispatch_id = start(dispatch_id, settings)
            else:
                return dispatch_id

            # Making sure the dispatch_info is the one received from the parent function
            nonlocal dispatch_info

            # The `DispatchInfo` object takes priority over `tags` and other `DispatchInfo` parameters if both are provided.
            if dispatch_info:
                if isinstance(dispatch_info, dict):
                    dispatch_info = DispatchInfo(**dispatch_info)
                add_dispatch_info(dispatch_id, dispatch_info, settings)
            elif tags:
                add_dispatch_info(dispatch_id, DispatchInfo(tags=tags), settings)

            return dispatch_id

        except Exception as e:
            handle_error(e)

    return wrapper


def redispatch(
    dispatch_id: str,
    rebuild: bool = False,
    settings: Settings = settings,
) -> Callable[..., str]:
    """
    Re-dispatches a Covalent workflow to the Covalent Cloud and returns the assigned dispatch ID.

    Args:
        dispatch_id: The dispatch ID of the workflow to re-dispatch.
        rebuild: Whether to rebuild the workflow locally before re-dispatching. Defaults to False.
        settings: The settings object to use. If None, the default settings will be used.

    Returns:
        Callable redispatch workflow function.

    Examples:

    .. highlight:: python
    .. code-block:: python

        import time
        import covalent as ct
        import covalent_cloud as cc

        cc.save_api_key("your-api-key")

        default_exec = cc.CloudExecutor()

        @ct.electron(executor=default_exec)
        def add(a: int, b: int) -> int:
            return a + b

        @ct.lattice(executor=default_exec, workflow_executor=default_exec)
        def my_lattice(a: int, b: int) -> int:
            return add(a, b)

        # dispatch the lattice and get the assigned dispatch ID
        dispatch_id_0 = cc.dispatch(my_lattice)(2, 3)
        # wait for the result...
        result_0 = cc.get_result(dispatch_id_0, wait=True)

        # re-dispatch the lattice with new inputs without rebuilding locally
        redispatch_id_1 = cc.redispatch(dispatch_id_0)([3, 4], {})
        time.sleep(60) # wait for the new dispatch to register and start
        # wait for the new result...
        result_1 = cc.get_result(redispatch_id_1, wait=True)

        # re-dispatch the lattice with new inputs, rebuilding locally
        redispatch_id_2 = cc.redispatch(dispatch_id_0, rebuild=True)([5, 6], {})
        # wait for another new result...
        result_2 = cc.get_result(redispatch_id_2, wait=True)

    """

    def func(*input_args: Any, **input_kwargs: Any) -> str:
        """Redispatch workflow function.

        Args:
            input_args: The positional arguments of the workflow.
            input_kwargs: The keyword arguments of the workflow.

        Returns:
            The dispatch ID of the re-dispatched workflow.

        """
        message = ""
        if rebuild:
            response = rebuild_redispatch(dispatch_id, input_args, input_kwargs, settings)
            redispatch_id = response
            message = f"Rebuilt and re-dispatched workflow, original dispatch_id: {dispatch_id}, new dispatch_id: {redispatch_id}"
        else:
            response = fast_redispatch(dispatch_id, input_args, input_kwargs, settings)
            redispatch_id = response
            message = f"Re-dispatched workflow, original dispatch_id: {dispatch_id}, new dispatch_id: {redispatch_id}"

        print(message)
        return redispatch_id

    return func


def get_result(
    dispatch_id: str,
    wait: bool = False,
    settings: Settings = settings,
    *,
    status_only: bool = False,
) -> Result:
    """
    Gets the result of a Covalent workflow that has been dispatched to the cloud.

    This function retrieves the result of a dispatched Covalent workflow that has been executed on the cloud. The function takes the dispatch ID of the workflow and retrieves the results from the cloud. The result is returned as a `Result` object that contains the status of the workflow, the final result of the lattice, and any error messages that may have occurred during execution.

    Args:
        dispatch_id: The dispatch ID assigned to the workflow.
        wait: Controls how long the function waits for the server to return a result. If False, the function will not wait and will return the current status of the workflow. If True, the function will wait for the result to finish and keep retrying until the result is available.
        status_only: If True, only retrieves the status of the workflow and not the full result.
        settings: The Covalent settings to use for the request.

    Returns:
        A `Result` object that contains the status of the workflow, the final result of the lattice, and any error messages that may have occurred during execution.

    Examples:

        .. highlight:: python
        .. code-block:: python

            # define a simple lattice
            import covalent_cloud as cc
            import covalent as ct

            @ct.lattice
            def my_lattice(a: int, b: int) -> int:
                return a + b

            # dispatch the lattice and get the assigned dispatch ID
            dispatch_id = cc.dispatch(my_lattice)(2, 3)

            # get the result of the dispatched lattice
            result = cc.get_result(dispatch_id, wait=True)

            # print the final result of the lattice
            print(result.result)
    """

    return rm.get_result(
        dispatch_id=dispatch_id,
        wait=wait,
        settings=settings,
        status_only=status_only,
    )


def rebuild_redispatch(
    dispatch_id: str,
    input_args: list,
    input_kwargs: dict,
    settings: Settings = settings,
) -> Callable:
    """
    Re-dispatches a Covalent workflow to the Covalent Cloud and returns the assigned dispatch ID.

    Args:
        dispatch_id: The dispatch ID of the workflow to re-dispatch.
        input_args: The positional arguments of the workflow.
        input_kwargs: The keyword arguments of the workflow.
        settings: The settings object to use. If None, the default settings will be used.

    Returns:
        The dispatch ID of the re-dispatched workflow.

    """

    try:
        # loading original dispatch
        original_dispatch = get_result(dispatch_id, wait=True, settings=settings)
        original_dispatch.result.load()

        # load lattice
        original_dispatch.lattice.workflow_function.load()
        original_dispatch.lattice.metadata["hooks"].load()

        # build lattice
        redispatch_lattice = ct.lattice(original_dispatch.lattice.workflow_function.value)
        redispatch_lattice.metadata = original_dispatch.lattice.metadata.copy()
        redispatch_lattice.metadata["hooks"] = original_dispatch.lattice.metadata[
            "hooks"
        ].value.copy()

        redispatch_id = dispatch(redispatch_lattice, settings=settings)(
            *input_args, **input_kwargs
        )

        # Update redispatch with original dispatch id
        update_response = track_redispatch(redispatch_id, dispatch_id, settings)
        if (
            update_response["dispatch_id"] != redispatch_id
            or update_response["original_dispatch_id"] != dispatch_id
        ):
            raise Exception(
                f"Failed to update redispatch: {redispatch_id} with original dispatch id: {dispatch_id}"
            )

    except Exception as e:
        raise e

    return redispatch_id
