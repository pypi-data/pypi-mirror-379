import asyncio
import subprocess
from typing import Optional

def close_process(process: subprocess.Popen) -> None:
    """Close a running process gracefully."""
    if process and process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()

async def run_command(command: str) -> str:
    """Run a shell command asynchronously and return its output."""
    proc = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(f"Command failed: {command}\n{stderr.decode()}")
    return stdout.decode().strip()

def start_bluetoothctl() -> subprocess.Popen:
    """Start a bluetoothctl subprocess."""
    return subprocess.Popen(
        ["bluetoothctl"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

async def send_command_in_process(
    process: subprocess.Popen, command: str, delay: float = 2
) -> None:
    """Send a command to bluetoothctl process."""
    if process.stdin is None:
        raise RuntimeError("Process has no stdin")
    process.stdin.write(command + "\n")
    process.stdin.flush()
    await asyncio.sleep(delay)

async def is_device_connected(address: str) -> bool:
    """Check if a device is connected via bluetoothctl."""
    output = await run_command(f"bluetoothctl info {address}")
    return "Connected: yes" in output

async def is_device_bonded(address: str) -> bool:
    """Check if a device is bonded via bluetoothctl."""
    output = await run_command(f"bluetoothctl info {address}")
    return "Bonded: yes" in output

async def is_device_paired(address: str) -> bool:
    """Check if a device is paired via bluetoothctl."""
    output = await run_command(f"bluetoothctl info {address}")
    return "Paired: yes" in output

async def get_first_manufacturer_data_byte(mac_address: str) -> Optional[int]:
    """Fetch the first manufacturer data byte for a given MAC address."""
    output = await run_command(f"bluetoothctl info {mac_address}")
    for line in output.splitlines():
        if "ManufacturerData Key" in line:
            try:
                # Extract first byte (assumes hex like 0x01 0x02 …)
                hex_values = line.split(":")[1].strip().split()
                return int(hex_values[0], 16)
            except Exception:
                return None
    return None
