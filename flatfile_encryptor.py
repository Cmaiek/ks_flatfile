import hashlib

accno = '37114020040000310277554478'
nip = '5361798973'
date = '20210908'

hash_input = date + nip + accno

def obtain_sha512(input):
	hash = hashlib.sha512(str( input ).encode("utf-8")).hexdigest()
	return hash	

for x in range(5000):
	result = obtain_sha512(hash_input)
	hash_input = result
	print(x, result)
	
	