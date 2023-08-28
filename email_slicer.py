def email_slicer(email):
    parts = email.split('@')
    username = parts[0]
    domain= parts[1]

    return username, domain

email = input("Enter your enail  adress: ")
username, domain = email_slicer(email)
print(f"Username: {username}")
print(f"Domain: {domain}")