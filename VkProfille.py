import requests
import os
from pprint import pprint
import time


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
									 "extended": "1",
									 })
		response = requests.get(self._build_url("photos.get"), params=params).json()["response"]["items"]

		photos_list = []
		like_count = set()
		for photo in response[:5]:
			photos_dict = {}
			if photo["likes"]["count"] not in like_count:
				photos_dict["file_name"] = str(photo["likes"]["count"]) + ".jpg"
				like_count.add(photo["likes"]["count"])
			else:
				date = time.strftime('%d.%m.%Y', time.localtime(photo["date"]))
				photos_dict["file_name"] = str(photo["likes"]["count"]) + "_" + str(date) + ".jpg"
			photos_dict["size"] = photo["sizes"][-1]["type"]
			img = requests.get(photo["sizes"][-1]['url']).content
			pprint(photos_dict)
		pprint(response)
		return
