import requests
import json

url = "https://platform.uipath.com/api/Account/Authenticate"
payload = {"TenancyName":"sriharishtenancy","UsernameOrEmailAddress":"sriharish.gutta@accenture.com","Password":"Harish613"}
response = requests.request("POST", url, data=payload)

responseText = json.loads(response.text)
access_token = responseText['result']

url = "https://platform.uipath.com/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"

header = {"Content-Type": "application/json","Authorization":access_token}
payload = {"startInfo":{"RobotIds":[6996],"ReleaseKey":"e70e3034-05f0-43bd-a101-f045f80bc1a7","Strategy":"Specific","NoOfRobots":1,"Source":"Manual"}}
response = requests.request("POST", url, data=payload, headers=header)
