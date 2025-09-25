"""
AI Code Tools Client - Python interface for communicating with the server.

Provides a simple Python API that communicates with the Docker-based server
via HTTP requests. Handles connection management and response formatting.
"""

import json
import time
import subprocess
import requests
from typing import Dict, Any, Optional, List, Callable
import os
import logging
import functools

# Import tool classes to extract docstrings
from aicodetools.tools import ReadTool, WriteTool, EditTool, RunTool


# Tool names for tools() method
# Available tools: "read_file", "write_file", "edit_file", "run_command"


class CodeToolsClient:
    """Client interface for AI Code Tools server."""

    def __init__(self, server_url: str = "http://localhost:18080", auto_start: bool = True,
                 docker_image: str = "python:3.11-slim", port: int = 18080):
        self.server_url = server_url.rstrip('/')
        self.session = requests.Session()
        self.docker_container = None
        self.docker_image = docker_image
        self.port = port

        if auto_start:
            self._ensure_server_running()

    def _ensure_server_running(self) -> bool:
        """Ensure the server is running, start if necessary."""
        try:
            # Check if server is already running
            response = self.session.get(f"{self.server_url}/api/status", timeout=2)
            if response.status_code == 200:
                logging.info("Server is already running")
                return True
        except requests.exceptions.RequestException:
            pass

        # Try to start server using Docker
        return self._start_docker_server()

    def _start_docker_server(self) -> bool:
        """Start the server using Docker."""
        try:
            logging.info("Starting AI Code Tools server in Docker...")

            # Check if Docker service is running
            try:
                result = subprocess.run(['docker', 'info'], capture_output=True, text=True, timeout=10)
                if result.returncode != 0:
                    logging.error("Docker service is not running. Please start Docker.")
                    return False
            except (subprocess.TimeoutExpired, FileNotFoundError):
                logging.error("Docker not found or not running. Please install and start Docker.")
                return False

            # Check if Docker image exists
            check_result = subprocess.run(['docker', 'images', '-q', self.docker_image],
                                        capture_output=True, text=True, timeout=10)

            if not check_result.stdout.strip():
                # Image doesn't exist - try to pull it
                logging.info(f"Pulling image: docker pull {self.docker_image}")
                pull_result = subprocess.run(['docker', 'pull', self.docker_image],
                                           capture_output=True, text=True, timeout=120)
                if pull_result.returncode != 0:
                    logging.error(f"Image '{self.docker_image}' not found. Please ensure it exists or use a standard Python image like 'python:3.11-slim'.")
                    return False

            # Clean up existing container
            subprocess.run(['docker', 'stop', 'aicodetools-container'], capture_output=True, text=True, timeout=10)
            subprocess.run(['docker', 'rm', 'aicodetools-container'], capture_output=True, text=True, timeout=10)

            # Start container with pip-installed package
            cmd_string = f'pip install --break-system-packages aicodetools && python -m aicodetools.server --host 0.0.0.0 --port 8080'
            run_cmd = [
                'docker', 'run', '-d', '--name', 'aicodetools-container',
                '-p', f'{self.port}:8080',
                '--rm',  # Auto-remove container when stopped
                self.docker_image,
                'bash', '-c', cmd_string
            ]

            # Show exact command for debugging
            exact_cmd = f"docker run -d --name aicodetools-container -p {self.port}:8080 --rm {self.docker_image} bash -c \"{cmd_string}\""
            logging.info(f"Starting container: {exact_cmd}")
            run_result = subprocess.run(run_cmd, capture_output=True, text=True, timeout=120)
            if run_result.returncode != 0:
                if "port is already allocated" in run_result.stderr:
                    logging.error(f"Port {self.port} is in use. Please stop other services or use a different port.")
                elif "permission denied" in run_result.stderr:
                    logging.error("Docker permission denied. Try running as administrator or add user to docker group.")
                else:
                    logging.error(f"Container failed to start: {run_result.stderr}")
                return False

            self.docker_container = 'aicodetools-container'

            # Wait for server to start
            for _ in range(30):  # Wait up to 30 seconds
                try:
                    response = self.session.get(f"{self.server_url}/api/status", timeout=2)
                    if response.status_code == 200:
                        logging.info("Server started successfully")
                        return True
                except requests.exceptions.RequestException:
                    pass
                time.sleep(1)

            logging.error("Server failed to start within timeout")
            return False

        except Exception as e:
            logging.error(f"Failed to start Docker server: {e}")
            return False

    def _make_request(self, endpoint: str, data: Optional[Dict[str, Any]] = None, method: str = 'POST') -> Dict[str, Any]:
        """Make HTTP request to server."""
        try:
            url = f"{self.server_url}/api/{endpoint}"

            if method == 'GET':
                response = self.session.get(url, timeout=30)
            else:
                response = self.session.post(url, json=data or {}, timeout=30)

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            return {"success": False, "error": "Request timed out"}
        except requests.exceptions.ConnectionError:
            return {"success": False, "error": "Failed to connect to server"}
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": f"Request failed: {str(e)}"}
        except json.JSONDecodeError:
            return {"success": False, "error": "Invalid JSON response from server"}

    # Tool Interface

    def tools(self, selection_list: List[str]) -> List[Callable]:
        """
        Get wrapped tool functions based on selection list.

        Args:
            selection_list: List of tool names (e.g., ["read_file", "write_file", "edit_file", "run_command"])

        Returns:
            List of wrapped tool functions in the same order as selection_list

        Usage:
            tools = client.tools(selection_list=["read_file", "write_file", "edit_file", "run_command"])
            read, write, edit, run_command = tools
        """
        # Map tool names to their wrapped versions
        tool_map = {
            "read_file": self._create_read_tool(),
            "write_file": self._create_write_tool(),
            "edit_file": self._create_edit_tool(),
            "run_command": self._create_run_tool()
        }

        return [tool_map[name] for name in selection_list]

    def _create_read_tool(self) -> Callable:
        """Create read tool function with docstring from tools/read.py"""
        def read_file_tool(file_path: str, lines_start: Optional[int] = None,
                          lines_end: Optional[int] = None, complete_lines: bool = False,
                          regex: Optional[str] = None) -> Dict[str, Any]:
            data = {"file_path": file_path}

            if regex:
                data["regex"] = regex
            elif lines_start is not None:
                data["lines_start"] = lines_start
                if lines_end is not None:
                    data["lines_end"] = lines_end
                if complete_lines:
                    data["complete_lines"] = complete_lines

            return self._make_request("read", data)

        # Copy docstring from actual ReadTool.read_file method
        read_file_tool.__doc__ = ReadTool.read_file.__doc__
        read_file_tool.__name__ = "read_file"

        return read_file_tool

    def _create_write_tool(self) -> Callable:
        """Create write tool function with docstring from tools/write.py"""
        def write_file_tool(file_path: str, content: str) -> Dict[str, Any]:
            data = {"file_path": file_path, "content": content}
            return self._make_request("write", data)

        # Copy docstring from actual WriteTool.write_file method
        write_file_tool.__doc__ = WriteTool.write_file.__doc__
        write_file_tool.__name__ = "write_file"

        return write_file_tool

    def _create_edit_tool(self) -> Callable:
        """Create edit tool function with docstring from tools/edit.py"""
        def edit_file_tool(file_path: str, old_string: str, new_string: str,
                          replace_all: bool = False) -> Dict[str, Any]:
            data = {
                "file_path": file_path,
                "old_string": old_string,
                "new_string": new_string,
                "replace_all": replace_all
            }
            return self._make_request("edit", data)

        # Copy docstring from actual EditTool.edit_file method
        edit_file_tool.__doc__ = EditTool.edit_file.__doc__
        edit_file_tool.__name__ = "edit_file"

        return edit_file_tool

    def _create_run_tool(self) -> Callable:
        """Create run tool function with docstring from tools/run.py"""
        def run_command_tool(command: str, timeout: int = 300, interactive: bool = False) -> Dict[str, Any]:
            data = {
                "command": command,
                "timeout": timeout,
                "interactive": interactive
            }
            return self._make_request("run", data)

        # Copy docstring from actual RunTool.run_command method
        run_command_tool.__doc__ = RunTool.run_command.__doc__
        run_command_tool.__name__ = "run_command"

        return run_command_tool

    def get_output(self, max_lines: int = 100) -> Dict[str, Any]:
        """Get output from active interactive process."""
        data = {"max_lines": max_lines}
        return self._make_request("get_output", data)

    def send_input(self, input_text: str) -> Dict[str, Any]:
        """Send input to active interactive process."""
        data = {"input_text": input_text}
        return self._make_request("send_input", data)

    def stop_process(self, force: bool = False) -> Dict[str, Any]:
        """Stop active interactive process."""
        data = {"force": force}
        return self._make_request("stop_process", data)

    def get_process_status(self) -> Dict[str, Any]:
        """Get status of active process."""
        return self._make_request("get_status", method='GET')

    # Server Management

    def get_status(self) -> Dict[str, Any]:
        """Get server status."""
        return self._make_request("status", method='GET')

    def stop_server(self) -> bool:
        """Stop the Docker server."""
        if self.docker_container:
            try:
                result = subprocess.run(['docker', 'stop', self.docker_container],
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    subprocess.run(['docker', 'rm', self.docker_container],
                                 capture_output=True, text=True)
                    self.docker_container = None
                    return True
            except Exception as e:
                logging.error(f"Failed to stop server: {e}")

        return False

    def restart_server(self) -> bool:
        """Restart the Docker server."""
        self.stop_server()
        time.sleep(2)
        return self._ensure_server_running()

    # Context Manager Support

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop_server()

