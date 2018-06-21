# Taken from: https://null-byte.wonderhowto.com/how-to/download-all-pdfs-webpage-with-python-script-0163031/
# mostly made changes in order for it to work in python3, and to also download
# files of other types than only pdf.

import urllib
import os
import sys
import requests

try:
	from bs4 import BeautifulSoup
except ImportError:
	print("[*] Please download and install Beautiful Soup first!")
	sys.exit(0)

url = input("[+] Enter the url: ")
download_path = input("[+] Enter the download path in full: ")
filetype = '.' + input("[+] Specify the type of file you want to download (e.g.: pdf or ppt): ")

try:
    i = 0
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    
    
    for tag in soup.find_all('a', href=True):
        tag['href'] = urllib.parse.urljoin(url, tag['href'])
        print(tag['href'])
        
        if os.path.splitext(os.path.basename(tag['href']))[1] == filetype:
            current = urllib.request.urlopen(tag['href'])
            print("\n[*] Downloading: %s" %(os.path.basename(tag['href'])))
            
            f = open(download_path + "/" + os.path.basename(tag['href']), "wb")
            f.write(current.read())
            f.close()
            i+=1
                 

except KeyboardInterrupt:
	print("[*] Exiting...")
	sys.exit(1)

except urllib.error.URLError as e:
	print("[*] Could not get information from server!!")
	sys.exit(2)

except:
	print("Sorry, unknown error!!")
	sys.exit(3)

print("\n[*] Downloaded %d files" %(i))
