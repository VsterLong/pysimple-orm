import configparser

from orm.sql_config import SqlConfig

config = configparser.ConfigParser()
config.read("./config/properties.conf")

sql_config = SqlConfig()

sql_config._host = config['mysql']['host']
sql_config._port = int(config['mysql']['port'])
sql_config._user = config['mysql']['username']
sql_config._passwd = config['mysql']['password']
sql_config._database = config['mysql']['database']
