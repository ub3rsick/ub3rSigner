# ub3rSigner
**APK Signing Utility**

Usage:
```
$ python ub3rSigner.py 
.  . ,-.  ,--, ,-.   ,-.  ,  ,-. .  . ,--. ,-.  
|  | |  )   /  |  ) (   ` | /    |\ | |    |  ) 
|  | |-<   `.  |-<   `-.  | | -. | \| |-   |-<  
|  | |  )    ) |  \ .   ) | \  | |  | |    |  \ 
`--` `-'  `-'  '  '  `-'  '  `-' '  ' `--' '  ' 
                          [APK SIGNING UTILITY]
                                ~ By UB3RSiCK ~

Usage: ub3rSigner.py <APK FILE>
```

Sample Output:
```
$ python ub3rSigner.py unsigned.apk 
.  . ,-.  ,--, ,-.   ,-.  ,  ,-. .  . ,--. ,-.  
|  | |  )   /  |  ) (   ` | /    |\ | |    |  ) 
|  | |-<   `.  |-<   `-.  | | -. | \| |-   |-<  
|  | |  )    ) |  \ .   ) | \  | |  | |    |  \ 
`--` `-'  `-'  '  '  `-'  '  `-' '  ' `--' '  ' 
                          [APK SIGNING UTILITY]
                                ~ By UB3RSiCK ~

[*] APK is Unsigned
[*] Beginning APK signing
[*] Old keystore found, Removing !!
[+] Old keystore deleted
[*] Generating keystore
[+] Keystore generated successfully
[*] Signing APK [unsigned.apk]
[+] APK [unsigned.apk] signed successfully
```
If APK is already signed:
```
$ python ub3rSigner.py unsigned.apk 
.  . ,-.  ,--, ,-.   ,-.  ,  ,-. .  . ,--. ,-.  
|  | |  )   /  |  ) (   ` | /    |\ | |    |  ) 
|  | |-<   `.  |-<   `-.  | | -. | \| |-   |-<  
|  | |  )    ) |  \ .   ) | \  | |  | |    |  \ 
`--` `-'  `-'  '  '  `-'  '  `-' '  ' `--' '  ' 
                          [APK SIGNING UTILITY]
                                ~ By UB3RSiCK ~

[+] APK is already Signed
```
