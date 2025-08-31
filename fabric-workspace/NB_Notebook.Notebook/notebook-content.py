# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "3b7d2652-0466-4156-a849-1e32ec57d563",
# META       "default_lakehouse_name": "LH_ISKADemo",
# META       "default_lakehouse_workspace_id": "4052e5a9-8a36-4838-9592-922c5e2a7dd1",
# META       "known_lakehouses": [
# META         {
# META           "id": "3b7d2652-0466-4156-a849-1e32ec57d563"
# META         }
# META       ]
# META     },
# META     "environment": {
# META       "environmentId": "7970d0e5-d3ae-95a4-4c2d-a2d1f6ddaafa",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# CELL ********************

import pkgutil
import importlib

def list_subpackages(package_name):
    package = importlib.import_module(package_name)
    print("Package path:", package.__path__)  # Debug print
    return [name for _, name, is_pkg in pkgutil.iter_modules(package.__path__) if is_pkg]

# Use the correct package name based on your structure:
print(list_subpackages("iska_python_project.iska_python_project"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
