import base64


def Encoding(Text):
    Encoded_text=Text.encode('ascii')
    print(Encoded_text)
    Encoded=base64.b64encode(Encoded_text)
    print(Encoded)
    return Encoded
    
def Decoding(Encode_code):
    Decoded=base64.b64decode(Encode_code)
    print(Decoded)
    return Decoded
    
Example="Good Morning Vieetnam!"    
Decoding(Encoding(Example))