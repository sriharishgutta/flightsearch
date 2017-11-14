import requests

url = "https://platform.uipath.com/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"

payload = "{\"startInfo\":{\"RobotIds\":[\"sriharishrobot\"],\"ReleaseKey\":\"9afeb5cc-75bd-4f89-9d0b-44004e97ee6e\",\"Strategy\":\"Specific\",\"NoOfRobots\":1,\"Source\":\"Manual\"}}"
response = requests.request("POST", url, data=payload)

print(response.text)