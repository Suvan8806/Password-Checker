import requests # to access pwned passwords API
import hashlib # for sha one hashing
import sys

# add k anonymity to the github, API use, 
# we need to hash the password with sha one and then feed it back, in which it will result
# hashing passwords assures security
# database has hashed versions of passwords, so it will give correct result
# called K anonymity 
# password123 -> cbfdac6008f9cab4083784cbd1874f76618d2a97
# we give API the first 5 letters of the hash, takex all the result passwords with those starting 5 from API,
# then check if out password ison the list, so then API never gets our password, and our information is secure

    
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char #connect to API and feed it the password you want to test
    res = requests.get(url) #request the result from the API
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines()) #-> converted hashes from each line into a tuple
    for h, count in hashes: #-> seperates the two arguments in the tuple to h and count
        if h == hash_to_check: #-> checks if the tail is in the arguments returned
            return count
    return 0


def pwned_api_check(password):
    #Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #-> sha1 convertor
    first5_char, tail = sha1password[:5], sha1password[5:] #splits so you have the first 5 char and the tail
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args): #takes in ur password input 
    for password in args:
        count = pwned_api_check(password) #gets count
        if count:

            #print(f'Your password was found {count} number of times, you should probably change your password!')
            #if you dont want it to print your password, uncomment the line above and comment the line below
            print(f'{password} was found {count} number of times, you should probably change your password!')
 
        else:

            #print(f'Your password was not found, good job!')
            #if you dont want it to print your password, uncomment the line above and comment the line below
            print(f'{password} was not found, good job!')

    return 'Done!'

def read_passwords_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()] # read the passwords txt file
    
if __name__ == '__main__':
    passwords = read_passwords_from_file('passwords.txt')  # Change this to your filename
    main(passwords)  # Call main with the list of passwords