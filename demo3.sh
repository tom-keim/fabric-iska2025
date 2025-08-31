cd /workspaces/fabric-iska2025/iska_python_project

# Remove dist folder to clean it up
rm -rf ./dist

# Bump the version of python project
uv version --bump patch

# Build a new wheels file
uv build

# Delete old and copy the new wheels file to the custom libraries folder for fabric
rm /workspaces/fabric-iska2025/fabric-workspace/ENV_Environment.Environment/Libraries/CustomLibraries/*.whl
cp ./dist/*.whl /workspaces/fabric-iska2025/fabric-workspace/ENV_Environment.Environment/Libraries/CustomLibraries/

#Run CICD python script
uv run cicd/deploy_fabric_demo3.py