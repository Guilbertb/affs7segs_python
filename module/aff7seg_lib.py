import socket,os,time


#adresse de l'afficheur en localhost
UDP_IP = "127.0.0.1"
UDP_PORT = 8585  #port de l'afficheur

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
    MESSAGE2 = "AFF7SEG;NB_DIGITS;9\n"
    chaine=list(MESSAGE2)
    chaine[18]=chr(48+nb_segments)
    MESSAGE2="".join(chaine)

    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE2, (UDP_IP, UDP_PORT))
    #sock.sendto(MESSAGE1, (UDP_IP,UDP_PORT))
    return

def afficheur7s(nb_aff,octet_aff):
    #MESSAGE1 = "AFF7SEG;DIGIT;0;255\n"
    MESSAGE1 = "AFF7SEG;DIGIT;"
    MESSAGE1 = MESSAGE1+format(nb_aff)+";"+format(octet_aff)+"\n"
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE1, (UDP_IP,UDP_PORT))
    return


