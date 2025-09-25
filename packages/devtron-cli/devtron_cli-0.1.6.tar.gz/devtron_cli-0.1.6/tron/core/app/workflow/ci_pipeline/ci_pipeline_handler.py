from tron.core.app.workflow.ci_pipeline.ci_pipeline_models import *


class CiPipelineHandlers:
    def __init__(self, base_url: str, headers: dict):
        self.base_url = base_url
        self.headers = headers


    @staticmethod
    def get_pre_post_ci_step(step: dict) -> PrePostBuildCOnfigStep:

        plugin_ref_detail = step.get("pluginRefStepDetail", {})
        input_variables = []
        for variable in plugin_ref_detail.get("inputVariables", []):
            input_variables.append(InputVariable(
                allow_empty_value=variable.get("allowEmptyValue", False),
                description=variable.get("description", ""),
                format=variable.get("format", "STRING"),
                _id=variable.get("id", 0),
                name=variable.get("name", ""),
                value=variable.get("value", ""),
                value_constraint=InputVariableValueCOnstraint(
                    _id=variable.get("valueConstraint", {}).get("id", 0),
                    choices=variable.get("valueConstraint", {}).get("choices", []),
                    block_custom_value=variable.get("valueConstraint", {}).get("blockCustomValue", False),
                    constraint=variable.get("valueConstraint", {}).get("constraint", {})
                ),
                variable_type=variable.get("variableType", "NEW")
            ))

        plugin_ref_step_detail = PluginRefStepDetail(
            plugin_id=plugin_ref_detail.get("pluginId", 0),
            plugin_name=plugin_ref_detail.get("pluginName", ""),
            plugin_version=plugin_ref_detail.get("pluginVersion", ""),
            input_var_data=input_variables,
            out_put_variables=plugin_ref_detail.get("outputVariables", []),
            condition_details=plugin_ref_detail.get("conditionDetails", []))

        pre_post_ci_step = PrePostBuildCOnfigStep(
            _id=step.get("id", 0),
            name=step.get("name", ""),
            description=step.get("description", ""),
            index=step.get("index", 0),
            step_type=step.get("stepType", ""),
            output_directory_path=step.get("outputDirectoryPath", ""),
            inline_step_detail=step.get("inlineStepDetail", {}),
            trigger_if_parent_stage_fail=step.get("triggerIfParentStageFail", False),
            plugin_ref_step_detail=plugin_ref_step_detail
        )

        return pre_post_ci_step


    @staticmethod
    def get_pre_post_build_config(ci_pipeline_details: dict) -> PrePostBuildConfig:


        pre_post_ci_steps = []

        for step in ci_pipeline_details.get("preBuildStage", {}).get("steps", []):
            pre_post_ci_step = CiPipelineHandlers.get_pre_post_ci_step(step)
            pre_post_ci_steps.append(pre_post_ci_step)



        pre_post_build_stage = PrePostBuildConfig(
            _type=ci_pipeline_details.get("preBuildStage", {}).get("type", ""),
            _id=ci_pipeline_details.get("preBuildStage", {}).get("id", 0),
            trigger_blocked_info=ci_pipeline_details.get("triggerBlockedInfo", {}),
            steps=pre_post_ci_steps
        )
        return pre_post_build_stage


    @staticmethod
    def check_if_plugin_updated(plugin_name: str = "", plugin_id: int = 0, plugin_version: str = "1.0.0", plugin_metadata: dict = None) -> dict:

        for plugin in plugin_metadata.get("parentPlugins", []):
            for minimal_plugin_version_data in plugin.get("pluginVersions", {}).get("minimalPluginVersionData", []):
                if plugin_name == minimal_plugin_version_data["name"]:

                    if plugin_version == minimal_plugin_version_data["pluginVersion"] and plugin_id == minimal_plugin_version_data["id"]:

                        return {
                            "is_modified": False,
                            "field": {}
                        }
                    elif plugin_version == minimal_plugin_version_data["pluginVersion"]:

                        return {
                            "is_modified": True,
                            "field": {
                                "pluginId" : minimal_plugin_version_data["id"],
                                "pluginVersion": minimal_plugin_version_data["pluginVersion"]
                            }
                        }

        return {
            "is_modified": True,
            "field": {"pluginName": plugin_name }
        }

    @staticmethod
    def update_pre_post_ci_steps(current_steps: list, new_steps: list, plugin_metadata: dict) -> list:
        try:
            current_steps_indices = {}
            plugin_minimal_data = {}

            for plugin in plugin_metadata.get("parentPlugins", []):
                for version in plugin.get("pluginVersions", {}).get("detailedPluginVersionData", []):
                    (plugin_name, plugin_version) = (version.get("name", ""), version.get("pluginVersion", ""))

                    if (plugin_name, plugin_version) is not ("", ""):
                        plugin_minimal_data[(plugin_name, plugin_version)] = version

            plugin_name = ""
            for i in range(len(current_steps)):
                for parentPlugin in plugin_metadata.get("parentPlugins", []):
                    for minimal_plugin_version_data in parentPlugin.get("pluginVersions", {}).get("minimalPluginVersionData", []):

                        if minimal_plugin_version_data.get("id", 0) == current_steps[i].pluginRefStepDetail.pluginId:
                            plugin_name = minimal_plugin_version_data.get("name", "")

                current_steps_indices[(current_steps[i].name, plugin_name)] = current_steps[i]
            indices = [(step["task_name"], step["name"]) for step in new_steps]

            index = 1

            updated_steps = []
            for step in new_steps:
                if current_steps_indices.get((step["task_name"], step["name"]), ("", "")):
                    patch_pre_post_ci_step_result = CiPipelineHandlers.patch_pre_post_ci_step(current_steps_indices.get((step["task_name"], step["name"])), step, index, plugin_minimal_data[(step["name"], step["version"])])
                    if not patch_pre_post_ci_step_result["success"]:
                        return current_steps
                    index += 1

                    updated_steps.append(patch_pre_post_ci_step_result.get("desired_step"))

            return updated_steps

        except Exception as e:
            print("Error coocurred:", str(e))
            return current_steps


    @staticmethod
    def patch_pre_post_ci_step(current_step: PrePostBuildCOnfigStep, desired_step: dict, index: int, plugin: dict)-> dict:
        try:

            input_variables = []
            for variable in current_step.pluginRefStepDetail.inputVariables:
                print("elu", vars(variable))

                tmp = InputVariable(
                    allow_empty_value=variable.allowEmptyValue,
                    description=variable.description,
                    format=variable.format,
                    _id=variable.id,
                    name=variable.name,
                    value=desired_step.get("input_variables", {}).get(variable.name),
                    value_constraint=variable.valueConstraint,
                    variable_type=variable.variableType
                )
                input_variables.append(tmp)




            current_step.index = index
            current_step.pluginRefStepDetail.pluginId = plugin.get("id", 0)
            current_step.pluginRefStepDetail.pluginVersion = desired_step.get("version", "")
            current_step.pluginRefStepDetail.inputVariables = input_variables


            return {
                "success": True,
                'desired_step': current_step,
                "message": "Configstep patched"
            }

        except Exception as e:
            print("Exception occurred:", e)
            return {
                "success": False,
                "error": str(e)
            }


    @staticmethod
    def update_pre_post_ci_steps_old(current_steps: list, new_steps: list, plugin_metadata: dict) -> list:
        index = 1
        for i in range(len(new_steps)):
            for j in range(len(current_steps)):
                if new_steps[i].get("task_name", "") == current_steps[j].name:
                    is_plugin_updated = CiPipelineHandlers.check_if_plugin_updated(new_steps[i].get("name", ""), current_steps[j].pluginRefStepDetail.pluginId, new_steps[i].get("version", ""), plugin_metadata)
                    if not is_plugin_updated["is_modified"]:
                        for variable in current_steps[j].pluginRefStepDetail.inputVariables:
                            variable.value = new_steps[i].get("input_variables", {}).get(variable.name, "")
                        current_steps[j].index = index
                        index += 1
                    else:
                        if is_plugin_updated.get("field", {}).get("pluginVersion", ""):
                            print("Version of the plugin is updated")
                        else:
                            print("Another plugin is getting used")
        return current_steps



    @staticmethod
    def update_pre_post_build_config(current_pre_post_build: PrePostBuildConfig, pre_post_build_config: list, plugin_metadata: dict) -> PrePostBuildConfig:

        current_pre_post_build.steps = CiPipelineHandlers.update_pre_post_ci_steps(
            current_pre_post_build.steps,
            pre_post_build_config,
            plugin_metadata
        )

        return current_pre_post_build



    @staticmethod
    def get_ci_material(ci_pipeline_details) -> list:
        ci_material = []
        for material in ci_pipeline_details.get("ciMaterial", []):

            ci_material_source = CIMaterialSource(
                _type=material.get("source", {}).get("type", ""),
                value=material.get("source", {}).get("value", ""),
                regex=material.get("source", {}).get("regex", "")
            )
            ci_material_value = CIMaterial(
                git_material_id=material.get("gitMaterialId", 0),
                _id=material.get("id", 0),
                git_material_name=material.get("gitMaterialName", ""),
                is_regex=material.get("isRegex", False),
                source=ci_material_source
            )
            ci_material.append(ci_material_value)

        return ci_material


    @staticmethod
    def update_ci_material(ci_material: list, branches: list) -> list:

        for i in range(len(branches)):
            ci_material[i].source.type  = branches[i].get("type",   ci_material[i].source.type)
            ci_material[i].source.value = branches[i].get("branch", ci_material[i].source.value)
            ci_material[i].source.regex = branches[i].get("regex",  ci_material[i].source.regex)

        return ci_material



    @staticmethod
    def get_ci_pipeline(base_url, headers, app_id: int, ci_pipeline_id: int) -> dict:

        import requests

        ci_pipeline_data = requests.get(f"{base_url}/orchestrator/app/ci-pipeline/{app_id}/{ci_pipeline_id}", headers=headers)


        if ci_pipeline_data.status_code != 200:
            return {'success': False, 'error': f"Failed to fetch CI pipeline details: {ci_pipeline_data.text}"}

        ci_pipeline_details = ci_pipeline_data.json().get("result", {})


        workflow_cache_config = WorkflowCacheConfig(
            _type=ci_pipeline_details.get("workflowCacheConfig", {}).get("type", ""),
            value=ci_pipeline_details.get("value", False),
            global_value=ci_pipeline_details.get("globalValue", False)
        )

        ci_material = CiPipelineHandlers.get_ci_material(ci_pipeline_details)

        external_ci_config = ExternalCiConfig()
        docker_args = DockerArgs()
        custom_tag = CustomTag()

        pre_build_stage = CiPipelineHandlers.get_pre_post_build_config(ci_pipeline_details)

        ci_pipeline = CiPipeline(
            isManual=ci_pipeline_details.get("isManual", False),
            appId=ci_pipeline_details.get("appId", 0),
            pipelineType=ci_pipeline_details.get("pipelineType", ""),
            name=ci_pipeline_details.get("name", ""),
            workflowCacheConfig=workflow_cache_config,
            externalCiConfig=external_ci_config,
            ciMaterial=ci_material,
            id=ci_pipeline_details.get("id", 0),
            active=ci_pipeline_details.get("active", False),
            linkedCount=ci_pipeline_details.get("linkedCount", 0),
            scanEnabled=ci_pipeline_details.get("scanEnabled", False),
            appWorkflowId=ci_pipeline_details.get("appWorkflowId", 0),
            preBuildStage=pre_build_stage,
            isDockerConfigOverridden=ci_pipeline_details.get("isDockerConfigOverridden", False),
            lastTriggeredEnvId=ci_pipeline_details.get("lastTriggeredEnvId", 0),
            defaultTag=[],
            enableCustomTag=False,
            dockerArgs=docker_args,
            customTag=custom_tag
        )

        return {'success': True, 'ci_pipeline': ci_pipeline}


    @staticmethod
    def update_current_ci_pipeline(base_url, headers, current_ci_pipeline: CiPipeline, ci_config: dict, plugin_metadata: dict):

        current_ci_pipeline.isManual      = ci_config.get("isManual", current_ci_pipeline.isManual)
        current_ci_pipeline.pipelineType  = ci_config.get("type", current_ci_pipeline.pipelineType)
        current_ci_pipeline.ciMaterial    = CiPipelineHandlers.update_ci_material(current_ci_pipeline.ciMaterial, ci_config.get("branches", []))
        current_ci_pipeline.preBuildStage = CiPipelineHandlers.update_pre_post_build_config(current_ci_pipeline.preBuildStage, ci_config.get("pre_build_configs", {}).get("tasks", []), plugin_metadata)

        patch_result = CiPipelineHandlers.patch_ci_pipeline(base_url, headers, current_ci_pipeline)
        if patch_result["success"]:

            return {"success": True, "message": "CI Pipeline has been updated successfully"}

        return {"success": False, "message": "Failed to update CI Pipeline"}


    @staticmethod
    def patch_ci_pipeline(base_url, headers, ci: CiPipeline):

        import requests

        payload = {
            "appId": ci.appId,
            "appWorkflowId": ci.appWorkflowId,
            "action": 1,
            "ciPipeline": {
                "isManual": ci.isManual,
                "workflowCacheConfig": ci.workflowCacheConfig.to_dict(),
                "dockerArgs": ci.dockerArgs.to_dict(),
                "isExternal": ci.isExternal,
                "parentCiPipeline": ci.parentCiPipeline,
                "parentAppId": ci.parentAppId,
                "appId": ci.appId,
                "externalCiConfig": {
            "id": 0,
            "webhookUrl": "",
            "payload": "",
            "accessKey": "",
            "payloadOption": None,
            "schema": None,
            "responses": None,
            "projectId": 0,
            "projectName": "",
            "environmentId": "",
            "environmentName": "",
            "environmentIdentifier": "",
            "appId": 0,
            "appName": "",
            "role": ""
        },
                "ciMaterial": [material.to_dict() for material in ci.ciMaterial],
                "name": ci.name,
                "id": ci.id,
                "active": True,
                "linkedCount": ci.linkedCount,
                "scanEnabled": ci.scanEnabled,
                "pipelineType": ci.pipelineType,
                "preBuildStage": ci.preBuildStage.to_dict(),
                "postBuildStage": {},
                "appWorkflowId": ci.appWorkflowId,
                "isDockerConfigOverridden": False,
                "dockerConfigOverride": ci.dockerConfigOverride,
                "lastTriggeredEnvId": 0,
                "defaultTag": ci.defaultTag,
                "enableCustomTag": ci.enableCustomTag,
                "customTag": ci.customTag.to_dict(),
            }



        }
        print(" ")
        print("payload", payload)
        response = requests.post(f"{base_url}/orchestrator/app/ci-pipeline/patch", headers=headers, json=payload)
        if response.status_code != 200:

            return {'success': False, 'error': f"Failed to patch CI pipeline: {response.text}"}
        return {
            "success": True,
            "message": "The Pipeline has been updated"
        }


    @staticmethod
    def get_pre_post_build_plugin_ids(ci_pipeline: CiPipeline) -> list:

        plugin_ids = []
        for step in ci_pipeline.preBuildStage.steps:

            plugin_ids.append(step.pluginRefStepDetail.pluginId)

        return plugin_ids


