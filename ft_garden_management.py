class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = {}

    # -------- Add Plant --------
    def add_plant(self, name: str, water_level: int, sunlight_hours: int) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")

        self.plants[name] = {
            "water": water_level,
            "sun": sunlight_hours
        }

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("Not enough water in tank")

            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str) -> None:
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' does not exist")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water < 1:
            raise ValueError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")

        if sun < 2:
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise ValueError(f"Sunlight hours {sun} is too high (max 12)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        print("Added tomato successfully")

        garden.add_plant("lettuce", 15, 6)
        print("Added lettuce successfully")

        garden.add_plant("", 4, 6)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato")
        garden.check_plant_health("lettuce")
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
