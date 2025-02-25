# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username = "admin", password = "secret")
    app.create_contact(Contact(first_name = "danil",last_name = "popov", city= "ryazan city", number_phone = "89997778866", email = "frost@yandex.ru"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username = "admin", password = "secret")
    app.create_contact(Contact(first_name = "",last_name = "", city= "", number_phone = "", email = ""))
    app.logout()





