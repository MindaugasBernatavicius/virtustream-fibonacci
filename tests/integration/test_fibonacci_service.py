import pytest
from flask import url_for

def test_root_endpoint(client):
    resp = client.get(url_for('root'))
    assert resp.status_code == 200
    assert 'Welcome to the Fibonacci sequence generator' in str(resp.data)
    
def test_fib_endpoint_empty(client):
    resp = client.get(url_for('fib'))
    assert resp.status_code == 200
    assert 'Please provide a URL query' in str(resp.data)
    
def test_fib_endpoint_small_n(client):
    data = {'limit': '5'}
    resp = client.get(url_for('fib', **data))
    assert resp.status_code == 200
    assert '2\\n3' in str(resp.data)
    
def test_fib_endpoint_big_n(client):
    data = {'limit': '1000'}
    resp = client.get(url_for('fib', **data))
    assert resp.status_code == 200
    assert '34151172899169723197082763985615764450078474174626\\n' in str(resp.data)