from flask import json
import pytest

@pytest.mark.parametrize('value', (
    1, 't', True, False, None,
    [], [1, 2, 3],
    {}, {'foo': u'🐍'},
))
@pytest.mark.parametrize('encoding', (
    'utf-8', 'utf-8-sig',
    'utf-16-le', 'utf-16-be', 'utf-16',
    'utf-32-le', 'utf-32-be', 'utf-32',
))
def test_detect_encoding(value, encoding):
    data = json.dumps(value).encode(encoding)
    assert json.detect_encoding(data) == encoding
    assert json.loads(data) == value
