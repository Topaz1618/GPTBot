"""
Author: Hang Yan
Date created: 2023/8/13
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""

from dotenv import load_dotenv


ENV = 'DEV'
# ENV = 'PROD'

if ENV == 'DEV':
    from config_dev import *
    load_dotenv('.env_dev')

elif env == 'PROD':
    from config_prod import *
    load_dotenv('.env_prod')