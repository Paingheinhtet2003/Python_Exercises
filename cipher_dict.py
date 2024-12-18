cipher_dict = {
    'a':'i', 'b':'h', 'c':'r', 'd':'k', 'e':'g', 'f':'w', 'g':'y', 'h':'v', 'i':'b',
    'j':'f', 'k':'p', 'l':'l', 'm':'n', 'n':'q', 'o':'o', 'p':'t', 'q':'j', 'r':'u',
    's':'x', 't':'s', 'u':'m', 'v':'z', 'w':'d', 'x':'e', 'y':'a', 'z':'c'
}

encrypted = "roloux ow svg dbqk"

decoded = ""

for char in encrypted:
    if char in cipher_dict:
        decoded += cipher_dict[char]
    else:
        decoded += char

print("Decoded Message: ", decoded)
