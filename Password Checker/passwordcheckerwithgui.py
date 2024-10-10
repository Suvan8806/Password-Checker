import tkinter as tk
import requests # to access pwned passwords API
import hashlib # for sha one hashing

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

def check_password(): #takes in ur password input 
    password = entry.get()
    count = pwned_api_check(password) #gets count
    if count:
        result_text = f'Your password was found {count} times, you should probably change it!'
    else:
        result_text = 'Your password was not found, good job!'
    
    text_box.delete(1.0, tk.END)  # Clear previous results
    text_box.insert(tk.END, result_text)  # Insert new result

# Create the main window
root = tk.Tk()
root.title("Password Checker")
root.geometry("400x300") # size
root.configure(bg='lightblue')  # Change the background color of the main window

# Create a label for instructions
label = tk.Label(root, text="Enter your password:", bg='lightblue', fg='darkblue')  # Change label colors
label.pack(pady=10)

# Create a text entry box for the password
entry = tk.Entry(root, width=40, show='*', bg='white', fg='black')  # show='*' masks the password, Change entry colors
entry.pack(pady=10)

# Create a button to check the password
button = tk.Button(root, text="Check Password", command=check_password, bg='darkblue', fg='white')  # Change button colors
button.pack(pady=5)

# Create a text box to display output
text_box = tk.Text(root, height=5, width=50, bg='white', fg='black')  # Change text box colors
text_box.pack(pady=10)

# Run the main loop
root.mainloop()