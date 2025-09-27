"""RyseBLEDevice: async wrapper around Bleak for RYSE devices.

This module intentionally keeps responsibilities small: connect/disconnect,
read/write GATT characteristics, and deliver notifications via a callback.
"""

from __future__ import annotations

import asyncio
from typing import Callable, Optional
from bleak import BleakClient, BleakScanner
import logging

_LOGGER = logging.getLogger(__name__)

class RyseBLEDevice:
    """Represent a RYSE device and provide async methods to interact with it."""

    def __init__(self, address: Optional[str] = None, rx_uuid: Optional[str] = None, tx_uuid: Optional[str] = None):
        self.address = address
        self.rx_uuid = rx_uuid
        self.tx_uuid = tx_uuid
        self.client: Optional[BleakClient] = None
        # Optional async callback: async def cb(position: int)
        self.update_callback: Optional[Callable[[int], None]] = None

    async def pair(self, timeout: float = 30.0) -> bool:
        """Connect to the device and subscribe to notifications."""
        if not self.address:
            _LOGGER.error("No device address provided for pairing.")
            return False

        _LOGGER.debug("Connecting to device %s", self.address)
        self.client = BleakClient(self.address)
        try:
            await self.client.connect(timeout=timeout)
            if self.client.is_connected:
                _LOGGER.debug("Connected to %s", self.address)
                if self.rx_uuid:
                    try:
                        await self.client.start_notify(self.rx_uuid, self._notification_handler)
                        _LOGGER.debug("Started notify on %s", self.rx_uuid)
                    except Exception as e:
                        _LOGGER.debug("Could not start notify: %s", e)
                return True
        except Exception as e:
            _LOGGER.error("Failed to connect to %s: %s", self.address, e)
        return False

    async def disconnect(self):
        if self.client:
            try:
                if self.rx_uuid:
                    try:
                        await self.client.stop_notify(self.rx_uuid)
                    except Exception:
                        pass
                await self.client.disconnect()
            except Exception as e:
                _LOGGER.debug("Error during disconnect: %s", e)
            finally:
                self.client = None

    async def _notification_handler(self, sender, data: bytes):
        """Handle BLE notifications from the device.

        Filter and extract position update (protocol-specific). If a callback
        is registered it will be awaited.
        """
        try:
            # Basic validation based on observed protocol
            if len(data) >= 5 and data[0] == 0xF5 and data[2] == 0x01 and data[3] == 0x18:
                # ignore REPORT USER TARGET data
                return

            _LOGGER.debug("Received notification: %s", data.hex())

            if len(data) >= 5 and data[0] == 0xF5 and data[2] == 0x01 and data[3] == 0x07:
                position = data[4]
                _LOGGER.debug("Parsed position: %d", position)
                if self.update_callback:
                    # allow callback to be coroutine or normal function
                    if asyncio.iscoroutinefunction(self.update_callback):
                        await self.update_callback(position)
                    else:
                        # run sync callbacks in event loop
                        loop = asyncio.get_running_loop()
                        loop.call_soon(self.update_callback, position)
        except Exception as e:
            _LOGGER.exception("Error in notification handler: %s", e)

    async def read_data(self) -> Optional[bytes]:
        """Read raw data from RX characteristic (if available)."""
        if not self.client or not self.client.is_connected:
            _LOGGER.debug("Client not connected for read")
            return None
        if not self.rx_uuid:
            _LOGGER.debug("No RX UUID configured for read")
            return None
        try:
            data = await self.client.read_gatt_char(self.rx_uuid)
            return bytes(data)
        except Exception as e:
            _LOGGER.error("read_data failed: %s", e)
            return None

    async def write_data(self, data: bytes) -> bool:
        """Write raw bytes to TX characteristic."""
        if not self.client or not self.client.is_connected:
            _LOGGER.debug("Client not connected for write")
            return False
        if not self.tx_uuid:
            _LOGGER.debug("No TX UUID configured for write")
            return False
        try:
            await self.client.write_gatt_char(self.tx_uuid, data)
            _LOGGER.debug("Wrote %d bytes to %s", len(data), self.tx_uuid)
            return True
        except Exception as e:
            _LOGGER.error("write_data failed: %s", e)
            return False

    @staticmethod
    async def discover(timeout: float = 5.0):
        """Discover BLE devices using BleakScanner; returns list of bleak device objects."""
        return await BleakScanner.discover(timeout=timeout)
