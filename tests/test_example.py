import unittest
from unittest.mock import patch, MagicMock
import cafe_specials

class TestCafeSpecials(unittest.TestCase):

    @patch('cafe_specials.sqlite3')
    def test_get_todays_specials_success(self, mock_sqlite):
        # Setup mock
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_sqlite.connect.return_value = mock_conn

        # Define what the mock cursor should return for fetchall
        mock_cursor.fetchall.return_value = [
            ('1', 'Coffee', '2.50'),
            ('2', 'Tea', '2.00')
        ]

        # Call the function
        with patch('builtins.print') as mocked_print:
            cafe_specials.get_todays_specials()

            # Check print calls (assert print was called with expected values)
            mocked_print.assert_any_call("Today's Special: Coffee - $2.50")
            mocked_print.assert_any_call("Today's Special: Tea - $2.00")

    @patch('cafe_specials.sqlite3')
    def test_get_todays_specials_exception(self, mock_sqlite):
        # Setup mock to raise an exception when connecting to the DB
        mock_sqlite.connect.side_effect = Exception("Database connection failed")

        # Call the function and check for expected print output (exception message)
        with patch('builtins.print') as mocked_print:
            cafe_specials.get_todays_specials()
            mocked_print.assert_called_with("An error occurred: Database connection failed")

if __name__ == '__main__':
    unittest.main()

