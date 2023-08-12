"""
Author: Hang Yan
Date created: 2023/4/17
Email: topaz1668@gmail.com

This code is licensed under the GNU General Public License v3.0.
"""

import requests
import logging
from ipwhois import IPWhois


logging.basicConfig(filename="../logs/ip_address.log",
                    filemode='a',
                    format='[%(levelname)s][%(asctime)s][line %(lineno)d, in <%(funcName)s>] %(message)s',
                    datefmt='%d/%b/%Y %H:%M:%S',
                    level=logging.INFO)


class PublicInfo(object):
    def check_ip_ownership(self, ip_address):
        result = IPWhois(ip_address).lookup_rdap()
        owner = result.get("asn_description", "Unknown")
        country_code = result.get("asn_country_code", "Unknown")
        print("Owner: ", owner)
        print("Country: ", country_code)
        return country_code

    def get_ip(self):
        """Gets the public IP address of the computer."""
        response = requests.get("https://api.ipify.org")
        logging.info(f"Public IP address: {response.text.strip()}")
        return response.text.strip()

    def get_public_ip(self):
        response = requests.get('http://ipinfo.io/json').json()
        country_code = response.get("country")
        ip_address = response.get("ip")
        logging.info(f"Country Code: {country_code} Public IP address: {ip_address}")
        return country_code, ip_address


if __name__ == "__main__":
    public_ip = PublicInfo()
    country_code, ip_address = public_ip.get_public_ip()
    if country_code and ip_address:
        logging.info(f"Country Code: {country_code} Public IP address: {ip_address}")
    else:
        print("Error retrieving public IP info.")



