import requests
import os


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

	def _build_url(self, api_method):
		return f"{self.API_BASE_URL}/{api_method}"

	def user_info(self):
		params = self.get_common_params()
		params.update({"user_id": self.user_id})
		response = requests.get(self._build_url("users.get"), params=params)
		return response.json()

	def get_photos_profile(self):
		params = self.get_common_params()
		params.update({"user_id": self.user_id,
									 "album_id": "profile",
									 "extented": "1",
									 })
		response = requests.get(self._build_url("photos.get"), params=params)
		return response.json().
