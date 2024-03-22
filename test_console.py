import unittest
from console import HBNBCommand

class TestConsoleMethods(unittest.TestCase):

    def test_destroy(self):
        my_console = HBNBCommand()
        result = my_console.do_destroy("BaseModel 123")
        self.assertTrue(result)  # Verify that the instance with ID 123 is deleted

    def test_update(self):
        my_console = HBNBCommand()
        result = my_console.do_update("BaseModel 123 name NewName")
        self.assertTrue(result)  # Verify that the instance with ID 123 has its name

    def test_create_post(self):
        my_console = HBNBCommand()
        result = my_console.do_create_post("123 New post content")
        self.assertTrue(result)  # Verify that a new post is created

    def test_show_post(self):
        my_console = HBNBCommand()
        result = my_console.do_show_post("123")
        self.assertTrue(result)  # Verify that the details of the post with ID 123 are printed

    def test_analyze_post(self):
        my_console = HBNBCommand()
        result = my_console.do_analyze_post("123")
        self.assertTrue(result)  # Verify that the engagement metrics of the post with ID 123 are printed

    def test_update_profile(self):
        my_console = HBNBCommand()
        result = my_console.do_update_profile("123 new_profile_data")
        self.assertTrue(result)  # Verify that the profile information of the user with ID 123 is updated

    def test_sign_up(self):
        my_console = HBNBCommand()
        result = my_console.do_sign_up("test@example.com password123")
        self.assertTrue(result)  # Verify that a new user is signed up

    def test_log_in(self):
        my_console = HBNBCommand()
        result = my_console.do_log_in("test@example.com password123")
        self.assertTrue(result)  # Verify that the user with the provided email and password is logged in

    def test_delete_account(self):
        my_console = HBNBCommand()
        result = my_console.do_delete_account("123")
        self.assertTrue(result)  # Verify that the account of the user with ID 123 is deleted

if __name__ == '__main__':
    unittest.main()

