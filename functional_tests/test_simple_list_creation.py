from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time


class newVisitorTest(FunctionalTest):

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get(self.server_url)
		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		
		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_text')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		# She types "Buy peacock feathers" into a text box (Edith's hobby
		# is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')
		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		
		time.sleep(3)
		edith_list_url = self.browser.current_url
		time.sleep(3)
		self.assertRegex(edith_list_url, '/lists/.+')
		
		time.sleep(1)
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)

		self.browser.find_element_by_id('id_text').send_keys('Use peacock feathers to make a fly')
		time.sleep(1)
		self.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)
		time.sleep(7)

		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# Now a new user, Francis, comes along to the site.

		## We use a new browser session to make sure that no information
		## of Edith's is coming through from cookies, etc
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# Francis visits the home page. There is no sign of Ediths's list
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		time.sleep(1)
		self.assertNotIn('Buy peacock feathers', page_text)
		time.sleep(1)
		self.assertNotIn('make a fly', page_text)
		time.sleep(1)

		# Francis starts a new list by entering a new item. He
		# is less interesting than Edith...
		inputbox = self.browser.find_element_by_id('id_text')
		time.sleep(1)
		inputbox.send_keys('Buy milk')
		time.sleep(1)
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		# Francis gets his own unique URL
		francis_list_url = self.browser.current_url
		time.sleep(1)
		self.assertRegex(francis_list_url, '/lists/.+')
		time.sleep(1)
		self.assertNotEqual(francis_list_url, edith_list_url)
		time.sleep(1)
		# Again, there is no trace of Edith's list
		page_text = self.browser.find_element_by_tag_name('body').text
		time.sleep(1)
		self.assertNotIn('Buy peacock feathers', page_text)
		time.sleep(1)
		self.assertIn('Buy milk', page_text)
		time.sleep(1)

		# Satisfied, tehy both go back to sleep