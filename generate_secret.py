import secrets 
import string 






def generate_key():
    secret_key_hex = secrets.token_hex(32)
    print("Your'e Secret Token Hex Key: ", secret_key_hex)


print("Check")

generate_key()















