import json
import unittest
from string import ascii_uppercase

from utils.tree_validator import (CHOICE_TEXT_NOT_STRING_IN_CHOICE,
                                          CHOICES_NOT_LIST_IN_CHOICE,
                                          ID_NOT_STRING_IN_CHOICE,
                                          MORE_THAN_THREE_CHOICES,
                                          NAME_NOT_STRING_IN_CHOICE,
                                          NAME_TOO_LONG_IN_CHOICE,
                                          NO_CHOICES_IN_CHOICE,
                                          NO_ID_IN_CHOICE, NO_LOCATION_IN_ROOT,
                                          NO_NAME_IN_CHOICE,
                                          NO_SELECTIONTEXT_IN_CHOICE,
                                          NO_STORYTEXT_IN_CHOICE,
                                          SELECTIONTEXT_NOT_STRING_IN_CHOICE,
                                          STORYTEXT_NOT_STRING_IN_CHOICE,
                                          UNDERSCORE_COUNT_OFF, VALID,
                                          TreeValidator)
from tests import test_data


class TestTreeValidity(unittest.TestCase):
    treeValidator = TreeValidator()

    def test_only_root_tree(self):
        self.assertEqual(
            self.treeValidator.check_tree_validity(test_data.only_root), VALID
        )

    def test_simple_tree(self):
        self.assertEqual(
            self.treeValidator.check_tree_validity(
                test_data.simple_tree), VALID
        )

    def test_complex_tree(self):
        self.assertEqual(
            self.treeValidator.check_tree_validity(
                test_data.complex_tree), VALID
        )

    def test_no_location(self):
        no_loc = json.loads(
            """
            { 
                "id": "a",
                "name": "root",
                "selectionText": "",
                "storyText": "lorem ipsum",
                "choices": {}
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(no_loc), NO_LOCATION_IN_ROOT
        )

    def test_invalid_location(self):
        # Already tested exhaustively above - just confirm that any of the location issues are caught
        invalid_loc = json.loads(
            """
            { 
                "id": "a",
                "location": "bad",
                "name": "root",
                "selectionText": "",
                "storyText": "lorem ipsum",
                "choices": []
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(
                invalid_loc), UNDERSCORE_COUNT_OFF
        )

    def test_no_name(self):
        no_name = json.loads(
            """
            { 
                "id": "a",
                "location": "A_1:30",
                "selectionText": "",
                "storyText": "lorem ipsum",
                "choices": []
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(no_name), NO_NAME_IN_CHOICE
        )

    def test_invalid_name_type(self):
        invalid_name_type = json.loads(
            """
            { 
                "id": "a",
                "location": "A_1:30",
                "name": 123,
                "selectionText": "",
                "storyText": "lorem ipsum",
                "choices": []
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(invalid_name_type),
            NAME_NOT_STRING_IN_CHOICE,
        )

    def test_invalid_name_length(self):
        invalid_name_type = json.loads(
            """
            { 
                "id": "a",
                "location": "A_1:30",
                "name": "borem snorem",
                "selectionText": "",
                "storyText": "lorem ipsum",
                "choices": []
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(invalid_name_type),
            NAME_TOO_LONG_IN_CHOICE,
        )

    def test_no_selectiontext(self):
        no_text = json.loads(
            """
            { 
                "id": "a",
                "location": "A_1:30",
                "name": "glom",
                "storyText": "flom",
                "choices": []
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(
                no_text), NO_SELECTIONTEXT_IN_CHOICE
        )

    def test_invalid_storytext_type(self):
        invalid_text_type = json.loads(
            """
            { 
                "id": "a",
                "location": "A_1:30",
                "name": "stroop",
                "selectionText": ["scroop"],
                "storyText": "bloop",
                "choices": []
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(invalid_text_type),
            SELECTIONTEXT_NOT_STRING_IN_CHOICE,
        )

    def test_no_storytext(self):
        no_text = json.loads(
            """
            { 
                "id": "a",
                "location": "A_1:30",
                "name": "borem",
                "selectionText": "",
                "choices": []
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(
                no_text), NO_STORYTEXT_IN_CHOICE
        )

    def test_invalid_storytext_type(self):
        invalid_text_type = json.loads(
            """
            { 
                "id": "a",
                "location": "A_1:30",
                "name": "boop",
                "selectionText": "",
                "storyText": ["slip"],
                "choices": []
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(invalid_text_type),
            STORYTEXT_NOT_STRING_IN_CHOICE,
        )

    def test_no_choices(self):
        no_choices = json.loads(
            """
            { 
                "id": "a",
                "location": "A_1:30",
                "name": "flound",
                "selectionText": "",
                "storyText": "lorem ipsum"
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(
                no_choices), NO_CHOICES_IN_CHOICE
        )

    def test_invalid_choices_type(self):
        invalid_choice_type = json.loads(
            """
            { 
                "id": "a",
                "location": "A_1:30",
                "name": "fun!",
                "selectionText": "",
                "storyText": "lorem ipsum",
                "choices": "silly rabbit"
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(invalid_choice_type),
            CHOICES_NOT_LIST_IN_CHOICE,
        )

    #  def test_too_many_choices(self): # This test is like life
    #    too_many_choices = json.loads('''
    # {
    #  "id": "a",
    #  "location": "A_1:30",
    #  "name": "fun!",
    #  "selectionText": "",
    #  "storyText": "lorem ipsum",
    #  "choices": [
    #    {
    #      "id": "b",
    #      "name": "1",
    #      "selectionText": "yo",
    #      "storyText": "a",
    #      "choices": []
    #    },
    #    {
    #      "id": "c",
    #      "name": "2",
    #      "selectionText": "momma",
    #      "storyText": "b",
    #      "choices": []
    #    },
    #    {
    #      "id": "d",
    #      "name": "3",
    #      "selectionText": "so",
    #      "storyText": "c",
    #      "choices": []
    #    },
    #    {
    #      "id": "e",
    #      "name": "4",
    #      "selectionText": "awesome",
    #      "storyText": "sad",
    #      "choices": []
    #    }
    #  ]
    # }
    #    ''')
    #    self.assertEqual(self.treeValidator.check_tree_validity(too_many_choices), MORE_THAN_THREE_CHOICES)

    def test_invalid_nested_choice(self):
        invalid_nested_choice = json.loads(
            """
            {
                "id": "a",
                "location": "A_1:30",
                "name": "goober",
                "selectionText": "",
                "storyText": "floop",
                "choices": [
                    {
                        "id": "b",
                        "selectionText": "hobswapper",
                        "storyText": "gobstopper",
                        "choices": {}
                    }
                ]
            }
            """
        )
        self.assertEqual(
            self.treeValidator.check_tree_validity(invalid_nested_choice),
            NO_NAME_IN_CHOICE,
        )
