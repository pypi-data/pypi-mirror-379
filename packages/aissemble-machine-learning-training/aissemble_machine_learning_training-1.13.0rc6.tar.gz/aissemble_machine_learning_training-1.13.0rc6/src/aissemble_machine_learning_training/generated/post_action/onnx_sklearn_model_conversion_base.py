###
# #%L
# aiSSEMBLE::Test::MDA::Machine Learning::Machine Learning Training
# %%
# Copyright (C) 2021 Booz Allen
# %%
# This software package is licensed under the Booz Allen Public License. All Rights Reserved.
# #L%
###
from abc import ABC, abstractmethod
from ...config.pipeline_config import PipelineConfig
from krausening.logging import LogManager
from onnxmltools.convert import convert_sklearn
import mlflow
from os import path


class OnnxSklearnModelConversionBase(ABC):
    """
    Base onnx model conversion post-action class.

    GENERATED CODE - DO NOT MODIFY (add your customizations in ExampleOnnxSklearnConversion).

    Generated from: templates/post-action/model.conversion.base.py.vm
    """
    logger = LogManager.get_instance().get_logger('OnnxSklearnModelConversionBase')


    def __init__(self) -> None:
        """
        Default constructor for a onnx model conversion post-action.
        """
        self._pipeline_config = PipelineConfig()


    @property
    def converted_model_file_directory(self) -> str:
        """
        The directory to save the converted model to.

        :return: the directory so save the converted model to
        """
        return self._pipeline_config.onnx_model_directory()


    @property
    def converted_model_file_name(self) -> str:
        """
        The file name to save the converted model as.

        :return: the file name to save the converted model as
        """
        return 'converted_sklearn_model.onnx'


    def _convert(self, source_model) -> any:
        """
        Performs the sklearn-to-onnx conversion on the source model and returns the converted model.

        :source_model: the model to perform the conversion on
        :return: the converted model
        """
        OnnxSklearnModelConversionBase.logger.info('Performing onnx model conversion...')

        converted_model = convert_sklearn(
            source_model,
            custom_shape_calculators=self.custom_shape_calculators,
            custom_conversion_functions=self.custom_conversion_functions,
            name=self.name,
            target_opset=self.target_opset,
            initial_types=self.initial_types,
            doc_string=self.doc_string,
        )

        OnnxSklearnModelConversionBase.logger.info('Converted sklearn model to onnx format')
        return converted_model


    def _save(self, converted_model) -> None:
        """
        Saves the converted onnx model.

        :converted_model: the converted model to save
        """
        OnnxSklearnModelConversionBase.logger.info('Saving converted onnx model...')

        mlflow.onnx.log_model(converted_model, self.converted_model_file_directory)

        OnnxSklearnModelConversionBase.logger.info('Saved converted onnx model to {}'.format(self.converted_model_file_directory))


    @property
    def custom_shape_calculators(self):
        """
        Optional custom_shape_calculators parameter for the sklearn-to-onnx conversion.

        :return: optional custom_shape_calculators parameter value
        """
        return None


    @property
    def custom_conversion_functions(self):
        """
        Optional custom_conversion_functions parameter for the sklearn-to-onnx conversion.

        :return: optional custom_conversion_functions parameter value
        """
        return None


    @property
    def name(self):
        """
        Optional name parameter for the sklearn-to-onnx conversion.

        :return: optional name parameter value
        """
        return None


    @property
    def target_opset(self):
        """
        Optional target_opset parameter for the sklearn-to-onnx conversion.

        :return: optional target_opset parameter value
        """
        return None


    @property
    @abstractmethod
    def initial_types(self):
        """
        Required initial_types parameter for the sklearn-to-onnx conversion.

        :return: required initial_types parameter value
        """
        pass


    @property
    def doc_string(self):
        """
        Optional doc_string parameter for the sklearn-to-onnx conversion.

        :return: optional doc_string parameter value
        """
        return ''


