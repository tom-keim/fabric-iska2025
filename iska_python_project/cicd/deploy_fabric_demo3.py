from fabric_cicd import FabricWorkspace, publish_all_items
from azure.identity import AzureCliCredential
import shutil
import os

target_environment = "TEST"

if target_environment == "TEST":
    target_workspace_id = "e10ae2d3-b7c3-43ad-8cc2-4680c4b17e27"
else:
    raise Exception("unknown environment selected.")

# copy parameterfile for demo 2 to correct location
current_file_dir = os.path.dirname(os.path.abspath(__file__))
shutil.copyfile(
    os.path.join(current_file_dir, "parameter_demo2.yml"),
    "/workspaces/fabric-iska2025/fabric-workspace/parameter.yml"
)

item_type_in_scope = [
    "Notebook",
    "DataPipeline",
    "Lakehouse",
    "Environment"  # For this demo we will deploy the environment
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
