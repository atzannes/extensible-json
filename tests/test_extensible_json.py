import datetime
import json
import pytest

from extensible_json import extensible_json, plugins


def test_extensible_json():
	plugs = [plugins.DatetimeToTimestampPlugin()]

	fac = extensible_json.ExtensibleJsonFactory(plugs)

	def testFac(obj):
		ser = json.dumps(obj, cls=fac.encoder)
		res = json.loads(ser, cls=fac.decoder)
		assert obj == res
		assert obj is not res

	testFac({"a": 2})
	testFac(datetime.datetime(2019, 5, 28))
	with pytest.raises(Exception):
		testFac(datetime.date(2019, 5, 28))

	obj = 1
	ser = json.dumps(obj, cls=fac.encoder)
	with pytest.raises(Exception):
		json.loads(ser, cls=fac.decoder, object_hook=lambda obj: obj)
