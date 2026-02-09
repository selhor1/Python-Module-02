class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Error related to plant problems."""
    pass


class WaterError(GardenError):
    """Error related to watering problems."""
    pass


def check_plant_health() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water_level() -> None:
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water_level()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        check_plant_health()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water_level()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Caught unexpected error: {e}")
