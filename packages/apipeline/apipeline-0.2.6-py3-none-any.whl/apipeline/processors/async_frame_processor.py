#
# Copyright (c) 2024, Daily
#
# SPDX-License-Identifier: BSD 2-Clause License
#

import logging
import asyncio

from apipeline.frames.sys_frames import Frame, StartInterruptionFrame
from apipeline.frames.control_frames import EndFrame
from apipeline.processors.frame_processor import FrameDirection, FrameProcessor


class AsyncFrameProcessor(FrameProcessor):
    def __init__(
        self, *, name: str | None = None, loop: asyncio.AbstractEventLoop | None = None, **kwargs
    ):
        super().__init__(name=name, loop=loop, **kwargs)

        self._push_frame_task = None
        # Create push frame task. This is the task that will push frames in
        # order. We also guarantee that all frames are pushed in the same task.
        self._create_push_task()

    async def process_frame(self, frame: Frame, direction: FrameDirection):
        await super().process_frame(frame, direction)

        if isinstance(frame, StartInterruptionFrame):
            await self._handle_interruptions(frame)

    async def cleanup(self):
        if self._push_frame_task:
            self._push_frame_task.cancel()
            await self._push_frame_task

    #
    # Handle interruptions
    #
    async def _handle_interruptions(self, frame: Frame):
        # Cancel the task. This will stop pushing frames downstream.
        self._push_frame_task.cancel()
        await self._push_frame_task
        self._push_frame_task = None
        # Push an out-of-band frame (i.e. not using the ordered push
        # frame task).
        await self.push_frame(frame)
        # Create a new queue and task.
        self._create_push_task()

    #
    # Push frames task
    #

    def _create_push_task(self):
        """
        NOTE: all async frame processors must have create a new queue and task, don't to check task is None
        """
        # logging.debug(f"{self} create push task {self._push_frame_task}")
        self._push_queue = asyncio.Queue()
        self._push_frame_task = self.get_event_loop().create_task(self._push_frame_task_handler())

    async def queue_frame(
        self, frame: Frame, direction: FrameDirection = FrameDirection.DOWNSTREAM
    ):
        await self._push_queue.put((frame, direction))

    async def _push_frame_task_handler(self):
        running = True
        while running:
            try:
                (frame, direction) = await asyncio.wait_for(self._push_queue.get(), timeout=1)
                await self.push_frame(frame, direction)
                running = not isinstance(frame, EndFrame)
            except asyncio.TimeoutError:
                pass
            except asyncio.CancelledError:
                logging.info(f"{self.name} _push_frame_task_handle cancelled")
                break
            except Exception as ex:
                logging.exception(f"{self.name} Unexpected error in _push_frame_task_handler: {ex}")
                if self.get_event_loop().is_closed():
                    logging.warning(f"{self.name} event loop is closed")
                    break
