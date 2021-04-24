import bcrypt

def gen_password_hash(password: str)-> bytes:
    password_bytes = password.encode("utf-8")
    pass_salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password=password_bytes, salt=pass_salt)
    return hashed_pass

def check_pass(password: str, pass_hash: bytes) -> bool:
    password_bytes = password.encode('utf-8')
    pass_check = bcrypt.checkpw(password_bytes, pass_hash)
    return pass_check

if __name__ == "__main__":
    print("Check Hashed Passwords Here")
    password = input("Enter a Password to hash : ")
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    pass_hash = bcrypt.hashpw(password_bytes, salt)
    print("Password's Hash is", pass_hash)
    print("Enter Another Password to check if the earlier one is same as this one")
    new_pass = input("New Password : ")
    new_pass_bytes = new_pass.encode('utf-8')
    new_pass_hash = bcrypt.hashpw(new_pass_bytes, salt)
    print("New Password's hash is", new_pass_hash)
    print("Checking if both passwords are same without equating them. This uses bcrypt to do the same")
    if bcrypt.checkpw(new_pass_hash, pass_hash):
        print("Password matches")
    else:
        print("Password does not match")

