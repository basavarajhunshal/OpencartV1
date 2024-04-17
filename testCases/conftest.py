import os
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    if request == "edge":
        driver = webdriver.Edge()
    elif request == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################


# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'pythonSeleniumProject2'
#     config._metadata['Module Name'] = 'LoginPage'
#     config._metadata['Tester'] = 'Basavaraj'
#     #config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
#
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
#
# #Specifying report folder location and save report with timestamp
#     @pytest.hookimpl(tryfirst=True)
#     def pytest_configure(config):
#         config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getOptions("--browser")
