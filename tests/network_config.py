from configparser import ConfigParser


'''Firstly this function reads api pool_endpoint from pytest.ini file then return sampleurl which store API'''
def getconfig():
    config = ConfigParser()
    config.read('../pytest.ini')
    sampleurl = config.get('api', 'network_endpoint')
    return sampleurl
