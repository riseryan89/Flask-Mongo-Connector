from configparser import ConfigParser


conf = ConfigParser()
conf.read('conf/.key_store')
DB_LOCAL = conf['DB']['MONGO_LOCAL']
DB_TEST = conf['DB']['MONGO_TEST']
DB_MAIN = conf['DB']['MONGO_MAIN']

JWT = conf['JWT']['JWT_SECRET']