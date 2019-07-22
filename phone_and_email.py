import re, pyperclip

phone_regex = re.compile(r'^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$')
email_regex = re.compile(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b')

target_text = pyperclip.paste()

extracted_phone = phone_regex.findall(target_text)
extracted_email = email_regex.findall(target_text)

print(extracted_phone)
print(extracted_email)
