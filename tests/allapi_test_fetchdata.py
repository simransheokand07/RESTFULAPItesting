from allapi_convertdataintocsv import *
from assertpy import assert_that
import requests

def test_check_status_code_of_csv_file():
    df = pd.read_csv('inputdata/allapi_symbolslist.csv', index_col=0)
    csvlist = df.index
    print(list(csvlist))

    for item in csvlist:
        new_response = requests.get(item)
        assert_that(new_response.status_code == 200)
