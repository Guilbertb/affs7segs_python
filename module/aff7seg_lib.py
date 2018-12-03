import socket,os,time


#adresse de l'afficheur en localhost
UDP_IP = "127.0.0.1"
UDP_PORT = 8585  #port de l'afficheur
adress= ('127.0.0.1' , 8585)

def pipo():
    return 0

def init_aff7seg(nb_segments):
    # nb_segments doit etre entre 1 et 9
    if  nb_segments<=0:
        nb_segments=1
        
    if  nb_segments>9:
        nb_segments=9
    # appel de l'afficheur     
    os.system('pkill Aff7seg')
    os.system('./aff7seg/Aff7seg &')
    time.sleep(1) #le temps de lancer le proces
    #adresse de l'afficheur en localhost
#    UDP_IP = "127.0.0.1"
#    UDP_PORT = 8585  #port de l'afficheur
    #MESSAGE1 = "AFF7SEG;DIGIT;0;255\n"
    MESSAGE2 = 'AFF7SEG;NB_DIGITS;9\n'
    chaine=list(MESSAGE2)
    chaine[18]=chr(48+nb_segments)
    MESSAGE2="".join(chaine)
    MESSAGE2= str.encode(MESSAGE2)
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE2, adress)
    #sock.sendto(MESSAGE1, (UDP_IP,UDP_PORT))
    return

def afficheur7s(nb_aff,octet_aff):
    #MESSAGE1 = "AFF7SEG;DIGIT;0;255\n"
    MESSAGE1 = 'AFF7SEG;DIGIT;'
    MESSAGE1 = MESSAGE1+format(nb_aff)+";"+format(octet_aff)+"\n"
    MESSAGE1= str.encode(MESSAGE1)
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE1, (UDP_IP,UDP_PORT))
    return


