from story.location_validator import LocationValidator

VALID = (True, "")
NO_LOCATION_IN_ROOT = (False, "'location' not present in root")
NO_NAME_IN_CHOICE = (False, "'name' not present in choice")
NAME_NOT_STRING_IN_CHOICE = (False, "'name' not string in choice")
NAME_TOO_LONG_IN_CHOICE = (False, "'name' more than 7 characters in choice")
NO_TEXT_IN_CHOICE = (False, "'text' not present in choice")
TEXT_NOT_STRING_IN_CHOICE = (False, "'text' not string in choice")
NO_CHOICES_IN_CHOICE = (False, "'choices' not present in choice")
CHOICES_NOT_LIST_IN_CHOICE = (False, "'choices' not list in choice")
MORE_THAN_THREE_CHOICES = (False, "More than three choices provided in choice") 

class TreeValidator():
    def check_tree_validity(self, root):
        return self.__check_root_validity(root)

    def __check_root_validity(self, root):
        if "location" not in root:
            return NO_LOCATION_IN_ROOT

        (is_location_valid, location_reason) = LocationValidator().check_location_validity(root["location"])
        (is_choice_valid, choice_reason) = self.__check_choice_validity(root)
    
        if not is_location_valid:
            return (False, location_reason)
        elif not is_choice_valid:
            return (False, choice_reason)
        else:
            return VALID

    def __check_choice_validity(self, choice):
        (is_name_valid, name_reason) = self.__check_name_validity(choice)
        (is_text_valid, text_reason) = self.__check_text_validity(choice)
        (is_choices_valid, choices_reason) = self.__check_choices_validity(choice)
    
        if not is_name_valid:
            return (False, name_reason)
        elif not is_text_valid:
            return (False, text_reason)
        elif not is_choices_valid:
            return (False, choices_reason)
        else:
            return VALID

    def __check_name_validity(self, choice):
        if "name" not in choice:
            return NO_NAME_IN_CHOICE
        elif not isinstance(choice["name"], str):
            return NAME_NOT_STRING_IN_CHOICE
        elif len(choice["name"]) > 7:
            return NAME_TOO_LONG_IN_CHOICE
        else:
            return VALID

    def __check_text_validity(self, choice):
        if "text" not in choice:
            return NO_TEXT_IN_CHOICE
        elif not isinstance(choice["text"], str):
            return TEXT_NOT_STRING_IN_CHOICE
        else:
            return VALID

    def __check_choices_validity(self, choice):
        if "choices" not in choice:
            return NO_CHOICES_IN_CHOICE
        elif not isinstance(choice["choices"], list):
            return CHOICES_NOT_LIST_IN_CHOICE
        elif len(choice["choices"]) > 3:
            return MORE_THAN_THREE_CHOICES
        else:
            for choice in choice["choices"]:
                (is_valid_choice, reason) = self.__check_choice_validity(choice)
                if not is_valid_choice:
                    return (False, reason)
            return VALID
