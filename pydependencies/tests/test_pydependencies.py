from pydependencies import __version__
from pydependencies.pydependencies import get_data

def test_version():
    assert __version__ == '0.1.0'

def test_get_data():
    url = "https://httpbin.org/json"
    
    assert type(get_data(url)) == dict, "get_data() should return a dict"

def test_get_data_response():
    url = "https://httpbin.org/json"
    response = {
        "slideshow": {
            "author": "Yours Truly",
            "date": "date of publication",
            "slides": [
            {
                "title": "Wake up to WonderWidgets!",
                "type": "all"
            },
            {
                "items": [
                "Why <em>WonderWidgets</em> are great",
                "Who <em>buys</em> WonderWidgets"
                ],
                "title": "Overview",
                "type": "all"
            }
            ],
            "title": "Sample Slide Show"
        }
        }
    
    assert get_data(url) == response, "get_data() response did not match"
