"""
- Pseudo-faker: A package for data pseudonymization
- This module defines the `PseudoCare` class, which encompasses the entire 
    pseudonymization process, from entity detection to the visualization 
    of pseudonymized reports
"""
from typing import Optional, Any, Dict, Type
from edsnlp import load
from faker import Faker
from spacy import displacy
from pseudocare.providers.custom_date_provider import CustomDateProvider

class PseudoCare:
    """
    The `PseudoCare` class handles the entire pseudonymization process, 
    from entity detection to replacing personal information with pseudonyms. 
    It leverages a pre-trained NLP model and customizable pseudonymization providers.

    Key Features:
    - Loads a pre-trained NLP model or a user-defined model
    - Uses seeded Faker instances for consistent pseudonymization across documents
    - Supports entity-specific pseudonymization providers (custom providers)
    - Allows configurable date and birthdate sliding
    - Provides visualization of pseudonymized results
    """
    def __init__(self,
                model: Optional[Any] = None,
                max_birthdate_sliding: int = 5,
                max_date_sliding: int = 100,
                custom_providers: Optional[Dict[str, Type[Any]]] = None) -> None:
        """
        Initializes the Pseudonymization class
        Loads a pre-trained NLP model or uses a default one
        
        Args:
            model (Optional[Any]): A pre-trained NLP model (optional)
            max_birthdate_sliding (int): Maximum number of days for birthdate shifting
            max_date_sliding (int): Maximum number of days for general date shifting
            custom_providers: Optional[Dict[str, Type[Any]]]): Dictionary of custom providers 
                    where keys are entity types and values are provider classes
                    Each provider class must implement a method named `pseudonymize_<entity_type>`
                    
        Raises:
            ValueError: If max_birthdate_sliding or max_date_sliding is negative
            AttributeError: If a provider class does not implement the required pseudo method
        
        Returns:
            None
        """
        
        if max_birthdate_sliding <= 0:
            raise ValueError("max_birthdate_sliding must be non-negative.")
        if max_date_sliding <= 0:
            raise ValueError("max_date_sliding must be non-negative.")
        
        # If no model passed, lets load default one
        self.nlp = model if model else load("AP-HP/eds-pseudo-public", auto_update=True)
        
        self.seeds_by_ipp = {}
        self.mappings = {}
        self.birthdate_sliding = max_birthdate_sliding
        self.date_sliding = max_date_sliding
        self.custom_providers = custom_providers or {}
        for entity_type, provider_class in self.custom_providers.items():
            if not hasattr(provider_class, f"pseudonymize_{entity_type.lower()}"):
                raise AttributeError(
                    f"Provider `{provider_class.__name__}` must have method:" 
                    f"`pseudonymize_{entity_type.lower()}`.")

    def _init_mappings_for_ipp(self, ipp: str) -> Dict[str, Dict[Any, Any]]:
        """
        Initializes the mapping dictionnaries for a given IPP if they do not already exists
        
        Args:
            ipp (str): The unique patient identifier
            
        Returns:
            Dict[str, Dict[Any, Any]]: A dict containing mapping for diff entities
        """
        if ipp not in self.mappings:
            self.mappings[ipp] = {
                'PRENOM': {},
                'NOM': {},
                'TEL': {},
                'VILLE': {},
                'ZIP': {},
                'ADRESSE': {},
                'IPP': {},
                'DATE_NAISSANCE': {},
                'MAIL': {},
                'SECU': {},
                'NDA': {}
            }
        return self.mappings[ipp]

    def _get_faker_for_ipp(self, ipp: str) -> Dict[str, Faker]:
        """
        Returns a dict of Faker instances, seeded with  fixed value for the given IPP
        
        Args:
            ipp (str): The unique patient identifier
        
        Returns:
            Dict[str, Faker]: A dict with OPP as the key and corresponding Faker instance as value
        """
        if ipp not in self.seeds_by_ipp:
            self._init_mappings_for_ipp(ipp)
            seed = ipp  # --> We can create an encoded seed from the ipp,
                        #     actualy I use the ipp as a seed !
            faker = Faker("fr_FR")
            faker.seed_instance(seed) # ça marche peut importe ce qu'on lui donne "12.5", "test"

            # Create a set of custom provider types
            custom_types = set(self.custom_providers.keys()) if self.custom_providers else set()
            print(f"{custom_types = }")
            # Add custom providers
            if self.custom_providers:
                print(f"Custom providers used : {self.custom_providers}")
                for _, provider_class in self.custom_providers.items():
                    # Verify if a providre accepte `mappings`
                    init_params = provider_class.__init__.__code__.co_varnames
                    print(f"{init_params = }")
                    provider_instance = (
                            provider_class(faker, self.mappings[ipp])
                            if "mappings" in init_params
                            else provider_class(faker)
                    )
                    faker.add_provider(provider_instance)

            # Add default providers that have not been replaced
            if 'DATE' not in custom_types:
                faker.add_provider(CustomDateProvider(faker))

            self.seeds_by_ipp[ipp] = faker
        return self.seeds_by_ipp[ipp]

    def run(self, document: str, ipp: str) -> str:
        """
        Main entry point for document pseudonymization.
        
        Args:
            document (str): Document text to be pseudonymized
            ipp (str): The unique patient identifier for pseudonymization
        
        Returns:
            str: Pseudonymized document text
        """
        entities = self._predict(document)
        pseudonymized_document, _ = self._pseudonymize_entities(entities, ipp)
        return pseudonymized_document

    def _predict(self, document: str):
        """
        Predict named entities in the document
        
        Args:
            document (str): Text content to analyze
        
        Returns:
            Doc: spaCy Doc object with entity predictions
        """
        return self.nlp(document)

    def _pseudonymize_entities(self, doc, ipp:str) -> str:
        """
        Pseudonymize the entities in one or more documents by replacing personal informations
        with pseudonyms, using a Faker instance seeded with a specific IPP
        
        Args:
            doc: Doc to be pseudonymized
            ipp: The patient identifier used for consistency in pseudonymization

        Returns:
            str: A string containing the pseudonymized text
        """
        # Get the faker instance for the specific IPP
        faker = self._get_faker_for_ipp(ipp)

        # Get the mapping dict for the IPP
        mappings = self._init_mappings_for_ipp(ipp)

        # Crezate a Stamp instance to process entities in the doc
        tampon = Stamp(faker=faker,
                        mappings=mappings,
                        date_sliding=self.date_sliding,
                        birthdate_sliding=self.birthdate_sliding,
                        ipp= ipp,
                        custom_providers=self.custom_providers)

        pseudonymized_text = ""

        # Process entities in the doc
        for token in self.nlp(doc):
            if token.ent_iob != 1:
                pseudonymized_text += tampon.use()
            tampon.add(token.text, token.ent_type_, token.whitespace_)

        pseudonymized_text += tampon.use()
        return pseudonymized_text, mappings

    def display(self, document: str, ipp: str) -> str:
        """
        Generate HTML visualization for document with pseudonymized entities
        
        Args:
            document (str): Original document text
            ipp (str): Unique patient identifier
        
        Returns:
            str: HTML content with visualization
        """
        # Predict entities and pseudonymize
        doc_pred = self._predict(document)
        doc_pseudo, _ = self._pseudonymize_entities(doc_pred, ipp)

        # Create HTML visualization
        ref_html = displacy.render(self._predict(document), style="ent", jupyter=False)
        pseudonymized_html = displacy.render(self._predict(doc_pseudo), style="ent", jupyter=False)

        html_content = f"""
        <table style="border-collapse: collapse; width: 100%;">
            <thead>
                <tr>
                    <th style="border: 1px solid black; padding: 10px;">Document original</th>
                    <th style="border: 1px solid black; padding: 10px;">Document pseudonymisé</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="border: 1px solid black; padding: 10px;">{ref_html}</td>
                    <td style="border: 1px solid black; padding: 10px;">{pseudonymized_html}</td>
                </tr>
            </tbody>
        </table>
        """

        return html_content

