from dotenv import load_dotenv
import os
from VkProfille import UserVk
from YaUploader import YaUploader

load_dotenv()

api_token = os.getenv('API_TOKEN')

if __name__ == "__main__":
	a = UserVk()
	b = YaUploader()