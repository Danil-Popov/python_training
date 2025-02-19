# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        # login
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def create_contact(self, contact):
        # add new contact
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        # fill contact group
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.city)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.number_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # creation contact

        wd.find_element_by_xpath("//input[20]").click()


    def return_to_contacts(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        self.open_home_page()
        self.login(username = "admin", password = "secret")
        self.create_contact(Contact(first_name = "danil",last_name = "popov", city= "ryazan city", number_phone = "89997778866", email = "frost@yandex.ru"))
        self.return_to_contacts()
        self.logout()

    def test_add_empty_contact(self):
        self.open_home_page()
        self.login(username = "admin", password = "secret")
        self.create_contact(Contact(first_name = "",last_name = "", city= "", number_phone = "", email = ""))
        self.return_to_contacts()
        self.logout()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
