
#!/usr/bin/env python3
# I suspect that I haven't got to grips with the way phthon does things, but soppusely this will setup the path to allod for the sonnen batteri moduel to be in a separate location
# To me having to do this for testing seems a horrendous hack
import asyncio
import os
import sys
import time
import json
import sys
import base64, binascii, hashlib, hmac, string
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")
from pprint import pprint
import hashlib

# this is based on the test code by rust dust

def main():
    challenge="39bdd8a304b84c76"
    username="User"
    password="sonnenUser3552!"
    salt="04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb_02bbe1e15021947b232050cc88b07772"
    testResponse=create_response_from_values(username,password,challenge,salt)
    wantedResponse="39b5cb8cc21772b482cdbbcbd135f4a05af4974f3e1b9e4c8aa846d6e64bcc1a"


    if testResponse==wantedResponse:
        print("It works!")
    else:
        print("doesnt work :(")
    
    print("Response: "+testResponse)


def create_response_from_values(username, password, challenge, salt):
    pw_sha512_hex = hashlib.sha512(password.encode("utf-8")).hexdigest()
    pw_bytes = pw_sha512_hex.encode("utf-8")
    dk = hashlib.pbkdf2_hmac("sha512", pw_bytes, salt.encode("utf-8"), 7500, dklen=64)
    derived_hex = dk.hex()
    key = derived_hex.encode("utf-8")
    response = hmac.new(key, challenge.encode("utf-8"), hashlib.sha256).hexdigest()
    return response


if __name__ == '__main__':
  main()
