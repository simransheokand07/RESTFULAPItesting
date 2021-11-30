from configparser import ConfigParser


'''This function reads the API Endpoint from pytest.ini file and return sampleurl which stores the API'''
def getconfig():
    config = ConfigParser()
    config.read('pytest.ini')
    sampleurl = config.get('api', 'endpoint')
    return sampleurl