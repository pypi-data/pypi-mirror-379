# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock_agent import type_defs as bs_td


class BEDROCK_AGENTCaster:

    def associate_agent_collaborator(
        self,
        res: "bs_td.AssociateAgentCollaboratorResponseTypeDef",
    ) -> "dc_td.AssociateAgentCollaboratorResponse":
        return dc_td.AssociateAgentCollaboratorResponse.make_one(res)

    def associate_agent_knowledge_base(
        self,
        res: "bs_td.AssociateAgentKnowledgeBaseResponseTypeDef",
    ) -> "dc_td.AssociateAgentKnowledgeBaseResponse":
        return dc_td.AssociateAgentKnowledgeBaseResponse.make_one(res)

    def create_agent(
        self,
        res: "bs_td.CreateAgentResponseTypeDef",
    ) -> "dc_td.CreateAgentResponse":
        return dc_td.CreateAgentResponse.make_one(res)

    def create_agent_action_group(
        self,
        res: "bs_td.CreateAgentActionGroupResponseTypeDef",
    ) -> "dc_td.CreateAgentActionGroupResponse":
        return dc_td.CreateAgentActionGroupResponse.make_one(res)

    def create_agent_alias(
        self,
        res: "bs_td.CreateAgentAliasResponseTypeDef",
    ) -> "dc_td.CreateAgentAliasResponse":
        return dc_td.CreateAgentAliasResponse.make_one(res)

    def create_data_source(
        self,
        res: "bs_td.CreateDataSourceResponseTypeDef",
    ) -> "dc_td.CreateDataSourceResponse":
        return dc_td.CreateDataSourceResponse.make_one(res)

    def create_flow(
        self,
        res: "bs_td.CreateFlowResponseTypeDef",
    ) -> "dc_td.CreateFlowResponse":
        return dc_td.CreateFlowResponse.make_one(res)

    def create_flow_alias(
        self,
        res: "bs_td.CreateFlowAliasResponseTypeDef",
    ) -> "dc_td.CreateFlowAliasResponse":
        return dc_td.CreateFlowAliasResponse.make_one(res)

    def create_flow_version(
        self,
        res: "bs_td.CreateFlowVersionResponseTypeDef",
    ) -> "dc_td.CreateFlowVersionResponse":
        return dc_td.CreateFlowVersionResponse.make_one(res)

    def create_knowledge_base(
        self,
        res: "bs_td.CreateKnowledgeBaseResponseTypeDef",
    ) -> "dc_td.CreateKnowledgeBaseResponse":
        return dc_td.CreateKnowledgeBaseResponse.make_one(res)

    def create_prompt(
        self,
        res: "bs_td.CreatePromptResponseTypeDef",
    ) -> "dc_td.CreatePromptResponse":
        return dc_td.CreatePromptResponse.make_one(res)

    def create_prompt_version(
        self,
        res: "bs_td.CreatePromptVersionResponseTypeDef",
    ) -> "dc_td.CreatePromptVersionResponse":
        return dc_td.CreatePromptVersionResponse.make_one(res)

    def delete_agent(
        self,
        res: "bs_td.DeleteAgentResponseTypeDef",
    ) -> "dc_td.DeleteAgentResponse":
        return dc_td.DeleteAgentResponse.make_one(res)

    def delete_agent_alias(
        self,
        res: "bs_td.DeleteAgentAliasResponseTypeDef",
    ) -> "dc_td.DeleteAgentAliasResponse":
        return dc_td.DeleteAgentAliasResponse.make_one(res)

    def delete_agent_version(
        self,
        res: "bs_td.DeleteAgentVersionResponseTypeDef",
    ) -> "dc_td.DeleteAgentVersionResponse":
        return dc_td.DeleteAgentVersionResponse.make_one(res)

    def delete_data_source(
        self,
        res: "bs_td.DeleteDataSourceResponseTypeDef",
    ) -> "dc_td.DeleteDataSourceResponse":
        return dc_td.DeleteDataSourceResponse.make_one(res)

    def delete_flow(
        self,
        res: "bs_td.DeleteFlowResponseTypeDef",
    ) -> "dc_td.DeleteFlowResponse":
        return dc_td.DeleteFlowResponse.make_one(res)

    def delete_flow_alias(
        self,
        res: "bs_td.DeleteFlowAliasResponseTypeDef",
    ) -> "dc_td.DeleteFlowAliasResponse":
        return dc_td.DeleteFlowAliasResponse.make_one(res)

    def delete_flow_version(
        self,
        res: "bs_td.DeleteFlowVersionResponseTypeDef",
    ) -> "dc_td.DeleteFlowVersionResponse":
        return dc_td.DeleteFlowVersionResponse.make_one(res)

    def delete_knowledge_base(
        self,
        res: "bs_td.DeleteKnowledgeBaseResponseTypeDef",
    ) -> "dc_td.DeleteKnowledgeBaseResponse":
        return dc_td.DeleteKnowledgeBaseResponse.make_one(res)

    def delete_knowledge_base_documents(
        self,
        res: "bs_td.DeleteKnowledgeBaseDocumentsResponseTypeDef",
    ) -> "dc_td.DeleteKnowledgeBaseDocumentsResponse":
        return dc_td.DeleteKnowledgeBaseDocumentsResponse.make_one(res)

    def delete_prompt(
        self,
        res: "bs_td.DeletePromptResponseTypeDef",
    ) -> "dc_td.DeletePromptResponse":
        return dc_td.DeletePromptResponse.make_one(res)

    def get_agent(
        self,
        res: "bs_td.GetAgentResponseTypeDef",
    ) -> "dc_td.GetAgentResponse":
        return dc_td.GetAgentResponse.make_one(res)

    def get_agent_action_group(
        self,
        res: "bs_td.GetAgentActionGroupResponseTypeDef",
    ) -> "dc_td.GetAgentActionGroupResponse":
        return dc_td.GetAgentActionGroupResponse.make_one(res)

    def get_agent_alias(
        self,
        res: "bs_td.GetAgentAliasResponseTypeDef",
    ) -> "dc_td.GetAgentAliasResponse":
        return dc_td.GetAgentAliasResponse.make_one(res)

    def get_agent_collaborator(
        self,
        res: "bs_td.GetAgentCollaboratorResponseTypeDef",
    ) -> "dc_td.GetAgentCollaboratorResponse":
        return dc_td.GetAgentCollaboratorResponse.make_one(res)

    def get_agent_knowledge_base(
        self,
        res: "bs_td.GetAgentKnowledgeBaseResponseTypeDef",
    ) -> "dc_td.GetAgentKnowledgeBaseResponse":
        return dc_td.GetAgentKnowledgeBaseResponse.make_one(res)

    def get_agent_version(
        self,
        res: "bs_td.GetAgentVersionResponseTypeDef",
    ) -> "dc_td.GetAgentVersionResponse":
        return dc_td.GetAgentVersionResponse.make_one(res)

    def get_data_source(
        self,
        res: "bs_td.GetDataSourceResponseTypeDef",
    ) -> "dc_td.GetDataSourceResponse":
        return dc_td.GetDataSourceResponse.make_one(res)

    def get_flow(
        self,
        res: "bs_td.GetFlowResponseTypeDef",
    ) -> "dc_td.GetFlowResponse":
        return dc_td.GetFlowResponse.make_one(res)

    def get_flow_alias(
        self,
        res: "bs_td.GetFlowAliasResponseTypeDef",
    ) -> "dc_td.GetFlowAliasResponse":
        return dc_td.GetFlowAliasResponse.make_one(res)

    def get_flow_version(
        self,
        res: "bs_td.GetFlowVersionResponseTypeDef",
    ) -> "dc_td.GetFlowVersionResponse":
        return dc_td.GetFlowVersionResponse.make_one(res)

    def get_ingestion_job(
        self,
        res: "bs_td.GetIngestionJobResponseTypeDef",
    ) -> "dc_td.GetIngestionJobResponse":
        return dc_td.GetIngestionJobResponse.make_one(res)

    def get_knowledge_base(
        self,
        res: "bs_td.GetKnowledgeBaseResponseTypeDef",
    ) -> "dc_td.GetKnowledgeBaseResponse":
        return dc_td.GetKnowledgeBaseResponse.make_one(res)

    def get_knowledge_base_documents(
        self,
        res: "bs_td.GetKnowledgeBaseDocumentsResponseTypeDef",
    ) -> "dc_td.GetKnowledgeBaseDocumentsResponse":
        return dc_td.GetKnowledgeBaseDocumentsResponse.make_one(res)

    def get_prompt(
        self,
        res: "bs_td.GetPromptResponseTypeDef",
    ) -> "dc_td.GetPromptResponse":
        return dc_td.GetPromptResponse.make_one(res)

    def ingest_knowledge_base_documents(
        self,
        res: "bs_td.IngestKnowledgeBaseDocumentsResponseTypeDef",
    ) -> "dc_td.IngestKnowledgeBaseDocumentsResponse":
        return dc_td.IngestKnowledgeBaseDocumentsResponse.make_one(res)

    def list_agent_action_groups(
        self,
        res: "bs_td.ListAgentActionGroupsResponseTypeDef",
    ) -> "dc_td.ListAgentActionGroupsResponse":
        return dc_td.ListAgentActionGroupsResponse.make_one(res)

    def list_agent_aliases(
        self,
        res: "bs_td.ListAgentAliasesResponseTypeDef",
    ) -> "dc_td.ListAgentAliasesResponse":
        return dc_td.ListAgentAliasesResponse.make_one(res)

    def list_agent_collaborators(
        self,
        res: "bs_td.ListAgentCollaboratorsResponseTypeDef",
    ) -> "dc_td.ListAgentCollaboratorsResponse":
        return dc_td.ListAgentCollaboratorsResponse.make_one(res)

    def list_agent_knowledge_bases(
        self,
        res: "bs_td.ListAgentKnowledgeBasesResponseTypeDef",
    ) -> "dc_td.ListAgentKnowledgeBasesResponse":
        return dc_td.ListAgentKnowledgeBasesResponse.make_one(res)

    def list_agent_versions(
        self,
        res: "bs_td.ListAgentVersionsResponseTypeDef",
    ) -> "dc_td.ListAgentVersionsResponse":
        return dc_td.ListAgentVersionsResponse.make_one(res)

    def list_agents(
        self,
        res: "bs_td.ListAgentsResponseTypeDef",
    ) -> "dc_td.ListAgentsResponse":
        return dc_td.ListAgentsResponse.make_one(res)

    def list_data_sources(
        self,
        res: "bs_td.ListDataSourcesResponseTypeDef",
    ) -> "dc_td.ListDataSourcesResponse":
        return dc_td.ListDataSourcesResponse.make_one(res)

    def list_flow_aliases(
        self,
        res: "bs_td.ListFlowAliasesResponseTypeDef",
    ) -> "dc_td.ListFlowAliasesResponse":
        return dc_td.ListFlowAliasesResponse.make_one(res)

    def list_flow_versions(
        self,
        res: "bs_td.ListFlowVersionsResponseTypeDef",
    ) -> "dc_td.ListFlowVersionsResponse":
        return dc_td.ListFlowVersionsResponse.make_one(res)

    def list_flows(
        self,
        res: "bs_td.ListFlowsResponseTypeDef",
    ) -> "dc_td.ListFlowsResponse":
        return dc_td.ListFlowsResponse.make_one(res)

    def list_ingestion_jobs(
        self,
        res: "bs_td.ListIngestionJobsResponseTypeDef",
    ) -> "dc_td.ListIngestionJobsResponse":
        return dc_td.ListIngestionJobsResponse.make_one(res)

    def list_knowledge_base_documents(
        self,
        res: "bs_td.ListKnowledgeBaseDocumentsResponseTypeDef",
    ) -> "dc_td.ListKnowledgeBaseDocumentsResponse":
        return dc_td.ListKnowledgeBaseDocumentsResponse.make_one(res)

    def list_knowledge_bases(
        self,
        res: "bs_td.ListKnowledgeBasesResponseTypeDef",
    ) -> "dc_td.ListKnowledgeBasesResponse":
        return dc_td.ListKnowledgeBasesResponse.make_one(res)

    def list_prompts(
        self,
        res: "bs_td.ListPromptsResponseTypeDef",
    ) -> "dc_td.ListPromptsResponse":
        return dc_td.ListPromptsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def prepare_agent(
        self,
        res: "bs_td.PrepareAgentResponseTypeDef",
    ) -> "dc_td.PrepareAgentResponse":
        return dc_td.PrepareAgentResponse.make_one(res)

    def prepare_flow(
        self,
        res: "bs_td.PrepareFlowResponseTypeDef",
    ) -> "dc_td.PrepareFlowResponse":
        return dc_td.PrepareFlowResponse.make_one(res)

    def start_ingestion_job(
        self,
        res: "bs_td.StartIngestionJobResponseTypeDef",
    ) -> "dc_td.StartIngestionJobResponse":
        return dc_td.StartIngestionJobResponse.make_one(res)

    def stop_ingestion_job(
        self,
        res: "bs_td.StopIngestionJobResponseTypeDef",
    ) -> "dc_td.StopIngestionJobResponse":
        return dc_td.StopIngestionJobResponse.make_one(res)

    def update_agent(
        self,
        res: "bs_td.UpdateAgentResponseTypeDef",
    ) -> "dc_td.UpdateAgentResponse":
        return dc_td.UpdateAgentResponse.make_one(res)

    def update_agent_action_group(
        self,
        res: "bs_td.UpdateAgentActionGroupResponseTypeDef",
    ) -> "dc_td.UpdateAgentActionGroupResponse":
        return dc_td.UpdateAgentActionGroupResponse.make_one(res)

    def update_agent_alias(
        self,
        res: "bs_td.UpdateAgentAliasResponseTypeDef",
    ) -> "dc_td.UpdateAgentAliasResponse":
        return dc_td.UpdateAgentAliasResponse.make_one(res)

    def update_agent_collaborator(
        self,
        res: "bs_td.UpdateAgentCollaboratorResponseTypeDef",
    ) -> "dc_td.UpdateAgentCollaboratorResponse":
        return dc_td.UpdateAgentCollaboratorResponse.make_one(res)

    def update_agent_knowledge_base(
        self,
        res: "bs_td.UpdateAgentKnowledgeBaseResponseTypeDef",
    ) -> "dc_td.UpdateAgentKnowledgeBaseResponse":
        return dc_td.UpdateAgentKnowledgeBaseResponse.make_one(res)

    def update_data_source(
        self,
        res: "bs_td.UpdateDataSourceResponseTypeDef",
    ) -> "dc_td.UpdateDataSourceResponse":
        return dc_td.UpdateDataSourceResponse.make_one(res)

    def update_flow(
        self,
        res: "bs_td.UpdateFlowResponseTypeDef",
    ) -> "dc_td.UpdateFlowResponse":
        return dc_td.UpdateFlowResponse.make_one(res)

    def update_flow_alias(
        self,
        res: "bs_td.UpdateFlowAliasResponseTypeDef",
    ) -> "dc_td.UpdateFlowAliasResponse":
        return dc_td.UpdateFlowAliasResponse.make_one(res)

    def update_knowledge_base(
        self,
        res: "bs_td.UpdateKnowledgeBaseResponseTypeDef",
    ) -> "dc_td.UpdateKnowledgeBaseResponse":
        return dc_td.UpdateKnowledgeBaseResponse.make_one(res)

    def update_prompt(
        self,
        res: "bs_td.UpdatePromptResponseTypeDef",
    ) -> "dc_td.UpdatePromptResponse":
        return dc_td.UpdatePromptResponse.make_one(res)

    def validate_flow_definition(
        self,
        res: "bs_td.ValidateFlowDefinitionResponseTypeDef",
    ) -> "dc_td.ValidateFlowDefinitionResponse":
        return dc_td.ValidateFlowDefinitionResponse.make_one(res)


bedrock_agent_caster = BEDROCK_AGENTCaster()
