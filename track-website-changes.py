import requests
import hashlib
import time

# URL of the website to track
# url = "https://www.apple.com/newsroom/"
url = "https://github.com/carlosreyes00/python-files-college"

# File to store the hash of the page content
hash_file = "apple_newsroom_page_hash.txt"

def get_page_content(url):
    response = requests.get(url)
    return response.text

def hash_content(content):
    return hashlib.sha256(content.encode()).hexdigest()

def check_for_changes():
    # Fetch the page content
    content = get_page_content(url)
    
    # Hash the current content
    current_hash = hash_content(content)

    try:
        # Read the previous hash from file
        with open(hash_file, 'r') as file:
            previous_hash = file.read()

        # Compare the current hash with the previous hash
        if current_hash != previous_hash:
            print("The website content has changed!")
            
            # Update the stored hash with the new one
            with open(hash_file, 'w') as file:
                file.write(current_hash)
        else:
            print("No changes detected.")
    except FileNotFoundError:
        # If it's the first run, store the current hash
        with open(hash_file, 'w') as file:
            file.write(current_hash)
        print("First run. Stored the current page hash.")

# Run the check every X seconds
if __name__ == "__main__":
    while True:
        check_for_changes()
        # Wait for X seconds before checking again
        time.sleep(2)
