# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create(Contact(first_name ="danil", last_name ="popov", city="ryazan city", number_phone ="89997778866", email ="frost@yandex.ru"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create(Contact(first_name ="", last_name ="", city="", number_phone ="", email =""))
    app.session.logout()





