# cafe_specials.py

import sqlite3

# Intentional security vulnerability: Hardcoded credentials
DATABASE_PATH = 'path/to/cafe_moments.db'
USERNAME = 'admin'
PASSWORD = 'password123'  # This is a bad practice!

def get_todays_specials():
    # Connect to the database (this is a simulated connection for demonstration purposes)
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        
        # Imagine we're executing a query to fetch today's specials
        cursor.execute("SELECT * FROM specials WHERE date = CURRENT_DATE")
        specials = cursor.fetchall()
        
        for special in specials:
            print(f"Today's Special: {special[1]} - ${special[2]}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    get_todays_specials()
