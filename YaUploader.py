import requests
import os
from pprint import pprint
from tqdm import tqdm


class YaUploader:
	API_BASE_URL_YA = "https://cloud-api.yandex.net/v1/disk/resources"
	directory = "photos/"

	def __init__(self, token):
		self.token = token

	def get_common_params(self):
		return {
			"path": "",
		}

	def get_common_headers(self):
		return {
			'Authorization': self.token,
			'Content-Type': 'application/json'
		}

	def create_folder(self):
		params = self.get_common_params()
		params.update({"path": self.directory})
		requests.put(self.API_BASE_URL_YA, headers=self.get_common_headers(), params=params)

	def upload_photos(self):
		self.create_folder()
		current_dir = os.getcwd()
		photos_dir = os.path.join(self.directory)
		photos = os.listdir(photos_dir)
		for photo in tqdm(photos):
			params = self.get_common_params()
			params.update({
				"path": f"{photos_dir}{photo}",
				"overwrite": "true"
			})
			url_for_upload = requests.get(f"{self.API_BASE_URL_YA}/upload", headers=self.get_common_headers(), params=params)
			href = url_for_upload.json()["href"]
			upload = requests.put(href, open(photos_dir + photo, "rb"))
		return f"Файлы загружены"
