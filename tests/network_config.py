from configparser import ConfigParser


'''Firstly this function reads api pool_endpoint from pytest.ini file then return sampleurl which store API'''
def getconfig():
    config = ConfigParser()
    setup_cfg = os.path.join(root, "pytest.ini")
    parser = config.SafeConfigParser()
    with open(setup_cfg, "r") as f:
        parser.readfp(f)
    sampleurl = parser.get("api", "network_endpoint") # mandatory
    return sampleurl
