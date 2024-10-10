# Password-Checker
This Python script leverages the Have I Been Pwned (HIBP) API to securely check if passwords have been compromised in known data breaches, using a privacy-preserving technique known as K-anonymity. By hashing passwords with the SHA-1 algorithm, the script ensures the actual password never leaves the user's machine. Instead, only the first five characters of the hash are sent to the HIBP API, significantly reducing the risk of exposing sensitive information.

Once the API returns a list of potentially matching hashes, the script compares the rest of the password’s hash to determine if it has been compromised. This process ensures that the password remains as an input from the GUI, and never reaches the API, safeguarding the user's privacy.

The script features a user-friendly graphical interface built using Tkinter, making it easy to input passwords and receive immediate feedback. Users can enter their passwords directly into the GUI, which then checks for breaches and displays the results clearly. This provides a simple yet powerful tool for maintaining online security without compromising user privacy.

![image](https://github.com/user-attachments/assets/b95d831d-b63c-4659-911b-6c3b210d74dc)


# Instructions
1. Download passwordcheckerwithgui
2. Enter your password in the GUI and click the "Check Password" button.
3. If your password has been found in a breach, you will be alerted to change it; otherwise, you will receive a message confirming the password's safety.
   
   To check for multiple passwords at once,
1. Download checkmypass.py and passwords.txt, ensuring they're on the same folder.
2. Input them into the text file named passwords.txt.
3. Run checkmypass.py
4. If any of your passwords have been found in a breach, you will be alerted to change it; otherwise, you will receive a message confirming the password's safety.
