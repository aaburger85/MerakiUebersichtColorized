######################## Meraki MX script to display Connectivity Data  ############################################
######################## By Alex Burger ############################################################################
######################## 12-01-2018 ################################################################################
import urllib.request
import json

############################# Meraki Firewall Detection and Info ####################################################
try:
        firewallresp = urllib.request.urlopen('http://wired.meraki.com/index.json').read()
        merakifirewalljson = json.loads(firewallresp)
        if 'error' not in merakifirewalljson:
                FirewallName = merakifirewalljson['config']['node_name']
                FirewallModel = merakifirewalljson['config']['product_model']
                FirewallIP = merakifirewalljson['connection_state']['wired_ip']
                print("Firewall Name:<strong>", FirewallName, "</strong>|", "Firewall IP:<strong>", FirewallIP, "</strong>|", "FW Model:<strong>", FirewallModel, "</strong>")
        else:
                print("Not Connected to an MX")
except:
        print ("Not Connected to an MX")
####################################################################################################################
