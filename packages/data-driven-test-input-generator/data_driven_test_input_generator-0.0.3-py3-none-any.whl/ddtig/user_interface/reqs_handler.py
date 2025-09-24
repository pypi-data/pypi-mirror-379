from __future__ import annotations
import json
from pathlib import Path
from typing import TextIO
from dataclasses import dataclass
from ddtig.infrastructure import TestLogger

@dataclass
class RequirementsHandler():
    """
    A class that loads and validates test requirements from a JSON file,
    extracting information necessary for generating test inputs.

    Attributes
    ----------
    requirements : dict
        Dictionary storing the test requirements.
    
    logger : TestLogger
        Logger for tracking the test input generation process.
    """

    # Parameters expected to be of type int
    int_params = ["n_testinputs", "sample_limit", "n_predictions", "max_depth"]

    # Parameters expected to be of type float
    float_params = ["epsilon", "performance_threshold"]

    # Parameters expected to be of type str with restricted values
    str_params_values = [["bva", "dtc"]]
    str_params        = ["test_coverage_criterium"]

    # Parameters expected to be of type bool
    bool_params = ["inverse_alloc"]

    # Parameters that must be present in the requirements file
    must_params = ["test_coverage_criterium", "n_testinputs"]


    def __init__(
        self,
        reqs_file: Path | TextIO,
        logger: TestLogger) -> None:
        """
        Loads and validates test requirements from a JSON file.
        For details on defining requirements, refer to README.md.

        Example:
        {
            "test_coverage_criterium": "bva", 
            "n_testinputs": 2000,
            ...
        }

        Args:
            reqs_file : JSON file containing test requirements.
            logger : Logger for logging validation messages.
        """
        self.logger = logger

        # Load JSON file
        with open(reqs_file) as f:
            try:
                self.requirements = json.load(f)
            except Exception as e:
                if self.logger:
                    self.logger.log_error("Failed to import requirement file.")
                print("Import JSON file unsuccessful.")
                print("Error message: " + str(e))

        # Validate presence of mandatory parameters
        for must_param in self.must_params:
            if must_param not in self.requirements:
                if self.logger:
                    self.logger.log_error("Missing required parameters in requirement file.")
                raise KeyError(f"Missing required parameter: '{must_param}'") 

        # Validate integer parameters
        for int_param in self.int_params:
            if int_param in self.requirements:
                value = self.requirements[int_param]
                if not isinstance(value, int):
                    if self.logger:
                        self.logger.log_error("Incorrect type for integer parameter.")
                    raise TypeError(f"Expected type 'int', but got '{type(value).__name__}' instead.")

        # Validate float parameters
        for float_param in self.float_params:
            if float_param in self.requirements:
                value = self.requirements[float_param]
                if not (isinstance(value, float) or (isinstance(value, int) and not isinstance(value, bool))):
                    if self.logger:
                        self.logger.log_error("Incorrect type for float parameter.")
                    raise TypeError(f"Expected type 'float', but got '{type(value).__name__}' instead.")
        
         # Validate string parameters and their allowed values
        for str_param, str_params_value in zip(self.str_params, self.str_params_values):
            if str_param in self.requirements:
                value = self.requirements[str_param]
                if not isinstance(value, str):
                    if self.logger:
                        self.logger.log_error("Incorrect type for string parameter.")
                    raise TypeError(f"Expected type 'str', but got '{type(value).__name__}' instead.")
                if value not in str_params_value:
                    if self.logger:
                        self.logger.log_error("Invalid value for string parameter.")
                    raise ValueError(f"Invalid value: '{value}'. Allowed values are: {str_params_value}")
        
        # Validate boolean parameters
        for bool_param in self.bool_params:
            if bool_param in self.requirements:
                value = self.requirements[bool_param]
                if not isinstance(value, bool):
                    if self.logger:
                        self.logger.log_error("Incorrect type for boolean parameter.")
                    raise TypeError(f"Expected type 'bool', but got '{type(value).__name__}' instead.")

        # Validate nominal_attributes list
        if "nominal_attributes" in self.requirements:
            nominal_lst = self.requirements["nominal_attributes"]
            if not isinstance(nominal_lst, list):
                if self.logger:
                    self.logger.log_error("Incorrect type for 'nominal_attributes'.")
                raise TypeError("The value for key 'nominal_attributes' must be a list.")
            if not all(isinstance(item, str) for item in nominal_lst):
                if self.logger:
                    self.logger.log_error("Invalid item type in 'nominal_attributes'.")
                raise TypeError("All items in 'nominal_attributes' must be of type 'str'.")
