# 140810180009 Naufal Ariful Amri
# 140810180011 Alfari Sidnan
# 140810180017 Sina Mustopa

import numpy as np

key_matrix = [[0] * 2 for t in range(2)]
key_mat = [[0] * 2 for t in range(2)]
chiper_text = [[0] * 2 for t in range(2)]
plain_text = [[0] * 2 for t in range(2)]
numbertext = [[0]  for t in range(2)]
plaintext = [[0]  for t in range(2)]
chipertext = [[0]  for t in range(2)]


# Mengubah char kunci menjadi angka
def getKeyNumber(key):
	k = 0
	for i in range (2):
		for j in range(2):
			key_matrix[i][j] = ord(key[k]) - 65
			k += 1
	return key_matrix

# Mengubah char chipertext menjadi angka
def getChNumber(key):
	k = 0
	for i in range (2):
		for j in range(2):
			chiper_text[i][j] = ord(key[k]) - 65
			k += 1
	return chiper_text

# Mengubah char plaintext menjadi angka
def getPlNumber(key):
	k = 0
	for i in range (2):
		for j in range(2):
			plain_text[i][j] = ord(key[k]) - 65
			k += 1
	return plain_text

# enkripsi
def encrypt(text,key):
	for i in range(2):
		plaintext[i] = ord(text[i]) - 65
	
	#melakukan rumus dari C = K * P
	for i in range(2):
		value = 0
		for j in range(2):
			value = value + key_matrix[i][j] * plaintext[j]
		numbertext[i] = value % 26

#dekripsi
def decrypt(text,key):
	#mencari GCD dari key matrix
	temp = np.linalg.det(key_matrix) 
	a = round(temp) % 26
	b = 26    
	x,y, t1,t0 = 0,1, 1,0
	while a != 0:
		q, r = b//a , b%a
		m, n = x-t1*q , y-t0 * q
		b,a , x,y , t1,t0 = a,r ,t1,t0 , m,n
	gcd = x % 26
	

	t = np.linalg.inv(key_matrix) * temp * gcd
	tek = np.round(t)
	y = tek.astype(int) 
	
	
	for i in range(2):
		chipertext[i] = ord(text[i]) - 65
	#Melakukan rumus P = K^-1 * c
	for i in range(2):
		value = 0
		for j in range(2):
			value = value + y[i][j] * chipertext[j]
		numbertext[i] = value % 26

def keyFunction(pl,ch):
	#mengubah Chiper dan Plaintext menjadi angka
	plain = getPlNumber(pl)
	chiper = getChNumber(ch)
	
	#mencari determinan plain dan chiper
	temp = np.linalg.det(chiper) 
	temp1 = np.linalg.det(plain) 

	#mencari gcd dari chiper text
	a = round(temp) 
	b = 26    
	x,y, t1,t0 = 0,1, 1,0
	while a != 0:
		q, r = b//a , b%a
		m, n = x-t1*q , y-t0 * q
		b,a , x,y , t1,t0 = a,r ,t1,t0 , m,n
	gcd = x % 26

	#mencari plain invers dengan cara P^-1 = adj(P) * det^1(C)
	plain_invers = np.mod(np.linalg.inv(plain) * -temp1 * gcd, 26)
	keey = np.dot(plain_invers,chiper)
	y = np.round(np.mod(keey,26))

	return y.astype(int)


def hillchiper(text, key, number):
	getKeyNumber(key)
	if number == 1:
		encrypt(text,key)
		for i in range (2):
			chipertext[i] = chr(numbertext[i] + 65)
		return chipertext
	elif number == 2:
		decrypt(text,key)		
		for i in range (2):
			plaintext[i] = chr(numbertext[i] + 65)
		return plaintext
	else:
		temp = keyFunction(text,key)
		for i in range(2) :
			for j in range(2):
				key_mat[j][i] = chr(temp[i][j] + 65)
		return key_mat
			


def main():
	message = "FR"
	message1 = "FRPQ"
	pl = "FRID"
	ch = "PQCF"
	key = "HITD"
	print('\nMessage : ' , message)
	print('key : ' , key)
	
	print ('Encrypt : ' , hillchiper(message,key,1))
	
	print('\nMessage : ' , message1)
	print('key : ' , key)
	print ('Decrypt : ' , hillchiper(message1,key,2))	
	
	print('\nChiper : ' , message)
	print('Plain: ' , message1)
	print ('Key : ' , hillchiper(pl,ch,3))
	

if __name__ == "__main__":
	main()