# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_comprehendmedical import type_defs as bs_td


class COMPREHENDMEDICALCaster:

    def describe_entities_detection_v2_job(
        self,
        res: "bs_td.DescribeEntitiesDetectionV2JobResponseTypeDef",
    ) -> "dc_td.DescribeEntitiesDetectionV2JobResponse":
        return dc_td.DescribeEntitiesDetectionV2JobResponse.make_one(res)

    def describe_icd10_cm_inference_job(
        self,
        res: "bs_td.DescribeICD10CMInferenceJobResponseTypeDef",
    ) -> "dc_td.DescribeICD10CMInferenceJobResponse":
        return dc_td.DescribeICD10CMInferenceJobResponse.make_one(res)

    def describe_phi_detection_job(
        self,
        res: "bs_td.DescribePHIDetectionJobResponseTypeDef",
    ) -> "dc_td.DescribePHIDetectionJobResponse":
        return dc_td.DescribePHIDetectionJobResponse.make_one(res)

    def describe_rx_norm_inference_job(
        self,
        res: "bs_td.DescribeRxNormInferenceJobResponseTypeDef",
    ) -> "dc_td.DescribeRxNormInferenceJobResponse":
        return dc_td.DescribeRxNormInferenceJobResponse.make_one(res)

    def describe_snomedct_inference_job(
        self,
        res: "bs_td.DescribeSNOMEDCTInferenceJobResponseTypeDef",
    ) -> "dc_td.DescribeSNOMEDCTInferenceJobResponse":
        return dc_td.DescribeSNOMEDCTInferenceJobResponse.make_one(res)

    def detect_entities(
        self,
        res: "bs_td.DetectEntitiesResponseTypeDef",
    ) -> "dc_td.DetectEntitiesResponse":
        return dc_td.DetectEntitiesResponse.make_one(res)

    def detect_entities_v2(
        self,
        res: "bs_td.DetectEntitiesV2ResponseTypeDef",
    ) -> "dc_td.DetectEntitiesV2Response":
        return dc_td.DetectEntitiesV2Response.make_one(res)

    def detect_phi(
        self,
        res: "bs_td.DetectPHIResponseTypeDef",
    ) -> "dc_td.DetectPHIResponse":
        return dc_td.DetectPHIResponse.make_one(res)

    def infer_icd10_cm(
        self,
        res: "bs_td.InferICD10CMResponseTypeDef",
    ) -> "dc_td.InferICD10CMResponse":
        return dc_td.InferICD10CMResponse.make_one(res)

    def infer_rx_norm(
        self,
        res: "bs_td.InferRxNormResponseTypeDef",
    ) -> "dc_td.InferRxNormResponse":
        return dc_td.InferRxNormResponse.make_one(res)

    def infer_snomedct(
        self,
        res: "bs_td.InferSNOMEDCTResponseTypeDef",
    ) -> "dc_td.InferSNOMEDCTResponse":
        return dc_td.InferSNOMEDCTResponse.make_one(res)

    def list_entities_detection_v2_jobs(
        self,
        res: "bs_td.ListEntitiesDetectionV2JobsResponseTypeDef",
    ) -> "dc_td.ListEntitiesDetectionV2JobsResponse":
        return dc_td.ListEntitiesDetectionV2JobsResponse.make_one(res)

    def list_icd10_cm_inference_jobs(
        self,
        res: "bs_td.ListICD10CMInferenceJobsResponseTypeDef",
    ) -> "dc_td.ListICD10CMInferenceJobsResponse":
        return dc_td.ListICD10CMInferenceJobsResponse.make_one(res)

    def list_phi_detection_jobs(
        self,
        res: "bs_td.ListPHIDetectionJobsResponseTypeDef",
    ) -> "dc_td.ListPHIDetectionJobsResponse":
        return dc_td.ListPHIDetectionJobsResponse.make_one(res)

    def list_rx_norm_inference_jobs(
        self,
        res: "bs_td.ListRxNormInferenceJobsResponseTypeDef",
    ) -> "dc_td.ListRxNormInferenceJobsResponse":
        return dc_td.ListRxNormInferenceJobsResponse.make_one(res)

    def list_snomedct_inference_jobs(
        self,
        res: "bs_td.ListSNOMEDCTInferenceJobsResponseTypeDef",
    ) -> "dc_td.ListSNOMEDCTInferenceJobsResponse":
        return dc_td.ListSNOMEDCTInferenceJobsResponse.make_one(res)

    def start_entities_detection_v2_job(
        self,
        res: "bs_td.StartEntitiesDetectionV2JobResponseTypeDef",
    ) -> "dc_td.StartEntitiesDetectionV2JobResponse":
        return dc_td.StartEntitiesDetectionV2JobResponse.make_one(res)

    def start_icd10_cm_inference_job(
        self,
        res: "bs_td.StartICD10CMInferenceJobResponseTypeDef",
    ) -> "dc_td.StartICD10CMInferenceJobResponse":
        return dc_td.StartICD10CMInferenceJobResponse.make_one(res)

    def start_phi_detection_job(
        self,
        res: "bs_td.StartPHIDetectionJobResponseTypeDef",
    ) -> "dc_td.StartPHIDetectionJobResponse":
        return dc_td.StartPHIDetectionJobResponse.make_one(res)

    def start_rx_norm_inference_job(
        self,
        res: "bs_td.StartRxNormInferenceJobResponseTypeDef",
    ) -> "dc_td.StartRxNormInferenceJobResponse":
        return dc_td.StartRxNormInferenceJobResponse.make_one(res)

    def start_snomedct_inference_job(
        self,
        res: "bs_td.StartSNOMEDCTInferenceJobResponseTypeDef",
    ) -> "dc_td.StartSNOMEDCTInferenceJobResponse":
        return dc_td.StartSNOMEDCTInferenceJobResponse.make_one(res)

    def stop_entities_detection_v2_job(
        self,
        res: "bs_td.StopEntitiesDetectionV2JobResponseTypeDef",
    ) -> "dc_td.StopEntitiesDetectionV2JobResponse":
        return dc_td.StopEntitiesDetectionV2JobResponse.make_one(res)

    def stop_icd10_cm_inference_job(
        self,
        res: "bs_td.StopICD10CMInferenceJobResponseTypeDef",
    ) -> "dc_td.StopICD10CMInferenceJobResponse":
        return dc_td.StopICD10CMInferenceJobResponse.make_one(res)

    def stop_phi_detection_job(
        self,
        res: "bs_td.StopPHIDetectionJobResponseTypeDef",
    ) -> "dc_td.StopPHIDetectionJobResponse":
        return dc_td.StopPHIDetectionJobResponse.make_one(res)

    def stop_rx_norm_inference_job(
        self,
        res: "bs_td.StopRxNormInferenceJobResponseTypeDef",
    ) -> "dc_td.StopRxNormInferenceJobResponse":
        return dc_td.StopRxNormInferenceJobResponse.make_one(res)

    def stop_snomedct_inference_job(
        self,
        res: "bs_td.StopSNOMEDCTInferenceJobResponseTypeDef",
    ) -> "dc_td.StopSNOMEDCTInferenceJobResponse":
        return dc_td.StopSNOMEDCTInferenceJobResponse.make_one(res)


comprehendmedical_caster = COMPREHENDMEDICALCaster()
