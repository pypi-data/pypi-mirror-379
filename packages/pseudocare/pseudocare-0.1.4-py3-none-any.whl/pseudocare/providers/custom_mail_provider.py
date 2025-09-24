'''
- Module providing a custom email provider for pseudonymization
- This module defines the `CustomMailProvider` class, which extends the 
`BaseProvider` from `Faker`

This custom provider is specific for Reims's hospital, so use it as an example.
'''
import re
import random
import string
from typing import Dict, Optional
from faker.providers import BaseProvider
from faker import Faker

class CustomMailProvider(BaseProvider):
    """
    Custom email provider for handling pseudonymization

    This class extracts names from email addresses and replaces them with pseudonyms
    using predefined mappings or generates a random fallback

    Attributes:
        mappings (dict): Dictionary containing mappings for pseudonymization
    """
    def __init__(self,
                    generator: Faker,
                    mappings: Optional[Dict[str, Dict[str, str]]] = None) -> None:
        """
        Initializes the provider with a Faker generator and mappings
        
        Args:
            generator (Faker): The faker generator instance
            mappings (Optional[Dict[str, str]]]): Dictionary containing mappings for 
            pseudonymization
        """
        super().__init__(generator)
        self.mappings = mappings or {}

    def _extract_name_from_email(self, email: str) -> Optional[str]:
        """
        Extracts the name from the mail according Reims's CHU dormat, taking the substring
        from the second letter until '@'
        
        Args:
            email (str): The email address to process
            
        Returns:
            Optional[str]: The extracted name in lowercase, or None if no match found
        """
        match = re.match(r'^.(.*?)@', email)
        if match:
            return match.group(1).lower().strip()
        return None

    def pseudonymize_mail(self, original_email: str) -> str:
        """
        Pseudonymizes an email address based on the extracted name and existing mappings
        
        Args:
            original_email (str): The original email address to be pseudonymized
        
        Returns:
            str: The pseudonymized email address
        """
        extracted_name = self._extract_name_from_email(original_email)
        random_letter = random.choice(string.ascii_lowercase)
        if not extracted_name:
            return f"{random_letter}{self.generator.last_name().lower()}@chu-reims.fr"

        # Search for the extracted name in the mappings dict
        for original_name, pseudonymized_name in self.mappings['NOM'].items():
            if extracted_name.lower() == original_name.lower():
                # random_letter = random.choice(string.ascii_lowercase)
                return f"{random_letter}{pseudonymized_name.lower()}@chu-reims.fr"

        # If no match id found generate a new name
        return f"{random_letter}{self.generator.last_name().lower()}@chu-reims.fr"
    