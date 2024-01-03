import pytest


from src.helper.api_request_wrapper import  post_request,put_request
from src.constant.api_constants import  APIConstants
from src.helper.utils import common_headers_json
from src.helper.payload_manager import payload_create_booking,payload_create_token
from src.helper.common_verification import verify_responce_key_should_not_be_none,verify_http_status_code
class TestCreateBooking(object):
     def test_create_token(self):
        response=post_request(url=APIConstants.url_create_token(),
                              header=common_headers_json(),
                             auth = None ,
                             payload=payload_create_token(),
                              in_json=False
                             )

        verify_http_status_code(response,expect_data=200)
        print(response.json)
        token=response.json()["token"]
        print(token)
        verify_responce_key_should_not_be_none(token)
        return token
     def test_create_booking(self):

             response = post_request(url=APIConstants.url_create_booking(), auth=None, header=common_headers_json(),
                                     payload=payload_create_booking(), in_json=False)
             print(response)
             verify_responce_key_should_not_be_none(response.json()["bookingid"])
             verify_http_status_code(response, expect_data=200)
             bookingid = response.json()["bookingid"]
             print(bookingid)
             return bookingid

     def test_update_booking(self):
             token=""
             put_url=APIConstants.url_create_booking()
             response = put_request(url=put_url, auth=None, header=common_headers_json(),
                                     payload=payload_create_booking(), in_json=False)
             print(response)
             verify_responce_key_should_not_be_none(response.json()["bookingid"])
             verify_http_status_code(response, expect_data=200)
             bookingid = response.json()["bookingid"]
             print(bookingid)

     def test_delete_booking(self):
         pass
