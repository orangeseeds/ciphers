# this is a program that can either encrypt or decrypt a message using caeser cipher.
# "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."


def encrypt(message, key=0):
    cypher_text = ""
    for char in message:
        if char in SYMBOLS:
            cypher_index = SYMBOLS.find(char)+key
            if cypher_index >= len(SYMBOLS):
                cypher_index = cypher_index % len(SYMBOLS)
            elif cypher_index < 0:
                cypher_text = len(SYMBOLS) - cypher_text

            cypher_text = cypher_text + SYMBOLS[cypher_index]
        else:
            cypher_text = cypher_text + char
    return (cypher_text)


def decrypt(message, key=0):
    plain_text = ''
    for char in message:
        if char in SYMBOLS:
            plain_index = SYMBOLS.find(char) - key
            if plain_index >= len(SYMBOLS):
                plain_index = plain_index % len(SYMBOLS)
            elif plain_index < 0:
                plain_index = len(SYMBOLS) + plain_index
            plain_text = plain_text + SYMBOLS[plain_index]
        else:
            plain_text = plain_text + char
    return (plain_text)


def decode_force(message):
    key = 0
    while key < len(SYMBOLS):
        plain_text = ''
        for char in message:
            if char in SYMBOLS:
                plain_index = SYMBOLS.find(char) - key

                while plain_index >= len(SYMBOLS):
                    plain_index = plain_index % len(SYMBOLS)

                if plain_index < 0:
                    plain_index = len(SYMBOLS) + plain_index

                plain_text = plain_text + SYMBOLS[plain_index]

            else:
                plain_text = plain_text + char
        print(f"#key {key}: {plain_text}")
        key = key + 1

# string = "This is a support message"
# print(f"This is the encoded message:\n{encode(string, 1)}\n")
# # print(f"This is the decoded message:\n{decode(encode(string, 1),1)}")
# decode_force(encode(string, 1))
