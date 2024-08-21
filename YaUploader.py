import requests
import os
from pprint import pprint

class YaUploader:
	API_BASE_URL_YA = 'https://cloud-api.yandex.net/v1/disk/resources/'

	def __init__(self, token):
		self.token = token

	def upload_photos(self):
		directory = 'photos'

		headers = {
			'Authorization': self.token,
			'Content-Type': 'application/json'
		}
		params = {
			"path": directory,
			"overwrite": "true"
		}

		requests.put(self.API_BASE_URL_YA, headers=headers, params=params)
		current_dir = os.getcwd()
		photos_dir = os.path.join(current_dir, directory)
		photos = os.listdir(photos_dir)
		print(photos)


