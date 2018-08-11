#!/usr/bin/env python

import os
import sys
import glob
import shlex
import subprocess

def printBanner():
	banner = ("LiAgLiAsLS4gICwtLSwgLC0uICAgLC0uICAsICAsLS4gLiAgLiAsLS0uICwtLiAgCnwgIHwgfC"
		 "AgKSAgIC8gIHwgICkgKCAgIGAgfCAvICAgIHxcIHwgfCAgICB8ICApIAp8ICB8IHwtPCAgIGAu"
		 "ICB8LTwgICBgLS4gIHwgfCAtLiB8IFx8IHwtICAgfC08ICAKfCAgfCB8ICApICAgICkgfCAgXC"
		 "AuICAgKSB8IFwgIHwgfCAgfCB8ICAgIHwgIFwgCmAtLWAgYC0nICBgLScgICcgICcgIGAtJyAg"
		 "JyAgYC0nICcgICcgYC0tJyAnICAnIAogICAgICAgICAgICAgICAgICAgICAgICAgIFtBUEsgU0"
		 "lHTklORyBVVElMSVRZXQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH4gQnkgVUIz"
		 "UlNpQ0sgfgo=")
	print banner.decode('base64', 'strict')

def isSigned():
	VRFY_JAR = "jarsigner -verify %s" % sys.argv[1]
	vrfy_out = subprocess.check_output(VRFY_JAR, shell=True)
	if not "jar is unsigned" in vrfy_out:
		print "[+] APK is already Signed"
		return True
	else:
		print "[*] APK is Unsigned\n[*] Beginning APK signing" 
		return False

def main():

	printBanner()

	if not len(sys.argv) == 2:
        	print "Usage: %s <APK FILE>\n" % sys.argv[0]
        	sys.exit()

	if isSigned():
		sys.exit()	

	KEYGEN_CMD = \
	("keytool -genkey -noprompt "
 	"-alias UB3RK3Y "
	"-keyalg RSA -keysize 1024 "
	"-sigalg SHA1withRSA -validity 10000 "
 	"-dname 'CN=dude.ub3rsick.com, OU=ID, O=UB3R, L=Home, S=BLAH, C=IN' "
 	"-keystore ub3r.keystore "
 	"-storepass ub3rpass "
 	"-keypass ub3rpass")


	SIGN_APK = \
	("jarsigner -keystore ub3r.keystore %s "
	"-sigalg SHA1withRSA "
  	"-storepass ub3rpass "
  	"-keypass ub3rpass "
	"-digestalg SHA1 UB3RK3Y") % sys.argv[1]

	# remove old keystore if present
	rm_kystr = "rm %s"
	old_key = glob.glob("ub3r.keystore")
	if not len(old_key) == 0:
		print "[*] Old keystore found, Removing !!"
		retCode = subprocess.call(shlex.split(rm_kystr % old_key[0]), stdout=subprocess.PIPE)
	        if retCode == 0:
        	        print "[+] Old keystore deleted"
       		else:
                	print "[-] Unable to delete old keystore"
			sys.exit()
		

	print "[*] Generating keystore"
	retCode = subprocess.call(shlex.split(KEYGEN_CMD), stdout=subprocess.PIPE) # Not safe; os pipe may get filled
	if retCode == 0:
		print "[+] Keystore generated successfully"
	else:
		print "[-] Unable to generate keystore"
		sys.exit()

	print "[*] Signing APK [%s]" % sys.argv[1]
	retCode = subprocess.call(shlex.split(SIGN_APK), stdout=subprocess.PIPE)
        if retCode == 0:
                print "[+] APK [%s] signed successfully" % sys.argv[1]
        else:
                print "[-] Error while signing APK"
                sys.exit()

if __name__ == "__main__":
	main()
