"""Background agent configuration classes for NCP."""

from dataclasses import dataclass, field
from typing import List, Optional, Union
from datetime import timedelta


@dataclass
class BackgroundTask:
    """
    Configuration for a single background task within an agent.

    Each task can run on its own schedule (either interval or cron) and
    represents a specific autonomous operation the agent should perform.

    Example:
        # Interval-based task
        task = BackgroundTask(
            name="health_check",
            description="Check system health every 5 minutes",
            task="Check the health of all monitored services and alert if any issues are found",
            interval=300  # 5 minutes in seconds
        )

        # Cron-based task
        task = BackgroundTask(
            name="daily_report",
            description="Generate daily reports",
            task="Generate and send daily performance reports",
            schedule="0 9 * * *"  # 9 AM every day
        )
    """

    name: str
    description: str
    task: str  # The actual task/prompt to execute

    # Scheduling - exactly one interval or schedule must be provided
    interval: Optional[Union[int, timedelta]] = None  # seconds or timedelta
    schedule: Optional[str] = None  # cron expression

    # Configuration
    timezone: str = "UTC"
    enabled: bool = True

    def __post_init__(self):
        """Validate the task configuration."""
        # Convert timedelta to seconds if needed first
        if isinstance(self.interval, timedelta):
            self.interval = int(self.interval.total_seconds())

        # Check for zero or negative interval before other validations
        if self.interval is not None and self.interval <= 0:
            raise ValueError(f"Task '{self.name}' interval must be positive")

        # Check that exactly one of interval or schedule is provided
        if not self.interval and not self.schedule:
            raise ValueError(f"Task '{self.name}' must have either interval or schedule")

        if self.interval and self.schedule:
            raise ValueError(f"Task '{self.name}' cannot have both interval and schedule")

    @property
    def is_interval_based(self) -> bool:
        """Check if this task uses interval scheduling."""
        return self.interval is not None

    @property
    def is_cron_based(self) -> bool:
        """Check if this task uses cron scheduling."""
        return self.schedule is not None

    @property
    def interval_seconds(self) -> Optional[int]:
        """Get the interval in seconds."""
        return self.interval if isinstance(self.interval, int) else None


@dataclass
class BackgroundConfig:
    """
    Configuration for background agent execution.

    Supports multiple tasks, each with their own scheduling configuration.
    Tasks run independently and concurrently within the same agent context.

    Example:
        from datetime import timedelta

        config = BackgroundConfig(
            enabled=True,
            tasks=[
                BackgroundTask(
                    name="monitor",
                    description="Monitor system status",
                    task="Check all services and report any issues",
                    interval=timedelta(minutes=5)
                ),
                BackgroundTask(
                    name="cleanup",
                    description="Daily cleanup",
                    task="Clean up temporary files and optimize database",
                    schedule="0 2 * * *"  # 2 AM daily
                )
            ]
        )
    """

    enabled: bool = True
    tasks: List[BackgroundTask] = field(default_factory=list)

    def __post_init__(self):
        """Validate the background configuration."""
        if not self.tasks:
            raise ValueError("BackgroundConfig must have at least one task")

        # Check for duplicate task names
        task_names = [task.name for task in self.tasks]
        if len(task_names) != len(set(task_names)):
            raise ValueError("BackgroundConfig cannot have duplicate task names")

    @property
    def enabled_tasks(self) -> List[BackgroundTask]:
        """Get only the enabled tasks."""
        return [task for task in self.tasks if task.enabled]

    @property
    def has_enabled_tasks(self) -> bool:
        """Check if there are any enabled tasks."""
        return len(self.enabled_tasks) > 0

    def get_task(self, name: str) -> Optional[BackgroundTask]:
        """Get a task by name."""
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def add_task(self, task: BackgroundTask):
        """Add a new background task."""
        if self.get_task(task.name):
            raise ValueError(f"Task '{task.name}' already exists")
        self.tasks.append(task)

    def remove_task(self, name: str) -> bool:
        """Remove a task by name. Returns True if the task was found and removed."""
        for i, task in enumerate(self.tasks):
            if task.name == name:
                del self.tasks[i]
                return True
        return False

    def enable_task(self, name: str) -> bool:
        """Enable a task by name. Returns True if the task was found."""
        task = self.get_task(name)
        if task:
            task.enabled = True
            return True
        return False

    def disable_task(self, name: str) -> bool:
        """Disable a task by name. Returns True if the task was found."""
        task = self.get_task(name)
        if task:
            task.enabled = False
            return True
        return False