# pylint: disable= too-many-instance-attributes
class Stamp:
    """
    A class used to handle the transformation of text entities with pseudonymization
    
    Attributes:
        str (str): The current string being processed
        type (str): The type of entity (NOM, PRENOM, DATE, DATE_NAISSANCE, TEL, 
                    VILLE, ADRESSE, ZIP, IPP, MAIL, SECU, NDA)
        whitespace (str): The whitespace following entity
        faker (Faker): The Faker instance used for generating pseudonyms
        mappings (Dict[str, Dict[syt, str]]): The mappinsg for ech entity type
        date_sliding (int): The max allowed sliding for dates
        birthdate_sliding (int): The max allowed sliding for birthdates
        custom_providers (Dict[str, type]): Custom provider classes for pseudonymisation

    Methods:
        add(text: str, entity_type: str, whitespace: str): Adds an entity and its
            type to be transforme
        use(): Transforms the added entity and returns the pseudonymized text
        _default_transformation(): Applies the default transformation logic based 
            on the entity type
    """
    # pylint: disable=too-many-arguments too-many-positional-arguments
    def __init__(self,
                    faker: Faker,
                    mappings: Dict[str, Dict[str, str]],
                    date_sliding: int,
                    birthdate_sliding: int,
                    ipp: str,
                    custom_providers: Dict[str, type] = None):

        """
        Initializes a Stamp instance to handle entity transformations
        
        Args:
            faker (Faker): The Faker instance used for generating pseudonyms
            mappings (Dict[str, Dict[syt, str]]): A dict storing the mapping 
                    between original entities and their pseudonymized versions, each entityentity
                    type containss a dict where the key is the original value and the value is the
                    corresponding pseudonymized version. This mechanism ensures consistency in 
                    pseudonimization, the same input value will always be replaced with the same
                    outuput value 
            date_sliding (int): The max allowed sliding for dates
            birthdate_sliding (int): The max allowed sliding for birthdates
            custom_providers (Dict[str, type]): Custom provider classes for pseudonymisation
        """

        self.str = ""
        self.type = None
        self.whitespace = ""
        self.faker = faker
        self.mappings = mappings
        self.date_sliding = date_sliding
        self.birthdate_sliding = birthdate_sliding
        self.ipp = ipp
        self.custom_providers = custom_providers or {}

    def add(self, text: str, entity_type: str, whitespace: str = "") -> None:
        """
        Adds an entity to be pseudonymized

        Args:
            text (str): The text to be pseudonymized
            entity_type (str): The entity type
            whitespace (str): The whitespace following the entity
        """

        self.str = f"{self.str} {text}" if self.str != "" else text
        self.type = entity_type
        self.whitespace = whitespace

    def use(self) -> str:
        """
        Transforms the current entity and returns the pseudonymized
        text

        Returns:
            str: The pseudonymized text, or the original text if no transformation
                was applied
        """
        transformed = None
        # Check if a custom provider exists for this entity type
        if self.type in self.custom_providers:
            if hasattr(self.faker, f'pseudonymize_{self.type.lower()}'):
                transformed = getattr(self.faker,
                                        f'pseudonymize_{self.type.lower()}')(self.str)
        else:
            transformed = self._default_transformation()

        if transformed is not None:
            transformed += self.whitespace
        else:
            transformed = ""

        self.str = ""
        self.type = None
        self.whitespace = ""
        return transformed

    def _default_transformation(self):
        """
        Applies the default transformation for the entity type.

        Returns:
            str: The transformed (pseudonymized) entity.
        """

        entity_mappings = {
            "PRENOM": self.faker.first_name,
            "NOM": self.faker.last_name,
            "TEL": self.faker.phone_number, #lambda: generate_phone_number(self.faker)
            "DATE": lambda: self.faker.pseudonymize_date(self.ipp, 
                                                        self.str,
                                                        self.date_sliding),
            "DATE_NAISSANCE": lambda: self.faker.pseudonymize_date(self.ipp,
                                                                    self.str,
                                                                    self.birthdate_sliding),
            "VILLE": self.faker.city,
            "ZIP": self.faker.postcode,
            "ADRESSE": self.faker.street_address,
            "IPP": lambda: self.faker.bothify(text="########", letters=""),
            "NDA": lambda: self.faker.bothify(text="#########", letters=""),
            "MAIL": self.faker.email,
            "SECU": self.faker.ssn
        }

        if self.type in entity_mappings:
            if self.type not in self.mappings:
                self.mappings[self.type] = {}

            if self.str.lower() not in self.mappings[self.type]:
                self.mappings[self.type][self.str.lower()] = entity_mappings[self.type]()

            return self.mappings[self.type][self.str.lower()]

        return self.str  # Default case
