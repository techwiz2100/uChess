#! /usr/bin/python
from flask import Flask
import argparse
import datetime
import configparser

app_name = "uChess"
app_version = "v0.1"
configFile = None
config = configparser.ConfigParser()
dataProvider = None
app = Flask(app_name)
login_manager = LoginManager()

def selectDataProvider(providerType):
	if providerType is 'mysql':
		return MySQLProvider()
	else:
		return None

@app.route('/')
def index():
	return app_name + " " + app_version

@login_manager.user_loader
def load_user(userid):
	return None
	#TODO utilize data provider to retrieve user from database

if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog=app_name, description=app_name + ' server ' + app_version)
	parser.add_argument('--debug', dest='debug', action='store_true')
	parser.add_argument('-p', '--port', dest='port', type=int, default=8080, metavar='PORT', help='Set server port')
	parser.add_argument('-c', '--config', dest='configFile', type=str, default='server.conf', metavar='CONFIG', help='Set config file to use')
	args = parser.parse_args(argv)
	configFile = args.configFile
	config.read(configFile)
	dataProvider = selectDataProvider(config['Server']['dataProviderType'])
	dataProvider.init(config['dataProvider'])
	login_manager.init_app(app)
	app.run(vars(args), host='0.0.0.0')