#!/usr/bin/env python3

from flowcean.sklearn.model import SciKitModel
from flowcean.torch.model import PyTorchModel
from pathlib import Path
from typing import BinaryIO
from flowcean.core.model import Model
import polars as pl
from ddtig.infrastructure import TestLogger

class ModelHandler():
    """
    A class to load a Flowcean model and access its underlying machine learning model.

    Attributes
    ----------
    model : flowcean.core.model.Model
        The loaded Flowcean model.
    
    logger : TestLogger
        Logger used to log the test input generation process.
    
    Methods
    -------
    get_ml_model()
        Returns the underlying machine learning model from the Flowcean model.
    
    get_model_prediction()
        Returns predictions from the Flowcean model as a LazyFrame.
    
    get_model_prediction_as_lst()
        Returns predictions from the Flowcean model as a Python list.
    """


    def __init__(
        self,
        file: Path | BinaryIO,
        logger: TestLogger
    ) -> None:
        """
        Initializes the ModelHandler.

        Args:
            file : File containing the Flowcean model.
            logger : Logger for logging validation messages.
        """
        # Load the Flowcean model from the given file
        with open(file, "rb") as f:
            self.model = Model.load(f)
        self.logger = logger


    def get_ml_model(self) -> SciKitModel | PyTorchModel:
        """
        Extracts the underlying machine learning model from the Flowcean model.

        Returns:
            The machine learning model (either a Scikit-learn or PyTorch model).
        """
        if (type(self.model) == SciKitModel):
            ml_model = self.model.model
        else:
            ml_model = self.model.module
        if self.logger:
            self.logger.log_debug("Successfully extracted the underlying ML model from the Flowcean model.")
        return ml_model
    

    def get_model_prediction(self, input: pl.DataFrame) -> pl.LazyFrame:
        """
        Generates predictions using the Flowcean model.

        Args:
            input: A Polars DataFrame containing input features.

        Returns:
            A LazyFrame with predicted outputs.
        """
        return self.model.predict(input.lazy())
    
    
    def get_model_prediction_as_lst(self, input: pl.DataFrame) -> list:
        """
        Generates predictions using the Flowcean model and returns them as a list.

        Args:
            input: A Polars DataFrame containing input features.

        Returns:
            A list of predicted output values.
        """
        pred_df = self.model.predict(input.lazy()).collect()
        target_name = pred_df.columns[-1]
        return pred_df[target_name].to_list()