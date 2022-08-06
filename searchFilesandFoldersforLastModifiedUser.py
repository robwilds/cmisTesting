import requests
import curlify
import json

global _namestr
global globalBaseURL

    

globalBaseURL = "https://sse.dev.alfrescocloud.com"


url = globalBaseURL + "/alfresco/api/-default-/public/search/versions/1/search"

folderRequestDat = "{\"query\":{\"query\":\"cm:modifier:ftic_admin\"},\"filterQueries\":[{\"query\":\"TYPE:'cm:content' or TYPE:'cm:folder'\"}]}"

temp = requests.post(url, data = folderRequestDat, auth = ('rwilds', 'demo'))

responseData = temp.json()

print(responseData)



