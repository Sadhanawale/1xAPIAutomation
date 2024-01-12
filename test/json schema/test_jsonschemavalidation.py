import json
import os


from src.helper.api_request_wrapper import  post_request
from src.constant.api_constants import  APIConstants
from src.helper.utils import common_headers_json
from src.helper.payload_manager import payload_create_booking
from src.helper.common_verification import verify_responce_key_should_not_be_none,verify_http_status_code



import requests
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError



class TestCreateBooking(object):
    def load_schema(self,schema_file):
        with open(schema_file, 'r')as file:
            return json.load(file)
    @pytest.mark.positive
    def test_create_booking_Tc1(self):

        response=post_request(url=APIConstants.url_create_booking(),auth=None,header=common_headers_json(),payload=payload_create_booking(),in_json=False)
        print(response)
        verify_responce_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response,expect_data=200)
        bookingid=response.json()["bookingid"]
        print(bookingid)
        response_json=response.json()

        file=os.getcwd() +"/schema.json"
        schema=self.load_schema(file)
        print(schema)

        try:
            validate(instance=response_json,schema=schema)
        except ValidationError as  e:
            print(e.message)


