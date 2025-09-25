###
# #%L
# aiSSEMBLE::Test::MDA::Data Delivery Pyspark Basic
# %%
# Copyright (C) 2021 Booz Allen
# %%
# This software package is licensed under the Booz Allen Public License. All Rights Reserved.
# #L%
###
from ...step.abstract_data_action_impl import AbstractDataActionImpl

class AbstractPipelineStep(AbstractDataActionImpl):
    """
    Performs common step configurationbased on the pipeline.

    GENERATED CODE - DO NOT MODIFY (Add your customization in your step implementation classes)

    Generated from: templates/data-delivery-pyspark/abstract.pipeline.step.py.vm
    """

    def __init__(self, subject, action):
        super().__init__(subject, action)
