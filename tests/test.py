import json
from location_validator import *
from tree_validator import *
from string import ascii_uppercase
import test_data
import unittest

class TestLocationValidity(unittest.TestCase):
  locationValidator = LocationValidator()

  def test_man(self):
    self.assertEqual(self.locationValidator.check_location_validity("Man"), VALID)

  def test_esplanade(self):
    valid_hours = [f"{num}" for num in range(1, 13)]
    valid_minutes = ["00", "15", "30", "45"]
    for hour in valid_hours:
        for minute in valid_minutes:
            self.assertEqual(self.locationValidator.check_location_validity(f"Esplanade_{hour}:{minute}"), VALID)

  def test_valid(self):
    valid_letters = ascii_uppercase
    valid_hours = [f"{num}" for num in range(1, 13)]
    valid_minutes = ["00", "15", "30", "45"]
    for letter in valid_letters:
        for hour in valid_hours:
            for minute in valid_minutes:
                self.assertEqual(self.locationValidator.check_location_validity(f"{letter}_{hour}:{minute}"), VALID)

  def test_invalid_man(self):
    self.assertEqual(self.locationValidator.check_location_validity("man"), UNDERSCORE_COUNT_OFF)
    self.assertEqual(self.locationValidator.check_location_validity("MAN"), UNDERSCORE_COUNT_OFF)
    self.assertEqual(self.locationValidator.check_location_validity("Manly"), UNDERSCORE_COUNT_OFF)

  def test_invalid_esplanade(self):
    self.assertEqual(self.locationValidator.check_location_validity("esplanade_12:00"), LETTER_COUNT_OFF)
    self.assertEqual(self.locationValidator.check_location_validity("ESPLANADE_1:15"), LETTER_COUNT_OFF)
    self.assertEqual(self.locationValidator.check_location_validity("Esplanadey_3:45"), LETTER_COUNT_OFF)

  def test_invalid_letter_count(self):
    self.assertEqual(self.locationValidator.check_location_validity("AB_1:15"), LETTER_COUNT_OFF)
    self.assertEqual(self.locationValidator.check_location_validity("_1:15"), LETTER_COUNT_OFF)

  def test_invalid_upper_letter(self):
    self.assertEqual(self.locationValidator.check_location_validity("a_6:30"), NOT_UPPER)
    self.assertEqual(self.locationValidator.check_location_validity(";_7:15"), NOT_UPPER)
    self.assertEqual(self.locationValidator.check_location_validity(" _4:45"), NOT_UPPER)

  def test_invalid_colon_count(self):
    self.assertEqual(self.locationValidator.check_location_validity("A_130"), COLON_COUNT_OFF)
    self.assertEqual(self.locationValidator.check_location_validity("K_7:45:00"), COLON_COUNT_OFF)

  def test_invalid_hour(self):
    self.assertEqual(self.locationValidator.check_location_validity("A_a:30"), INVALID_HOUR)
    self.assertEqual(self.locationValidator.check_location_validity("A_K:30"), INVALID_HOUR)
    self.assertEqual(self.locationValidator.check_location_validity("A_0:30"), INVALID_HOUR)
    self.assertEqual(self.locationValidator.check_location_validity("A_13:30"), INVALID_HOUR)
    self.assertEqual(self.locationValidator.check_location_validity("A_:30"), INVALID_HOUR)
    self.assertEqual(self.locationValidator.check_location_validity("A_111:30"), INVALID_HOUR)
    self.assertEqual(self.locationValidator.check_location_validity("A_.:30"), INVALID_HOUR)

  def test_invalid_minute(self):
    self.assertEqual(self.locationValidator.check_location_validity("I_1:01"), INVALID_MINUTE)
    self.assertEqual(self.locationValidator.check_location_validity("I_1:-"), INVALID_MINUTE)
    self.assertEqual(self.locationValidator.check_location_validity("I_1:50"), INVALID_MINUTE)
    self.assertEqual(self.locationValidator.check_location_validity("I_4:000"), INVALID_MINUTE)
    self.assertEqual(self.locationValidator.check_location_validity("I_4:00k"), INVALID_MINUTE)
    self.assertEqual(self.locationValidator.check_location_validity("I_4:r"), INVALID_MINUTE)

