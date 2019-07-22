import pyperclip, json

def hash_something(something):
    hashed_list = []
    for ch in something:
        hashed_list.append(ord(ch) + 6)
    return hashed_list

def undo_hash(something):
    return_string = ""
    for ascii_sec in something:
        #print(chr(ascii_sec - 6))
        return_string = return_string + chr(ascii_sec - 6)
    return return_string

def show_database(dict_database):
    #convert it into json
    string_dict = json.dumps(dict_database)
    print(string_dict)
    
json_database = input("add database :: ")
dict_database = json.loads(json_database)

while True:
    command = input(">> ")
    if command == 'show-database':
        show_database(dict_database)
    elif command == 'update-database':
        account_name = input("enter account name :: ")
        hashed_password = hash_something(input("enter password :: "))
        dict_database[account_name] = hashed_password
    else:
        if command in dict_database:
            hashed_pass = dict_database[command]
            pyperclip.copy(undo_hash(hashed_pass))
        else:
            choice = input("there is no account named " + command + " you wanna add it? (y/n) ")
            if choice == 'y' or choice == 'Y':
                hashed_password = hash_something(input("enter password :: "))
                #print(type(dict_database), hashed_account_name, hashed_password)
                dict_database[command] = hashed_password
                print("-- cred created")
        
