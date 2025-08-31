from fabric_cicd import FabricWorkspace, publish_all_items
from azure.identity import AzureCliCredential
import os

target_environment = "TEST"

if target_environment == "TEST":
    target_workspace_id = "e10ae2d3-b7c3-43ad-8cc2-4680c4b17e27"
else:
    raise Exception("unknown environment selected.")

# to make the demos working, make sure that this example does not use the parameter.yml as that is not expected for this demo
param_file = os.path.join(
    os.path.dirname(__file__),
    "/workspaces/fabric-iska2025/fabric-workspace/parameter.yml",
)

if os.path.exists(param_file):
    os.remove(param_file)

item_type_in_scope = [
    "Notebook",
    "DataPipeline",
    "Lakehouse",
    # "Environment" #For this demo we will NOT deploy the environment
]

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=target_workspace_id,
    environment=target_environment,
    repository_directory="/workspaces/fabric-iska2025/fabric-workspace/",
    item_type_in_scope=item_type_in_scope,
    token_credential=AzureCliCredential(),
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)

# We do not unpublish orphaned items here
# unpublish_all_orphan_items(target_workspace)
