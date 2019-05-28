import datetime

from extensible_json import plugins


def test_date_plugin():
	pi = plugins.DateToStringPlugin()

	# encodeCondition
	assert pi.encodeCondition(None) is False
	assert pi.encodeCondition(1) is False
	assert pi.encodeCondition(datetime.date(2000, 1, 1)) is True
	assert pi.encodeCondition(datetime.datetime(200, 1, 1)) is False

	# encode-decode
	d = datetime.date(2019, 5, 28)
	enc = pi.encode(d)
	assert enc == {pi.KEY: "2019/5/28"}
	assert pi.decodeCondition(enc) is True
	assert pi.decode(enc) == d

def test_datetime_plugin():
	pi = plugins.DatetimeToTimestampPlugin()

	# encodeCondition
	assert pi.encodeCondition(None) is False
	assert pi.encodeCondition(1) is False
	assert pi.encodeCondition(datetime.datetime(2000, 1, 1)) is True
	assert pi.encodeCondition(datetime.date(2000, 1, 1)) is False

	# encode-decode
	dt = datetime.datetime(2019, 5, 28)
	enc = pi.encode(dt)
	assert enc == {pi.KEY: dt.timestamp()}
	assert pi.decodeCondition(enc) is True
	assert pi.decode(enc) == dt
