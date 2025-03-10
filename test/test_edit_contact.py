_author_ = 'Danil'
from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name ="test", last_name ="test", city="test", number_phone ="test", email ="test"))
    app.contact.edit_contact(Contact(first_name ="alex", last_name ="kozlov", city="ryazan city", number_phone ="888888888", email ="falex@yandex.ru"))
