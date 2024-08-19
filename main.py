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
	pprint(vk.get_photos_profile())
