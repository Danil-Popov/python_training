_author_ = 'Danil'

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len (wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def delete_first_group (self):
        wd = self.app.wd
        self.open_groups()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def element_edit_group(self):
        # open modification form
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def element_update_group(self):
        # submit modification
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def modify_first_group(self, new_group_data):
        self.open_groups()
        self.select_first_group()
        self.element_edit_group()
        self.fill_group_form(new_group_data)
        self.element_update_group()
        self.return_to_groups()

    def edit_group (self,new_group_data):
        self.open_groups()
        self.select_first_group()
        self.element_edit_group()
        self.fill_group_form(new_group_data)
        self.element_update_group()
        self.return_to_groups()

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups()
        return len (wd.find_elements_by_name("selected[]"))