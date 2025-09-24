from __future__ import annotations
import json
from pathlib import Path
from typing import TextIO
import polars as pl
from ddtig.infrastructure import TestLogger

class SystemSpecsHandler():
    """
    A class that loads and decodes a specification file to extract information
    required for generating test inputs.

    Attributes
    ----------
    specs : dict
        Dictionary storing system specifications.
        
    n_features : int
        Number of features.

    logger : TestLogger
        Logger for tracking the test input generation process.

    Methods
    -------
    get_n_features()
        Returns the number of features.

    get_nominal_features()
        Returns the indices of all nominal features.
    
    get_numerical_features()
        Returns the indices of all numerical features.
    
    get_int_features()
        Returns the indices of all features with type 'int'.

    extract_minmax_values()
        Extracts min and max values from specifications.

    extract_input_types()
        Extracts value types from specifications.
    
    extract_feature_names()
        Extracts feature names.

    extract_feature_names_with_idx()
        Extract feature names along with their corresponding indices.
    
    extract_feature_names_with_idx_reversed()
        Extract feature indices along with their corresponding names.
    """


    def __init__(
        self,
        data: pl.DataFrame,
        specs_file: Path | TextIO,
        logger: TestLogger) -> None:
        """
        Loads specifications from a JSON file or infers them from a dataset.
        For details on defining specifications in JSON, refer to README.md.

        Example JSON structure:
        {
            "features": [
                {
                    "name": "feature_0_name",
                    "min": 0,
                    "max": 100,
                    "type": "float" or "int",
                    "nominal": true or false
                },
                ...
            ]
        }

        Args:
            data : Dataset used to infer specifications if specs_file is not provided.
            specs_file : JSON file containing system specifications.
            logger : Logger for logging messages.
        """
        self.logger = logger
        if data is not None:
            # Drop the target column (assumed to be the last column)
            target_col = data.columns[-1]
            data = data.drop(target_col)

            # Infer specifications from dataset
            features = []
            column_names = data.columns
            maxs = data.max().row(0)
            mins = data.min().row(0)
            dtypes = data.dtypes
            self.n_features = len(column_names)
            for i in range(len(column_names)):
                feature = {}
                feature['name'] = column_names[i]
                feature['min'] = mins[i]
                feature['max'] = maxs[i]
                if dtypes[i].is_float():
                    feature['type'] = 'float'
                else:
                    feature['type'] = 'int'
                unique_vals = data.select(pl.col(column_names[i]).unique()).to_series()
                feature['nominal'] = set(unique_vals) <= {0, 1}
                features.append(feature)
            self.specs = {"features": features}

            if self.logger:
                self.logger.log_debug("Specifications successfully extracted from dataset.")

        else:
            # Load specifications from JSON file
            with open(specs_file) as f:
                try:
                    self.specs = json.load(f)
                except Exception as e:
                    if self.logger:
                        self.logger.log_error("Failed to import specification file.")
                    print("Import JSON file unsuccessful.")
                    print("Error message:", str(e))

            # Validate JSON structure
            if self.specs.get('features') is None:
                if self.logger:
                    self.logger.log_error("Specification file structure is invalid.")
                raise LookupError("Invalid JSON structure. Refer to README.md.")

            self.n_features = self.get_n_features()

            for i in range(self.n_features):
                feature = self.specs['features'][i]

                # Validate presence of required keys
                if not all(k in feature for k in ['name', 'min', 'max', 'type', 'nominal']) or len(feature) != 5:
                    if self.logger:
                        self.logger.log_error("Specification file structure is invalid.")
                    raise LookupError("Invalid JSON structure. Refer to README.md.")

                # Validate types
                if not isinstance(feature['name'], str):
                    if self.logger:
                        self.logger.log_error("Invalid value type for 'name'.")
                    raise ValueError("'name' must be a string.")

                if feature['type'] not in ['int', 'float']:
                    raise ValueError("'type' must be either 'int' or 'float'.")

                if not isinstance(feature['min'], (int, float)) or not isinstance(feature['max'], (int, float)):
                    if self.logger:
                        self.logger.log_error("Invalid value type for 'min' or 'max'.")
                    raise TypeError("'min' and 'max' must be int or float.")

                if feature['type'] == 'int' and not (isinstance(feature['min'], int) and isinstance(feature['max'], int)):
                    if self.logger:
                        self.logger.log_error("Type mismatch for 'int' feature.")
                    raise ValueError("'min' and 'max' must be int for type 'int'.")

                if feature['type'] == 'float' and not all(isinstance(v, (int, float)) for v in [feature['min'], feature['max']]):
                    if self.logger:
                        self.logger.log_error("Type mismatch for 'float' feature.")
                    raise ValueError("'min' and 'max' must be numeric for type 'float'.")

                if not isinstance(feature['nominal'], bool):
                    if self.logger:
                        self.logger.log_error("Invalid value type for 'nominal'.")
                    raise TypeError("'nominal' must be a boolean.")

                if feature['nominal'] and feature['type'] != 'int':
                    if self.logger:
                        self.logger.log_error("Nominal feature must be of type 'int'.")
                    raise TypeError("Nominal features must be of type 'int'.")
                
                if feature['min'] > feature['max']:
                    if self.logger:
                        self.logger.log_error("'min' is larger than 'max'.")
                    raise TypeError("'min' must be smaller than or equal to 'max'.")

            if self.logger:
                self.logger.log_debug("Specifications successfully extracted from file.")


    def get_n_features(self) -> int:
        """
        Returns the number of features defined in the specifications.

        Returns:
            Number of features.
        """
        return len(self.specs['features'])
    
    
    def get_nominal_features(self) -> list:
        """
        Returns the indices of nominal features.

        Returns:
            A list containing indices of nominal features.
        """
        nominal_features = []
        for feature in range(self.n_features):
            if (self.specs["features"][feature]['nominal']):
                nominal_features.append(feature)
        return nominal_features
    
    
    def get_numerical_features(self) -> list:
        """
        Returns the indices of numerical features.

        Returns:
            A list containing indices of numerical features.
        """
        numerical_features = []
        for feature in range(self.n_features):
            if not (self.specs["features"][feature]['nominal']):
                numerical_features.append(feature)
        return numerical_features
    

    def get_int_features(self) -> list:
        """
        Returns the indices of features with type 'int'.

        Returns:
            A list containing indices of integer-type features.
        """
        int_features = []
        for feature in range(self.n_features):
            if (self.specs["features"][feature]['type'] == 'int'):
                int_features.append(feature)
        return int_features
    

    def extract_minmax_values(self) -> dict:
        """
        Extracts the min and max values for each feature.

        Returns:
            Dictionary mapping feature index to its min and max values.
            Example:
            {
                0: {'min': 0.5, 'max': 5.3},
                1: {'min': 0, 'max': 500},
                2: {'min': 0.0, 'max': 10.0}
            }
        """
        minmax_dict = {}
        for feature in range(self.n_features):
            min_value = self.specs["features"][feature]['min']
            max_value = self.specs["features"][feature]['max']
            feature_range = {'min': min_value, 'max': max_value}
            minmax_dict.update({feature: feature_range})
        return minmax_dict
    

    def extract_input_types(self) -> dict:
        """
        Extract the input type of each feature from the specifications.

        Returns:
            A dictionary mapping feature index to its type.
            Example:
                {
                    0: {'type': 'float'},
                    1: {'type': 'int'},
                    2: {'type': 'float'}
                }
        """
        type_dict = {}
        for feature in range(self.n_features):
            input_type = self.specs["features"][feature]['type']
            feature_type = {'type': input_type}
            type_dict.update({feature: feature_type})
        return type_dict
    

    def extract_feature_names(self) -> list:
        """
        Extract the name of each feature from the specifications.

        Returns:
            A list of feature names.
            Example:
                ["pH", "temperature", "humidity"]
        """
        name_lst = []
        for feature in range(self.n_features):
            name_lst.append(self.specs["features"][feature]['name'])
        return name_lst
    

    def extract_feature_names_with_idx(self) -> dict:
        """
        Extract feature names along with their corresponding indices.

        Returns:
            A dictionary mapping feature names to their indices.
            Example:
                {
                    "pH": 0,
                    "temperature": 1,
                    "humidity": 2
                }
        """
        name_dict = {}
        for feature in range(self.n_features):
            name_dict[self.specs["features"][feature]['name']] = feature
        return name_dict
    

    def extract_feature_names_with_idx_reversed(self) -> dict:
        """
        Extract feature indices along with their corresponding names.

        Returns:
            A dictionary mapping feature indices to their names.
            Example:
                {
                    0: "pH",
                    1: "temperature",
                    2: "humidity"
                }
        """
        name_dict = {}
        for feature in range(self.n_features):
            name_dict[feature] = self.specs["features"][feature]['name']
        return name_dict
