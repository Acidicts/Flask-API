import requests

ltn = {
    'z': 0,  # Added mapping for 'z'
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
}

print('Welcome to the API Client!')
print('Hello, Help, Bye')
inp = input('What Method should we use?')

url = 'http://127.0.0.1:5000/api?code={}'.format(inp.lower())

response = requests.post(url)
try:
    rep = dict(response.json())
    print(rep['message'])
except requests.exceptions.JSONDecodeError:
    resp = str(response.text)
    print(resp)
    oup = ''
    for letter in resp:
        if letter in ltn:
            oup += str(ltn[letter])
        else:
            oup += letter

    print(oup)