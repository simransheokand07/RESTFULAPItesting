from AssetTokenStat_FetchData import *
import pandas as pd


'''This function mainly used to make a csv file which stores symbols and pricetoken from symbolpricetoken_dict
    by using pandas'''
def symbol_and_pricetoken_in_csv(url_response):
    symbols_list = symbol_in_list(url_response)
    pricetoken_list = pricetoken_in_list(url_response)
    symbolpricetoken_dict = dict(zip(symbols_list, pricetoken_list))
    print(symbolpricetoken_dict)

    df1 = pd.DataFrame(symbolpricetoken_dict.items())
    df1.to_csv('Assettoken_symbolpricetokendict2.csv',index=False)
    return df1
