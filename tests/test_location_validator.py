import unittest
from string import ascii_uppercase

from story_manager.location_validator import (COLON_COUNT_OFF, INVALID_HOUR,
                                              INVALID_MINUTE, LETTER_COUNT_OFF,
                                              NOT_UPPER, UNDERSCORE_COUNT_OFF,
                                              VALID, LocationValidator)


class TestLocationValidity(unittest.TestCase):
    locationValidator = LocationValidator()

    def test_man(self):
        self.assertEqual(
            self.locationValidator.check_location_validity("Man"), VALID)

    def test_esplanade(self):
        valid_hours = [f"{num}" for num in range(1, 13)]
        valid_minutes = ["00", "15", "30", "45"]
        for hour in valid_hours:
            for minute in valid_minutes:
                self.assertEqual(
                    self.locationValidator.check_location_validity(
                        f"Esplanade_{hour}:{minute}"
                    ),
                    VALID,
                )

    def test_valid(self):
        valid_letters = ascii_uppercase
        valid_hours = [f"{num}" for num in range(1, 13)]
        valid_minutes = ["00", "15", "30", "45"]
        for letter in valid_letters:
            for hour in valid_hours:
                for minute in valid_minutes:
                    self.assertEqual(
                        self.locationValidator.check_location_validity(
                            f"{letter}_{hour}:{minute}"
                        ),
                        VALID,
                    )

    def test_invalid_man(self):
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "man"), UNDERSCORE_COUNT_OFF
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "MAN"), UNDERSCORE_COUNT_OFF
        )
        self.assertEqual(
            self.locationValidator.check_location_validity("Manly"),
            UNDERSCORE_COUNT_OFF,
        )

    def test_invalid_random(self):
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "random"), UNDERSCORE_COUNT_OFF
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "RANDOM"), UNDERSCORE_COUNT_OFF
        )
        self.assertEqual(
            self.locationValidator.check_location_validity("Randomly"),
            UNDERSCORE_COUNT_OFF,
        )

    def test_invalid_esplanade(self):
        self.assertEqual(
            self.locationValidator.check_location_validity("esplanade_12:00"),
            LETTER_COUNT_OFF,
        )
        self.assertEqual(
            self.locationValidator.check_location_validity("ESPLANADE_1:15"),
            LETTER_COUNT_OFF,
        )
        self.assertEqual(
            self.locationValidator.check_location_validity("Esplanadey_3:45"),
            LETTER_COUNT_OFF,
        )

    def test_invalid_letter_count(self):
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "AB_1:15"), LETTER_COUNT_OFF
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "_1:15"), LETTER_COUNT_OFF
        )

    def test_invalid_upper_letter(self):
        self.assertEqual(
            self.locationValidator.check_location_validity("a_6:30"), NOT_UPPER
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(";_7:15"), NOT_UPPER
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(" _4:45"), NOT_UPPER
        )

    def test_invalid_colon_count(self):
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "A_130"), COLON_COUNT_OFF
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "K_7:45:00"), COLON_COUNT_OFF
        )

    def test_invalid_hour(self):
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "A_a:30"), INVALID_HOUR
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "A_K:30"), INVALID_HOUR
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "A_0:30"), INVALID_HOUR
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "A_13:30"), INVALID_HOUR
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "A_:30"), INVALID_HOUR
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "A_111:30"), INVALID_HOUR
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "A_.:30"), INVALID_HOUR
        )

    def test_invalid_minute(self):
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "I_1:01"), INVALID_MINUTE
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "I_1:-"), INVALID_MINUTE
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "I_1:50"), INVALID_MINUTE
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "I_4:000"), INVALID_MINUTE
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "I_4:00k"), INVALID_MINUTE
        )
        self.assertEqual(
            self.locationValidator.check_location_validity(
                "I_4:r"), INVALID_MINUTE
        )
