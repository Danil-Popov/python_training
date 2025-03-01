_author_ = 'Danil'
from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="ghbdtn", header="ghbdtn", footer="ghbdtn"))
    app.session.logout()