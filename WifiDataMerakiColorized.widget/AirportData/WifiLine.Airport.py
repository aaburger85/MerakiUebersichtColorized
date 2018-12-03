######################## Airport subprocess script to display Wifi Data ############################################
######################## By Alex Burger ############################################################################
######################## 12-01-2018 ################################################################################
import re
import ast
import json
import subprocess
####################################################################################################################
wificommand = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=subprocess.PIPE)
wifioutputnosplit = wificommand.stdout.read()
wifioutput = wifioutputnosplit.decode('UTF-8').splitlines()
wifidisconnected = 'AirPort: Off'
RSSIGoodStart = "RSSI:<strong><font color='lightgreen'>"
RSSIOKStart = "RSSI:<strong><font color='yellow'>"
RSSIBadStart = "RSSI:<strong><font color='red'>"
FontEnd = "</font></strong>|"
NoiseFloorStart = "Noise Floor:<strong>"
NoiseFloorGoodStart = "Noise Floor:<strong><font color='lightgreen'>"
NoiseFloorOKStart = "Noise Floor:<strong><font color='yellow'>"
NoiseFloorBadStart = "Noise Floor:<strong><font color='red'>"
FieldEnd = "</strong>|"
SSIDStart = "SSID:<strong>"
BSSIDStart = "BSSID:<strong>"
TxRateStart = "TxRate:<strong>"
MCSStart = "MCS:<strong>"
ChannelStart = "Channel:<strong>"
ChWidthStart = "Ch Width:<strong>"
ChWidthEnd = "MHz</strong>"
####################################################################################################################
if wifidisconnected not in wifioutput:
        for line in wifioutput:
            if re.search(r'agrCtlRSSI', line):
                signal = line,
        tuplesignal = [tuple(i.split(': ')) for i in signal]
        signaldict = dict((x, y) for x, y in tuplesignal)
        signaldict = {k.replace(" ",""): v for k,v in signaldict.items()}
        RSSI = signaldict['agrCtlRSSI']
####################################################################################################################
        for line in wifioutput:
            if re.search(r'agrCtlNoise', line):
              noise = line,
        tuplenoise = [tuple(i.split(': ')) for i in noise]
        noisedict = dict((x, y) for x, y in tuplenoise)
        noisedict = {k.replace(" ",""): v for k,v in noisedict.items()}
        NoiseFloor = noisedict['agrCtlNoise']
####################################################################################################################
        for line in wifioutput:
            if re.search(r'\bSSID', line):
                ssid = line,
        tuplessid = [tuple(i.split(': ')) for i in ssid]
        ssiddict = dict((x, y) for x, y in tuplessid)
        ssiddict = {k.replace(" ",""): v for k,v in ssiddict.items()}
        SSID = ssiddict['SSID']
####################################################################################################################
        for line in wifioutput:
            if re.search(r'BSSID', line):
                bssid = line,
        tuplebssid = [tuple(i.split(': ')) for i in bssid]
        bssiddict = dict((x, y) for x, y in tuplebssid)
        bssiddict = {k.replace(" ",""): v for k,v in bssiddict.items()}
        BSSID = bssiddict['BSSID']
####################################################################################################################
        for line in wifioutput:
            if re.search(r'lastTxRate', line):
                txrate = line,
        tupletxrate = [tuple(i.split(': ')) for i in txrate]
        txratedict = dict((x, y) for x, y in tupletxrate)
        txratedict = {k.replace(" ",""): v for k,v in txratedict.items()}
        TxRate = txratedict['lastTxRate']
####################################################################################################################
        for line in wifioutput:
            if re.search(r'MCS', line):
                MCSrate = line,
        tupleMCSrate = [tuple(i.split(': ')) for i in MCSrate]
        MCSratedict = dict((x, y) for x, y in tupleMCSrate)
        MCSratedict = {k.replace(" ",""): v for k,v in MCSratedict.items()}
        MCSRate = MCSratedict['MCS']
####################################################################################################################
        for line in wifioutput:
            if re.search(r'channel', line):
                channel = line,
        tuplechannel = [tuple(i.split(': ')) for i in channel]
        channeldict = dict((x, y) for x, y in tuplechannel)
        channeldict = {k.replace(" ",""): v for k,v in channeldict.items()}
        channelnumber = channeldict['channel']
        Channel = channelnumber.split(',')[0]
        for line in channelnumber:
                if re.search(r'[0-9]{1,3}\b,1$', channelnumber):
                        channelwidth = 40
                if re.search(r'[0-9]{1,3}\b,-1$', channelnumber):
                        channelwidth = 40
                elif re.search(r'[0-9]{1,3}\b,80$', channelnumber):
                        channelwidth = 80
                else:
                        channelwidth = 20
############################# RSSI Coloring ########################################################################
        if RSSI <= '-67':        
                RSSIStart = RSSIGoodStart
        elif '-67'< RSSI <= '-75':
                RSSIStart = RSSIOKStart
        else:
                RSSIStart = RSSIBadStart
####################### Noise Floor Coloring #######################################################################
        if NoiseFloor >= '-90':
                NoiseFloorStart = NoiseFloorGoodStart
        elif '-90' > NoiseFloor >= '-85':
                NoiseFloorStart = NoiseFloorOKStart 
        else:
                NoiseFloorStart = NoiseFloorBadStart
############################# This is where the text output is formatted ###########################################
        print (RSSIGoodStart, RSSI, "dBm", FontEnd, NoiseFloorStart, NoiseFloor, "dB", FontEnd, SSIDStart, SSID, FieldEnd, BSSIDStart, BSSID, FieldEnd, TxRateStart, TxRate, "Mbps", FieldEnd, MCSStart, MCSRate, FieldEnd, ChannelStart, Channel, FieldEnd, ChWidthStart, channelwidth, ChWidthEnd)
####################################################################################################################
else:
        print("Disconnected")
####################################################################################################################
