"""
Author: Hang Yan
Date created: 2023/8/9
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""
import os
import json
from dotenv import load_dotenv


from public_info import PublicInfo

# Load environment variables from .env file
load_dotenv()

# Access the paragraph from the environment variable
paragraph = os.getenv("OPENAI_API_KEY")
print(paragraph)