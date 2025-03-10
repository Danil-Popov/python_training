_author_ = 'Danil'

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        # add new contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_group(contact)
        # creation contact
        wd.find_element_by_xpath("//input[20]").click()
        self.return_to_contacts()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_group(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname",contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("address", contact.city)
        self.change_field_value("mobile", contact.number_phone)
        self.change_field_value("email", contact.email)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def edit_contact(self,contact):
        wd = self.app.wd
        self.select_first_contact()
        #edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_group(contact)
        #update contact
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()

    def return_to_contacts(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()