#argrarse and pytest_addioption features have some similarities
import pytest


# both of these helps to access inupt(flags) at runtime

def pytest_addoption(parser):
    parser.addoption("--custom-option",
                     action="store",
                     default="test",
                     help="Description of the custom option.")

# now access the custom option value in the below test function using request fixture

