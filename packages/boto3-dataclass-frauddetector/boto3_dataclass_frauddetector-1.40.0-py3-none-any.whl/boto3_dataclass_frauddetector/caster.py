# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_frauddetector import type_defs as bs_td


class FRAUDDETECTORCaster:

    def batch_create_variable(
        self,
        res: "bs_td.BatchCreateVariableResultTypeDef",
    ) -> "dc_td.BatchCreateVariableResult":
        return dc_td.BatchCreateVariableResult.make_one(res)

    def batch_get_variable(
        self,
        res: "bs_td.BatchGetVariableResultTypeDef",
    ) -> "dc_td.BatchGetVariableResult":
        return dc_td.BatchGetVariableResult.make_one(res)

    def create_detector_version(
        self,
        res: "bs_td.CreateDetectorVersionResultTypeDef",
    ) -> "dc_td.CreateDetectorVersionResult":
        return dc_td.CreateDetectorVersionResult.make_one(res)

    def create_model_version(
        self,
        res: "bs_td.CreateModelVersionResultTypeDef",
    ) -> "dc_td.CreateModelVersionResult":
        return dc_td.CreateModelVersionResult.make_one(res)

    def create_rule(
        self,
        res: "bs_td.CreateRuleResultTypeDef",
    ) -> "dc_td.CreateRuleResult":
        return dc_td.CreateRuleResult.make_one(res)

    def delete_events_by_event_type(
        self,
        res: "bs_td.DeleteEventsByEventTypeResultTypeDef",
    ) -> "dc_td.DeleteEventsByEventTypeResult":
        return dc_td.DeleteEventsByEventTypeResult.make_one(res)

    def describe_detector(
        self,
        res: "bs_td.DescribeDetectorResultTypeDef",
    ) -> "dc_td.DescribeDetectorResult":
        return dc_td.DescribeDetectorResult.make_one(res)

    def describe_model_versions(
        self,
        res: "bs_td.DescribeModelVersionsResultTypeDef",
    ) -> "dc_td.DescribeModelVersionsResult":
        return dc_td.DescribeModelVersionsResult.make_one(res)

    def get_batch_import_jobs(
        self,
        res: "bs_td.GetBatchImportJobsResultTypeDef",
    ) -> "dc_td.GetBatchImportJobsResult":
        return dc_td.GetBatchImportJobsResult.make_one(res)

    def get_batch_prediction_jobs(
        self,
        res: "bs_td.GetBatchPredictionJobsResultTypeDef",
    ) -> "dc_td.GetBatchPredictionJobsResult":
        return dc_td.GetBatchPredictionJobsResult.make_one(res)

    def get_delete_events_by_event_type_status(
        self,
        res: "bs_td.GetDeleteEventsByEventTypeStatusResultTypeDef",
    ) -> "dc_td.GetDeleteEventsByEventTypeStatusResult":
        return dc_td.GetDeleteEventsByEventTypeStatusResult.make_one(res)

    def get_detector_version(
        self,
        res: "bs_td.GetDetectorVersionResultTypeDef",
    ) -> "dc_td.GetDetectorVersionResult":
        return dc_td.GetDetectorVersionResult.make_one(res)

    def get_detectors(
        self,
        res: "bs_td.GetDetectorsResultTypeDef",
    ) -> "dc_td.GetDetectorsResult":
        return dc_td.GetDetectorsResult.make_one(res)

    def get_entity_types(
        self,
        res: "bs_td.GetEntityTypesResultTypeDef",
    ) -> "dc_td.GetEntityTypesResult":
        return dc_td.GetEntityTypesResult.make_one(res)

    def get_event(
        self,
        res: "bs_td.GetEventResultTypeDef",
    ) -> "dc_td.GetEventResult":
        return dc_td.GetEventResult.make_one(res)

    def get_event_prediction(
        self,
        res: "bs_td.GetEventPredictionResultTypeDef",
    ) -> "dc_td.GetEventPredictionResult":
        return dc_td.GetEventPredictionResult.make_one(res)

    def get_event_prediction_metadata(
        self,
        res: "bs_td.GetEventPredictionMetadataResultTypeDef",
    ) -> "dc_td.GetEventPredictionMetadataResult":
        return dc_td.GetEventPredictionMetadataResult.make_one(res)

    def get_event_types(
        self,
        res: "bs_td.GetEventTypesResultTypeDef",
    ) -> "dc_td.GetEventTypesResult":
        return dc_td.GetEventTypesResult.make_one(res)

    def get_external_models(
        self,
        res: "bs_td.GetExternalModelsResultTypeDef",
    ) -> "dc_td.GetExternalModelsResult":
        return dc_td.GetExternalModelsResult.make_one(res)

    def get_kms_encryption_key(
        self,
        res: "bs_td.GetKMSEncryptionKeyResultTypeDef",
    ) -> "dc_td.GetKMSEncryptionKeyResult":
        return dc_td.GetKMSEncryptionKeyResult.make_one(res)

    def get_labels(
        self,
        res: "bs_td.GetLabelsResultTypeDef",
    ) -> "dc_td.GetLabelsResult":
        return dc_td.GetLabelsResult.make_one(res)

    def get_list_elements(
        self,
        res: "bs_td.GetListElementsResultTypeDef",
    ) -> "dc_td.GetListElementsResult":
        return dc_td.GetListElementsResult.make_one(res)

    def get_lists_metadata(
        self,
        res: "bs_td.GetListsMetadataResultTypeDef",
    ) -> "dc_td.GetListsMetadataResult":
        return dc_td.GetListsMetadataResult.make_one(res)

    def get_model_version(
        self,
        res: "bs_td.GetModelVersionResultTypeDef",
    ) -> "dc_td.GetModelVersionResult":
        return dc_td.GetModelVersionResult.make_one(res)

    def get_models(
        self,
        res: "bs_td.GetModelsResultTypeDef",
    ) -> "dc_td.GetModelsResult":
        return dc_td.GetModelsResult.make_one(res)

    def get_outcomes(
        self,
        res: "bs_td.GetOutcomesResultTypeDef",
    ) -> "dc_td.GetOutcomesResult":
        return dc_td.GetOutcomesResult.make_one(res)

    def get_rules(
        self,
        res: "bs_td.GetRulesResultTypeDef",
    ) -> "dc_td.GetRulesResult":
        return dc_td.GetRulesResult.make_one(res)

    def get_variables(
        self,
        res: "bs_td.GetVariablesResultTypeDef",
    ) -> "dc_td.GetVariablesResult":
        return dc_td.GetVariablesResult.make_one(res)

    def list_event_predictions(
        self,
        res: "bs_td.ListEventPredictionsResultTypeDef",
    ) -> "dc_td.ListEventPredictionsResult":
        return dc_td.ListEventPredictionsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResultTypeDef",
    ) -> "dc_td.ListTagsForResourceResult":
        return dc_td.ListTagsForResourceResult.make_one(res)

    def update_model_version(
        self,
        res: "bs_td.UpdateModelVersionResultTypeDef",
    ) -> "dc_td.UpdateModelVersionResult":
        return dc_td.UpdateModelVersionResult.make_one(res)

    def update_rule_version(
        self,
        res: "bs_td.UpdateRuleVersionResultTypeDef",
    ) -> "dc_td.UpdateRuleVersionResult":
        return dc_td.UpdateRuleVersionResult.make_one(res)


frauddetector_caster = FRAUDDETECTORCaster()
