import requests
from assertpy import assert_that
from .pool_config import *
import pytest


'''This function is giving us a response from Api'''
@pytest.fixture()
def get_new_response():
    sampleurl = getconfig()
    response = requests.get(sampleurl)
    return response


'''Firstly we take previous API and stores the symbols in a list i.e. newsymbols_list ,then we pass the newsymbols_list
    in the url1 and then we fetch the new_symbol from json_data and then check that new_symbol is equal to values of 
    keys i.e. in newsymbols_list , finally check that balance is greater than or equal to zero'''
def test_check_symbol_and_balance(get_new_response):
    response_body = get_new_response.json()
    newsymbols_list = []
    for item in response_body:
        newsymbols_list.append(item["externalAsset"]["symbol"])
    for keys in newsymbols_list:
        symbol_url = f"{get_new_response}/{keys}"
        new_response = requests.get(symbol_url)
        json_data = new_response.json()
        new_symbol = json_data["Pool"]["externalAsset"]["symbol"]
        assert_that(new_symbol).is_equal_to(keys)
        balance = json_data["Pool"]["externalAsset"]["balance"]
        assert_that(float(balance)).is_greater_than_or_equal_to(0)














        

