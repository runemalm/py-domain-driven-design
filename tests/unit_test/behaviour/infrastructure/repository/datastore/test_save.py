from unittest import skip
from unittest.mock import MagicMock

import pytest
from google.cloud import datastore

from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle
from unit_test.behaviour.infrastructure.repository.datastore.vehicle_repository import \
    DatastoreVehicleRepository
from unit_test.behaviour.infrastructure.repository.in_memory.vehicle_repository import (
    InMemoryVehicleRepository,
)
from unit_test.behaviour.unit_test_case import UnitTestCase


@skip
class TestSave(UnitTestCase):
    def test_creates_when_dont_exist(
        self,
    ):
        raise NotImplementedError()

        # # arrange
        # vehicle_repository = DatastoreVehicleRepository(client=None)
        # vehicle = Vehicle(id="test-id", color="red")
        #
        # # act
        # vehicle_repository.save(vehicle)
        #
        # found_vehicles = vehicle_repository.find_all()
        #
        # # assert
        # self.assertEqual(1, len(found_vehicles))
        # self.assertEqual(vehicle, found_vehicles[0])

    def test_updates_when_exists(
        self,
    ):
        raise NotImplementedError()

    def test_raises_when_no_entity_id(
        self,
    ):
        raise NotImplementedError()
