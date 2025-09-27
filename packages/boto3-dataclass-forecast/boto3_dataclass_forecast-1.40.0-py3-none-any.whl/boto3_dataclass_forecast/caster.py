# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_forecast import type_defs as bs_td


class FORECASTCaster:

    def create_auto_predictor(
        self,
        res: "bs_td.CreateAutoPredictorResponseTypeDef",
    ) -> "dc_td.CreateAutoPredictorResponse":
        return dc_td.CreateAutoPredictorResponse.make_one(res)

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_dataset_group(
        self,
        res: "bs_td.CreateDatasetGroupResponseTypeDef",
    ) -> "dc_td.CreateDatasetGroupResponse":
        return dc_td.CreateDatasetGroupResponse.make_one(res)

    def create_dataset_import_job(
        self,
        res: "bs_td.CreateDatasetImportJobResponseTypeDef",
    ) -> "dc_td.CreateDatasetImportJobResponse":
        return dc_td.CreateDatasetImportJobResponse.make_one(res)

    def create_explainability(
        self,
        res: "bs_td.CreateExplainabilityResponseTypeDef",
    ) -> "dc_td.CreateExplainabilityResponse":
        return dc_td.CreateExplainabilityResponse.make_one(res)

    def create_explainability_export(
        self,
        res: "bs_td.CreateExplainabilityExportResponseTypeDef",
    ) -> "dc_td.CreateExplainabilityExportResponse":
        return dc_td.CreateExplainabilityExportResponse.make_one(res)

    def create_forecast(
        self,
        res: "bs_td.CreateForecastResponseTypeDef",
    ) -> "dc_td.CreateForecastResponse":
        return dc_td.CreateForecastResponse.make_one(res)

    def create_forecast_export_job(
        self,
        res: "bs_td.CreateForecastExportJobResponseTypeDef",
    ) -> "dc_td.CreateForecastExportJobResponse":
        return dc_td.CreateForecastExportJobResponse.make_one(res)

    def create_monitor(
        self,
        res: "bs_td.CreateMonitorResponseTypeDef",
    ) -> "dc_td.CreateMonitorResponse":
        return dc_td.CreateMonitorResponse.make_one(res)

    def create_predictor(
        self,
        res: "bs_td.CreatePredictorResponseTypeDef",
    ) -> "dc_td.CreatePredictorResponse":
        return dc_td.CreatePredictorResponse.make_one(res)

    def create_predictor_backtest_export_job(
        self,
        res: "bs_td.CreatePredictorBacktestExportJobResponseTypeDef",
    ) -> "dc_td.CreatePredictorBacktestExportJobResponse":
        return dc_td.CreatePredictorBacktestExportJobResponse.make_one(res)

    def create_what_if_analysis(
        self,
        res: "bs_td.CreateWhatIfAnalysisResponseTypeDef",
    ) -> "dc_td.CreateWhatIfAnalysisResponse":
        return dc_td.CreateWhatIfAnalysisResponse.make_one(res)

    def create_what_if_forecast(
        self,
        res: "bs_td.CreateWhatIfForecastResponseTypeDef",
    ) -> "dc_td.CreateWhatIfForecastResponse":
        return dc_td.CreateWhatIfForecastResponse.make_one(res)

    def create_what_if_forecast_export(
        self,
        res: "bs_td.CreateWhatIfForecastExportResponseTypeDef",
    ) -> "dc_td.CreateWhatIfForecastExportResponse":
        return dc_td.CreateWhatIfForecastExportResponse.make_one(res)

    def delete_dataset(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_dataset_group(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_dataset_import_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_explainability(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_explainability_export(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_forecast(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_forecast_export_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_monitor(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_predictor(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_predictor_backtest_export_job(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_resource_tree(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_what_if_analysis(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_what_if_forecast(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_what_if_forecast_export(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_auto_predictor(
        self,
        res: "bs_td.DescribeAutoPredictorResponseTypeDef",
    ) -> "dc_td.DescribeAutoPredictorResponse":
        return dc_td.DescribeAutoPredictorResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_dataset_group(
        self,
        res: "bs_td.DescribeDatasetGroupResponseTypeDef",
    ) -> "dc_td.DescribeDatasetGroupResponse":
        return dc_td.DescribeDatasetGroupResponse.make_one(res)

    def describe_dataset_import_job(
        self,
        res: "bs_td.DescribeDatasetImportJobResponseTypeDef",
    ) -> "dc_td.DescribeDatasetImportJobResponse":
        return dc_td.DescribeDatasetImportJobResponse.make_one(res)

    def describe_explainability(
        self,
        res: "bs_td.DescribeExplainabilityResponseTypeDef",
    ) -> "dc_td.DescribeExplainabilityResponse":
        return dc_td.DescribeExplainabilityResponse.make_one(res)

    def describe_explainability_export(
        self,
        res: "bs_td.DescribeExplainabilityExportResponseTypeDef",
    ) -> "dc_td.DescribeExplainabilityExportResponse":
        return dc_td.DescribeExplainabilityExportResponse.make_one(res)

    def describe_forecast(
        self,
        res: "bs_td.DescribeForecastResponseTypeDef",
    ) -> "dc_td.DescribeForecastResponse":
        return dc_td.DescribeForecastResponse.make_one(res)

    def describe_forecast_export_job(
        self,
        res: "bs_td.DescribeForecastExportJobResponseTypeDef",
    ) -> "dc_td.DescribeForecastExportJobResponse":
        return dc_td.DescribeForecastExportJobResponse.make_one(res)

    def describe_monitor(
        self,
        res: "bs_td.DescribeMonitorResponseTypeDef",
    ) -> "dc_td.DescribeMonitorResponse":
        return dc_td.DescribeMonitorResponse.make_one(res)

    def describe_predictor(
        self,
        res: "bs_td.DescribePredictorResponseTypeDef",
    ) -> "dc_td.DescribePredictorResponse":
        return dc_td.DescribePredictorResponse.make_one(res)

    def describe_predictor_backtest_export_job(
        self,
        res: "bs_td.DescribePredictorBacktestExportJobResponseTypeDef",
    ) -> "dc_td.DescribePredictorBacktestExportJobResponse":
        return dc_td.DescribePredictorBacktestExportJobResponse.make_one(res)

    def describe_what_if_analysis(
        self,
        res: "bs_td.DescribeWhatIfAnalysisResponseTypeDef",
    ) -> "dc_td.DescribeWhatIfAnalysisResponse":
        return dc_td.DescribeWhatIfAnalysisResponse.make_one(res)

    def describe_what_if_forecast(
        self,
        res: "bs_td.DescribeWhatIfForecastResponseTypeDef",
    ) -> "dc_td.DescribeWhatIfForecastResponse":
        return dc_td.DescribeWhatIfForecastResponse.make_one(res)

    def describe_what_if_forecast_export(
        self,
        res: "bs_td.DescribeWhatIfForecastExportResponseTypeDef",
    ) -> "dc_td.DescribeWhatIfForecastExportResponse":
        return dc_td.DescribeWhatIfForecastExportResponse.make_one(res)

    def get_accuracy_metrics(
        self,
        res: "bs_td.GetAccuracyMetricsResponseTypeDef",
    ) -> "dc_td.GetAccuracyMetricsResponse":
        return dc_td.GetAccuracyMetricsResponse.make_one(res)

    def list_dataset_groups(
        self,
        res: "bs_td.ListDatasetGroupsResponseTypeDef",
    ) -> "dc_td.ListDatasetGroupsResponse":
        return dc_td.ListDatasetGroupsResponse.make_one(res)

    def list_dataset_import_jobs(
        self,
        res: "bs_td.ListDatasetImportJobsResponseTypeDef",
    ) -> "dc_td.ListDatasetImportJobsResponse":
        return dc_td.ListDatasetImportJobsResponse.make_one(res)

    def list_datasets(
        self,
        res: "bs_td.ListDatasetsResponseTypeDef",
    ) -> "dc_td.ListDatasetsResponse":
        return dc_td.ListDatasetsResponse.make_one(res)

    def list_explainabilities(
        self,
        res: "bs_td.ListExplainabilitiesResponseTypeDef",
    ) -> "dc_td.ListExplainabilitiesResponse":
        return dc_td.ListExplainabilitiesResponse.make_one(res)

    def list_explainability_exports(
        self,
        res: "bs_td.ListExplainabilityExportsResponseTypeDef",
    ) -> "dc_td.ListExplainabilityExportsResponse":
        return dc_td.ListExplainabilityExportsResponse.make_one(res)

    def list_forecast_export_jobs(
        self,
        res: "bs_td.ListForecastExportJobsResponseTypeDef",
    ) -> "dc_td.ListForecastExportJobsResponse":
        return dc_td.ListForecastExportJobsResponse.make_one(res)

    def list_forecasts(
        self,
        res: "bs_td.ListForecastsResponseTypeDef",
    ) -> "dc_td.ListForecastsResponse":
        return dc_td.ListForecastsResponse.make_one(res)

    def list_monitor_evaluations(
        self,
        res: "bs_td.ListMonitorEvaluationsResponseTypeDef",
    ) -> "dc_td.ListMonitorEvaluationsResponse":
        return dc_td.ListMonitorEvaluationsResponse.make_one(res)

    def list_monitors(
        self,
        res: "bs_td.ListMonitorsResponseTypeDef",
    ) -> "dc_td.ListMonitorsResponse":
        return dc_td.ListMonitorsResponse.make_one(res)

    def list_predictor_backtest_export_jobs(
        self,
        res: "bs_td.ListPredictorBacktestExportJobsResponseTypeDef",
    ) -> "dc_td.ListPredictorBacktestExportJobsResponse":
        return dc_td.ListPredictorBacktestExportJobsResponse.make_one(res)

    def list_predictors(
        self,
        res: "bs_td.ListPredictorsResponseTypeDef",
    ) -> "dc_td.ListPredictorsResponse":
        return dc_td.ListPredictorsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_what_if_analyses(
        self,
        res: "bs_td.ListWhatIfAnalysesResponseTypeDef",
    ) -> "dc_td.ListWhatIfAnalysesResponse":
        return dc_td.ListWhatIfAnalysesResponse.make_one(res)

    def list_what_if_forecast_exports(
        self,
        res: "bs_td.ListWhatIfForecastExportsResponseTypeDef",
    ) -> "dc_td.ListWhatIfForecastExportsResponse":
        return dc_td.ListWhatIfForecastExportsResponse.make_one(res)

    def list_what_if_forecasts(
        self,
        res: "bs_td.ListWhatIfForecastsResponseTypeDef",
    ) -> "dc_td.ListWhatIfForecastsResponse":
        return dc_td.ListWhatIfForecastsResponse.make_one(res)

    def resume_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def stop_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


forecast_caster = FORECASTCaster()
