import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
sys.path.append('./')
from db import posts, users, helpers

class CommentTest(unittest.TestCase):
    def setUp(self):
        # Setup the Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5001')  # Adjust the URL to your application's login page

    def test_comment(self):
        driver = self.driver

        # Fill the login form and submit
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        username.send_keys('test')  # Username is 'test'
        password.send_keys('test')  # Password is 'test'
        driver.find_element(By.ID, 'Login').click()  # Click the login button

        # Wait for login to complete and redirect to the main page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'post'))
        )

        # Create a new post
        post_text = driver.find_element(By.ID, 'post-text')
        post_text.send_keys('Hello, this is a test post.')
        driver.find_element(By.ID, 'post-submit').click()

        # Wait for post to appear and then find the comment field
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'comment'))
        )

        # Create a comment on the post
        post_text = driver.find_element(By.ID, 'comment-text')
        post_text.send_keys('Hello, this is a test comment.')
        driver.find_element(By.ID, 'comment-submit').click()


        # Check if the post is commented on
        # Using sleep to give time for the post comment to appear
        import time
        time.sleep(2)
        posts = driver.find_elements(By.ID, "post")
        self.assertEqual(len(posts), 0)

    def tearDown(self):
        # Close the WebDriver
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
