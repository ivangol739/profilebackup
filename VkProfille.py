import json
import requests
import os
import time
from tqdm import tqdm


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

	def save_directory(self, folder_name="photos"):
		if not os.path.exists(folder_name):
			os.makedirs(folder_name)
			print(f"Папка {folder_name} создана.")
		else:
			print(f"Папка {folder_name} существует.")

	def user_info(self):
		params = self.get_common_params()
		params.update({"user_id": self.user_id})
		response = requests.get(self._build_url("users.get"), params=params)
		return response.json()

	def get_photos_profile(self):
		self.save_directory()
		params = self.get_common_params()
		params.update(dict(user_id=self.user_id, album_id="profile", extended="1"))
		response = requests.get(self._build_url("photos.get"), params=params).json()["response"]["items"]

		photos_list = []
		like_count = set()
		for photo in tqdm(response[:5]):
			photos_dict = {}
			if photo["likes"]["count"] not in like_count:
				photos_dict["file_name"] = str(photo["likes"]["count"]) + ".jpg"
				like_count.add(photo["likes"]["count"])
			else:
				date = time.strftime('%d.%m.%Y', time.localtime(photo["date"]))
				photos_dict["file_name"] = str(photo["likes"]["count"]) + "_" + str(date) + ".jpg"
			photos_dict["size"] = photo["sizes"][-1]["type"]
			photos_list.append(photos_dict)
			img = requests.get(photo["sizes"][-1]['url']).content
			with open("photos" + "/" + photos_dict["file_name"], "wb") as file:
				file.write(img)
		with open("data.json", "w", encoding="utf-8") as file:
			json.dump(photos_list, file)
		return f"Сохранение из ВК завершено"
