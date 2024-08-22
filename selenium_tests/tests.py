from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
import time
from selenium.webdriver.common.keys import Keys


# Database connection settings
DB_HOST = "mysql"  # Ensure this is the correct service name in your Docker network
DB_USER = "wog_user"
DB_PASSWORD = "userpassword"
DB_NAME = "games"

# Set up Selenium Chrome options for headless mode
def get_chrome_driver():
    options = Options()
    options.add_argument('--headless')  # Run Chrome in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Explicitly specify the ChromeDriver path
    service = Service('/usr/bin/chromedriver')
    return webdriver.Chrome(service=service, options=options)

# UI Test: Test the intro page for invalid inputs
def test_intro_page():
    print("Starting UI test: test_intro_page")
    driver = None
    try:
        driver = get_chrome_driver()

        # Retry mechanism to ensure the web app is ready
        for _ in range(5):
            try:
                driver.get('http://intro:8000/')
                break
            except Exception:
                time.sleep(5)
        else:
            raise Exception("Web application did not become ready in time.")

        # Explicit wait for the element to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )

        # Test invalid input
        input_element = driver.find_element(By.NAME, "name")
        input_element.clear()
        input_element.send_keys("1234")
        input_element.send_keys(Keys.RETURN)

        # Verify the error message for invalid name
        assert "Name should not contain only numbers" in driver.page_source
        print("UI test: test_intro_page passed")
    except Exception as e:
        print(f"UI test: test_intro_page failed with error: {e}")
    finally:
        if driver:
            driver.quit()

# Database Test: Test database connection
def test_db_connection():
    print("Starting DB test: test_db_connection")
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        assert db_name[0] == DB_NAME
        print("DB test: test_db_connection passed")
    except mysql.connector.Error as err:
        print(f"DB test: test_db_connection failed with error: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Database Test: Test inserting and retrieving scores from the DB
def test_insert_and_retrieve_score():
    print("Starting DB test: test_insert_and_retrieve_score")
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()

        # Insert a test player and score
        test_username = "test_user"
        test_score = 50
        cursor.execute(f"INSERT INTO scores_player (name, score) VALUES (%s, %s)", (test_username, test_score))
        connection.commit()

        # Retrieve the inserted player and verify score
        cursor.execute("SELECT score FROM scores_player WHERE name = %s", (test_username,))
        result = cursor.fetchone()
        assert result[0] == test_score
        print("DB test: test_insert_and_retrieve_score passed")

        # Clean up by deleting the test data
        cursor.execute("DELETE FROM scores_player WHERE name = %s", (test_username,))
        connection.commit()

    except mysql.connector.Error as err:
        print(f"DB test: test_insert_and_retrieve_score failed with error: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    # Run UI test for the intro page
    test_intro_page()
    
    # Run DB tests
    test_db_connection()
    test_insert_and_retrieve_score()