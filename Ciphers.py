import base64
import subprocess
subprocess.call(['pip', 'install', 'rsa'])
import rsa
import string
import random

def caesar_cipher(message, shift):
    all_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    encrypted_message = ''
    for char in message:
        if char == ' ':
            encrypted_message += char
        elif char in all_characters:
            char_index = all_characters.find(char)
            shifted_index = (char_index + shift) % len(all_characters)
            encrypted_message += all_characters[shifted_index]
        else:
            encrypted_message += char
    return encrypted_message

def vigenere_cipher(message, key, decrypt=False):
    all_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    result_message = ''
    key_index = 0
    for char in message:
        if char == ' ':
            result_message += char
        elif char in all_characters:
            char_index = all_characters.find(char)
            key_char_index = all_characters.find(key[key_index % len(key)])
            if decrypt:
                shifted_index = (char_index - key_char_index) % len(all_characters)
            else:
                shifted_index = (char_index + key_char_index) % len(all_characters)
            result_message += all_characters[shifted_index]
            key_index += 1
        else:
            result_message += char
    return result_message

def encrypt_decrypt_rsa(message, public_key, private_key):
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
    return encrypted_message, decrypted_message

def generate_rsa_key_pair():
    # Generate RSA key pair
    pub_key, priv_key = rsa.newkeys(2048)
    # Convert keys to PEM format
    pub_key_pem = pub_key.save_pkcs1().decode()
    priv_key_pem = priv_key.save_pkcs1().decode()
    return pub_key, priv_key, pub_key_pem, priv_key_pem

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', 
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def encrypt_to_morse(message):
    morse_code = ''
    for char in message:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + ' '
        else:
            morse_code += ' '  # Add space for unrecognized characters
    return morse_code.strip()

def decrypt_from_morse(morse_code):
    message = ''
    morse_dict = {morse: char for char, morse in morse_code_dict.items()}
    for code in morse_code.split():
        if code in morse_dict:
            message += morse_dict[code]
        else:
            message += ' '  # Add space for unrecognized codes
    return message

print(' WELCOME TO Ciphers.py')
print('***********************')
print('\nHello user, this program will encrypt and decrypt messages using various ciphers.\nThe ciphers available in the program are mentioned below,')
print('''\n1. Caesar Cipher: This cipher shifts each letter by a fixed number of places. 
                              The number of places is determined by the user.''')
print('''\n2. Vigenere Cipher: This cipher uses a key to shift each letter in the message. 
                                The key is a string of letters either determined by the user or generated randomly.''')
print('''\n3. RSA Algorithm: This cipher uses the RSA algorithm to encrypt and decrypt messages. 
                                The key is a pair of public and private keys given by the user or randomly generated.''')
print('''\n4. Morse Code: This cipher uses the Morse Code to encrypt and decrypt messages.
                                The message is encrypted in the form of dots and dashes.''')

