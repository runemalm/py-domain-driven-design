import socket
import pytest
import subprocess
import time
import requests
from google.cloud import datastore


class DatastoreEmulatorMixin:
    @pytest.fixture(autouse=True, scope="function")
    def setup_datastore_emulator(self):
        port = self.find_free_port()

        self.emulator_process = subprocess.Popen(
            [
                "gcloud",
                "beta",
                "emulators",
                "datastore",
                "start",
                f"--host-port=localhost:{port}",
                "--no-store-on-disk",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Poll the emulator's health check endpoint until it responds successfully
        health_check_url = f"http://localhost:{port}"
        max_attempts = 20
        for attempt in range(max_attempts):
            try:
                response = requests.get(health_check_url)
                if response.status_code == 200:
                    self.datastore_client = datastore.Client(
                        project="test-project",
                        client_options={"api_endpoint": f"http://localhost:{port}"},
                    )
                    break
            except requests.ConnectionError:
                pass
            time.sleep(1)
        else:
            raise RuntimeError("Datastore emulator did not become ready in time")

        yield

        # Stop the emulator
        self.emulator_process.terminate()
        self.emulator_process.wait()

    def find_free_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))  # Bind to a free port provided by the host.
            return s.getsockname()[1]  # Return the port number assigned.
