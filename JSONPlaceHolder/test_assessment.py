import pytest
from JSONPlaceHolder import JSONPlaceHolder
import json

Obj = JSONPlaceHolder('https://jsonplaceholder.typicode.com/posts') 

def test_Get_ByID():
    Request = Obj.Get_ByID(1)
    assert Request.status_code == 200

def test_Create_Post():
    Request = Obj.Create_Post('Test Title', 500, 'This is a test')
    assert Request.status_code == 201

def test_Get_Title():
    assert Obj.Get_Title(Obj.Get_ByID(1)) == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'

def test_Delete_ByID():
    Request = Obj.Delete_ByID(1)
    assert Request.status_code == 200