while True:
  print('''\nEnter the serial number of the cipher to select it: 
              1. Caesar Cipher
              2. Vigenere Cipher
              3. RSA Algorithm
              4. Morse Code
              Press enter to exit''')
  cipher = input()

  
  if cipher == '1':
      while True:
          print('\nWelcome to Caesar Cipher\n')
          print('Choose the following options:\n1. Encrypt\n2. Decrypt\nPress Enter to exit')
          choice = input()
          if choice == '1':
              print('\nEnter the message to encrypt: ')
              message = input()
              print('\nEnter the shift value: ')
              shift = int(input())
              encrypted_message = caesar_cipher(message, shift)
              print('\nThe encrypted message is: ' + encrypted_message)
          elif choice == '2':
              print('\nEnter the message to decrypt: ')
              message = input()
              print('\nEnter the shift value: ')
              shift = int(input())
              decrypted_message = caesar_cipher(message, -shift)
              print('\nThe decrypted message is: ' + decrypted_message)
          else:
              break
          
          print('\nDo you want to encrypt/decrypt again? (y/n)')
          cont = input()
          if cont == 'y':
              continue
          else:
              break
  elif cipher == '2':
      while True:
          print('\nWelcome to Vigenere Cipher\n')
          print('Choose the following options:\n1. Encrypt\n2. Decrypt\nPress Enter to exit')
          choice = input()
          if choice == '1':
              print('\nEnter the message to encrypt: ')
              message = input()
              key=''
              print('\nEnter 1 to randomly generate key\nPress Enter to enter your own key')
              if input() == '1':
                  print('Enter the length of the key:')
                  length = int(input())
                  key = ''.join(random.choice(string.ascii_letters) for _ in range(length))
                  print('\nThe randomly generated key is: ' + key)
              else:
                  print('\nEnter the key: ')
                  key = input()
              encrypted_message = vigenere_cipher(message, key)
              print('\nThe encrypted message is: ' + encrypted_message)
          elif choice == '2':
              print('\nEnter the message to decrypt: ')
              message = input()
              print('\nEnter the key: ')
              key = input()
              decrypted_message = vigenere_cipher(message, key, decrypt=True)
              print('\nThe decrypted message is: ' + decrypted_message)
          else:
              break

          print('\nDo you want to encrypt/decrypt again? (y/n)')
          cont = input()
          if cont == 'y':
              continue
          else:
              break
  elif cipher == '3':
      while True:
          print('Choose the following options:\n1. Generate Key Pair\n2. Encrypt\n3. Decrypt\nPress Enter to exit')
          choice = input()
          if choice == '1':
            pub_key, priv_key, pub_key_pem, priv_key_pem = generate_rsa_key_pair()
            print('Public Key (PEM):\n', pub_key_pem)
            print('Private Key (PEM):\n', priv_key_pem)
            print('The key pair has been generated successfully.')
                
          elif choice == '2':
            print('Enter the message to encrypt: ')
            message = input()
            print('Enter the public key (PEM format): ')
            pub_key_str = input()
            pub_key = rsa.PublicKey.load_pkcs1(pub_key_str.encode())
            print('Enter the private key (PEM format): ')
            priv_key_str = input()
            priv_key = rsa.PrivateKey.load_pkcs1(priv_key_str.encode())
            encrypted_message = encrypt_decrypt_rsa(message, pub_key, priv_key)
            print('The encrypted message is:', encrypted_message)

          elif choice == '3':
              print('Enter the message to decrypt: ')
              message = input()
              print('Enter the public key (PEM format): ')
              pub_key_str = input()
              pub_key = rsa.PublicKey.load_pkcs1(pub_key_str.encode())
              print('Enter the private key (PEM format): ')
              priv_key_str = input()
              priv_key = rsa.PrivateKey.load_pkcs1(priv_key_str.encode())
              decrypted_message = encrypt_decrypt_rsa(message, pub_key, priv_key)
              print('The decrypted message is:', decrypted_message)
          else:
              break    
          print('\nDo you want to encrypt/decrypt again? (y/n)')
          cont = input()
          if cont == 'y':
              continue
          else:
              break
  elif cipher == '4':
      while True:
          print('\nWelcome to Morse Code\n')
          print('Choose the following options:\n1. Encrypt\n2. Decrypt\nPress Enter to exit')
          choice = input()
          if choice == '1':
              print('\nEnter the message to encrypt: ')
              message = input()
              encrypted_message = encrypt_to_morse(message)
              print('\nThe encrypted message is: ' + encrypted_message)
          elif choice == '2':
              print('\nEnter the message to decrypt: ')
              message = input()
              decrypted_message = decrypt_from_morse(message)
              print('\nThe decrypted message is: ' + decrypted_message)
          else:
              break
          print('\nDo you want to encrypt/decrypt again? (y/n)')
          cont = input()
          if cont == 'y':
              continue
          else:
              break
  else:
      break



    