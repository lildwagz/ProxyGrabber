#!/usr/bin/env python
import re, sys, os
from time import sleep, ctime
import urllib

baca=''

if os.name in ['nt', 'win32']:
        os.system('cls')
else:
        os.system('clear')
print '''
______                      _____           _     _               
| ___ \                    |  __ \         | |   | |              
| |_/ / __ _____  ___   _  | |  \/_ __ __ _| |__ | |__   ___ _ __ 
|  __/ '__/ _ \ \/ / | | | | | __| '__/ _` | '_ \| '_ \ / _ \ '__|
| |  | | | (_) >  <| |_| | | |_\ \ | | (_| | |_) | |_) |  __/ |   
\_|  |_|  \___/_/\_\\__, |  \____/_|  \__,_|_.__/|_.__/ \___|_|   
                     __/ |                                        
                    |___/   Coder : lildwagz                                      

    '''
    
#Pilihan
print '[1] Fresh Proxy'
print '[2] Random proxy'
print '[3] Random Proxy2'
print '[4] Random Proxy3'+'\n------------------'
pilihan = raw_input('[+] Enter your choice : ')

print '[+] Try Connecting ...'
try:
    if pilihan=='1':
        url=urllib.urlopen('http://nntime.com/').read()
    elif pilihan == '2':
        url=urllib.urlopen('http://nntime.com/proxy-list-01.htm').read()
    elif pilihan=='3':
        url=urllib.urlopen('http://nntime.com/proxy-list-02.htm').read()
    elif pilihan=='4':
        url=urllib.urlopen('http://nntime.com/proxy-list-03.htm').read()
except:
    print '[*] Failed to connect !'
    sys.exit('[*] Check your internet connection !')

#salin halaman
for isi in url:
        baca+=isi    
print '[+] Connected !'
sleep(2)
print '[+] Fresh Proxy List !! Enjoy it !!'

# cari judul
#cari_judul = re.findall(r'>\w.*</a></th>',baca)
#judul=[]
#for i in cari_judul:
#    judul.append(i[1:-9])
print '-----------------------------------------------------------------------------------'
print 'IP Address\t\t Anonimity\t Updated\t Registered To'
print '-----------------------------------------------------------------------------------'

#cari IP Address & Port
cari_IP = re.findall(r'td>\d+\.\d+\.\d+\.\d+<',baca)
ip=[]
for i in cari_IP:
    ip.append(i[3:-1])
cari_port = re.findall(r'value="\d*.\d*\.\d*\.\d*" onclick',baca)
port=[]
pan=[]
j=0
cari_pan = re.findall(r'":".*\)',baca)
for i in cari_pan:
    pan.append(i[3:-1])
    
for i in cari_port:
    batas = -9 - len(pan[j])/2
    port.append(i[batas:-9])
    j+=1

#cari tipe proxy
cari_tipe=re.findall(r'<td>\w+\W\w+</td>|<td>\w+\s</td>',baca)
tipe=[]
n=0
for i in cari_tipe:
    if i[4:-5]=='transparent proxy':
        i='transparent '
        tipe.append(i)
    else:
        tipe.append(i[4:-5])
    
#cari update
cari_update = re.findall(r'GMT">.*</dfn>',baca)
update=[]
for i in cari_update:
    update.append(i[5:-6])

#cari org
cari_org = re.findall(r'organization">.*</td>',baca)
org=[]
for i in cari_org:
    org.append(i[14:-5])

try:
    for rr in range(0,(len(ip)-1)):
        print ip[rr]+':'+ port[rr] + '\t|' + tipe[rr] + '\t|' + update[rr] + '\t|' + org[rr]
        sleep(2)
except KeyboardInterrupt:
    print '\n[+] Menghentikan proses !'
    sleep(1)
    sys.exit(1)

#cari tanggal update
#tanggal=re.search(r'Updated \w+.*Total',baca)
#tanggal=tanggal.group()
print '-----------------------------------------------------------------------------------'
#print tanggal[:-5]
print 'Thanks for using this tool'
print '-----------------------------------------------------------------------------------'