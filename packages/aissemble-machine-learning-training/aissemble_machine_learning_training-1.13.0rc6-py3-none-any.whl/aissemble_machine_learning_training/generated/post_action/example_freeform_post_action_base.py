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
from krausening.logging import LogManager


class ExampleFreeformPostActionBase(ABC):
    """
    Base ExampleFreeformPostAction post-action class.

    GENERATED CODE - DO NOT MODIFY (add your customizations in ExampleFreeformPostAction).

    Generated from: templates/post-action/post.action.base.py.vm
    """
    logger = LogManager.get_instance().get_logger('ExampleFreeformPostActionBase')


    def __init__(self, training_run_id: str, model: any) -> None:
        """
        Default constructor for this post-action.

        :model: the model to apply this post-action on
        :training_run_id: the training run identifier associated with this post-action
        """
        super().__init__()
        self._training_run_id = training_run_id
        self._model = model


    @property
    def training_run_id(self) -> str:
        """
        The training run identifier associated with this post-action.

        :return: the training run identifier associated with this post-action.
        """
        return self._training_run_id


    @property
    def model(self) -> any:
        """
        The model to apply this post-action on.

        :return: the model to apply this post-action on
        """
        return self._model


    @abstractmethod
    def apply(self) -> None:
        """
        Applies this freeform post-action.
        """
        pass
