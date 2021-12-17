import hashlib
import secrets
import base64
import json

password = "Okta1234!"

salt = secrets.token_bytes(16)
print("\nThe salt that will be use presented as bytes-like object is : " + str(salt) + "\n")

salted_password =  salt + bytes(password, "utf-8")
hashed = hashlib.sha1(salted_password)
result = {
    "algorithm": "SHA-1",
    "salt": base64.b64encode(salt).decode("ascii"),
    "saltOrder": "PREFIX",
    "value": base64.b64encode(hashed.digest()).decode("ascii"),
}
print(json.dumps(result, indent=4))


    