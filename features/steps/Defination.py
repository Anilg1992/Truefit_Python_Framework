import unittest

from pytest import fail
from selenium import webdriver
import os
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import logging
import time
from behave import *

import configparser
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
from utility.WrapperDriver import WrapperDriver

config = configparser.ConfigParser()
d = WrapperDriver()

class Defination(unittest.TestCase):
    @Given("I open a browser")
    def I_open_a_browser(context):
        d.openBrowser()

    @When("I am loading google page")
    def I_am_loading_google_page(context):
        d.loadURL("http://www.google.com")

    @When("I am loading google url as \"{url}\"")
    def I_am_loading_google_url_as(context, url):
        d.loadURL(url)

    @Then("I am making sure google logo is displayed")
    def I_am_making_sure_google_logo_is_displayed(context):
        print("Verifying google logo is present")
        if (d.isElementPresent("//img[@id='hplogo']", locatorType='xpath') != True):
            d.screenShot("I_am_making_sure_google_logo_is_displayed")

    @Then("I am making sure that search box is present")
    def I_am_making_sure_that_search_box_is_present(context):
        print("Verifying for search box present")
        if (d.isElementPresent("//input[@title='Search']", locatorType='xpath') != True):
            d.screenShot("I_am_making_sure_that_search_box_is_present")
            fail("I am making sure that search box is present")

    @Then("I am making sure that search button is present")
    def I_am_making_sure_that_search_button_is_present(context):
        print("checking for search button present")
        if (d.isElementPresent("//input[@name='btnK']", locatorType='xpath') != True):
            d.screenShot("I_am_making_sure_that_search_button_is_present")
            fail("I am making sure that search button is present")

    @When("I am clicking search button without entering anything on textbox")
    def I_am_clicking_search_button_without_entering_anything_on_textbox(context):
        print("Without text clicking google search")
        d.elementClick("//*[@class='A8SBwf']//div[@class='FPdoLc VlcLAe']//input[1]", locatorType='xpath')

    @Then("I am still on the google home page and no search results are displayed")
    def I_am_still_on_the_google_home_page_and_no_search_results_are_displayed(context):
        print("Results are not displayed")
        if (d.isElementPresent("//input[@name='btnI']", locatorType='xpath') != True):
            d.screenShot("I_am_still_on_the_google_home_page_and_no_search_results_are_displayed")
            fail("I am still on the google home page and no search results are displayed")

    @When("I am clicking search button by entering \"{input}\" on textbox")
    def I_am_clicking_search_button_by_entering(context, input):
        print("Sending text into the search box")
        d.sendKeys(input, "//input[@title='Search']", locatorType='xpath')
        time.sleep(10)
        print("After Sending text into the search box clicking google search")
        d.elementClick("//input[@value='Google Search']", locatorType='xpath')

    @Then("I am making sure that I am getting the search results")
    def I_am_making_sure_that_I_am_getting_the_search_results(context):
        print("Search results displayed")
        time.sleep(10)
        if (d.isElementPresent("(//a[contains(@href,'truefit')])[1]", locatorType='xpath') != True):
            d.screenShot('I_am_making_sure_that_I_am_getting_the_search_results')
            fail("I am making sure that I am getting the search results")

    @Then("I am closing the browser")
    def I_am_closing_the_browser(context):
        d.quitBrowser()
