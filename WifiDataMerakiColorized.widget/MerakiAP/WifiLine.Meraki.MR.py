######################## Meraki MR script to display Connectivity Data  ############################################
######################## By Alex Burger ############################################################################
######################## 12-01-2018 ################################################################################
import re
import urllib.request
import ast
import json

APNameStart = "AP Name:<strong>"
FieldEnd = "</strong>|"
APIPStart = "AP IP:<strong>"
APModelStart = "AP Model:<strong>"
SNRGoodStart = "SNR at AP:<strong><font color=lightgreen>"
SNROKStart = "SNR at AP:<strong><font color='yellow'>"
SNRBadStart = "SNR at AP:<strong><font color='red'>"
SNREnd = "</font></strong>|"
APNetworkStart = "Meraki Network:<strong>"
EndLine = "</strong>"

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
                        print (APNameStart, MerakiAP, FieldEnd, APIPStart, MerakiAPIP, FieldEnd, APModelStart, MerakiModel, FieldEnd,  SNRGoodStart, SignaldB,"dB",SNREnd, APNetworkStart, MerakiNetwork, EndLine)
                elif '19' <= SignaldB < '29':
                        print (APNameStart, MerakiAP, FieldEnd, APIPStart, MerakiAPIP, FieldEnd, APModelStart, MerakiModel, FieldEnd,  SNROKStart, SignaldB,"dB",SNREnd, APNetworkStart, MerakiNetwork, EndLine)
                else:
                        print (APNameStart, MerakiAP, FieldEnd, APIPStart, MerakiAPIP, FieldEnd, APModelStart, MerakiModel, FieldEnd,  SNRBadStart, SignaldB,"dB",SNREnd, APNetworkStart, MerakiNetwork, EndLine)
        else:
                print("Not Connected to an MR")
except:
        print ("Not Connected to an MR")
####################################################################################################################
