import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\hunshab\PycharmProjects\pythonSeleniumProject2\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('Common Info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('Common Info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Common Info', 'password')
        return password

