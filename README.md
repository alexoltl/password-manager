# password-manager
manages passwords securely by encryption, will update soon.

this uses cryptography-fernet to encrypt and decrypt passwords with a .key file.
i also use colorama to make the program look nicer.


my next steps are to add a "master password" feature which will be used to unlock the files.
this is my first repo, i don't want to sound pushy but please give constructive critisism.


26/4/22: i restructured and reprogrammed the entire source code, so now the code features kinda works as intended, you need a master password to unlock all the passwords. this is perfected, but now if you put in the wrong master password, the program just crashes instead of failing to decrypt. i'm not sure why. maybe it's impossible to solve, i'm still gonna try to finish this.

30/4/22: i think it's impossible to fix, fernet self checks if it's correct beforehand so that's my release for now.
