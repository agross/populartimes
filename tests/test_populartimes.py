import numbers
from populartimes.crawler import get_populartimes, PopulartimesException
import pytest # type: ignore

API_KEY = 'secret'
PLACE_ID = 'ChIJhzuapHT3pkcRGu_j_x8heXM'

def test_existing_place():
    result = get_populartimes(API_KEY, PLACE_ID)

    # pytest -s
    print(result)

    assert result['id'] == PLACE_ID
    assert 'Crunch Fit' in result['name']
    assert 'Zschochersche Str' in result['address']
    assert 'gym' in result['types']
    assert 'coordinates' in result

    assert 'current_popularity' in result
    assert isinstance(result['current_popularity'], numbers.Number)

    assert 'populartimes' in result
    assert len(result['populartimes']) == 7
    assert result['populartimes'][0]['name'] == 'Monday'
    assert len(result['populartimes'][0]['data']) == 24

    assert 'time_spent' in result
    assert len(result['time_spent']) == 2

def test_bogus_place():
    with pytest.raises(PopulartimesException):
        get_populartimes(API_KEY, 'doesnotexist')

def test_api_key_wrong():
    with pytest.raises(PopulartimesException):
        get_populartimes('not an API key', '')
