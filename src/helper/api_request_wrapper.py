# To make the post,put,patch,delete
import requests
import json
#http methods -generic function


def get_request(url,auth,in_json):
    response=requests.get(url=url,auth=auth)
    if in_json is True:
        return response.json()
        return response


def post_request(url,auth,header,payload,in_json):
    post_responce=requests.post(url=url,headers=header,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return post_responce.json()
    return post_responce

def patch_request(url,auth,header,payload,in_json):
    patch_responce_data=requests.potch(url=url,headers=header,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return  patch_responce_data.json()
    return  patch_responce_data


def put_request(url,auth,header,payload,in_json):
    put_responce_data=requests.put(url=url,headers=header,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return  put_responce_data.json()
    return put_responce_data



def delete_request(url,auth,header,payload,in_json):
    delete_responce_data=requests.delete(url=url,headers=header,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return   delete_responce_data.json()
    return delete_responce_data
