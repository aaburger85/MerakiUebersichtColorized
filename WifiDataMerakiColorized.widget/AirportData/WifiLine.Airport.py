######################## Airport subprocess script to display Wifi Data ############################################
######################## By Alex Burger ############################################################################
######################## 12-01-2018 ################################################################################
import re
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
# print(wifioutput[0])
# print('_____________________________________________________________________')
# print(str(wifioutputnosplit))

# format data for use ----------------------------------------------#
def formatData(signal, prop):
        tuplesignal = [tuple(i.split(': ')) for i in signal]
        signaldict = dict((x, y) for x, y in tuplesignal)
        signaldict = {k.strip():  v for k,v in signaldict.items()}
        return signaldict[prop]
####################################################################################################################
if wifidisconnected not in wifioutput:
        for line in wifioutput:
                if re.search(r'agrCtlRSSI', line):
                        signal = line,
                        RSSI = formatData(signal, 'agrCtlRSSI')
# RSSI ----------------------------------------------#
                elif re.search(r'agrCtlNoise', line):
                        noise = line,
                        NoiseFloor = formatData(noise, 'agrCtlNoise')
# SSID ----------------------------------------------#
                elif re.search(r'\bSSID', line):
                        ssid = line,
                        SSID = formatData(ssid, 'SSID')
# BSSID ---------------------------------------------#
                elif re.search(r'BSSID', line):
                        bssid = line,
                        BSSID = formatData(bssid, 'BSSID')
# TxRate ---------------------------------------------#
                elif re.search(r'lastTxRate', line):
                        txrate = line,
                        TxRate = formatData(txrate, 'lastTxRate')
# MCS ------------------------------------------------#
                elif re.search(r'MCS', line):
                        MCSrate = line,
                        MCSRate = formatData(MCSrate, 'MCS')
# Channel --------------------------------------------#
                elif re.search(r'channel', line):
                        channel = line,
                        channelnumber = formatData(channel, 'channel')
                        
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
############################ Main if else statement #####################################################################
else:
        print("Disconnected")
####################################################################################################################
