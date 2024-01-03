from src.helper.api_request_wrapper import  post_request
from src.constant.api_constants import  APIConstants
from src.helper.utils import common_headers_json
from src.helper.payload_manager import payload_create_booking
from src.helper.common_verification import verify_responce_key_should_not_be_none,verify_http_status_code



import requests
import pytest



class TestCreateBooking(object):
    @pytest.mark.positive
    def test_create_booking_tc1(self):
        response=post_request(url=APIConstants.url_create_booking(),auth=None,header=common_headers_json(),payload=payload_create_booking(),in_json=False)
        print(response)
        verify_responce_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response,expect_data=200)
        bookingid=response.json()["bookingid"]
        print(bookingid)

    @pytest.mark.negative
    def test_create_booking_tc2(self):
     response = post_request(url=APIConstants.url_create_booking(), auth=None, header=common_headers_json(),
                            payload={}, in_json=False)

     verify_http_status_code(response, expect_data=500)

