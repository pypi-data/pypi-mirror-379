from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Sequence
from airflow.providers.microsoft.fabric.hooks.run_item.job import JobSchedulerConfig, MSFabricRunJobHook
from airflow.providers.microsoft.fabric.hooks.run_item.model import (
    ItemDefinition, RunItemTracker,
)
from airflow.providers.microsoft.fabric.operators.run_item.base import MSFabricItemLink, BaseFabricRunItemOperator
from airflow.providers.microsoft.fabric.triggers.run_item.job import MSFabricRunJobTrigger

if TYPE_CHECKING:
    from airflow.utils.context import Context

class MSFabricRunJobOperator(BaseFabricRunItemOperator):
    """Run a Fabric job via the Job Scheduler."""

    # Keep template-able primitives as top-level attributes
    template_fields: Sequence[str] = (
        "fabric_conn_id",
        "workspace_id",
        "item_id",
        "job_type",
        "timeout",
        "check_interval",
        "deferrable",
        "job_params",
        "api_host",
        "scope",
    )
    template_fields_renderers = {"job_params": "json"}  # optional

    operator_extra_links = (MSFabricItemLink(),)

    def __init__(
        self,
        *,
        fabric_conn_id: str,
        workspace_id: str,
        item_id: str,
        job_type: str,
        timeout: int = 60 * 60,   # 1 hour
        check_interval: int = 30,
        deferrable: bool = True,
        job_params: str = "",
        api_host: str = "https://api.fabric.microsoft.com",
        scope: str = "https://api.fabric.microsoft.com/.default",
        wait_for_termination = True,
        **kwargs,
    ) -> None:
        # Store raw values so Airflow can template them later
        self.fabric_conn_id = fabric_conn_id
        self.workspace_id = workspace_id
        self.item_id = item_id
        self.job_type = job_type
        self.timeout = timeout
        self.check_interval = check_interval
        self.deferrable = deferrable
        self.job_params = job_params or ""
        self.api_host = api_host
        self.scope = scope
        self.wait_for_termination = wait_for_termination # do not document this, available for backwards compatibility only

        # deal with bad config in UI template
        if job_type == "RunPipeline":
            self.job_type = "Pipeline"
            

        # Build initial dataclasses from the *current* values
        config = JobSchedulerConfig(
            fabric_conn_id=self.fabric_conn_id,
            timeout_seconds=self.timeout,
            poll_interval_seconds=self.check_interval,
            api_host=self.api_host,
            api_scope=self.scope,
            job_params=self.job_params,
        )
        item = ItemDefinition(
            workspace_id=self.workspace_id,
            item_type=self.job_type,
            item_id=self.item_id,
        )

        # If your hook needs more than conn_id, add it here
        hook = MSFabricRunJobHook(config=config)

        # Pass required args to the base class (fixes the missing kwargs error)
        super().__init__(hook=hook, item=item, **kwargs)

        # Keep the config around if you want to pass it to triggers, etc.
        self.config = config

    # Optional but recommended: ensure post-templating objects are rebuilt
    def render_template_fields(self, context, jinja_env=None):
        super().render_template_fields(context, jinja_env=jinja_env)

        # Rebuild objects with the *rendered* values so they’re up to date
        self.config = JobSchedulerConfig(
            fabric_conn_id=self.fabric_conn_id,
            timeout_seconds=self.timeout,
            poll_interval_seconds=self.check_interval,
            api_host=self.api_host,
            api_scope=self.scope,
            job_params=self.job_params,
        )
        self.item = ItemDefinition(
            workspace_id=self.workspace_id,
            item_type=self.job_type,
            item_id=self.item_id,
        )
        self.hook = MSFabricRunJobHook(self.config)

    def create_trigger(self, tracker: RunItemTracker) -> MSFabricRunJobTrigger:
        """Create and return the FabricHook (cached)."""
        return MSFabricRunJobTrigger(
            config=self.config.to_dict(),
            tracker=tracker.to_dict())

    def execute(self, context: Context) -> None:
        """Execute the Fabric item run."""
        self.log.info("Starting Fabric item run - workspace_id: %s, job_type: %s, item_id: %s",
                      self.item.workspace_id, self.item.item_type, self.item.item_id)

        asyncio.run(self._execute_core(context, self.deferrable, self.wait_for_termination))
