	#!/usr/bin/python3
	# /opt/borg/api/chacha20helper.py
	# Parte do projeto BORG
	
	import json;
	
	from base64 import b64encode, b64decode;
	from Crypto.Cipher import ChaCha20;
	from Crypto.Random import get_random_bytes;
	
	class ChaChaHelper():
	    def __init__(self, key=None):
	        if key == None:
	            self.key = get_random_bytes(32);
	        else:
	            self.key = key;
	    def encrypt(self, message):
	        cipher = ChaCha20.new(key=self.key);
	        ciphertext = cipher.encrypt(message.encode('utf-8'));
	        nonce = b64encode(cipher.nonce).decode('utf-8')
	        ct = b64encode(ciphertext).decode('utf-8')	        result = json.dumps({'nonce':nonce, 'ciphertext':ct})
	        return result;
	    def decrypt(self, message):
	        b64 = json.loads(message);
	        nonce = b64decode(b64['nonce']);	        ciphertext = b64decode(b64['ciphertext']);
	        cipher = ChaCha20.new(key=self.key, nonce=nonce);
	        plaintext = cipher.decrypt(ciphertext);
	        return plaintext.decode("utf-8");
	
	if __name__ == "__main__":
	    c = ChaChaHelper();
	    text = "Acesse canal aiedonline no Youtube!!!";
	    encrypted = c.encrypt(text);	    decrypted = c.decrypt(encrypted);
	    print("Text: ", text);
	    print("Encripted: ", encrypted);
	    print("Decripted: ", decrypted);
