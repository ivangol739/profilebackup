from dotenv import load_dotenv
import os
from VkProfille import UserVk
from YaUploader import YaUploader
from pprint import pprint

if __name__ == "__main__":
	load_dotenv()
	api_token = os.getenv('API_TOKEN_VK')
	user_id = "90962492"
	vk = UserVk(api_token, user_id)
	print(vk.get_photos_profile())
	api_token_ya = os.getenv('API_TOKEN_YA')
	ya = YaUploader(api_token_ya)
	print(ya.upload_photos())
