#!/usr/bin/env python3
# alien_contact.py

from typing import Optional
from enum import Enum
from datetime import datetime

try:
    from pydantic import BaseModel, model_validator, Field, ValidationError
except Exception as e:
    print(e)
    print("Try this instructions:")
    print("    python3 -m venv venv")
    print("    source venv/bin/activate")
    print("    pip python-pydantic")
    print("    python3 alien_contact.py")
    exit(1)


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_valid_contact(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least "
                "3 witnesses"
            )
        if (
            self.contact_type == ContactType.physical
            and not self.is_verified
        ):
            raise ValueError("Physical contact reports must be verified")
        if (
            self.signal_strength > 7.0
            and self.message_received is None
        ):
            raise ValueError(
                "Strong signals (> 7.0) should "
                "include received messages"
            )

        return self


def print_error(e: ValidationError):
    for error in e.errors():
        print(f"{error['msg']}")


def print_data(ac: AlienContact):
    print(f"ID: {ac.contact_id}")
    print(f"Type: {ac.contact_type.name}")
    print(f"Location: {ac.location}")
    print(f"Signal: {ac.signal_strength}")
    print(f"Duration: {ac.duration_minutes}")
    print(f"Witnesses: {ac.witness_count}")
    print(f"Message: {ac.message_received}")
    print(f"Verified: {ac.is_verified}")
    print()


def main():

    print("Alien Contact Log Validation")
    print("==========================================")
    print("Valid contact report:")
    try:
        ac_right = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-01-22T00:00:00",
            location="Atacama Desert, Chile",
            contact_type="visual",
            signal_strength=9.6,
            duration_minutes=99,
            witness_count=11,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False)
        print_data(ac_right)
    except ValidationError as e:
        print_error(e)

    print("==========================================")
    print("Expected validation error:")
    try:
        ac_wrong = AlienContact(
            contact_id="aC_2024_001",
            timestamp="2024-01-22T00:00:00",
            location="Atacama Desert, Chile",
            contact_type="physical",
            signal_strength=9.6,
            duration_minutes=99,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True)
        print_data(ac_wrong)
    except ValidationError as e:
        print_error(e)


main()
