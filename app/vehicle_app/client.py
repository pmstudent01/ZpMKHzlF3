"""Thin service wrapper around the generated Vehicle Service SDK.

This module keeps all SDK interaction in one place so the CLI (or any other
front end) does not need to know the SDK's internal method names.
"""

from __future__ import annotations

from typing import Any, Optional

from vehicle_service_collection_sdk import VehicleServiceCollectionSdk
from vehicle_service_collection_sdk.models import CreateAVehicleRequest

from .config import Config


class VehicleService:
    """High-level operations for the Vehicle Service API.

    Wraps the generated ``VehicleServiceCollectionSdk`` client and exposes a
    clean, intention-revealing method per endpoint.
    """

    def __init__(self, config: Optional[Config] = None) -> None:
        self._config = config or Config.from_env()
        self._sdk = VehicleServiceCollectionSdk(
            api_key=self._config.api_key,
            base_url=self._config.base_url,
            timeout=10,
        )

    @property
    def _service(self):
        # The generated client exposes the service under this attribute name.
        return self._sdk.vehicle_service_collection_sdk

    # -- Operations -------------------------------------------------------

    def list_vehicles(self) -> Any:
        """GET /vehicles — return all vehicles."""
        return self._service.get_all_vehicles()

    def get_vehicle(self, vehicle_id: str) -> Any:
        """GET /vehicles/:id — return a single vehicle."""
        return self._service.retrieve_a_vehicle(str(vehicle_id))

    def create_vehicle(
        self,
        *,
        nick_name: Optional[str] = None,
        vin: Optional[str] = None,
        make: Optional[str] = None,
        model: Optional[str] = None,
        year: Optional[str] = None,
        miles: Optional[int] = None,
    ) -> Any:
        """POST /vehicles — create a new vehicle."""
        body = CreateAVehicleRequest(
            nick_name=nick_name,
            vin=vin,
            make=make,
            model=model,
            year=year,
            miles=miles,
        )
        return self._service.create_a_vehicle(body)

    def update_vehicle(
        self,
        vehicle_id: str,
        *,
        nick_name: Optional[str] = None,
        vin: Optional[str] = None,
        make: Optional[str] = None,
        model: Optional[str] = None,
        year: Optional[str] = None,
        miles: Optional[int] = None,
    ) -> Any:
        """PATCH /vehicles/:id — update an existing vehicle."""
        body = CreateAVehicleRequest(
            nick_name=nick_name,
            vin=vin,
            make=make,
            model=model,
            year=year,
            miles=miles,
        )
        return self._service.update_a_collection(body, str(vehicle_id))

    def delete_vehicle(self, vehicle_id: str) -> Any:
        """DELETE /vehicles/:id — delete a vehicle."""
        return self._service.delete_a_vehicle(str(vehicle_id))
