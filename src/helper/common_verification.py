#http status code verification
def verify_http_status_code(response_data,expect_data):
    assert response_data.status_code==expect_data,"Expected http status code"+str(expect_data)

def verify_json_key_not_null(key):
    assert key != 0, "key is not empty" +key
    assert key>0, "key is  greater than zero"



def verify_responce_key_should_not_be_none(key):
     assert key is not None

def verify_response_time():
    pass


#comman verification
 #http status code
 #headers
 #data verification
 #json schema