_author_ = 'Danil'
from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test",header="test", footer="test"))
    app.group.edit_group(Group(name="ghbdtn", header="ghbdtn", footer="ghbdtn"))
