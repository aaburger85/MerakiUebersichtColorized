######################## Meraki MS script to display Connectivity Data  ############################################
######################## By Alex Burger ############################################################################
######################## 12-01-2018 ################################################################################
import re
import urllib.request
import ast
import json
################################# Meraki Switch Detection and Info ###################################################
try:
        switchresp = urllib.request.urlopen('http://switch.meraki.com/index.json').read()
        merakiswitchjson = json.loads(switchresp)
        if 'error' not in merakiswitchjson:
                SwitchName = merakiswitchjson['config']['node_name']
                SwitchModel = merakiswitchjson['config']['product_model']
                SwitchIP = merakiswitchjson['connection_state']['wired_ip']
                #SwitchMaster = merakiswitchjson['stack_info']['master']
                SwitchVLAN = merakiswitchjson['client']['vlan']
                SwitchPort = merakiswitchjson['client']['port']
                print( "Switch Name: <strong>", SwitchName, "</strong>|", "Switch IP:<strong>", SwitchIP, "</strong>|", "Switch Model:<strong>", SwitchModel, "</strong>|", "Port:<strong>", SwitchPort, "</strong>|", "VLAN:<strong>", SwitchVLAN, "</strong>")
        else:
                print("Not Connected to an MS")
except:
        print ("Not Connected to an MS")
####################################################################################################################
