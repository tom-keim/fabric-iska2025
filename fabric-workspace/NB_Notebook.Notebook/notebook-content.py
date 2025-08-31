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
# META     }
# META   }
# META }

# MARKDOWN ********************

# - 4052e5a9-8a36-4838-9592-922c5e2a7dd1 = Dev
# - e10ae2d3-b7c3-43ad-8cc2-4680c4b17e27 = Test
# - 04ec29e9-d622-4c11-a868-f680497c5328 = Prod

# CELL ********************

# Install sempy
%pip install semantic-link --q 

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Do an API call to get the attached notebook workspace ID
import sempy.fabric as fabric

def get_connected_lakehouse_workspace() -> str:
    match fabric.get_notebook_workspace_id():
        case '4052e5a9-8a36-4838-9592-922c5e2a7dd1':
            return "DEV"
        case 'e10ae2d3-b7c3-43ad-8cc2-4680c4b17e27':
            return "TEST"
        case '04ec29e9-d622-4c11-a868-f680497c5328':
            return "PROD"
        case _:
            return "Unknown"

print(f"Connected lakehouse is connected to the {get_connected_lakehouse_workspace()} environment")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
