#from network_config import *
import requests
from assertpy import assert_that

from configparser import ConfigParser


'''Firstly this function reads api pool_endpoint from pytest.ini file then return sampleurl which store API'''
def getconfig():
    config = ConfigParser()
    config.read('../pytest.ini')
    sampleurl = config.get('api', 'network_endpoint')
    return sampleurl

'''This Test is checking status_code, content-type , content-length and also checks that amount is greater than or
    equal to zero and check address is not empty'''
def test_check_statuscode_and_headers_and_amount_is_greaterthan_equalto_zero_and_address_is_notempty():
    sampleurl = getconfig()
    item = "dispensation"
    keys = "lm_bonus"
    new_url = f'{sampleurl}/{item}/{keys}'
    response = requests.get(new_url)
    total_length = response.headers['content-length']
    assert_that(int(total_length)).is_between(90000, 100000)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers['content-type']).is_equal_to('application/json')

    response_body = response.json()
    amount = response_body["Output"][0]["coins"][0]["amount"]
    assert_that(float(amount)).is_greater_than_or_equal_to(0)

    address = response_body["Output"][0]["address"]
    assert_that(address).is_not_empty()
