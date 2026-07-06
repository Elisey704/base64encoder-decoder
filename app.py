import base64




def Encode(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    print(encoded_bytes)

def decode(text):
    decoded_bytes = base64.b64decode(str(text))
    decoded_string = decoded_bytes.decode('utf-8')
    print(decoded_string)



if input() == 'encode':
    print('Введите текст')
    text = input()
    Encode(text)
elif input() == 'decode':
    print('Введите код base64')
    text = input()
    decode(text)

