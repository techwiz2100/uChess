class DataProvider(object):
	config = None
	
	def set(key, value, constraints=None):
		pass
	def get(key, constraints=None):
		pass
	def init(config):
		self.config = config

#TODO This skeleton class should be extended
# possibly for the support of the various data types across the various data providers