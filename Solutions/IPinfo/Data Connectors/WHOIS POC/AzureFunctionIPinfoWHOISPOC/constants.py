import os

__all__ = [
    'RESOURCE_ID', 'IPINFO_TOKEN', 'TENANT_ID', 'CLIENT_ID', 'CLIENT_SECRET',
    'LOCATION', 'SUBCRIPTION_ID', 'RESOURCE_GROUP_NAME', 'WORKSPACE_NAME', 
    'RETENTION_IN_DAYS', 'TOTAL_RETENTION_IN_DAYS', 'DATA_COLLECTION_ENDPOINT_NAME', 
    'WHOIS_POC_DCR_NAME', 'WHOIS_POC_TABLE_NAME', 'WHOIS_POC_STREAM_DECLARATION', 
    'AZURE_SCOPE', 'AZURE_BASE_URL', 'IPINFO_BASE_URL', 'CSV_NAME', 
    'WHOIS_POC_TABLE_SCHEMA', 'WHOIS_POC_TABLE_COLUMNS'
]

# Enviornment Virables
RESOURCE_ID = os.environ["RESOURCE_ID"]
IPINFO_TOKEN = os.environ["IPINFO_TOKEN"]
TENANT_ID = os.environ["TENANT_ID"]
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
RETENTION_IN_DAYS = os.environ["RETENTION_IN_DAYS"]
TOTAL_RETENTION_IN_DAYS = os.environ["TOTAL_RETENTION_IN_DAYS"]
LOCATION = os.environ["LOCATION"]

parts = RESOURCE_ID.split("/")
SUBCRIPTION_ID = parts[2]
RESOURCE_GROUP_NAME = parts[4]
WORKSPACE_NAME = parts[8]

DATA_COLLECTION_ENDPOINT_NAME = "ipinfo-logs-ingestion"
WHOIS_POC_DCR_NAME = "ipinfo_rule_for_WHOIS_POC_tables"
WHOIS_POC_TABLE_NAME = "Ipinfo_WHOIS_POC_CL"
WHOIS_POC_STREAM_DECLARATION = "Custom-Ipinfo_WHOIS_POC_CL"

AZURE_SCOPE = "https://management.azure.com/.default"
AZURE_BASE_URL = f"https://management.azure.com/subscriptions/{SUBCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP_NAME}/providers/Microsoft."
IPINFO_BASE_URL = "https://ipinfo.io/data"
CSV_NAME = "whois_poc.csv.gz"

WHOIS_POC_TABLE_SCHEMA = {
    "properties": {
        "totalRetentionInDays": TOTAL_RETENTION_IN_DAYS,
        "archiveRetentionInDays": 0,
        "plan": "Analytics",
        "retentionInDaysAsDefault": True,
        "totalRetentionInDaysAsDefault": True,
        "schema": {
            "tableSubType": "DataCollectionRuleBased",
            "name": WHOIS_POC_TABLE_NAME,
            "tableType": "CustomLog",
            "description": "Range based table",
            "columns": [
                {"name": "TimeGenerated", "type": "datetime", "isDefaultDisplay": False, "isHidden": False},
                {"name": "whois_id", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "name", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "mobilephone", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "officephone", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "fax", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "address", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "country", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "email", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "abuse_email", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "created", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "updated", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "source", "type": "string", "isDefaultDisplay": False, "isHidden": False},
            ],
            "standardColumns": [{"name": "TenantId", "type": "guid", "isDefaultDisplay": False, "isHidden": False}],
            "solutions": ["LogManagement"],
            "isTroubleshootingAllowed": True,
        },
        "provisioningState": "Succeeded",
        "retentionInDays": RETENTION_IN_DAYS,
    },
    "id": f"/subscriptions/{SUBCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP_NAME}/providers/Microsoft.OperationalInsights/workspaces/{WORKSPACE_NAME}/tables/{WHOIS_POC_TABLE_NAME}",
    "name": WHOIS_POC_TABLE_NAME,
}

WHOIS_POC_TABLE_COLUMNS = {
    "columns": [
        {"name": "TimeGenerated", "type": "datetime"},
        {"name": "whois_id", "type": "string"},
        {"name": "name", "type": "string"},
        {"name": "mobilephone", "type": "string"},
        {"name": "officephone", "type": "string"},
        {"name": "fax", "type": "string"},
        {"name": "address", "type": "string"},
        {"name": "country", "type": "string"},
        {"name": "email", "type": "string"},
        {"name": "abuse_email", "type": "string"},
        {"name": "created", "type": "string"},
        {"name": "updated", "type": "string"},
        {"name": "source", "type": "string"},
    ]
}
