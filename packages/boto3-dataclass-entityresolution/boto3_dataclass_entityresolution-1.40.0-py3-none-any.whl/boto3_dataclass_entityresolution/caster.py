# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_entityresolution import type_defs as bs_td


class ENTITYRESOLUTIONCaster:

    def add_policy_statement(
        self,
        res: "bs_td.AddPolicyStatementOutputTypeDef",
    ) -> "dc_td.AddPolicyStatementOutput":
        return dc_td.AddPolicyStatementOutput.make_one(res)

    def batch_delete_unique_id(
        self,
        res: "bs_td.BatchDeleteUniqueIdOutputTypeDef",
    ) -> "dc_td.BatchDeleteUniqueIdOutput":
        return dc_td.BatchDeleteUniqueIdOutput.make_one(res)

    def create_id_mapping_workflow(
        self,
        res: "bs_td.CreateIdMappingWorkflowOutputTypeDef",
    ) -> "dc_td.CreateIdMappingWorkflowOutput":
        return dc_td.CreateIdMappingWorkflowOutput.make_one(res)

    def create_id_namespace(
        self,
        res: "bs_td.CreateIdNamespaceOutputTypeDef",
    ) -> "dc_td.CreateIdNamespaceOutput":
        return dc_td.CreateIdNamespaceOutput.make_one(res)

    def create_matching_workflow(
        self,
        res: "bs_td.CreateMatchingWorkflowOutputTypeDef",
    ) -> "dc_td.CreateMatchingWorkflowOutput":
        return dc_td.CreateMatchingWorkflowOutput.make_one(res)

    def create_schema_mapping(
        self,
        res: "bs_td.CreateSchemaMappingOutputTypeDef",
    ) -> "dc_td.CreateSchemaMappingOutput":
        return dc_td.CreateSchemaMappingOutput.make_one(res)

    def delete_id_mapping_workflow(
        self,
        res: "bs_td.DeleteIdMappingWorkflowOutputTypeDef",
    ) -> "dc_td.DeleteIdMappingWorkflowOutput":
        return dc_td.DeleteIdMappingWorkflowOutput.make_one(res)

    def delete_id_namespace(
        self,
        res: "bs_td.DeleteIdNamespaceOutputTypeDef",
    ) -> "dc_td.DeleteIdNamespaceOutput":
        return dc_td.DeleteIdNamespaceOutput.make_one(res)

    def delete_matching_workflow(
        self,
        res: "bs_td.DeleteMatchingWorkflowOutputTypeDef",
    ) -> "dc_td.DeleteMatchingWorkflowOutput":
        return dc_td.DeleteMatchingWorkflowOutput.make_one(res)

    def delete_policy_statement(
        self,
        res: "bs_td.DeletePolicyStatementOutputTypeDef",
    ) -> "dc_td.DeletePolicyStatementOutput":
        return dc_td.DeletePolicyStatementOutput.make_one(res)

    def delete_schema_mapping(
        self,
        res: "bs_td.DeleteSchemaMappingOutputTypeDef",
    ) -> "dc_td.DeleteSchemaMappingOutput":
        return dc_td.DeleteSchemaMappingOutput.make_one(res)

    def generate_match_id(
        self,
        res: "bs_td.GenerateMatchIdOutputTypeDef",
    ) -> "dc_td.GenerateMatchIdOutput":
        return dc_td.GenerateMatchIdOutput.make_one(res)

    def get_id_mapping_job(
        self,
        res: "bs_td.GetIdMappingJobOutputTypeDef",
    ) -> "dc_td.GetIdMappingJobOutput":
        return dc_td.GetIdMappingJobOutput.make_one(res)

    def get_id_mapping_workflow(
        self,
        res: "bs_td.GetIdMappingWorkflowOutputTypeDef",
    ) -> "dc_td.GetIdMappingWorkflowOutput":
        return dc_td.GetIdMappingWorkflowOutput.make_one(res)

    def get_id_namespace(
        self,
        res: "bs_td.GetIdNamespaceOutputTypeDef",
    ) -> "dc_td.GetIdNamespaceOutput":
        return dc_td.GetIdNamespaceOutput.make_one(res)

    def get_match_id(
        self,
        res: "bs_td.GetMatchIdOutputTypeDef",
    ) -> "dc_td.GetMatchIdOutput":
        return dc_td.GetMatchIdOutput.make_one(res)

    def get_matching_job(
        self,
        res: "bs_td.GetMatchingJobOutputTypeDef",
    ) -> "dc_td.GetMatchingJobOutput":
        return dc_td.GetMatchingJobOutput.make_one(res)

    def get_matching_workflow(
        self,
        res: "bs_td.GetMatchingWorkflowOutputTypeDef",
    ) -> "dc_td.GetMatchingWorkflowOutput":
        return dc_td.GetMatchingWorkflowOutput.make_one(res)

    def get_policy(
        self,
        res: "bs_td.GetPolicyOutputTypeDef",
    ) -> "dc_td.GetPolicyOutput":
        return dc_td.GetPolicyOutput.make_one(res)

    def get_provider_service(
        self,
        res: "bs_td.GetProviderServiceOutputTypeDef",
    ) -> "dc_td.GetProviderServiceOutput":
        return dc_td.GetProviderServiceOutput.make_one(res)

    def get_schema_mapping(
        self,
        res: "bs_td.GetSchemaMappingOutputTypeDef",
    ) -> "dc_td.GetSchemaMappingOutput":
        return dc_td.GetSchemaMappingOutput.make_one(res)

    def list_id_mapping_jobs(
        self,
        res: "bs_td.ListIdMappingJobsOutputTypeDef",
    ) -> "dc_td.ListIdMappingJobsOutput":
        return dc_td.ListIdMappingJobsOutput.make_one(res)

    def list_id_mapping_workflows(
        self,
        res: "bs_td.ListIdMappingWorkflowsOutputTypeDef",
    ) -> "dc_td.ListIdMappingWorkflowsOutput":
        return dc_td.ListIdMappingWorkflowsOutput.make_one(res)

    def list_id_namespaces(
        self,
        res: "bs_td.ListIdNamespacesOutputTypeDef",
    ) -> "dc_td.ListIdNamespacesOutput":
        return dc_td.ListIdNamespacesOutput.make_one(res)

    def list_matching_jobs(
        self,
        res: "bs_td.ListMatchingJobsOutputTypeDef",
    ) -> "dc_td.ListMatchingJobsOutput":
        return dc_td.ListMatchingJobsOutput.make_one(res)

    def list_matching_workflows(
        self,
        res: "bs_td.ListMatchingWorkflowsOutputTypeDef",
    ) -> "dc_td.ListMatchingWorkflowsOutput":
        return dc_td.ListMatchingWorkflowsOutput.make_one(res)

    def list_provider_services(
        self,
        res: "bs_td.ListProviderServicesOutputTypeDef",
    ) -> "dc_td.ListProviderServicesOutput":
        return dc_td.ListProviderServicesOutput.make_one(res)

    def list_schema_mappings(
        self,
        res: "bs_td.ListSchemaMappingsOutputTypeDef",
    ) -> "dc_td.ListSchemaMappingsOutput":
        return dc_td.ListSchemaMappingsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def put_policy(
        self,
        res: "bs_td.PutPolicyOutputTypeDef",
    ) -> "dc_td.PutPolicyOutput":
        return dc_td.PutPolicyOutput.make_one(res)

    def start_id_mapping_job(
        self,
        res: "bs_td.StartIdMappingJobOutputTypeDef",
    ) -> "dc_td.StartIdMappingJobOutput":
        return dc_td.StartIdMappingJobOutput.make_one(res)

    def start_matching_job(
        self,
        res: "bs_td.StartMatchingJobOutputTypeDef",
    ) -> "dc_td.StartMatchingJobOutput":
        return dc_td.StartMatchingJobOutput.make_one(res)

    def update_id_mapping_workflow(
        self,
        res: "bs_td.UpdateIdMappingWorkflowOutputTypeDef",
    ) -> "dc_td.UpdateIdMappingWorkflowOutput":
        return dc_td.UpdateIdMappingWorkflowOutput.make_one(res)

    def update_id_namespace(
        self,
        res: "bs_td.UpdateIdNamespaceOutputTypeDef",
    ) -> "dc_td.UpdateIdNamespaceOutput":
        return dc_td.UpdateIdNamespaceOutput.make_one(res)

    def update_matching_workflow(
        self,
        res: "bs_td.UpdateMatchingWorkflowOutputTypeDef",
    ) -> "dc_td.UpdateMatchingWorkflowOutput":
        return dc_td.UpdateMatchingWorkflowOutput.make_one(res)

    def update_schema_mapping(
        self,
        res: "bs_td.UpdateSchemaMappingOutputTypeDef",
    ) -> "dc_td.UpdateSchemaMappingOutput":
        return dc_td.UpdateSchemaMappingOutput.make_one(res)


entityresolution_caster = ENTITYRESOLUTIONCaster()
