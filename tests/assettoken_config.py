from configparser import ConfigParser

'''This function reads the API tokenstat_endpoint from pytest.ini file and return sampleurl which stores the API'''


def getconfig():
    config = ConfigParser()
    config.read('tests/pytest.ini')
    sampleurl = config.get('api','tokenstat_endpoint')
    return sampleurl
