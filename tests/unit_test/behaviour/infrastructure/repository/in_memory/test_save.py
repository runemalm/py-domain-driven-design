import pytest

from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle
from unit_test.behaviour.infrastructure.repository.in_memory.vehicle_repository import \
    InMemoryVehicleRepository
from unit_test.behaviour.unit_test_case import UnitTestCase


class TestSave(UnitTestCase):
    def test_creates_when_dont_exist(
        self,
    ):
        # arrange
        vehicle_repository = InMemoryVehicleRepository()
        vehicle = Vehicle(id="test-id", color="red")

        # act
        vehicle_repository.save(vehicle)

        found_vehicles = vehicle_repository.find_all()

        # assert
        self.assertEqual(1, len(found_vehicles))
        self.assertEqual(vehicle, found_vehicles[0])

    def test_updates_when_exists(
        self,
    ):
        # arrange
        vehicle_repository = InMemoryVehicleRepository()
        vehicle = Vehicle(id="test-id", color="red")
        vehicle_repository.save(vehicle)
        vehicle.color = "green"

        # act
        vehicle_repository.save(vehicle)

        found_vehicles = vehicle_repository.find_all()

        # assert
        self.assertEqual(1, len(found_vehicles))
        self.assertEqual("green", found_vehicles[0].color)

    def test_raises_when_no_entity_id(
        self,
    ):
        # arrange
        vehicle_repository = InMemoryVehicleRepository()

        vehicle = Vehicle(id=None, color="red")

        # act + assert
        with pytest.raises(AttributeError, match="The entity needs to have an ID."):
            vehicle_repository.save(vehicle)
