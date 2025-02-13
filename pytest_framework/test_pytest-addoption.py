import pytest


def test_customoption(request):
    custom_value=request.config.getoption("--custom-option")
    print("custom value: ", custom_value)

@pytest.fixture
def env(request):
    return request.config.getoption("--custom-option")