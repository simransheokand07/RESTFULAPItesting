from AssetTokenStat_FetchData import *
import pandas as pd


'''This function is used to make a csv file of upper and lower bound of pricetoken from symbolroundoff_dict '''
def upper_bound_and_lower_bound_of_pricetoken_in_csv(url_response):
    symbols_list = symbol_in_list(url_response)
    pricetoken_list = pricetoken_in_list(url_response)
    valuesRoundUp = []
    valuesRoundDown = []
    for number in pricetoken_list:
        valuesRoundUp.append(math.ceil(number))
        valuesRoundDown.append(math.floor(number))
    roundoff_list = list(zip(valuesRoundUp, valuesRoundDown))
    symbolroundoff_dict = dict(zip(symbols_list, roundoff_list))
    print(symbolroundoff_dict)

    df1 = pd.DataFrame(symbolroundoff_dict.items())
    df1.to_csv("Assettoken_upperlowerbound.csv", index=False)
    return df1