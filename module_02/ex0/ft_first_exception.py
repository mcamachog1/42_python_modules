#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """
    Converts a string to an integer and checks if it's a valid temperature.
    """

    try:
        temp: int = int(temp_str)
        if temp < 0 or temp > 40:
            if temp < 0:
                print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            else:
                print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


# Example usage:
def main():
    print("=== Garden Temperature Checker ===")
    print()
    list_of_temps = ["25", "abc", "100", "-50"]
    for temp_str in list_of_temps:
        print(f"Testing temperature: {temp_str}")
        temp = check_temperature(temp_str)
        if temp is not None:
            print(f"Temperature {temp}°C is perfect for plants!")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
