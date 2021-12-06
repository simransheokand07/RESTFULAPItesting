import requests
import pytest
from .pool_config import *
from assertpy.assertpy import assert_that
import pandas as pd
import logging
LOGGER = logging.getLogger('pytest.ini')


'''This function is giving us a response from Api'''
@pytest.fixture()
def get_response():
    sampleurl = getconfig()
    response = requests.get(sampleurl)
    return response


'''This test is checking status_code, content-type and content-length that are 200 ,'application/json' and length 
is in between 16000 to 18000 respectively'''
@pytest.mark.xfail(raises=AssertionError)
def test_check_response_status_and_headers(get_response):
    assert_that(get_response.status_code == 200)
    assert_that(get_response.headers['content-type'] == 'application/json')
    assert_that(int(get_response.headers['content-length'])).is_between(16000, 18000)


'''This function stores the symbols in symbol_list'''
def symbols_in_list(get_response):
    response_body = get_response.json()
    symbols_list = []
    for item in response_body:
        symbols_list.append(item["externalAsset"]["symbol"])
    return symbols_list


'''This Function reads the data from csv file and give a symbols list i.e csvlist'''
def baseline_symbol_from_csv_file():
    df = pd.read_csv('inputdata/pool_symbolslist.csv', index_col=0)
    csvlist = df.index
    return list(csvlist)


'''This test is comparing the symbols from csv file and symbols from API ,if symbols are not same ,so it return 
    the difference between them'''
def test_compare_csv_files_and_symbol_list(get_response):
    csvlist = baseline_symbol_from_csv_file()
    symbols_list = symbols_in_list(get_response)
    if symbols_list == csvlist:
        LOGGER.info(f"Both are successfully compared")
    else:
        list1 = sorted(set(symbols_list) - set(csvlist))
        list2 = sorted(set(csvlist) - set(symbols_list))
        LOGGER.info(f"symbol in Api: {list1}")
        LOGGER.info(" ***************** ")
        LOGGER.info(f"symbol in csv file: {list2}")


'''This test is comparing the length of baselinesymbols(csvlist) and symbol_list from API and return the lengths of 
    both'''
def test_compare_length_of_baselinesymbols_and_symbol_list(get_response):
    csvlist = baseline_symbol_from_csv_file()
    symbols_list = symbols_in_list(get_response)

    len_list1 = len(symbols_list)
    len_list2 = len(csvlist)
    LOGGER.info(f"length of symbols_list:, {len_list1}")
    LOGGER.info(f"length of baselinesymbols:, {len_list2}")
