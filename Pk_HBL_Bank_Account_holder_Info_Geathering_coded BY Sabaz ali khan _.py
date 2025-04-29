import requests
from bs4 import BeautifulSoup

# URL of the Pakistan HBL website
url = 'https://www.hbl.com.pk/en/personal-banking/account-inquiry'

# User input for account number
account_number = input("Enter your account number: ")

# User input for account type
account_type = input("Enter your account type (Savings or Current): ")

# User input for account holder name
account_holder_name = input("Enter your account holder name: ")

# Prepare the payload for the POST request
payload = {
    'AccountNumber': account_number,
    'AccountType': account_type,
    'AccountHolderName': account_holder_name,
    'Submit': 'Submit'
}

# Send a POST request to the website
response = requests.post(url, data=payload)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the account details section
account_details = soup.find('div', {'class': 'col-sm-9'})

# Extract the account information
account_info = account_details.find_all('p')

# Print the account information
for info in account_info:
    print(info.text.strip())