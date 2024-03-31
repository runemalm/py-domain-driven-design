from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle
from unit_test.behaviour.infrastructure.repository.in_memory.vehicle_repository import (
    InMemoryVehicleRepository,
)
from unit_test.behaviour.unit_test_case import UnitTestCase


class TestNonGenericMethod(UnitTestCase):
    def test_returns_all_with_color(
        self,
    ):
        # arrange
        vehicle_repository = InMemoryVehicleRepository()

        vehicle_1 = Vehicle(id="test-id-1", color="red")
        vehicle_2 = Vehicle(id="test-id-2", color="green")
        vehicle_3 = Vehicle(id="test-id-3", color="blue")
        vehicle_4 = Vehicle(id="test-id-4", color="green")
        vehicle_repository.save(vehicle_1)
        vehicle_repository.save(vehicle_2)
        vehicle_repository.save(vehicle_3)
        vehicle_repository.save(vehicle_4)

        # act
        all_green_vehicles = vehicle_repository.find_with_colors(colors=["green"])

        # assert
        self.assertIsNotNone(all_green_vehicles)
        self.assertEqual(2, len(all_green_vehicles))
        self.assertEqual([vehicle_2, vehicle_4], all_green_vehicles)
