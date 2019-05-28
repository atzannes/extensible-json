import datetime

from abc import ABC, abstractmethod


class ExtensibleJsonPluginInterface(ABC):
	@abstractmethod
	def encodeCondition(self, obj) -> bool:
		""" Returns True iff this plugin should encode the given object
		"""
		pass

	@abstractmethod
	def encode(self, obj):
		pass

	@abstractmethod
	def decodeCondition(self, dct) -> bool:
		pass

	@abstractmethod
	def decode(self, dct):
		pass


class DatetimeToTimestampPlugin(ExtensibleJsonPluginInterface):
	KEY = '__datetime.datetime.timestamp__'

	def encodeCondition(self, obj):
		return isinstance(obj, datetime.datetime)

	def encode(self, obj):
		return {self.KEY: obj.timestamp()}

	def decodeCondition(self, dct):
		return self.KEY in dct

	def decode(self, dct):
		return datetime.datetime.fromtimestamp(dct[self.KEY])


class DateToStringPlugin(ExtensibleJsonPluginInterface):
	KEY = '__datetime.date.str__'

	def encodeCondition(self, obj):
		return type(obj) is datetime.date

	def encode(self, obj):
		return {
			self.KEY: '{}/{}/{}'.format(obj.year, obj.month, obj.day)
		}

	def decodeCondition(self, dct):
		return self.KEY in dct

	def decode(self, dct):
		year, month, day = dct[self.KEY].split('/')

		return datetime.date(
			int(year), int(month), int(day)
		)
