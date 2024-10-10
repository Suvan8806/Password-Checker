# Password-Checker
This Python script leverages the Have I Been Pwned (HIBP) API to securely check if passwords have been compromised in known data breaches, using a privacy-preserving technique known as K-anonymity. By hashing passwords with the SHA-1 algorithm, the script ensures the actual password never leaves the user's machine. Instead, only the first five characters of the hash are sent to the HIBP API, significantly reducing the risk of exposing sensitive information.

Once the API returns a list of potentially matching hashes, the script compares the rest of the password’s hash to determine if it has been compromised. This process ensures that the password remains securely stored in the local file and never reaches the API, safeguarding the user's privacy.

The script is designed to read passwords from a text file, making it easy to check multiple passwords at once. If a password has been found in a breach, the user is alerted to change it; otherwise, they receive a message confirming the password's safety. This provides a simple yet powerful tool for maintaining online security without compromising user privacy.

**Instructions**
Download both files and open in any code editor youd like
Enter your password in passwords.txt, and save
Run Checkmypass.py, and see if your password has ever been leaked before!
