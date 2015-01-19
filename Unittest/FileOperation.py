import unittest
from items_management.item_operations import ItemOperations

class FileOperationTest(unittest.TestCase):

    def test_a_file_is_created_when_send_a_name_that_not_exit_previously(self):
        new_file_name = "newFileCreated.txt"
        path_file = "c:"

    def test_the_name_of_file_is_changed_the_name_is_changed(self):
        file_path = "c:"
        file_name = "testFile.txt"
        file_new_name = "testFileRenamed.txt"

        file = open(file_name, 'w+')

        item_operation = ItemOperations()
        item_operation.rename_item(file_path,file_name, file_new_name)
        # file_name doesnt exit
        # file_new_name_exit

if __name__ == '__main__':
    unittest.main
