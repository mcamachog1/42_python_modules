#!/usr/bin/env python3


from enum import Enum
from datetime import datetime
from typing_extensions import Self
from typing import Optional

try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
except Exception as e:
    print(e)
    print("Try this instructions:")
    print("    python3 -m venv venv")
    print("    source venv/bin/activate")
    print("    pip install pydantic")
    print("    python3 space_crew.py")
    exit(1)


class Rank(Enum):
    CAD = 'cadet'
    OFF = 'officer'
    LIE = 'lieutenant'
    CAP = 'captain'
    COM = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: Optional[datetime] = Field(default=None)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned', min_length=5, max_length=15)
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        commanders: int = len([c for c in self.crew if c.rank == Rank.COM])
        captains: int = len([c for c in self.crew if c.rank == Rank.CAP])

        if commanders < 1 and captains < 1:
            raise ValueError(
                "Mission must have at least one "
                "Commander or Captain"
            )

        half_crew: int = len(self.crew) // 2
        experienced: int = len(
                [c for c in self.crew if c.years_experience >= 5])

        if self.duration_days > 365 and experienced < half_crew:
            raise ValueError(
                "Long missions (> 365 days) need "
                "50% experienced crew (5+ years)"
            )

        is_active: list[bool] = [c.is_active for c in self.crew]

        if not all(is_active):
            raise ValueError("All crew members must be active")
        return self


def print_data(sm: SpaceMission):
    print(f"Mission: {sm.mission_name}")
    print(f"ID: {sm.mission_id}")
    print(f"Destination: {sm.destination}")
    print(f"Duration: {sm.duration_days} days")
    print(f"Budget: ${sm.budget_millions}M")
    print(f"Crew size: {len(sm.crew)}")
    for member in sm.crew:
        print(
            f"  - {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )
    print()


def main():
    # Create Crew
    try:
        sarah = CrewMember(
            member_id='001',
            name='Sarah Connor',
            rank=Rank.COM,
            age=30,
            specialization='Mission Command',
            years_experience=8
        )

        john = CrewMember(
            member_id='002',
            name='John Smith',
            rank=Rank.LIE,
            age=30,
            specialization='Navigation',
            years_experience=8
        )

        alice = CrewMember(
            member_id='003',
            name='Alice Johnson',
            rank=Rank.OFF,
            age=30,
            specialization='Engineering',
            years_experience=8
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'].removeprefix('Value error, ')}")

    print("Space Mission Crew Validation")

    # Create Right Mission
    print("========================================")
    print("Valid mission created:")
    try:
        right_mission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            duration_days=900,
            budget_millions=2500.0,
            crew=[sarah, john, alice]
        )
        print_data(right_mission)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'].removeprefix('Value error, ')}")

    # Create Wrong Mission
    print("========================================")
    print("Expected validation error:")
    try:
        wrong_mission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            duration_days=900,
            budget_millions=2500.0,
            crew=[john, alice]
        )
        print_data(wrong_mission)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg'].removeprefix('Value error, ')}")


if __name__ == "__main__":
    main()
