import requests
import json

class JSONPlaceHolder:
    def __init__(self, BaseURI):
        self.BaseURI = BaseURI
    def Get_ByID(self, id):
        Uri = self.BaseURI + '/' + str(id)
        Request = requests.get(Uri)
        return Request
    def Create_Post(self, Title, UserID, Body):
        Headers =  {'Content-type': 'application/json; charset=UTF-8'}
        RequestBody = {'title': Title, 'body': Body, 'userId': UserID}
        Request = requests.post(self.BaseURI, headers=Headers, data=json.dumps(RequestBody))
        return Request
    def Get_Title(self, Request):
        return json.loads(Request.content)['title']
    def Delete_ByID(self, id):
        Uri = self.BaseURI + '/' + str(id)
        Request = requests.delete(Uri)
        return Request
