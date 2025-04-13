file_name = "user_list.txt"
credentials = {}

def auth(uname, pword):
    """ read the file, use the file provided to check the user name and password and return a string """
    with open(file_name) as ul:
        for line in ul:
            usr, pwd = line.rstrip().split(" : ")
            credentials[usr] = pwd
    ul.close()

    # If the user name and password are correct, return the string “success”
    if credentials[uname] == pword:
        return 'success'
    # If the user name is correct but the password is not, return the string “bad pass”
    elif credentials[uname] != pword:
        return 'bad pass'
    # If the user name is bad, return the string “no user”
    elif uname not in credentials.keys():
        return 'no user'

    # could have done a try catch block as shown in class
    # try:
    #     if credentials[uname] == pword:
    #         return 'success'
    #     return 'bad pass'
    # except KeyError:
    #     return 'no user'


def add_user(uname, pword):
    """ add (append) username and password to the file """
    with open(file_name, 'a') as ul:
        ul.write(f"\n{uname} : {pword}")
    ul.close()