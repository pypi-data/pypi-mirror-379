import subprocess

import structlog

logger = structlog.get_logger()


class Multipass:
    """Manager class for multipass operations with logging."""

    def __init__(self, instance_name: str, snapshot_name: str):
        self.instance_name = instance_name
        self.snapshot_name = snapshot_name

    def __enter__(self) -> 'Multipass':
        """
        Context manager entry: resets the VM to a clean state and starts it.
        This includes stop, restore, start, and waiting for the service.
        """
        logger.info('Entering Multipass context: Resetting VM environment...')
        self.stop()
        self.restore()
        self.start()
        logger.info('VM is ready and accessible.')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Context manager exit: ensures the VM is stopped.
        """
        logger.info('Exiting Multipass context: Stopping VM instance...')
        self.stop()

    def _run_command(self, cmd: list[str], operation: str) -> None:
        """Run a multipass command with logging."""
        logger.info(f"Executing {operation}: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)

    def stop(self) -> None:
        """Stop the multipass instance."""
        cmd = ['multipass', 'stop', self.instance_name]
        self._run_command(cmd, 'stop multipass instance')

    def restore(self) -> None:
        """Restore the multipass snapshot."""
        cmd = [
            'multipass', 'restore',
            f'{self.instance_name}.{self.snapshot_name}',
            '--destructive',
        ]
        self._run_command(cmd, 'restore multipass snapshot')

    def start(self) -> None:
        """Start the multipass instance."""
        cmd = ['multipass', 'start', self.instance_name]
        self._run_command(cmd, 'start multipass instance')

    def delete_snapshot(self, snapshot_type: str) -> None:
        """Delete a specific snapshot for the given type."""
        snapshot_full_name = f'{self.instance_name}.{snapshot_type}'
        cmd = ['multipass', 'delete', '--purge', snapshot_full_name]
        try:
            self._run_command(
                cmd, f"delete multipass snapshot {snapshot_type}",
            )
        except subprocess.CalledProcessError:
            logger.warning(
                'Failed to delete multipass snapshot for this openapi type',
                instance_name=self.instance_name,
                snapshot_type=snapshot_type,
            )

    def create_snapshot(self, snapshot_type: str) -> None:
        """Create a snapshot with the given type name."""
        cmd = [
            'multipass', 'snapshot', '--name', snapshot_type,
            self.instance_name,
        ]
        self._run_command(cmd, f"create multipass snapshot {snapshot_type}")
