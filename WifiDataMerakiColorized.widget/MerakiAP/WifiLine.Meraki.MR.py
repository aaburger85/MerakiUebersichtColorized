######################## Meraki MR script to display Connectivity Data  ############################################
######################## By Alex Burger ############################################################################
######################## 12-01-2018 ################################################################################
import urllib.request
import json

status = ('lightgreen', 'yellow', 'red')

def printData(MerakiAP,MerakiAPIP,MerakiModel,status,SignaldB,MerakiNetwork):
        print("AP Name:<strong> %s </strong>| AP IP:<strong> %s </strong>| AP Model:<strong> %s </strong>| SNR at AP:<strong><font color=%s> %s dB </font></strong>| Meraki Network:<strong> %s </strong>" 
        % (MerakiAP,MerakiAPIP,MerakiModel,status,SignaldB,MerakiNetwork))

########################### Meraki AP Detection and Info ###########################################################
try:  
        apresp = urllib.request.urlopen('http://ap.meraki.com/index.json').read()
        merakiapjson = json.loads(apresp)
        if 'error' not in merakiapjson:
                SignaldB = merakiapjson['client']['rssi']
                MerakiNetwork = merakiapjson['config']['network_name']
                MerakiAP = merakiapjson['config']['node_name']
                MerakiModel = merakiapjson['config']['product_model']
                
                try:
                        MerakiAPIP = merakiapjson['connection_state']['wired_ip']
                except:
                        MerakiAPIP = "No IP(Mesh)"
                if SignaldB >= '29':
                        printData(MerakiAP,MerakiAPIP,MerakiModel,status[0],SignaldB,MerakiNetwork)
                elif '19' <= SignaldB < '29':
                        printData(MerakiAP,MerakiAPIP,MerakiModel,status[1],SignaldB,MerakiNetwork)
                else:
                        printData(MerakiAP,MerakiAPIP,MerakiModel,status[2],SignaldB,MerakiNetwork)
        else:
                print("Not Connected to an MR")
except:
        print ("Not Connected to an MR")
####################################################################################################################
