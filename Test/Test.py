import mock
# from pytest_mock import mocker
from mock import Mock, patch

import Test
from Test import echo


def trys():
    return 3


@patch("Test.echo.print_echo")
def testMyMethod(ex):
    echo.print_echo.return_value = "Cream Cheese"
    print(echo.print_echo("Dark Cat"))
