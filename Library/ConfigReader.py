from configparser import RawConfigParser

def readConfigData(section,key):
    config=RawConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")
    return config.get(section,key)

def fetchElementLocators(section,key):
    config = RawConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section, key)
