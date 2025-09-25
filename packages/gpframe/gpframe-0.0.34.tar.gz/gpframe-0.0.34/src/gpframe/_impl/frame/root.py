from __future__ import annotations

from dataclasses import dataclass

import inspect
import logging

from typing import Callable
from contextlib import contextmanager

from gpframe.contracts.protocols import gproot, frame, routine

from gpframe.exceptions import FrameAlreadyStartedError

from gpframe._impl.routine.base import IntraProcessRoutineExecution
from gpframe._impl.routine.asynchronous import AsyncRoutine
from gpframe._impl.routine.synchronous import SyncRoutine

from gpframe._impl.frame.frame_base import (
    _FrameBaseState,
)

from gpframe._impl.frame.root_base import (
    _RootFrameBaseRole,
    _RootFrameBaseState,
    create_root_frame_base_role
)

from gpframe._impl.frame.sub import _SubFrameRole, create_sub_frame_role
from gpframe._impl.frame.sub_ipc import _IPCSubFrameRole, create_ipc_sub_frame_role

from gpframe._impl.context import create_root_event_context, create_root_routine_context

from gpframe._impl.frame.future import FrameFutureImpl, run_circuit_in_thread, wrap_to_interface

@dataclass(slots = True)
class _RootFrameState:
    logger: logging.Logger

    event_context: gproot.event.Context
    routine_context: gproot.routine.Context

    routine_execution: IntraProcessRoutineExecution

    sub_frames: dict[str, tuple[frame.SubFrame, _SubFrameRole | _IPCSubFrameRole]]

    started_frame_futures: list[FrameFutureImpl]

@dataclass(slots = True)
class _RootFrameRole:
    root_frame_base_role: _RootFrameBaseRole
    state: _RootFrameState
    updater: _RootFrameUpdater
    interface_type: type[frame.RootFrame]


class _RootFrameUpdater:
    def create_state(
            self,
            logger: logging.Logger,
            routine: Callable,
            frame_base_state: _FrameBaseState,
            root_frame_base_state: _RootFrameBaseState
        ) -> _RootFrameState:
        
        sub_frames = {}
        started_frame_futures: list[FrameFutureImpl] = []

        def start_sub_frame(frame_name: str) -> FrameFutureImpl:
            # Sub-frames are started via ctx.start_sub_frame, so they cannot be started
            # before the main frame itself has been started.
            def fn():
                sub_frame_role = sub_frames[frame_name][1]
                if any(frame_name == fut.frame_name for fut in started_frame_futures):
                    raise FrameAlreadyStartedError(
                        f"The sub frame named '{frame_name}' is already started."
                    )
                frame_future = sub_frame_role.start_fn()
                started_frame_futures.append(frame_future)
                return frame_future
            return frame_base_state.phase_role.interface.on_started(fn)
        
        event_context = create_root_event_context(
            frame_base_state.frame_name,
            logger,
            root_frame_base_state.environment_message,
            root_frame_base_state.request_message,
            frame_base_state.event_message,
            frame_base_state.routine_message,
            frame_base_state.routine_result,
            root_frame_base_state.inter_frame_message,
            root_frame_base_state.ipc_message,
            start_sub_frame,
        )

        routine_context = create_root_routine_context(
            frame_base_state.frame_name,
            logger,
            root_frame_base_state.environment_message,
            root_frame_base_state.request_message,
            frame_base_state.event_message,
            frame_base_state.routine_message,
            frame_base_state.routine_result,
            root_frame_base_state.inter_frame_message,
            root_frame_base_state.ipc_message,
            start_sub_frame
        )

        if inspect.iscoroutinefunction(routine):
            routine_execution = AsyncRoutine(frame_base_state.intra_frame_lock)
        else:
            routine_execution = SyncRoutine(frame_base_state.intra_frame_lock)

        return _RootFrameState(
            logger,
            event_context,
            routine_context,
            routine_execution,
            sub_frames,
            started_frame_futures
        )

def create_root_frame_role(frame_name: str, routine: routine.Root, *, logger: logging.Logger):
    root_frame_base_role = create_root_frame_base_role(frame_name, logger)
    
    frame_base_state = root_frame_base_role.frame_base_role.state
    root_base_state = root_frame_base_role.state

    updater = _RootFrameUpdater()

    state = updater.create_state(logger, routine, frame_base_state, root_base_state)

    class _Interface(frame.RootFrame, root_frame_base_role.interface_type):

        def create_sub_frame(self, frame_name: str, routine: routine.Sub) -> frame.SubFrame:
            def fn():
                sub_frame_role = create_sub_frame_role(
                    frame_name,
                    logger,
                    routine,
                    root_base_state.environment_message,
                    root_base_state.request_message,
                    root_base_state.inter_frame_message,
                    root_base_state.ipc_message
                    )
                sub_frame = sub_frame_role.interface_type()
                state.sub_frames[frame_name] = (sub_frame, sub_frame_role)
                return sub_frame
            return frame_base_state.phase_role.interface.on_load(fn)

        def create_ipc_sub_frame(self, frame_name: str, routine: routine.ipc.Sub) -> frame.SubFrame:
            def fn():
                ipc_sub_frame_role = create_ipc_sub_frame_role(
                    frame_base_state.frame_name,
                    logger,
                    routine,
                    root_base_state.ml_sync_manager,
                    root_base_state.environment_message,
                    root_base_state.request_message,
                    root_base_state.inter_frame_message,
                    root_base_state.ipc_message,
                    )
                sub_frame = ipc_sub_frame_role.interface_type()
                state.sub_frames[frame_name] = (sub_frame, ipc_sub_frame_role)
                return sub_frame
            return frame_base_state.phase_role.interface.on_load(fn)
        
        def stop_routine(self) -> None:
            state.routine_execution.request_stop_routine()
        
        @contextmanager
        def start(self):
            def wait_targets_getter():
                def fn():
                    return tuple(state.started_frame_futures)
                return frame_base_state.phase_role.interface.on_terminated(fn)
            
            def fn():
                frame_future = run_circuit_in_thread(
                    frame_base_state,
                    state.event_context,
                    state.routine_context,
                    state.routine_execution,
                    routine,
                    wait_targets_getter
                )
                return wrap_to_interface(frame_future)
            try:
                yield frame_base_state.phase_role.interface.to_started(fn)
            finally:
                root_frame_base_role.cleanup_fn()
        
    return _RootFrameRole(
        root_frame_base_role = root_frame_base_role,
        state = state,
        updater = updater,
        interface_type = _Interface
    )


def create_frame(frame_name: str, routine: routine.Root, *, logger: logging.Logger | None = None) -> frame.RootFrame:
    logger = logger if logger else logging.getLogger("gpframe")
    role = create_root_frame_role(frame_name, routine, logger = logger)
    return role.interface_type()

