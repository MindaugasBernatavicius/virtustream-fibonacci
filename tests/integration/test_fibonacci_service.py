import pytest
from flask import url_for

def test_root_url(client):
    assert client.get(url_for('root')).status_code == 200