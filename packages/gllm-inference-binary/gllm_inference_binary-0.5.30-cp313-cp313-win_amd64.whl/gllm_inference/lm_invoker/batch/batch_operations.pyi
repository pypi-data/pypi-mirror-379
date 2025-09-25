from gllm_inference.schema import BatchStatus as BatchStatus, LMOutput as LMOutput, Message as Message, MessageContent as MessageContent
from typing import Any

class BatchOperations:
    """Handles batch operations for an LM invoker.

    This class provides a wrapper around the batch operations of an LM invoker.
    It provides a simple interface for creating, retrieving, and canceling batch jobs.

    This enables LM invokers to support the following batch operations:

        Create a batch job:
        >>> batch_id = await lm_invoker.batch.create(...)

        Get the status of a batch job:
        >>> status = await lm_invoker.batch.status(batch_id)

        Retrieve the results of a batch job:
        >>> results = await lm_invoker.batch.retrieve(batch_id)

        List the batch jobs:
        >>> batch_jobs = await lm_invoker.batch.list()

        Cancel a batch job:
        >>> await lm_invoker.batch.cancel(batch_id)
    """
    def __init__(self, invoker: BaseLMInvoker) -> None:
        """Initializes the batch operations.

        Args:
            invoker (BaseLMInvoker): The LM invoker to use for the batch operations.
        """
    async def create(self, requests: dict[str, list[Message] | list[MessageContent] | str], hyperparameters: dict[str, Any] | None = None) -> str:
        """Creates a new batch job.

        Args:
            requests (dict[str, list[Message] | list[MessageContent] | str]): The dictionary of requests that maps
                request ID to the request. Each request must be a valid input for the language model.
                1. If the request is a list of Message objects, it is used as is.
                2. If the request is a list of MessageContent or a string, it is converted into a user message.
            hyperparameters (dict[str, Any] | None, optional): A dictionary of hyperparameters for the language model.
                Defaults to None, in which case the default hyperparameters are used.

        Returns:
            str: The ID of the batch job.
        """
    async def status(self, batch_id: str) -> BatchStatus:
        """Gets the status of a batch job.

        Args:
            batch_id (str): The ID of the batch job to get the status of.

        Returns:
            BatchStatus: The status of the batch job.
        """
    async def retrieve(self, batch_id: str) -> dict[str, LMOutput]:
        """Retrieves the results of a batch job.

        Args:
            batch_id (str): The ID of the batch job to get the results of.

        Returns:
            dict[str, LMOutput]: The results of the batch job.
        """
    async def list(self) -> list[dict[str, Any]]:
        """Lists the batch jobs.

        Returns:
            list[dict[str, Any]]: The list of batch jobs.
        """
    async def cancel(self, batch_id: str) -> None:
        """Cancels a batch job.

        Args:
            batch_id (str): The ID of the batch job to cancel.
        """
