#!/usr/bin/env python3

'''
Written by: Eric Samuel Huddleston
Course: CS-4663 Section 001
Date: 09/18/2020
Written with python3
'''

    # creating string variables to hold the message and the key
key = ""
msg = ""
 
# here we ask user to enter a message from stdin
msg = input("Enter your message: ")

# here we ask user to enter a key from stdin
key = input("Enter your key: ")

# get the size of the message
size_of_msg = len(msg)

# here we store size of the key
size_of_key = len(key)

# here we create an empty list
tempr = ""

# here we create counter variable for the loop 
j = 0
# Now we store the key into 'msg' sized temp. array for the encrypted message
# loop through the 'msg' string
for i in range(size_of_msg):

	# swap values of the temp. and 'key' arrays.
	tempr += key[j]

	# increment 'j' counter variable
	j += 1

	# j must be within the length/size of 'key'
	if( j>=size_of_key ):
		# set j back to 0
		j = 0


# here we print out the encrypted message....
print("\nEncrypted message: ", end="")

# for each character in the 'msg' array
for i in range(size_of_msg):

	# here we get the total... mod by 255 since we must 
    # also show each character in ASCII code. 8-bit ASCII system has 0 - 255 
    # code points.
	t = (ord(msg[i]) + ord(tempr[i])) % 255

	# print...
	print("-", end = "")
	print(t, end = "")

# change the current line
print()

# Now we convert 'msg' into cypher text
print("\n\nEncrypted string: ", end="")
for i in range(size_of_msg):

	# here get the character... mod by the number of total ascii characters,
    # including the extended ascii chars. 128 - 255.
	c = chr((ord(msg[i]) + ord(tempr[i])) % 255)

	# print
	print(c, end = "")

# change the current line
print()

# here we convert 'msg' into cypher text, we simply shift over every letter in
# the string by the amount of the key which is also modded by 255 since we must 
# also show each character in ASCII code. 8-bit ASCII system has 0 - 255 code points.

# Now we prompt the user that stdout will display the deciphered text...
print("\n\nDecrypted string: ", end = "")

# here we store the ciphered message
ciphered = ""

# here we get the ciphered message mod by the number of total ascii characters,
# including the extended ascii chars. 128 - 255.
for i in range(size_of_msg):
	ciphered += chr((ord(msg[i]) + ord(tempr[i])) % 255)

# here we store the deciphered message as string
deciphered = ""

# here we get the deciphered message, size cannot exceed the size of user-
# inputed message
for i in range(size_of_msg):
	deciphered += chr((ord(ciphered[i]) - ord(tempr[i])) % 255)

#finally we print the deciphered string...
print(deciphered)
    
#run with python3 caesarcipher.py. Or chmod +x caesarcipher.py then 
#./caesarcipher.py
