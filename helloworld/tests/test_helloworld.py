from helloworld import __version__
from helloworld.main import helloworld

def test_version():
    assert __version__ == '0.1.0', 'Version does not match'

def test_helloworld():
    assert helloworld() == 'Hello World!', 'Hello World does not match'
    