from jproperties import Properties

config = Properties()

with open("C://UmaRaniDundigalla//UmaRani_workspace//GUVI//Guvi_Projects//GUVI_Project2//Configurations//config.properties", 'rb') as configFile:
    config.load(configFile)



class ReadConfig:

    @staticmethod
    def getAppUrl():
        url = config.get("baseURL").data
        return url

    @staticmethod
    def getUsername():
        username = config.get("username").data
        return username

    @staticmethod
    def getPassword():
        password = config.get("password").data
        return password

    @staticmethod
    def getInvalidPassword():
        password_invalid = config.get("password_invalid").data
        return password_invalid

    @staticmethod
    def getFirstName():
        firstname = config.get("firstname").data
        return firstname

    @staticmethod
    def getMiddleName():
        middlename = config.get("middlename").data
        return middlename

    @staticmethod
    def getLastName():
        lastname = config.get("lastname").data
        return lastname

    @staticmethod
    def getNickName():
        nickname = config.get("nickname").data
        return nickname









