# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_comprehend import type_defs as bs_td


class COMPREHENDCaster:

    def batch_detect_dominant_language(
        self,
        res: "bs_td.BatchDetectDominantLanguageResponseTypeDef",
    ) -> "dc_td.BatchDetectDominantLanguageResponse":
        return dc_td.BatchDetectDominantLanguageResponse.make_one(res)

    def batch_detect_entities(
        self,
        res: "bs_td.BatchDetectEntitiesResponseTypeDef",
    ) -> "dc_td.BatchDetectEntitiesResponse":
        return dc_td.BatchDetectEntitiesResponse.make_one(res)

    def batch_detect_key_phrases(
        self,
        res: "bs_td.BatchDetectKeyPhrasesResponseTypeDef",
    ) -> "dc_td.BatchDetectKeyPhrasesResponse":
        return dc_td.BatchDetectKeyPhrasesResponse.make_one(res)

    def batch_detect_sentiment(
        self,
        res: "bs_td.BatchDetectSentimentResponseTypeDef",
    ) -> "dc_td.BatchDetectSentimentResponse":
        return dc_td.BatchDetectSentimentResponse.make_one(res)

    def batch_detect_syntax(
        self,
        res: "bs_td.BatchDetectSyntaxResponseTypeDef",
    ) -> "dc_td.BatchDetectSyntaxResponse":
        return dc_td.BatchDetectSyntaxResponse.make_one(res)

    def batch_detect_targeted_sentiment(
        self,
        res: "bs_td.BatchDetectTargetedSentimentResponseTypeDef",
    ) -> "dc_td.BatchDetectTargetedSentimentResponse":
        return dc_td.BatchDetectTargetedSentimentResponse.make_one(res)

    def classify_document(
        self,
        res: "bs_td.ClassifyDocumentResponseTypeDef",
    ) -> "dc_td.ClassifyDocumentResponse":
        return dc_td.ClassifyDocumentResponse.make_one(res)

    def contains_pii_entities(
        self,
        res: "bs_td.ContainsPiiEntitiesResponseTypeDef",
    ) -> "dc_td.ContainsPiiEntitiesResponse":
        return dc_td.ContainsPiiEntitiesResponse.make_one(res)

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_document_classifier(
        self,
        res: "bs_td.CreateDocumentClassifierResponseTypeDef",
    ) -> "dc_td.CreateDocumentClassifierResponse":
        return dc_td.CreateDocumentClassifierResponse.make_one(res)

    def create_endpoint(
        self,
        res: "bs_td.CreateEndpointResponseTypeDef",
    ) -> "dc_td.CreateEndpointResponse":
        return dc_td.CreateEndpointResponse.make_one(res)

    def create_entity_recognizer(
        self,
        res: "bs_td.CreateEntityRecognizerResponseTypeDef",
    ) -> "dc_td.CreateEntityRecognizerResponse":
        return dc_td.CreateEntityRecognizerResponse.make_one(res)

    def create_flywheel(
        self,
        res: "bs_td.CreateFlywheelResponseTypeDef",
    ) -> "dc_td.CreateFlywheelResponse":
        return dc_td.CreateFlywheelResponse.make_one(res)

    def describe_dataset(
        self,
        res: "bs_td.DescribeDatasetResponseTypeDef",
    ) -> "dc_td.DescribeDatasetResponse":
        return dc_td.DescribeDatasetResponse.make_one(res)

    def describe_document_classification_job(
        self,
        res: "bs_td.DescribeDocumentClassificationJobResponseTypeDef",
    ) -> "dc_td.DescribeDocumentClassificationJobResponse":
        return dc_td.DescribeDocumentClassificationJobResponse.make_one(res)

    def describe_document_classifier(
        self,
        res: "bs_td.DescribeDocumentClassifierResponseTypeDef",
    ) -> "dc_td.DescribeDocumentClassifierResponse":
        return dc_td.DescribeDocumentClassifierResponse.make_one(res)

    def describe_dominant_language_detection_job(
        self,
        res: "bs_td.DescribeDominantLanguageDetectionJobResponseTypeDef",
    ) -> "dc_td.DescribeDominantLanguageDetectionJobResponse":
        return dc_td.DescribeDominantLanguageDetectionJobResponse.make_one(res)

    def describe_endpoint(
        self,
        res: "bs_td.DescribeEndpointResponseTypeDef",
    ) -> "dc_td.DescribeEndpointResponse":
        return dc_td.DescribeEndpointResponse.make_one(res)

    def describe_entities_detection_job(
        self,
        res: "bs_td.DescribeEntitiesDetectionJobResponseTypeDef",
    ) -> "dc_td.DescribeEntitiesDetectionJobResponse":
        return dc_td.DescribeEntitiesDetectionJobResponse.make_one(res)

    def describe_entity_recognizer(
        self,
        res: "bs_td.DescribeEntityRecognizerResponseTypeDef",
    ) -> "dc_td.DescribeEntityRecognizerResponse":
        return dc_td.DescribeEntityRecognizerResponse.make_one(res)

    def describe_events_detection_job(
        self,
        res: "bs_td.DescribeEventsDetectionJobResponseTypeDef",
    ) -> "dc_td.DescribeEventsDetectionJobResponse":
        return dc_td.DescribeEventsDetectionJobResponse.make_one(res)

    def describe_flywheel(
        self,
        res: "bs_td.DescribeFlywheelResponseTypeDef",
    ) -> "dc_td.DescribeFlywheelResponse":
        return dc_td.DescribeFlywheelResponse.make_one(res)

    def describe_flywheel_iteration(
        self,
        res: "bs_td.DescribeFlywheelIterationResponseTypeDef",
    ) -> "dc_td.DescribeFlywheelIterationResponse":
        return dc_td.DescribeFlywheelIterationResponse.make_one(res)

    def describe_key_phrases_detection_job(
        self,
        res: "bs_td.DescribeKeyPhrasesDetectionJobResponseTypeDef",
    ) -> "dc_td.DescribeKeyPhrasesDetectionJobResponse":
        return dc_td.DescribeKeyPhrasesDetectionJobResponse.make_one(res)

    def describe_pii_entities_detection_job(
        self,
        res: "bs_td.DescribePiiEntitiesDetectionJobResponseTypeDef",
    ) -> "dc_td.DescribePiiEntitiesDetectionJobResponse":
        return dc_td.DescribePiiEntitiesDetectionJobResponse.make_one(res)

    def describe_resource_policy(
        self,
        res: "bs_td.DescribeResourcePolicyResponseTypeDef",
    ) -> "dc_td.DescribeResourcePolicyResponse":
        return dc_td.DescribeResourcePolicyResponse.make_one(res)

    def describe_sentiment_detection_job(
        self,
        res: "bs_td.DescribeSentimentDetectionJobResponseTypeDef",
    ) -> "dc_td.DescribeSentimentDetectionJobResponse":
        return dc_td.DescribeSentimentDetectionJobResponse.make_one(res)

    def describe_targeted_sentiment_detection_job(
        self,
        res: "bs_td.DescribeTargetedSentimentDetectionJobResponseTypeDef",
    ) -> "dc_td.DescribeTargetedSentimentDetectionJobResponse":
        return dc_td.DescribeTargetedSentimentDetectionJobResponse.make_one(res)

    def describe_topics_detection_job(
        self,
        res: "bs_td.DescribeTopicsDetectionJobResponseTypeDef",
    ) -> "dc_td.DescribeTopicsDetectionJobResponse":
        return dc_td.DescribeTopicsDetectionJobResponse.make_one(res)

    def detect_dominant_language(
        self,
        res: "bs_td.DetectDominantLanguageResponseTypeDef",
    ) -> "dc_td.DetectDominantLanguageResponse":
        return dc_td.DetectDominantLanguageResponse.make_one(res)

    def detect_entities(
        self,
        res: "bs_td.DetectEntitiesResponseTypeDef",
    ) -> "dc_td.DetectEntitiesResponse":
        return dc_td.DetectEntitiesResponse.make_one(res)

    def detect_key_phrases(
        self,
        res: "bs_td.DetectKeyPhrasesResponseTypeDef",
    ) -> "dc_td.DetectKeyPhrasesResponse":
        return dc_td.DetectKeyPhrasesResponse.make_one(res)

    def detect_pii_entities(
        self,
        res: "bs_td.DetectPiiEntitiesResponseTypeDef",
    ) -> "dc_td.DetectPiiEntitiesResponse":
        return dc_td.DetectPiiEntitiesResponse.make_one(res)

    def detect_sentiment(
        self,
        res: "bs_td.DetectSentimentResponseTypeDef",
    ) -> "dc_td.DetectSentimentResponse":
        return dc_td.DetectSentimentResponse.make_one(res)

    def detect_syntax(
        self,
        res: "bs_td.DetectSyntaxResponseTypeDef",
    ) -> "dc_td.DetectSyntaxResponse":
        return dc_td.DetectSyntaxResponse.make_one(res)

    def detect_targeted_sentiment(
        self,
        res: "bs_td.DetectTargetedSentimentResponseTypeDef",
    ) -> "dc_td.DetectTargetedSentimentResponse":
        return dc_td.DetectTargetedSentimentResponse.make_one(res)

    def detect_toxic_content(
        self,
        res: "bs_td.DetectToxicContentResponseTypeDef",
    ) -> "dc_td.DetectToxicContentResponse":
        return dc_td.DetectToxicContentResponse.make_one(res)

    def import_model(
        self,
        res: "bs_td.ImportModelResponseTypeDef",
    ) -> "dc_td.ImportModelResponse":
        return dc_td.ImportModelResponse.make_one(res)

    def list_datasets(
        self,
        res: "bs_td.ListDatasetsResponseTypeDef",
    ) -> "dc_td.ListDatasetsResponse":
        return dc_td.ListDatasetsResponse.make_one(res)

    def list_document_classification_jobs(
        self,
        res: "bs_td.ListDocumentClassificationJobsResponseTypeDef",
    ) -> "dc_td.ListDocumentClassificationJobsResponse":
        return dc_td.ListDocumentClassificationJobsResponse.make_one(res)

    def list_document_classifier_summaries(
        self,
        res: "bs_td.ListDocumentClassifierSummariesResponseTypeDef",
    ) -> "dc_td.ListDocumentClassifierSummariesResponse":
        return dc_td.ListDocumentClassifierSummariesResponse.make_one(res)

    def list_document_classifiers(
        self,
        res: "bs_td.ListDocumentClassifiersResponseTypeDef",
    ) -> "dc_td.ListDocumentClassifiersResponse":
        return dc_td.ListDocumentClassifiersResponse.make_one(res)

    def list_dominant_language_detection_jobs(
        self,
        res: "bs_td.ListDominantLanguageDetectionJobsResponseTypeDef",
    ) -> "dc_td.ListDominantLanguageDetectionJobsResponse":
        return dc_td.ListDominantLanguageDetectionJobsResponse.make_one(res)

    def list_endpoints(
        self,
        res: "bs_td.ListEndpointsResponseTypeDef",
    ) -> "dc_td.ListEndpointsResponse":
        return dc_td.ListEndpointsResponse.make_one(res)

    def list_entities_detection_jobs(
        self,
        res: "bs_td.ListEntitiesDetectionJobsResponseTypeDef",
    ) -> "dc_td.ListEntitiesDetectionJobsResponse":
        return dc_td.ListEntitiesDetectionJobsResponse.make_one(res)

    def list_entity_recognizer_summaries(
        self,
        res: "bs_td.ListEntityRecognizerSummariesResponseTypeDef",
    ) -> "dc_td.ListEntityRecognizerSummariesResponse":
        return dc_td.ListEntityRecognizerSummariesResponse.make_one(res)

    def list_entity_recognizers(
        self,
        res: "bs_td.ListEntityRecognizersResponseTypeDef",
    ) -> "dc_td.ListEntityRecognizersResponse":
        return dc_td.ListEntityRecognizersResponse.make_one(res)

    def list_events_detection_jobs(
        self,
        res: "bs_td.ListEventsDetectionJobsResponseTypeDef",
    ) -> "dc_td.ListEventsDetectionJobsResponse":
        return dc_td.ListEventsDetectionJobsResponse.make_one(res)

    def list_flywheel_iteration_history(
        self,
        res: "bs_td.ListFlywheelIterationHistoryResponseTypeDef",
    ) -> "dc_td.ListFlywheelIterationHistoryResponse":
        return dc_td.ListFlywheelIterationHistoryResponse.make_one(res)

    def list_flywheels(
        self,
        res: "bs_td.ListFlywheelsResponseTypeDef",
    ) -> "dc_td.ListFlywheelsResponse":
        return dc_td.ListFlywheelsResponse.make_one(res)

    def list_key_phrases_detection_jobs(
        self,
        res: "bs_td.ListKeyPhrasesDetectionJobsResponseTypeDef",
    ) -> "dc_td.ListKeyPhrasesDetectionJobsResponse":
        return dc_td.ListKeyPhrasesDetectionJobsResponse.make_one(res)

    def list_pii_entities_detection_jobs(
        self,
        res: "bs_td.ListPiiEntitiesDetectionJobsResponseTypeDef",
    ) -> "dc_td.ListPiiEntitiesDetectionJobsResponse":
        return dc_td.ListPiiEntitiesDetectionJobsResponse.make_one(res)

    def list_sentiment_detection_jobs(
        self,
        res: "bs_td.ListSentimentDetectionJobsResponseTypeDef",
    ) -> "dc_td.ListSentimentDetectionJobsResponse":
        return dc_td.ListSentimentDetectionJobsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_targeted_sentiment_detection_jobs(
        self,
        res: "bs_td.ListTargetedSentimentDetectionJobsResponseTypeDef",
    ) -> "dc_td.ListTargetedSentimentDetectionJobsResponse":
        return dc_td.ListTargetedSentimentDetectionJobsResponse.make_one(res)

    def list_topics_detection_jobs(
        self,
        res: "bs_td.ListTopicsDetectionJobsResponseTypeDef",
    ) -> "dc_td.ListTopicsDetectionJobsResponse":
        return dc_td.ListTopicsDetectionJobsResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def start_document_classification_job(
        self,
        res: "bs_td.StartDocumentClassificationJobResponseTypeDef",
    ) -> "dc_td.StartDocumentClassificationJobResponse":
        return dc_td.StartDocumentClassificationJobResponse.make_one(res)

    def start_dominant_language_detection_job(
        self,
        res: "bs_td.StartDominantLanguageDetectionJobResponseTypeDef",
    ) -> "dc_td.StartDominantLanguageDetectionJobResponse":
        return dc_td.StartDominantLanguageDetectionJobResponse.make_one(res)

    def start_entities_detection_job(
        self,
        res: "bs_td.StartEntitiesDetectionJobResponseTypeDef",
    ) -> "dc_td.StartEntitiesDetectionJobResponse":
        return dc_td.StartEntitiesDetectionJobResponse.make_one(res)

    def start_events_detection_job(
        self,
        res: "bs_td.StartEventsDetectionJobResponseTypeDef",
    ) -> "dc_td.StartEventsDetectionJobResponse":
        return dc_td.StartEventsDetectionJobResponse.make_one(res)

    def start_flywheel_iteration(
        self,
        res: "bs_td.StartFlywheelIterationResponseTypeDef",
    ) -> "dc_td.StartFlywheelIterationResponse":
        return dc_td.StartFlywheelIterationResponse.make_one(res)

    def start_key_phrases_detection_job(
        self,
        res: "bs_td.StartKeyPhrasesDetectionJobResponseTypeDef",
    ) -> "dc_td.StartKeyPhrasesDetectionJobResponse":
        return dc_td.StartKeyPhrasesDetectionJobResponse.make_one(res)

    def start_pii_entities_detection_job(
        self,
        res: "bs_td.StartPiiEntitiesDetectionJobResponseTypeDef",
    ) -> "dc_td.StartPiiEntitiesDetectionJobResponse":
        return dc_td.StartPiiEntitiesDetectionJobResponse.make_one(res)

    def start_sentiment_detection_job(
        self,
        res: "bs_td.StartSentimentDetectionJobResponseTypeDef",
    ) -> "dc_td.StartSentimentDetectionJobResponse":
        return dc_td.StartSentimentDetectionJobResponse.make_one(res)

    def start_targeted_sentiment_detection_job(
        self,
        res: "bs_td.StartTargetedSentimentDetectionJobResponseTypeDef",
    ) -> "dc_td.StartTargetedSentimentDetectionJobResponse":
        return dc_td.StartTargetedSentimentDetectionJobResponse.make_one(res)

    def start_topics_detection_job(
        self,
        res: "bs_td.StartTopicsDetectionJobResponseTypeDef",
    ) -> "dc_td.StartTopicsDetectionJobResponse":
        return dc_td.StartTopicsDetectionJobResponse.make_one(res)

    def stop_dominant_language_detection_job(
        self,
        res: "bs_td.StopDominantLanguageDetectionJobResponseTypeDef",
    ) -> "dc_td.StopDominantLanguageDetectionJobResponse":
        return dc_td.StopDominantLanguageDetectionJobResponse.make_one(res)

    def stop_entities_detection_job(
        self,
        res: "bs_td.StopEntitiesDetectionJobResponseTypeDef",
    ) -> "dc_td.StopEntitiesDetectionJobResponse":
        return dc_td.StopEntitiesDetectionJobResponse.make_one(res)

    def stop_events_detection_job(
        self,
        res: "bs_td.StopEventsDetectionJobResponseTypeDef",
    ) -> "dc_td.StopEventsDetectionJobResponse":
        return dc_td.StopEventsDetectionJobResponse.make_one(res)

    def stop_key_phrases_detection_job(
        self,
        res: "bs_td.StopKeyPhrasesDetectionJobResponseTypeDef",
    ) -> "dc_td.StopKeyPhrasesDetectionJobResponse":
        return dc_td.StopKeyPhrasesDetectionJobResponse.make_one(res)

    def stop_pii_entities_detection_job(
        self,
        res: "bs_td.StopPiiEntitiesDetectionJobResponseTypeDef",
    ) -> "dc_td.StopPiiEntitiesDetectionJobResponse":
        return dc_td.StopPiiEntitiesDetectionJobResponse.make_one(res)

    def stop_sentiment_detection_job(
        self,
        res: "bs_td.StopSentimentDetectionJobResponseTypeDef",
    ) -> "dc_td.StopSentimentDetectionJobResponse":
        return dc_td.StopSentimentDetectionJobResponse.make_one(res)

    def stop_targeted_sentiment_detection_job(
        self,
        res: "bs_td.StopTargetedSentimentDetectionJobResponseTypeDef",
    ) -> "dc_td.StopTargetedSentimentDetectionJobResponse":
        return dc_td.StopTargetedSentimentDetectionJobResponse.make_one(res)

    def update_endpoint(
        self,
        res: "bs_td.UpdateEndpointResponseTypeDef",
    ) -> "dc_td.UpdateEndpointResponse":
        return dc_td.UpdateEndpointResponse.make_one(res)

    def update_flywheel(
        self,
        res: "bs_td.UpdateFlywheelResponseTypeDef",
    ) -> "dc_td.UpdateFlywheelResponse":
        return dc_td.UpdateFlywheelResponse.make_one(res)


comprehend_caster = COMPREHENDCaster()