class TestTreeValidity(unittest.TestCase):
  treeValidator = TreeValidator()

  def test_only_root_tree(self):
    self.assertEqual(self.treeValidator.check_tree_validity(test_data.only_root), VALID)

  def test_simple_tree(self):
    self.assertEqual(self.treeValidator.check_tree_validity(test_data.simple_tree), VALID)

  def test_complex_tree(self):
    self.assertEqual(self.treeValidator.check_tree_validity(test_data.complex_tree), VALID)

  def test_no_location(self):
    no_loc = json.loads('''
{ 
  "name": "root",
  "text": "lorem ipsum",
  "choices": []
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(no_loc), NO_LOCATION_IN_ROOT)

  def test_invalid_location(self):
    # Already tested exhaustively above - just confirm that any of the location issues are caught
    invalid_loc = json.loads('''
{ 
  "location": "bad",
  "name": "root",
  "text": "lorem ipsum",
  "choices": []
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(invalid_loc), UNDERSCORE_COUNT_OFF)

  def test_no_name(self):
    no_name = json.loads('''
{ 
  "location": "A_1:30",
  "text": "lorem ipsum",
  "choices": []
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(no_name), NO_NAME_IN_CHOICE)

  def test_invalid_name_type(self):
    invalid_name_type = json.loads('''
{ 
  "location": "A_1:30",
  "name": 123,
  "text": "lorem ipsum",
  "choices": []
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(invalid_name_type), NAME_NOT_STRING_IN_CHOICE)

  def test_no_text(self):
    no_text = json.loads('''
{ 
  "location": "A_1:30",
  "name": "lorem ipsum",
  "choices": []
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(no_text), NO_TEXT_IN_CHOICE)

  def test_invalid_text_type(self):
    invalid_text_type = json.loads('''
{ 
  "location": "A_1:30",
  "name": "boop snoop",
  "text": ["slip"],
  "choices": []
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(invalid_text_type), TEXT_NOT_STRING_IN_CHOICE)

  def test_no_choices(self):
    no_choices = json.loads('''
{ 
  "location": "A_1:30",
  "name": "flounders",
  "text": "lorem ipsum"
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(no_choices), NO_CHOICES_IN_CHOICE)

  def test_invalid_choices_type(self):
    invalid_choice_type = json.loads('''
{ 
  "location": "A_1:30",
  "name": "fun!",
  "text": "lorem ipsum",
  "choices": "silly rabbit"
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(invalid_choice_type), CHOICES_NOT_LIST_IN_CHOICE)

  def test_too_many_choices(self): # This test is like life
    too_many_choices = json.loads('''
{ 
  "location": "A_1:30",
  "name": "fun!",
  "text": "lorem ipsum",
  "choices": [
    {
      "name": "1",
      "text": "a",
      "choices": []
    },
    {
      "name": "2",
      "text": "b",
      "choices": []
    },
    {
      "name": "3",
      "text": "c",
      "choices": []
    },
    {
      "name": "4",
      "text": "sad",
      "choices": []
    }
  ]
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(too_many_choices), MORE_THAN_THREE_CHOICES)

  def test_invalid_nested_choice(self):
    invalid_nested_choice = json.loads('''
{
  "location": "A_1:30",
  "name": "goober",
  "text": "floop",
  "choices": [
    {
      "text": "gobstopper",
      "choices": []
    }
  ]
}
    ''')
    self.assertEqual(self.treeValidator.check_tree_validity(invalid_nested_choice), NO_NAME_IN_CHOICE)


if __name__ == '__main__':
    unittest.main()