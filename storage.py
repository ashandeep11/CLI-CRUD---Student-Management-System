import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "students.json"


def initialize_storage():
    """Create the JSON file if it does not exist."""

    if not DATA_FILE.exists():
        DATA_FILE.write_text(
            "[]",
            encoding="utf-8"
        )


def load_students():
    """Load student records from JSON."""

    initialize_storage()

    try:
        with DATA_FILE.open(
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):

        print(
            "Warning: Could not read existing data. "
            "Starting with empty records."
        )

        return []


def save_students(students):
    """Save student records to JSON."""

    with DATA_FILE.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            students,
            file,
            indent=4
        )