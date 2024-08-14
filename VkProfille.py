import requests
import os
import pprint


class UserVk:

	API_BASE_URL = 'https://api.vk.com/method'

	def __init__(self, access_token, user_id):
		self.access_token = access_token
		self.user_id = user_id

	def get_common_params(self):
		return {
			"access_token": self.access_token,
			"v": "5.131",
			}

	def
