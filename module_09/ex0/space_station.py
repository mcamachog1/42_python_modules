#!/usr/bin/env python3
# space_station.py

from datetime import datetime
from typing import Optional
try:
    from pydantic import BaseModel, Field, ValidationError
except Exception as e:
    print(e)
    print("Try this instructions:")
    print("    python3 -m venv venv")
    print("    source venv/bin/activate")
    print("    pip install pydantic")
    print("    python3 space_station.py")
    exit(1)


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: Optional[datetime] = None
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def print_error(e: ValidationError):
    for error in e.errors():
        print(f"{error['msg']}")


def print_data(sp: SpaceStation):
    print(f"ID: {sp.station_id}")
    print(f"Name: {sp.name}")
    print(f"Crew: {sp.crew_size} people")
    print(f"Power: {sp.power_level}%")
    print(f"Oxygen: {sp.oxygen_level}%")
    if sp.last_maintenance:
        print(f"Last maintenance: {sp.last_maintenance}")
    print(
        "Status: "
        f"{'Operational' if sp.is_operational else 'Not Operational'}")
    if sp.notes:
        print(f"Notes: {sp.notes}")
    print()


def right_data() -> SpaceStation:
    space_station = SpaceStation(
            station_id="101",
            name="Space Station 101",
            crew_size=15,
            power_level=98.4,
            oxygen_level=99.5,

        )
    return space_station


def wrong_data() -> SpaceStation:
    space_station = SpaceStation(
            station_id="s123451",
            name="Space Station 101",
            crew_size=35,
            power_level=98.4,
            oxygen_level=99.5,
        )
    return space_station


def main():
    print("\nSpace Station Data Validation")
    try:
        print("================================================")
        print("Valid Station created:")
        print_data(right_data())
        print("================================================")
        print("Expected validation error:")
        print_data(wrong_data())
    except ValidationError as e:
        print_error(e)


main()
