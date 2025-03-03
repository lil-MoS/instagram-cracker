Instagram Brute Force Tool 🔓
This is a simple tool designed to perform a brute force attack on Instagram accounts. It uses the instagram-private-api library to attempt logging into an Instagram account using a list of passwords.

⚠️ Warning
This tool is intended for educational purposes only and for penetration testing on systems you have permission to test. Unauthorized access to accounts is illegal and unethical. The developer of this tool is not responsible for any misuse.

🛠️ Prerequisites
Python 3.x

instagram-private-api library

To install the required library, run the following command:

bash
Copy
pip install git+https://github.com/ping/instagram_private_api.git@1.6.0
🚀 How to Use
Download the ig-cracker.py file.

Prepare a text file containing a list of passwords (one password per line).

Run the script and enter the Instagram username and the path to the password file.

bash
Copy
python ig-cracker.py
The script will start testing the passwords. If successful, it will save the login details in a file called hit.txt.

📋 Example
bash
Copy
Enter the Instagram username: target_username
Enter the path to the password list file: passwords.txt
⚡ Features
A 1-second delay between attempts to avoid detection and blocking by Instagram.

Logs successful attempts in hit.txt.

❗ Notes
This tool may stop working in the future due to changes in Instagram's API.

Use responsibly and only on accounts you own or have permission to test.

🤝 Contributing
If you'd like to contribute to this project, feel free to open a Pull Request.

