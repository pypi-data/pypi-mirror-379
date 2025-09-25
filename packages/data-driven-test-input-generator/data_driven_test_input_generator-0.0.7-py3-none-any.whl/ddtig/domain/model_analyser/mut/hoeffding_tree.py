#!/usr/bin/env python3
import polars as pl
from typing import Any
from river import metrics
from river import preprocessing
from river.tree import HoeffdingTreeRegressor, HoeffdingTreeClassifier
from ddtig.user_interface import SystemSpecsHandler
from ddtig.application import ModelHandler
from ddtig.infrastructure import TestLogger
from ddtig.domain import DataModel

class HoeffdingTree():
    """
    A class used to train a Hoeffding Tree using data generated from a neural network model.

    Attributes
    ----------
    datamodel : DataModel
        Object used to generate synthetic training inputs based on the original dataset.
    
    samples : list
        Original training inputs transformed to River-compatible format with predictions.
    
    nominal_attributes : list
        List of indices for nominal features.
    
    logger : TestLogger
        Logger for tracking the training process.

    Methods
    -------
    train_tree()
        Trains a Hoeffding Tree and returns the trained model.
    """

    N_SAMPLES = 5000    # Default number of samples to generate when more data is needed

    def __init__(
        self,
        inputs: pl.DataFrame,
        model_handler: ModelHandler,
        specs_handler: SystemSpecsHandler,
        logger: TestLogger
    ) -> None:
        """
        Initializes the HoeffdingTree trainer.

        Args:
            inputs : Original training dataset including target column.
            model_handler : Object used to generate predictions from the Flowcean model.
            specs_handler : Object containing feature specifications and metadata.
            logger : Logger for logging the training process.
        """
        # Remove target column to isolate input features
        inputs = inputs.drop(inputs.columns[-1])
        self.datamodel = DataModel(inputs, model_handler, specs_handler)

        # Generate River-compatible samples using original data
        self.samples = self.datamodel.generate_dataset(original_data=True)
        self.nominal_attributes = specs_handler.get_nominal_features()
        self.logger = logger

        
        

    def train_tree(self,
                   performance_threshold: float,
                   sample_limit: int,
                   n_predictions: int,
                   classification: bool,
                   **kwargs: Any) -> HoeffdingTreeRegressor | HoeffdingTreeClassifier:
        """
        Trains a Hoeffding Tree using synthetic samples until performance criteria are met.

        Args:
            performance_threshold : Minimum performance required to finalize the model.
            sample_limit : Maximum number of samples to use during training.
            n_predictions : Number of consecutive correct predictions required to stop training.
            classification : Indicates whether the task is classification or regression.
            **kwargs : Additional hyperparameters for the Hoeffding Tree model.

        Returns:
            Trained Hoeffding Tree model.
        """
        # Select appropriate metric and initialize model
        if classification:
            metric = metrics.F1()
            model = HoeffdingTreeClassifier(
                    nominal_attributes=self.nominal_attributes,
                    binary_split=True,
                    grace_period=10,
                    **kwargs)
        else:
            metric = metrics.MAE()
            model = (
                preprocessing.StandardScaler() |
                HoeffdingTreeRegressor(
                    nominal_attributes=self.nominal_attributes,
                    binary_split=True,
                    grace_period=10,
                    **kwargs         
                )
            )
           

        i = 0
        correct_predictions = 0

        # Pre-train
        for x,y in self.samples:
            if classification and isinstance(y, float):
                y = round(y)
            model.learn_one(x,y)

        # Main training loop
        for x,y in self.samples:
            if classification and isinstance(y, float):
                y = round(y)

            y_pred = model.predict_one(x)
            metric.update(y, y_pred)

            if metric.get() <= performance_threshold:
                correct_predictions += 1
                if correct_predictions == n_predictions:
                    break
            else:
                model.learn_one(x, y)
                correct_predictions = 0
            i += 1

            # Generate more samples if needed
            if i == len(self.samples):
                if len(self.samples) >= sample_limit:
                    break
                if (len(self.samples) + self.N_SAMPLES) >= sample_limit:
                    samples_to_generate = sample_limit - len(self.samples)
                else:
                    samples_to_generate = self.N_SAMPLES
                self.samples.extend(self.datamodel.generate_dataset(n_samples = samples_to_generate))

        if self.logger:
            self.logger.log_debug("Hoeffding Tree training completed successfully.")
        if classification:
            return model
        return model[1]
    
