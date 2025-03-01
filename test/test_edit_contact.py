_author_ = 'Danil'
from model.contact import Contact

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(first_name ="alex", last_name ="kozlov", city="ryazan city", number_phone ="888888888", email ="falex@yandex.ru"))
    app.session.logout()