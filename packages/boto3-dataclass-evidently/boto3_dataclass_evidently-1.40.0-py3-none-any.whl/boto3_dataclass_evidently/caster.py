# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_evidently import type_defs as bs_td


class EVIDENTLYCaster:

    def batch_evaluate_feature(
        self,
        res: "bs_td.BatchEvaluateFeatureResponseTypeDef",
    ) -> "dc_td.BatchEvaluateFeatureResponse":
        return dc_td.BatchEvaluateFeatureResponse.make_one(res)

    def create_experiment(
        self,
        res: "bs_td.CreateExperimentResponseTypeDef",
    ) -> "dc_td.CreateExperimentResponse":
        return dc_td.CreateExperimentResponse.make_one(res)

    def create_feature(
        self,
        res: "bs_td.CreateFeatureResponseTypeDef",
    ) -> "dc_td.CreateFeatureResponse":
        return dc_td.CreateFeatureResponse.make_one(res)

    def create_launch(
        self,
        res: "bs_td.CreateLaunchResponseTypeDef",
    ) -> "dc_td.CreateLaunchResponse":
        return dc_td.CreateLaunchResponse.make_one(res)

    def create_project(
        self,
        res: "bs_td.CreateProjectResponseTypeDef",
    ) -> "dc_td.CreateProjectResponse":
        return dc_td.CreateProjectResponse.make_one(res)

    def create_segment(
        self,
        res: "bs_td.CreateSegmentResponseTypeDef",
    ) -> "dc_td.CreateSegmentResponse":
        return dc_td.CreateSegmentResponse.make_one(res)

    def evaluate_feature(
        self,
        res: "bs_td.EvaluateFeatureResponseTypeDef",
    ) -> "dc_td.EvaluateFeatureResponse":
        return dc_td.EvaluateFeatureResponse.make_one(res)

    def get_experiment(
        self,
        res: "bs_td.GetExperimentResponseTypeDef",
    ) -> "dc_td.GetExperimentResponse":
        return dc_td.GetExperimentResponse.make_one(res)

    def get_experiment_results(
        self,
        res: "bs_td.GetExperimentResultsResponseTypeDef",
    ) -> "dc_td.GetExperimentResultsResponse":
        return dc_td.GetExperimentResultsResponse.make_one(res)

    def get_feature(
        self,
        res: "bs_td.GetFeatureResponseTypeDef",
    ) -> "dc_td.GetFeatureResponse":
        return dc_td.GetFeatureResponse.make_one(res)

    def get_launch(
        self,
        res: "bs_td.GetLaunchResponseTypeDef",
    ) -> "dc_td.GetLaunchResponse":
        return dc_td.GetLaunchResponse.make_one(res)

    def get_project(
        self,
        res: "bs_td.GetProjectResponseTypeDef",
    ) -> "dc_td.GetProjectResponse":
        return dc_td.GetProjectResponse.make_one(res)

    def get_segment(
        self,
        res: "bs_td.GetSegmentResponseTypeDef",
    ) -> "dc_td.GetSegmentResponse":
        return dc_td.GetSegmentResponse.make_one(res)

    def list_experiments(
        self,
        res: "bs_td.ListExperimentsResponseTypeDef",
    ) -> "dc_td.ListExperimentsResponse":
        return dc_td.ListExperimentsResponse.make_one(res)

    def list_features(
        self,
        res: "bs_td.ListFeaturesResponseTypeDef",
    ) -> "dc_td.ListFeaturesResponse":
        return dc_td.ListFeaturesResponse.make_one(res)

    def list_launches(
        self,
        res: "bs_td.ListLaunchesResponseTypeDef",
    ) -> "dc_td.ListLaunchesResponse":
        return dc_td.ListLaunchesResponse.make_one(res)

    def list_projects(
        self,
        res: "bs_td.ListProjectsResponseTypeDef",
    ) -> "dc_td.ListProjectsResponse":
        return dc_td.ListProjectsResponse.make_one(res)

    def list_segment_references(
        self,
        res: "bs_td.ListSegmentReferencesResponseTypeDef",
    ) -> "dc_td.ListSegmentReferencesResponse":
        return dc_td.ListSegmentReferencesResponse.make_one(res)

    def list_segments(
        self,
        res: "bs_td.ListSegmentsResponseTypeDef",
    ) -> "dc_td.ListSegmentsResponse":
        return dc_td.ListSegmentsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_project_events(
        self,
        res: "bs_td.PutProjectEventsResponseTypeDef",
    ) -> "dc_td.PutProjectEventsResponse":
        return dc_td.PutProjectEventsResponse.make_one(res)

    def start_experiment(
        self,
        res: "bs_td.StartExperimentResponseTypeDef",
    ) -> "dc_td.StartExperimentResponse":
        return dc_td.StartExperimentResponse.make_one(res)

    def start_launch(
        self,
        res: "bs_td.StartLaunchResponseTypeDef",
    ) -> "dc_td.StartLaunchResponse":
        return dc_td.StartLaunchResponse.make_one(res)

    def stop_experiment(
        self,
        res: "bs_td.StopExperimentResponseTypeDef",
    ) -> "dc_td.StopExperimentResponse":
        return dc_td.StopExperimentResponse.make_one(res)

    def stop_launch(
        self,
        res: "bs_td.StopLaunchResponseTypeDef",
    ) -> "dc_td.StopLaunchResponse":
        return dc_td.StopLaunchResponse.make_one(res)

    def test_segment_pattern(
        self,
        res: "bs_td.TestSegmentPatternResponseTypeDef",
    ) -> "dc_td.TestSegmentPatternResponse":
        return dc_td.TestSegmentPatternResponse.make_one(res)

    def update_experiment(
        self,
        res: "bs_td.UpdateExperimentResponseTypeDef",
    ) -> "dc_td.UpdateExperimentResponse":
        return dc_td.UpdateExperimentResponse.make_one(res)

    def update_feature(
        self,
        res: "bs_td.UpdateFeatureResponseTypeDef",
    ) -> "dc_td.UpdateFeatureResponse":
        return dc_td.UpdateFeatureResponse.make_one(res)

    def update_launch(
        self,
        res: "bs_td.UpdateLaunchResponseTypeDef",
    ) -> "dc_td.UpdateLaunchResponse":
        return dc_td.UpdateLaunchResponse.make_one(res)

    def update_project(
        self,
        res: "bs_td.UpdateProjectResponseTypeDef",
    ) -> "dc_td.UpdateProjectResponse":
        return dc_td.UpdateProjectResponse.make_one(res)

    def update_project_data_delivery(
        self,
        res: "bs_td.UpdateProjectDataDeliveryResponseTypeDef",
    ) -> "dc_td.UpdateProjectDataDeliveryResponse":
        return dc_td.UpdateProjectDataDeliveryResponse.make_one(res)


evidently_caster = EVIDENTLYCaster()
