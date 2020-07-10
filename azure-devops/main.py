from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

personal_access_token = "bqgzl7vlrgdjt3uv66pzlbhsnrccnyh4p6tmtrx2vfptaiwiwhwa"

organization_url = "https://rogerbrinkmann.visualstudio.com/"

credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

core_client = connection.clients.get_core_client()

# Get the first page of projects
get_projects_response = core_client.get_projects()
index = 0
while get_projects_response is not None:
    for project in get_projects_response.value:
        pprint.pprint("[" + str(index) + "] " + project.name)
        index += 1
    if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
        # Get the next page of projects
        get_projects_response = core_client.get_projects(continuation_token=get_projects_response.continuation_token)
    else:
        # All projects have been retrieved
        get_projects_response = None