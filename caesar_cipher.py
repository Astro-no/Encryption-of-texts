# caesar_cipher.py
#
# Program Description
# program that encodes / decodes messages by a key value which shifts each letter in the message up / down in the alphabet
#
# Algorithm (pseudocode)
# 1. Create an alphabet list
# 2. Ask the user whether they want to enocde or decode
# 3. Create an encode and a decode function
# 4. For the encode / decode function, ask for the message to encode / decode and then the key value
# 5. Create a loop that checks the position of the letter in the alphabet and adds/subtracts the keyvalue to the position
# 6. Next create a loop that changes the list into a string so it prints like abc instead of [a,b,c]
# 7. Print the original message, encoded / decoded message, and the key value to the user


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Main function that runs either the encode function or the decode function
def main():
	start = input('\nEnter "e" to encode and "d" to decode: ')
	if start == 'e':
		encodefunction()
	if start == 'd':
		decodefunction()


# Function to enocde a message
def encodefunction():
# Prompts to get the message and the key value
	message = str(input('\nEnter the message to encode: ')).lower()
	keyvalue = int(input('\nEnter the key value: '))
# Getting the length of the message for the loops, and setting positions/encoded to empty lists
	mlength = len(message)
	encoded = []
# Loop that finds the positions of all the letters in the message the user entered, and adds them to the list encoded
	for i in range(mlength):
		letter = message[i]
		position = alphabet.index(letter)+keyvalue
		encoded.insert(i, alphabet[position%26])
# Loops that both basically convert the lists to strings in order to print without having list format so [a,b,c] -> abc
	encodedmessage = ''
	for i in range(mlength):
		encodedmessage += encoded[i]
	originalmessage = ''
	for i in range(mlength):
		originalmessage += message[i]
# Final output, that tells the user their entered message, the message that is encoded, and their entered key value
	print('\nOriginal Message:',originalmessage,'\nEncoded Message:',encodedmessage,'\n**Key Value**:',keyvalue)


# Function to decode a message
def decodefunction():
# Prompts to get the message and the key value
	message = str(input('\nEnter the message to decode: ')).lower()
	keyvalue = int(input('\nEnter the key value: '))
# Getting the length of the message for the loops, and setting decoded to an empty list
	mlength = len(message)
	decoded = []
# Loop that finds the positions of all the letters in the message the user entered, and adds them to the list decoded
	for i in range(mlength):
		letter = message[i]
		position = alphabet.index(letter)-keyvalue
		decoded.insert(i, alphabet[position])
# Loops that both basically convert the lists to strings in order to print without having list format so [a,b,c] -> abc
	decodedmessage = ''
	for i in range(mlength):
		decodedmessage += decoded[i]
	originalmessage = ''
	for i in range(mlength):
		originalmessage += message[i]
# Final output, that tells the user their entered message, the message that is decoded, and their entered key value
	print('\nOriginal Message:',originalmessage,'\nDecoded Message:',decodedmessage,'\n**Key Value**:',keyvalue)
main()