import json
import threading
import uuid
from typing import TYPE_CHECKING, Any, Optional

import pydantic

from mindtrace.jobs.base.orchestrator_backend import OrchestratorBackend
from mindtrace.jobs.local.consumer_backend import LocalConsumerBackend
from mindtrace.jobs.local.fifo_queue import LocalQueue
from mindtrace.jobs.local.priority_queue import LocalPriorityQueue
from mindtrace.jobs.local.stack import LocalStack
from mindtrace.jobs.utils.checks import ifnone

if TYPE_CHECKING:  # pragma: no cover
    from mindtrace.jobs.consumers.consumer import Consumer


class LocalClient(OrchestratorBackend):
    """A pure-python in-memory message broker.
    This client subclasses BrokerClientBase and supports multiple unique instances based on the provided 'broker_id'
    parameter. It maintains a shared (in-memory) dictionary of declared queues and a store for job results.
    """

    def __init__(self, broker_id: str | None = None):
        super().__init__()
        self.broker_id = ifnone(broker_id, default="mtrix.default_broker")
        self.queues: dict[str, Any] = {}
        self._lock = threading.Lock()
        self._job_results: dict[str, Any] = {}

    @property
    def consumer_backend_args(self):
        raise NotImplementedError("LocalConsumerBackend needs to be created with access to a LocalClient instance.")

    def create_consumer_backend(self, consumer_frontend: "Consumer", queue_name: str) -> LocalConsumerBackend:
        return LocalConsumerBackend(queue_name, consumer_frontend, self)

    def declare_queue(self, queue_name: str, queue_type: str = "fifo", **kwargs) -> dict[str, str]:
        """Declare a queue of type 'fifo', 'stack', or 'priority'."""
        with self._lock:
            if queue_name in self.queues:
                return {
                    "status": "success",
                    "message": f"Queue '{queue_name}' already exists.",
                }
            if queue_type.lower() == "fifo":
                instance = LocalQueue()
            elif queue_type.lower() == "stack":
                instance = LocalStack()
            elif queue_type.lower() == "priority":
                instance = LocalPriorityQueue()
            else:
                raise TypeError(f"Unknown queue type '{queue_type}'.")
            self.queues[queue_name] = instance
            return {
                "status": "success",
                "message": f"Queue '{queue_name}' declared successfully.",
            }

    def delete_queue(self, queue_name: str, **kwargs):
        with self._lock:
            if queue_name not in self.queues:
                raise KeyError(f"Queue '{queue_name}' not found.")
            del self.queues[queue_name]
            return {
                "status": "success",
                "message": f"Queue '{queue_name}' deleted successfully.",
            }

    def publish(self, queue_name: str, message: pydantic.BaseModel, **kwargs):
        """Publish a message (as a pydantic model) to the specified queue.
        If the target queue is a priority queue, accepts an extra 'priority' parameter.
        """
        priority = kwargs.get("priority", 0)
        with self._lock:
            if queue_name not in self.queues:
                raise KeyError(f"Queue '{queue_name}' not found.")
            queue_instance = self.queues[queue_name]
        message_dict = message.model_dump()
        if "job_id" not in message_dict or message_dict["job_id"] is None:
            message_dict["job_id"] = str(uuid.uuid1())
        body = json.dumps(message_dict)
        if type(queue_instance).__name__ == "LocalPriorityQueue" and priority is not None:
            queue_instance.push(item=body, priority=priority)
        else:
            queue_instance.push(item=body)
        return message_dict["job_id"]

    def receive_message(self, queue_name: str, **kwargs) -> Optional[dict]:
        """Retrieve a message from the specified queue.
        Returns the message as a dict.
        Returns None if queue is empty.
        """
        block = kwargs.get("block", True)
        timeout = kwargs.get("timeout", None)
        with self._lock:
            if queue_name not in self.queues:
                raise KeyError(f"Queue '{queue_name}' not found.")
            queue_instance = self.queues[queue_name]
        try:
            raw_message = queue_instance.pop(block=block, timeout=timeout)
            if raw_message is None:
                return None
            message_dict = json.loads(raw_message)
            return message_dict
        except Exception:
            return None

    def clean_queue(self, queue_name: str, **kwargs) -> dict[str, str]:
        """Remove all messages from the specified queue."""
        with self._lock:
            if queue_name not in self.queues:
                raise KeyError(f"Queue '{queue_name}' not found.")
            queue_instance = self.queues[queue_name]
        queue_instance.clean()
        return {"status": "success", "message": f"Cleaned queue '{queue_name}'."}

    def count_queue_messages(self, queue_name: str, **kwargs) -> int:
        """Return the number of messages in the specified queue."""
        with self._lock:
            if queue_name not in self.queues:
                raise KeyError(f"Queue '{queue_name}' not found.")
            queue_instance = self.queues[queue_name]
        return queue_instance.qsize()

    def store_job_result(self, job_id: str, result: Any) -> dict[str, Any]:
        """Save the job result (JSON-serializable) keyed by job_id."""
        with self._lock:
            self._job_results[job_id] = result
        return {"status": "success", "message": f"Stored result for job_id: {job_id}."}

    def get_job_result(self, job_id: str) -> Any:
        """Retrieve the stored result for the given job_id."""
        with self._lock:
            return self._job_results.get(job_id, None)

    def move_to_dlq(
        self,
        source_queue: str,
        dlq_name: str,
        message: pydantic.BaseModel,
        error_details: str,
        **kwargs,
    ):
        """Move a failed message to a dead letter queue"""
        pass
