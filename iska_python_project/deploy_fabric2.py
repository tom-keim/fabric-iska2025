from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items
from azure.identity import AzureCliCredential
import shutil
target_environment = 'TEST'

if target_environment == 'TEST':
    target_workspace_id = 'e10ae2d3-b7c3-43ad-8cc2-4680c4b17e27'
else:
    raise Exception("unknown environment selected.")


shutil.copyfile("parameter2.yml",
                "/workspaces/fabric-iska2025/fabric-workspace/parameter.yml")

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=target_workspace_id,
    environment=target_environment,
    repository_directory="../fabric-workspace",
    item_type_in_scope=["Notebook", "DataPipeline", "Lakehouse"],
    token_credential=AzureCliCredential(),
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)

# Unpublish all items defined in item_type_in_scope not found in repository
unpublish_all_orphan_items(target_workspace)
