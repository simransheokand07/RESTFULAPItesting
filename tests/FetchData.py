import logging
import requests
import pytest
from assertpy import assert_that , soft_assertions
from config import *
import pandas as pd
import math
from inputdata import symbolpricetokendict2 , upperlowerbound

LOGGER = logging.getLogger('pytest.ini')

'''This fixture is getting url_response and pool_list i.e url_response is in JSON format and pool_list is in a list '''
@pytest.fixture
def url_response():
    sampleurl = getconfig()
    response = requests.get(sampleurl)
    response_body = response.json()
    pool_list = response_body["body"]["pools"]
    return pool_list


'''This Test is checking status_code and headers that are content-type and content-length'''
def test_check_status_code_and_headers():
    sampleurl = getconfig()
    response = requests.get(sampleurl)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers['content-type']).is_equal_to('application/json')
    total_length = response.headers['content-length']
    assert_that(int(total_length)).is_between(12000, 18000)


'''This function stores the symbols in symbols_list'''
def symbol_in_list(url_response):
    symbols_list = []
    for item in url_response:
        symbols_list.append(item["symbol"])
    return symbols_list


'''This function stores the priceToken in pricetoken_list'''
def pricetoken_in_list(url_response):
    pricetoken_list = []
    for item in url_response:
        pricetoken_list.append(item["priceToken"])
    return pricetoken_list


'''Firstly This Test is combining symbols_list and pricetoken_list into a dictionary and then it is checking that 
symbol is not empty for pricetoken '''
def test_check_symbol_is_not_empty_for_pricetoken(url_response):
    symbols_list = symbol_in_list(url_response)
    pricetoken_list = pricetoken_in_list(url_response)
    symbolpricetoken_dict = dict(zip(symbols_list, pricetoken_list))
    for k, v in symbolpricetoken_dict.items():
        assert_that({symbolpricetoken_dict[k]}).is_not_empty()
    return symbolpricetoken_dict


'''This function reads the data from the csv file and return a dictionary'''
def baseline_symbol_and_pricetoken_from_csv_file():
    df = pd.read_csv('symbolpricetokendict2.csv')
    csvDict = df.set_index('0')['1'].to_dict()
    return csvDict


'''This test is comparing csv file data i.e csvDict and data come from API i.e symbolpricetoken are equal or not and 
    then give the difference if they are not equal'''
def test_compare_csv_files_and_symbolpricetoken(url_response):
    csvDict = baseline_symbol_and_pricetoken_from_csv_file()
    symbolpricetoken_dict = test_check_symbol_is_not_empty_for_pricetoken(url_response)
    if symbolpricetoken_dict == csvDict:
        LOGGER.info('Both are successfully compared')
        assert True
    else:
        list1 = list(sorted(set(symbolpricetoken_dict.items()) - set(csvDict.items())))
        list2 = list(sorted(set(csvDict.items()) - set(symbolpricetoken_dict.items())))
        LOGGER.info(f"Different symbolpricetoken values in Api: {list1}")
        LOGGER.info(" ***************** ")
        LOGGER.info(f"Different symbolpricetoken values in csv file: {list2}")


'''This function stores pooldepth values in pooldepth_list'''
def pooldepth_in_list(url_response):
    pooldepth_list = []
    for item in url_response:
        pooldepth_list.append(item["poolDepth"])
    return pooldepth_list


'''Firstly This Test is combining symbols_list and pooldepth_list into a dictionary and then it is checking that 
symbol is not empty for pooldepth'''
def test_check_symbol_is_not_empty_for_pooldepth(url_response):
    symbols_list = symbol_in_list(url_response)
    pooldepth_list = pooldepth_in_list(url_response)
    symbolpooldepth_dict = dict(zip(symbols_list, pooldepth_list))
    for k, v in symbolpooldepth_dict.items():
        assert_that({symbolpooldepth_dict[k]}).is_not_empty()


'''This function stores volume values in volume_list'''
def volume_in_list(url_response):
    volume_list = []
    for item in url_response:
        volume_list.append(item["volume"])
    return volume_list


'''Firstly This Test is combining symbols_list and volume_list into a dictionary and then it is checking that 
symbol is not empty for volume'''
def test_check_symbol_is_not_empty_for_volume(url_response):
    symbols_list = symbol_in_list(url_response)
    volume_list = volume_in_list(url_response)
    symbolvolume_dict = dict(zip(symbols_list, volume_list))
    for k, v in symbolvolume_dict.items():
        assert_that({symbolvolume_dict[k]}).is_not_empty()


'''This function stores arb values in arb_list'''
def arb_in_list(url_response):
    arb_list = []
    for item in url_response:
        arb_list.append(item["arb"])
    return arb_list


'''Firstly This Test is combining symbols_list and arb_list into a dictionary and then it is checking that 
symbol is not empty for arb_list'''
def test_check_symbol_is_not_empty_for_arb(url_response):
    symbols_list = symbol_in_list(url_response)
    arb_list = arb_in_list(url_response)
    symbolarb_dict = dict(zip(symbols_list, arb_list))
    for k, v in symbolarb_dict.items():
        assert_that(symbolarb_dict[k]).is_not_none()


'''Firstly This function is giving upper bound and lower bound of pricetoken from pricetoken_list by using math.ceil 
   and math.floor, stores the values in valuesRoundUp and valuesRoundDown list, then combined the valuesRoundUp  and 
   valuesRoundDown in a list i.e. roundoff_list and finally combining the symbol_list and roundoff_list in a dictionary 
   i.e. symbolroundoff_dict'''
def upper_bound_and_lower_bound_of_pricetoken(url_response):
    symbols_list = symbol_in_list(url_response)
    pricetoken_list = pricetoken_in_list(url_response)
    valuesRoundUp = []
    valuesRoundDown = []
    for number in pricetoken_list:
        valuesRoundUp.append(math.ceil(number))
        valuesRoundDown.append(math.floor(number))
    roundoff_list = list(zip(valuesRoundUp, valuesRoundDown))
    symbolroundoff_dict = dict(zip(symbols_list, roundoff_list))
    return symbolroundoff_dict


'''This function reads the data from csv file i.e upperlowerbound.csv and then return a dictionary i.e csvDict'''
def baseline_symbol_and_pricetoken_with_upper_lower_bound_from_csv_file():
    df = pd.read_csv('upperlowerbound.csv')
    boundCsvDict = df.set_index('0')['1'].to_dict()
    return boundCsvDict


'''This test is comparing data from csv file with data from API i.e. check the upper and lower bound values are 
   equal or not and then gives the difference '''
def test_compare_csv_files_and_upper_lower_bound_of_pricetoken(url_response):
    boundCsvDict = baseline_symbol_and_pricetoken_with_upper_lower_bound_from_csv_file()
    symbolroundoff_dict = upper_bound_and_lower_bound_of_pricetoken(url_response)
    if symbolroundoff_dict == boundCsvDict:
        LOGGER.info('Both are successfully compared')
        assert True
    else:
        list1 = list(sorted(set(symbolroundoff_dict.items()) - set(boundCsvDict.items())))
        list2 = list(sorted(set(boundCsvDict.items()) - set(symbolroundoff_dict.items())))
        LOGGER.info(f"upper and lower bound in Api: {list1}")
        LOGGER.info("***********")
        LOGGER.info(f"upper and lower bound in csv file is: {list2}")
