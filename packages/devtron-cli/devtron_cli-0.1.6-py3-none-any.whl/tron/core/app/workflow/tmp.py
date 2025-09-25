def update_ci_pipeline(self, workflow, app_id):
    import requests

    get_ci_details_url = f"{self.base_url}/orchestrator/app/ci-pipeline/{app_id}"
    get_wf_details_url = f"{self.base_url}/orchestrator/app/app-wf/{app_id}"

    get_ci_details = requests.get(get_ci_details_url, headers=self.headers)
    get_wf_details = requests.get(get_wf_details_url, headers=self.headers)

    if get_ci_details.status_code != 200 or get_wf_details.status_code != 200:
        return {
            "success": False,
            "message": f"Failed to fetch workflow or ci details"
        }

    ci_details = get_ci_details.json().get("result", {}).get("ciPipelines", [])
    wf_details = get_wf_details.json().get("result", {}).get("workflows", [])

    if not ci_details or not wf_details:
        return {
            "success": False,
            "message": "Workflow/ci details not found"
        }

    ci_pipeline = None
    for ci in ci_details:
        if ci.get("name", "") == workflow.get("ci_pipeline", {}).get("name", ""):
            ci_pipeline = ci
    if not ci_pipeline:
        return {
            "success": False,
            "message": "CI Pipeline ID not found"
        }
    ci_pipeline_id = ci_pipeline.get("id", 0)
    app_workflow_id = 0
    for w in wf_details:
        tree = w.get("tree", [])
        for node in tree:
            if node.get("componentId", 0 == ci_pipeline_id):
                app_workflow_id = w.get("id", 0)
                break
    if not app_workflow_id:
        return {
            "success": False,
            "message": "App Workflow ID not found"
        }

    get_ci_details = self.get_ci_details(app_id, ci_pipeline_id)
    if not get_ci_details:
        return {
            "success": False,
            "message": "Failed to fetch CI Material"
        }

    ci = CiPipeline(**get_ci_details)
    patch_ci_pipeline_url = f"{self.base_url}/orchestrator/app/ci-pipeline/patch"
    payload = {
        "action": 1,
        "appId": app_id
    }

    return {
        "success": True,
        "message": "CI Pipeline updated successfully"
    }


def get_ci_details(self, app_id: int, ci_pipeline_id: int):
    import requests

    get_ci_details_url = f"{self.base_url}/orchestrator/app/ci-pipeline/{app_id}/{ci_pipeline_id}"
    get_ci_details = requests.get(get_ci_details_url, headers=self.headers)
    if get_ci_details.status_code != 200:
        return None
    return get_ci_details.json().get("result", {})