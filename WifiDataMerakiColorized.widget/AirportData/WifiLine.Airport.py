######################## Airport subprocess script to display Wifi Data ############################################
######################## By Alex Burger ############################################################################
######################## 12-01-2018 ################################################################################
######################## Refactored By Max Burger ############################################################################
import re
import subprocess
import json
####################################################################################################################
wificommand = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=subprocess.PIPE)
wifioutputnosplit = wificommand.stdout.read()
wifioutput = wifioutputnosplit.decode('UTF-8').splitlines()
wifidisconnected = 'AirPort: Off'
status= ('lightgreen','yellow','red')
props = ('agrCtlRSSI:','agrCtlNoise:','BSSID:','SSID:','lastTxRate:', 'MCS:','channel:')
data = []
# format data for use ----------------------------------------------#
def formatData(line):
    for prop in props: 
        if prop in str(line):
            signal = line,
            tuplesignal = [tuple(i.split(':')) for i in signal]
            signaldict = dict((x, y) for x, y in tuplesignal)
            signaldict = {k.strip():  v for k,v in signaldict.items()}
        #     print(signaldict) # for debug use to see values with there prop
            return signaldict[prop.replace(":","")]
####################################################################################################################
if wifidisconnected not in wifioutput:
#     print(wifioutput)
    for line in wifioutput:
        pLine = formatData(line)
        if pLine != None:
            data.append(pLine)

    channelnumber = data[6]
    Channel = channelnumber.split(',')[0]
    for line in channelnumber:
        if re.search(r'[0-9]{1,3}\b,1$' or r'[0-9]{1,3}\b,-1$', channelnumber):
                channelwidth = 40
        elif re.search(r'[0-9]{1,3}\b,80$', channelnumber):
                channelwidth = 80
        else:
                channelwidth = 20
############################# RSSI Coloring ########################################################################
    if data[0] <= '-67':        
            RSSIStart = status[0]
    elif '-67'< data[0] <= '-75':
            RSSIStart = status[1]
    else:
            RSSIStart = status[2]
####################### Noise Floor Coloring #######################################################################
    if data[1] >= '-90':
            NoiseStatus = status[0]
    elif '-90' > data[1] >= '-85':
            NoiseStatus = status[1] 
    else:
            NoiseStatus = status[2]
############################# This is where the text output is formatted in JSON for React ###########################################
    aiport_data = {
        "RSSI": f'{data[0]} dBm',
        "RSSI_Status": RSSIStart,
        "Noise_Floor": f'{data[1]} dB',
        "Noise_Floor_Status": NoiseStatus,
        "SSID": f'{data[4]}',
        "BSSID": f'{data[3]}',
        "TxRate": f'{data[2]}',
        "MCS": f'{data[5]}',
        "Channel": f'{channelnumber}',
        "Ch_Width": f'{channelwidth}'
     }
    print(json.dumps(aiport_data))
    
############################ Main if else statement else block ######################################################
else:
    print(json.dumps({"message":"Disconnected"}))
####################################################################################################################