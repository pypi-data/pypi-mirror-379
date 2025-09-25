'''
- Module providing a custom date provider for pseudonymization
- This module defines the `CustomDateProvider` class, which extends the 
`BaseProvider` from `Faker`
'''
import re
import random
from datetime import datetime, timedelta
from typing import Optional, Dict, Tuple
from enum import Enum
import dateutil.parser
from faker.providers import BaseProvider
from unidecode import unidecode

class DateType(Enum):
    '''
    Enum representing different types of date formats encountered in the pseudonymization process,
    This enumeration is used to categorize the various date formats being processed,
    which helps determine the appropriate formatting for pseudonymized dates
    
    Attributes:
        NORMAL (int): Standard date
        ONLY_MONTH (int): Date string contains only a month
        ONLY_DAY (int): Date string contains only a day
        SPECIFIC_MONTH (int): Special mid-month format ("mi-janvier")
        SPECIFIC_DATE (int): Month/year format without a day component ("MM/YYYY")
    '''
    NORMAL = 0
    ONLY_MONTH = 1
    ONLY_DAY = 2
    SPECIFIC_MONTH = 3
    SPECIFIC_DATE = 4

class CustomDateProvider(BaseProvider):
    """
    A custom date provider that manage frensh day and month names, including different formats
    
    Attributes:
        _sliding_cache (dict): A cache for storing temporary date related values
        days_of_week (list[str]): List of French names for the days of the week
        MONTHS (dict[str, str]): Mapping of full French month names to their numerical
            representation
        incorrect_months (dict[str, str]): Mapping of common incorrect month abbreviations
            to their numerical representation
        month_names (dict[str, str]): Reverse mapping of numerical month representations
            to full French names
    
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the CustomDateProvider with predefined mappings for days and months

        Args:
            *args: Positional arguments passed to the BaseProvider
            **kwargs: Keyword arguments passed to the BaseProvider
        """
        super().__init__(*args, **kwargs)
        self._sliding_cache = {}

        self.days_of_week = [
            "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"
        ]

        self.months = {
            "janvier": "01", "février": "02", "mars": "03", "avril": "04", 
            "mai": "05", "juin": "06", "juillet": "07", "août": "08", 
            "septembre": "09", "octobre": "10", "novembre": "11", "décembre": "12"
        }

        self.incorrect_months = {
            "janv": "01", "jan": "01", "fevr": "02", "fev": "02", "mar": "03",
            "avr": "04", "juil": "07", "aout": "08", "sep": "09",
            "sept": "09", "oct": "10", "nov": "11", "dec": "12"
        }

        self.month_names = {v: k for k, v in self.months.items()}

    def _get_sliding_for_patient(self, ipp_patient: str, max_sliding: int) -> int:
        """
        Returns a consistent sliding for a given patient
        This function ensures thta the sliding value remains the same for the same
        patient and max_sliding value, it uses a deterministic approch by seeding
        the random number generator with unique cache key, ensuring reproducibilty
        
        Args:
            ipp_patient (str): Unique identifier patient
            max_sliding (int): Maximum value for sliding
        
        Returns:
            int: Number of sliding days
        """
        cache_key = f"{ipp_patient}_{max_sliding}"

        if cache_key not in self._sliding_cache:
            # seed the random generator with a deterministic key to ensure
            # the saùe slifding value is generated for the same patient
            random.seed(cache_key)
            self._sliding_cache[cache_key] = random.randint(1, max_sliding)

        return self._sliding_cache[cache_key]

    def pseudonymize_date(self, ipp_patient:str, date_str: str, max_sliding: int) -> str:
        """
        Pseudonymises a date based on a unique IPP.
        
        Args:
            ipp_patient (str): Unique identifier patient
            date_str (str): The date to be pseudonymised
            max_sliding (int): Maximum value for sliding

        Returns:
            str: The pseudonymised date, formatted like the original
        """

        # Extrct the day of the week and the date
        day_of_week, clean_date_str = self._extract_day_and_date_string(date_str)

        # Normalize months
        month_is_alpha, clean_date_str = self._normalize_months(clean_date_str)

        # Normalize dates format
        clean_date_str, date_format = self._normalize_date_format(
            clean_date_str, month_is_alpha
        )

        # Parse date
        try:
            original_date = dateutil.parser.parse(clean_date_str, dayfirst=True)
            # More precise verification for the "MM YYYY" format (without day)
            if re.match(r'^(\d{1,2})[\s/-](\d{4})$', clean_date_str):
                # If the date is in month/year format, set the day to 1 instead of today day
                original_date = original_date.replace(day=1)
        except ValueError:
            return date_str

        # Get format and sliding value
        original_format = self._detect_date_format(clean_date_str)

        if original_format == "[DATE]":
            return "[DATE]"
        
        sliding_days = self._get_sliding_for_patient(ipp_patient, max_sliding)


        # Apply sliding
        pseudonymized_date = original_date + timedelta(days=sliding_days)

        # Format pseudonymized date
        pseudonymized_date_str = self._format_pseudonymized_date(
            pseudonymized_date,
            original_format,
            month_is_alpha,
            day_of_week
        )

        # Handle specific cases
        if date_format == DateType.ONLY_MONTH:#if only_month:
            return self.month_names.get(pseudonymized_date.strftime("%m"), "01")

        if date_format == DateType.SPECIFIC_MONTH:#if specific_month:
            return f"mi-{self.month_names.get(pseudonymized_date.strftime('%m'), '01')}"

        if date_format == DateType.ONLY_DAY:#if only_day:
            return f"{pseudonymized_date.strftime('%d')}"

        if date_format == DateType.SPECIFIC_DATE:#if specific_date:
            return f"{pseudonymized_date.strftime('%m/%Y')}"

        return pseudonymized_date_str


    def _extract_day_and_date_string(self, date_str: str) -> Tuple[Optional[str], str]:
        """
        Extracts the day of the week from a given date string and returns 
        the cleaned date string without the day of the week.

        Args:
            date_str (str): The input date string

        Returns:
            Tuple[Optional[str], str]: A tuple containing the extracted day of the week (if found) 
            and the cleaned date string.
        """
        day_of_week = None
        for day in self.days_of_week:
            if day in date_str.lower():
                day_of_week = day
                break  # Stop la boucle at the first match

        clean_date_str = re.sub(
            rf"\b(?:{'|'.join(self.days_of_week)})\b",
            "",
            date_str,
            flags=re.IGNORECASE
        ).strip()

        return day_of_week, clean_date_str

    def _normalize_months(self, clean_date_str: str) -> Tuple[bool, str, Dict[str, str]]:
        """
        Converts alphabetical month names into numeric format
        
        Args:
            clean_date_str (str): The input date string
        Returns:
            Tuple[bool, str, Dict[str, str]]:
                - A boolean indicating if an alphabetical month was found
                - The date string with numeric month values
                - A dictionary mapping original month names to their numeric values
        """
        month_is_alpha = False
        result_date = clean_date_str
        month_dict = {**self.months, **self.incorrect_months}

        # Normalize input date (remove accents + lowercase)
        normalized_input = unidecode(clean_date_str).lower()

        for month_name, month_number in month_dict.items():
            # Normalizze month_name (remove accents + lowercase)
            normalized_month = unidecode(month_name).lower()

            # Check if the normalized month_name is in the normalized input date
            if normalized_month in normalized_input:
                month_is_alpha = True
                # Function that replaces a specific month name with its numeric value
                # while ensuring that only exact matches are replaced
                def make_replacer(target_month, replacement):
                    def replace_func(match):
                        if unidecode(match.group(0)).lower() == target_month:
                            return replacement
                        return match.group(0)
                    return replace_func

                rep = make_replacer(normalized_month, month_number)
                result_date = re.sub(r'\b\w+\b', rep, result_date)

        return month_is_alpha, result_date

    def _normalize_date_format(self, clean_date_str: str,
                               month_is_alpha: bool) -> Tuple[str, bool, bool, bool]:
        """
        Normalizes different date formats into a consistent structure
        
        Args:
            clean_date_str (str): The input date string
            month_is_alpha (bool): Indicates whether the month is in alphabetical format

        Returns:
            Tuple[str, bool, bool, bool]: 
                - The normalized date string
                - A boolean indicating if the date contains only a month
                - A boolean indicating if the date contains only a day
                - A boolean indicating if the date specifies a specific month ("mi-janvier")
        """
        #only_month, only_day, specific_month, specific_date = False, False, False, False
        format_type = DateType.NORMAL
        # Treat ambiguous formats first
        if re.match(r'^\d{2}\s*[/\.]\s*\d{2}$', clean_date_str):
            clean_date_str = self._handle_ambiguous_format(clean_date_str)

        format_handlers = [
            # "12.05", "04.11"
            (r"^\d{2}\.\d{2}$", self._handle_ambiguous_format),
            # "12 / 05", "04/11"
            (r"^\d{2}\s*/\s*\d{2}$", self._handle_ambiguous_format),
            # "12 . 05", "04 . 11"
            (r"^\d{2} \. \d{2}$", lambda m: re.sub(r" \. (\d{2})$", r" 20\1", m) if month_is_alpha
                                                                                 else m),
            # "12", "'avril -> '04"
            (r"^(\d{2}|'\d{2})$", lambda m: self._handle_single_month(m, month_is_alpha)),
            # "9", "15"
            #(r"^\d{1,2}$", self._handle_single_day), # lambda m: self._handle_single_day(m)
            # "12.05 2023", "04.11 1999"
            (r"^\d{2}\.\d{2} \d{4}$", lambda m: re.sub(r"^(\d{2})\.(\d{2}) (\d{4})$",
                                                       r"\1 \2 \3", m)),
            # "12 05.2023", "04 11.1999" 
            (r"^\d{2} \d{2}\.\d{4}$", lambda m: re.sub(r"^(\d{2}) (\d{2})\.(\d{4})$",
                                                       r"\1/\2/\3", m)),
            # "mi-05", "mi - 11"
            (r"^mi\s*-\s*(\d{2})$", self._handle_specific_month),
            # "07 / 2018", "09 / 2020"
            (r"^\d{2}\s*/\s*\d{4}$", lambda m: re.sub(r"^(\d{2})\s*/\s*(\d{4})$", r"01/\1/\2", m)),
            # "09 - 2019", "07 - 2020"
            (r"^\d{2}\s*-\s*\d{4}$", lambda m: re.sub(r"^(\d{2})\s*-\s*(\d{4})$", r"01/\1/\2", m)),
            # "09 . 2019", "07 . 2020"
            (r"^\d{2}\s*\.\s*\d{4}$", lambda m: re.sub(r"^(\d{2})\s*\.\s*(\d{4})$", r"01/\1/\2",m)),
            # "09 22"
            (r"^\d{2}\s\d{2}$", lambda m: re.sub(r"^(\d{2})\s(\d{2})$", r"\1 20\2", m)),
        ]
        for pattern, handler in format_handlers:
            match = re.match(pattern, clean_date_str, re.IGNORECASE)
            if match:
                clean_date_str = handler(clean_date_str)

                if pattern == r"^(\d{2}|'\d{2})$" and month_is_alpha:
                    format_type = DateType.ONLY_MONTH#only_month = True
                elif pattern == r"^\d{1,2}$" and not month_is_alpha:
                    format_type = DateType.ONLY_DAY#only_day = True
                elif pattern == r"^mi\s*-\s*(\d{2})$":
                    format_type = DateType.SPECIFIC_MONTH#specific_month = True
                elif pattern in [r"^\d{2}\s*/\s*\d{4}$",
                                 r"^\d{2}\s*-\s*\d{4}$",
                                 r"^\d{2}\.\d{4}$",
                                 r"^\d{2}\s*\.\s*\d{4}$"]:
                    format_type = DateType.SPECIFIC_DATE#specific_date = True

                break

        return clean_date_str, format_type#only_month, only_day, specific_month, specific_date

    def _handle_single_month(self, date_str: str, month_is_alpha: bool) -> str:
        """
        Handles a date format containing only a month

        Args:
            date_str (str): The input date string
            month_is_alpha (bool): Indicates whether the month is in alphabetical format

        Returns:
            str: The formatted date string
        """
        if month_is_alpha:
            date_str = date_str.lstrip("'")
            return f"01.{date_str}.1970"

        return date_str

    def _handle_specific_month(self, date_str):
        """
        Handles a date format containing 'mi-' followed by a month

        Args:
            date_str (str): The input date string ('mi-janvier')

        Returns:
            str: The formatted date string
        """
        month_name = date_str.split('-')[1].strip()
        return f"01/{month_name}/1970"

    def _is_valid_month(self, value: str) -> bool:
        """
        Check if a value is valid month (1-12) ---> To check date such as (11/21) 
        wich is a month/year and (25/10) wich is day/month
        
        Args:
            value (str): The input value to check
        
        Returns:
            bool: True if the value is a valid month, false otherwise"""
        try:
            value = int(value)
            return 1 <= value <= 12
        except ValueError:
            return False

    def _is_valid_day(self, value):
        """
        Checks if a value is a valid day (1-31)
        
        Args:
            value (str): The input value to check

        Returns:
            bool: True if the value is a valid day, False otherwise
            """
        try:
            value = int(value)
            return 1 <= value <= 31
        except ValueError:
            return False

    def _determine_date_format(self, first_num: str, second_num: str) -> str | None:
        """
        Determines whether the format is day/month or month/year
        
        Args:
            first_num (str): First number in the date
            second_num (str): Second number in the date
        
        Returns:
            str | None: 'day_month' if the format is day/month,
                        'month_year' if the format is month/year,
                        None if the format is undetermined.
        """
        first_num = int(first_num)
        second_num = int(second_num)

        # If the first number > 12 it must be a day
        if first_num > 12:
            if self._is_valid_month(second_num):
                return 'day_month'
            return None

        # If the first number is a valid month
        if self._is_valid_month(first_num):
            # If the second number is ≤ 12 prefer day/month if it is a valid day
            if second_num <= 12 and self._is_valid_day(first_num):
                return 'day_month'
            # Otherwise, treat as month/year
            return 'month_year'

        return None

    def _handle_ambiguous_format(self, date_str: str) -> str:
        """
        Handles ambiguous date formats like DD/MM or MM/YY
        
        Args:
            date_str (str): The date string to analyze
        
        Returns:
            str: The normalized date string
        """
        clean_date = re.sub(r'\s+', '', date_str)
        match = re.match(r'^(\d{2})[/\.](\d{2})$', clean_date)

        if not match:
            return date_str

        first_num, second_num = match.groups()
        format_type = self._determine_date_format(first_num, second_num)

        if format_type == 'day_month':
            return f"{first_num}/{second_num}"

        if format_type == 'month_year':
            return f"{first_num}/20{second_num}"

        return date_str

    def _format_pseudonymized_date(self,
                                   pseudonymized_date: str,
                                   original_format: str,
                                   month_is_alpha: bool,
                                   day_of_week: bool) -> str:
        """
        Format a pseudonymized date according to the provided format, 
        converting numeric months to alphabetical if necessary, 
        and optionally adding the day of the week
        
        Args:
            pseudonymized_date (str): The date to be formated
            original_format (str): The format to apply when formatting the pseudonymized date
            month_is_alpha (bool): A boolean value indicating whether date contains months in alpha
            day_of_week (str): The day of the week to add to the formatted date (if provided)
        
        Returns:
            str: The pseudonymized date as a string in the specified format
        """
        pseudonymized_date_str = pseudonymized_date.strftime(original_format)

        if month_is_alpha:
            separator = next((sep for sep in [" ", ".", "/", "-"] if sep in pseudonymized_date_str),
                             None)
            if separator:
                parts = pseudonymized_date_str.split(separator)
            else:
                return pseudonymized_date_str

            def process_month(parts, index=1):
                month = parts[index]
                new_month = self.month_names.get(month)
                if new_month:
                    return re.sub(rf"\b{month}\b", new_month, pseudonymized_date_str)
                return pseudonymized_date_str

            # Case 1: day, month, year
            if len(parts) == 3 and parts[1] != ".":
                pseudonymized_date_str = process_month(parts, 1)

            # Case 2: month with a dot (month, year or month, day)
            elif len(parts) == 3 and parts[1] == ".":
                pseudonymized_date_str = process_month(parts, 0)

            # Case 3: month, year (with or without dot in month)
            elif len(parts) == 2 and (1 <= int(parts[0][:-1] if
                                        parts[0].endswith(".") else
                                        parts[0]) <= 12 and
                                        1900 <= int(parts[1])):
                month = parts[0][:-1] if parts[0].endswith(".") else parts[0]
                pseudonymized_date_str = process_month([month, parts[1]], 0)

            # Case 4: day, month (1-31, 1-12)
            elif len(parts) == 2 and (1 <= int(parts[0]) <= 31 and 1 <= int(parts[1]) <= 12):
                pseudonymized_date_str = process_month(parts, 1)

        # Add day of week if exists
        if day_of_week:
            pseudonymized_date_str = f"{day_of_week} {pseudonymized_date_str}"

        return pseudonymized_date_str

    def _convert_month_to_alpha(self, date_str: str) -> str:
        """
        Convert numeric months to alphabetical
        
        Args:
            date_str (str): The date string to check
        
        Returns:
            Converted string date
        """
        for month_num, month_alpha in self.month_names.items():
            date_str = re.sub(rf"\b{month_num}\b", month_alpha, date_str)
        return date_str

    def _detect_date_format(self, date_str: str) -> Optional[str]:
        """
        Detects the input date format from a list of possible formats
        
        Args:
            date_str (str): The date string to check
        
        Returns:
            Optional[str]: Date format detected
            
        Raises:
            ValueError: If no format corresponds to the given date
        
        """
        formats = [ "%d/%m", "%m/%Y",#"%m / %d",
            "%m.%Y", "%d-%m-%Y", "%d.%m.%Y", "%d/%m/%Y", "%d . %m . %Y", 
            "%d / %m", "%m / %Y", "%m / %y", "%d - %m - %Y", "%B %d, %Y", 
            "%d %B %Y", "%Y . %m . %d", "%b . %d", "%b %Y", "%m . %Y",
            "%Y", "%d %B", "%d / %m / %Y", "%d %m %Y", "%m %Y", 
            "%m . %Y", "%m / %Y", "%m . %y", "%d / %m / %y",
            "%d %m", "%d . %m", "%m - %y", "%m - %Y", "%m-%Y",
            "%d . %m . %y", "%d . %m %Y", "%d %m . %Y", "%m. %Y", "%m", "%d",
            "%Y/%m/%d", "%Y-%m-%d", "%d/%m/%y", "%d.%m.%y", "%d %m.%Y",
            "%Y-%m", "%Y/%m", "%d-%m"
        ]
        # Remove spaces between separators
        date_str = re.sub(r"\s*([/.-])\s*", r"\1", date_str)
        for fmt in formats:
            try:
                datetime.strptime(date_str, fmt)
                return fmt
            except ValueError:
                continue
        #raise ValueError(f"Impossible to detect format for this date : {date_str}")
        print(f"Date format not found for {date_str}")
        return "[DATE]"