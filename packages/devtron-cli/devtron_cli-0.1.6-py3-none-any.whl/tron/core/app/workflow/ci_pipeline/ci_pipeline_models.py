class CustomTag:

    def __init__(self, tag_pattern: str = "", counter_x: int = 0):
        self.tagPattern = tag_pattern
        self.counterX   = counter_x

    def to_dict(self):
        return {
            "tagPattern" : self.tagPattern,
            "counterX"   : self.counterX
        }


class WorkflowCacheConfig:

    def __init__(self, _type: str = "INHERIT", value: bool = True, global_value: bool = True):
        self.type        = _type
        self.value       = value
        self.globalValue = global_value

    def to_dict(self):
        return {
            "type"        : self.type,
            "value"       : self.value,
            "globalValue" : self.globalValue
        }


class CIMaterialSource:

    def __init__(self, _type: str = "", value: str = "", regex: str = ""):
        self.type  = _type
        self.value = value
        self.regex = regex

    def to_dict(self):
        return {
            "type"  : self.type,
            "value" : self.value,
            "regex" : self.regex
        }


class CIMaterial:

    def __init__(self, git_material_id: int = 0, _id: int = 0, source: CIMaterialSource = None, git_material_name: str = "", is_regex: bool = False):
        self.gitMaterialId   = git_material_id
        self.id              = _id
        self.gitMaterialName = git_material_name
        self.isRegex         = is_regex
        self.source          = source

    def to_dict(self):
        return {
            "gitMaterialId"   : self.gitMaterialId,
            "id"              : self.id,
            "source"          : self.source.to_dict()
        }


class ExternalCiConfig:

    def __init__(self):
        pass

    def to_dict(self):
        return {}


class DockerArgs:

    def __init__(self):
        pass

    def to_dict(self):
        return {}


class DockerConfigOverride:

    def __init__(self):
        pass


class InputVariableValueCOnstraint:

    def __init__(self, _id : int  = 0, choices: list = None, block_custom_value: bool = False, constraint: dict = None):
        self.id = _id
        self.choices = choices
        self.blockCustomValue = block_custom_value
        self.constraint = constraint

    def to_dict(self):
        return {

            "choices": self.choices,
            "blockCustomValue": self.blockCustomValue,

        }


class InputVariable:

    def __init__(self, allow_empty_value: bool = True, description: str = "", format: str = "STRING", _id: int = 0, name: str = "", value: str = "", value_constraint: InputVariableValueCOnstraint = None, variable_type: str = "NEW"):
        self.allowEmptyValue = allow_empty_value
        self. description = description
        self.format = format
        self.id = _id
        self.name = name
        self.value = value
        self.valueConstraint = value_constraint
        self.variableType = variable_type

    def to_dict(self):
        return {
            "refVariableName": "",
            "isRuntimeArg": False,
            "refVariableStage": None,
            "allowEmptyValue": self.allowEmptyValue,
            "description": self.description,
            "format": self.format,
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "valueConstraint": self.valueConstraint.to_dict(),
            "variableType": self.variableType
        }


class PluginRefStepDetail:

    def __init__(self, plugin_id: int = 39, plugin_name: str = "", plugin_version: str = "", input_var_data: list = None, out_put_variables: list = None, condition_details: list = None):
        self.pluginId         = plugin_id
        self.pluginName       = plugin_name
        self.pluginVersion    = plugin_version
        self.inputVariables   = input_var_data
        self.outputVariables  = out_put_variables
        self.conditionDetails = condition_details

    def to_dict(self):
        return {
            "pluginId": self.pluginId,
            "pluginName": self.pluginName,
            "pluginVersion": "",
            "inputVariables": [inputVariable.to_dict() for inputVariable in self.inputVariables],
            "outputVariables": self.outputVariables,
            "conditionDetails": self.conditionDetails
        }


class PrePostBuildCOnfigStep:

    def __init__(self, _id: int = 0, name: str = "", description: str = "", index: int = 0, step_type: str = "REF_PLUGIN", plugin_ref_step_detail: PluginRefStepDetail = None, output_directory_path: str = "", inline_step_detail: dict = None, trigger_if_parent_stage_fail: bool = False):
        self.id                       = _id
        self.name                     = name
        self.description              = description
        self.index                    = index
        self.stepType                 = step_type
        self.outputDirectoryPath      = output_directory_path
        self.inlineStepDetail         = inline_step_detail
        self.pluginRefStepDetail      = plugin_ref_step_detail
        self.triggerIfParentStageFail = trigger_if_parent_stage_fail

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "index": self.index,
            "stepType": self.stepType,
            "outputDirectoryPath": self.outputDirectoryPath,
            "inlineStepDetail": self.inlineStepDetail,
            "pluginRefStepDetail": self.pluginRefStepDetail.to_dict(),
            "triggerIfParentStageFail": self.triggerIfParentStageFail
        }


class PrePostBuildConfig:

    def __init__(self, _id: int = 0, steps: list = None, _type: str = "", trigger_blocked_info: dict = None):
        self.type               = _type
        self.id                 = _id
        self.steps              = steps
        self.triggerBlockedInfo = trigger_blocked_info

    def to_dict(self):
        return {
            "type"               : self.type,
            "id"                 : self.id,
            "steps"              : [step.to_dict() for step in self.steps],
            "triggerBlockedInfo" : None
        }


class CiPipeline:

    def __init__(self, active: bool = False, enableCustomTag: bool = False, isDockerConfigOverridden: bool = False, isExternal: bool = False, isManual: bool = False, scanEnabled: bool = False, appId: int = 0, appWorkflowId: int = 0, id: int = 0, lastTriggeredEnvId: int = 0, linkedCount: int = 0, parentAppId: int = 0, ciMaterial: list = None, defaultTag: list = None, name: str = "", pipelineType: str = "CI_BUILD", parentCiPipeline: int = 0, customTag: CustomTag = None, dockerArgs: DockerArgs = None, dockerConfigOverride: DockerConfigOverride = None, externalCiConfig: ExternalCiConfig = None, postBuildStage: PrePostBuildConfig = None, preBuildStage: PrePostBuildConfig = None, workflowCacheConfig: WorkflowCacheConfig = None):
        self.appId                    = appId
        self.appWorkflowId            = appWorkflowId
        self.active                   = active
        self.ciMaterial               = ciMaterial
        self.dockerArgs               = dockerArgs
        self.externalCiConfig         = externalCiConfig
        self.id                       = id
        self.isExternal               = isExternal
        self.isManual                 = isManual
        self.name                     = name
        self.linkedCount              = linkedCount
        self.scanEnabled              = scanEnabled
        self.pipelineType             = pipelineType
        self.customTag                = customTag
        self.workflowCacheConfig      = workflowCacheConfig
        self.preBuildStage            = preBuildStage
        self.postBuildStage           = postBuildStage
        self.dockerConfigOverride     = dockerConfigOverride
        self.parentCiPipeline         = parentCiPipeline
        self.parentAppId              = parentAppId
        self.isDockerConfigOverridden = isDockerConfigOverridden
        self.lastTriggeredEnvId       = lastTriggeredEnvId
        self.defaultTag               = defaultTag
        self.enableCustomTag          = enableCustomTag