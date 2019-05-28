import json


class ExtensibleJsonEncoder(json.JSONEncoder):
	def __init__(self, plugins, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._plugins = plugins

	def default(self, obj):
		for plugin in self._plugins:
			if plugin.encodeCondition(obj):
				return plugin.encode(obj)
		# else
		return json.JSONEncoder.default(self, obj)


class ExtensibleJsonDecoder(json.JSONDecoder):
	def __init__(self, plugins, *args, **kwargs):
		if 'object_hook' in kwargs:
			raise Exception(
				"'object_hook' "
			)
		kwargs['object_hook'] = self.object_hook
		super().__init__(*args, **kwargs)
		self._plugins = plugins

	def object_hook(self, dct):
		for plugin in self._plugins:
			if plugin.decodeCondition(dct):
				return plugin.decode(dct)
		return dct


class ExtensibleJsonFactory:
	def __init__(self, plugins):
		self._plugins = plugins

	def encoder(self, *args, **kwargs):
		return ExtensibleJsonEncoder(self._plugins, *args, **kwargs)

	def decoder(self, *args, **kwargs):
		return ExtensibleJsonDecoder(self._plugins, *args, **kwargs)