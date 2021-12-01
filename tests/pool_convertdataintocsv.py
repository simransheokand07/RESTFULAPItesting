import pandas as pd
from pool_test_comparing_symbols_from_csv_file_and_Api import *

'''This function is used to create a csv file of symbols and then symbols_list is converted into dataframe'''
def baselinesymbols_in_new_list_and_convert_into_dataframe(get_response):
    response_body = get_response.json()
    baselinesymbols = []
    for item in response_body:
        baselinesymbols.append(item["externalAsset"]["symbol"])
    print(baselinesymbols)

    df = pd.DataFrame(baselinesymbols)
    df.to_csv('pool_symbolslist.csv',index=False)
    return df

