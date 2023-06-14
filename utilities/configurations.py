import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\fedco\\Documents\\Python\\ValidationBookStoreAPI\\utilities\\properties.ini')
    return config
