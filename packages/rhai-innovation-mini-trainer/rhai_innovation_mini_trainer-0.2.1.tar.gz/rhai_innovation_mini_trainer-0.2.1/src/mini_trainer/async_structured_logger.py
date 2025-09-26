# SPDX-License-Identifier: Apache-2.0

# Standard
from datetime import datetime
import asyncio
import json
import threading
import torch.distributed as dist

# Third Party
import aiofiles

# Local imports
from mini_trainer import wandb_wrapper
from mini_trainer.wandb_wrapper import check_wandb_available



class AsyncStructuredLogger:
    def __init__(self, file_name="training_log.jsonl", use_wandb=False):
        self.file_name = file_name
        
        # wandb init is a special case -- if it is requested but unavailable,
        # we should error out early
        if use_wandb:
            check_wandb_available("initialize wandb")
        self.use_wandb = use_wandb

        self.logs = []
        self.loop = asyncio.new_event_loop()
        t = threading.Thread(
            target=self._run_event_loop, args=(self.loop,), daemon=True
        )
        t.start()
        asyncio.run_coroutine_threadsafe(self._initialize_log_file(), self.loop)

    def _run_event_loop(self, loop):
        asyncio.set_event_loop(loop)  #
        loop.run_forever()

    async def _initialize_log_file(self):
        self.logs = []
        try:
            async with aiofiles.open(self.file_name, "r") as f:
                async for line in f:
                    if line.strip():  # Avoid empty lines
                        self.logs.append(json.loads(line.strip()))
        except FileNotFoundError:
            # File does not exist but the first log will create it.
            pass

    async def log(self, data):
        """logs a dictionary as a new line in a jsonl file with a timestamp"""
        try:
            if not isinstance(data, dict):
                raise ValueError("Logged data must be a dictionary")
            data["timestamp"] = datetime.now().isoformat()
            self.logs.append(data)
            await self._write_logs_to_file(data)
            
            # log to wandb if enabled and wandb is initialized, but only log this on the MAIN rank
            # wandb already handles timestamps so no need to include
            if self.use_wandb and dist.get_rank() == 0:
                wandb_data = {k: v for k, v in data.items() if k != "timestamp"}
                wandb_wrapper.log(wandb_data)
            
            print(f"\033[92m{json.dumps(data, indent=4)}\033[0m")
        except Exception as e:
            print(f"\033[1;38;2;0;255;255mError logging data: {e}\033[0m")

    async def _write_logs_to_file(self, data):
        """appends to the log instead of writing the whole log each time"""
        async with aiofiles.open(self.file_name, "a") as f:
            await f.write(json.dumps(data, indent=None) + "\n")

    def log_sync(self, data: dict):
        """runs the log coroutine non-blocking"""
        asyncio.run_coroutine_threadsafe(self.log(data), self.loop)

    def __repr__(self):
        return f"<AsyncStructuredLogger(file_name={self.file_name})>"
