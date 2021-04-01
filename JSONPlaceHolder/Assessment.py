from JSONPlaceHolder import JSONPlaceHolder
from datetime import datetime
from datetime import timezone
import json

Obj = JSONPlaceHolder('https://jsonplaceholder.typicode.com/posts') 
print(Obj.Get_Title(Obj.Get_ByID(99)))

Post100 = Obj.Get_ByID(100)
Post100 = json.loads(Post100.content)
Post100['time'] = datetime.now(tz=timezone.utc).strftime("%d/%m/%Y, %H:%M:%S")
print(json.dumps(Post100))

NewPost = Obj.Create_Post('New Post', 500, 'Insertion with a known API')
if NewPost.status_code == 201:
    NewPostContent = json.loads(NewPost.content)
    RequestTuple = (NewPostContent['id'], NewPost.status_code, NewPost.headers['x-Powered-By'])
    print(RequestTuple)
    DeleteRequest = Obj.Delete_ByID(RequestTuple[0])
    if DeleteRequest.status_code == 200:
        print(str(RequestTuple[0]) + ' was deleted')
        print(DeleteRequest.headers['x-content-type-options'])

