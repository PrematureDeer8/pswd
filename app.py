import string
import random
password = string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase))];
while(True):
	pswd = input("What is the password: ");
	if(pswd == password):
		print("Correct password");
		break;
	else:
		print("Incorrect password");
