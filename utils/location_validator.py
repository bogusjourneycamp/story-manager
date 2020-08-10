VALID = (True, "")
UNDERSCORE_COUNT_OFF = (False, "Too many or too few underscores")
LETTER_COUNT_OFF = (False, "Too many or too few letters")
NOT_UPPER = (False, "Not an upper case letter")
COLON_COUNT_OFF = (False, "Too many or too few colons")
INVALID_HOUR = (False, "Invalid hour")
INVALID_MINUTE = (False, "Invalid minutes")


class LocationValidator:
    def check_location_validity(self, location):
        # Handle 'Man' special case
        if location == "Man" or location == "Random":
            return VALID

        letter_and_time = location.split("_")
        if len(letter_and_time) != 2:
            return UNDERSCORE_COUNT_OFF

        letter = letter_and_time[0]
        time = letter_and_time[1]

        (is_valid_letter, letter_reason) = self.__check_letter_validity(letter)
        (is_valid_time, time_reason) = self.__check_time_validity(time)

        if not is_valid_letter:
            return (False, letter_reason)
        elif not is_valid_time:
            return (False, time_reason)
        else:
            return VALID

    def __check_letter_validity(self, letter):
        # Handle "Esplanade" special case
        if letter == "Esplanade":
            return VALID
        elif len(letter) != 1:
            return LETTER_COUNT_OFF
        elif not letter.isupper():
            return NOT_UPPER
        else:
            return VALID

    def __check_time_validity(self, time):
        time_list = time.split(":")
        if len(time_list) != 2:
            return COLON_COUNT_OFF

        hour = time_list[0]
        minute = time_list[1]

        (is_valid_hour, reason1) = self.__check_hour_validity(hour)
        (is_valid_minute, reason2) = self.__check_minute_validity(minute)

        if not is_valid_hour:
            return (False, reason1)
        elif not is_valid_minute:
            return (False, reason2)
        else:
            return VALID

    def __check_hour_validity(self, hour):
        valid_hours = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"}
        if hour in valid_hours:
            return VALID
        else:
            return INVALID_HOUR

    def __check_minute_validity(self, minute):
        valid_minutes = {"00", "15", "30", "45"}
        if minute in valid_minutes:
            return VALID
        else:
            return INVALID_MINUTE
