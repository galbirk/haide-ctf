# script to extract all mouse pointer positions in pcap

# challenge was recorded with logitech g602 mouse.
# 
#  
# HOHMA
# -----
# calculating mouse position:
#       every packet represents relative movement to previous state.
#       so, saving relative value for every packet.
# 
# button state flags: 
#       left mouse btn is represented by Least Significant bit of button flags byte.
#       

from scapy.all import *
import pyautogui
import time


BTN_BYTE   = -8
X_BYTES    = -6
Y_BYTES    = -4
SCRN_WIDTH, SCRN_HIGHT = pyautogui.size()

packets = rdpcap('6.pcapng')


hid_datas = []
for packeta in packets[::2]:    # draw every fifth packet for speed?

    # HORIZONTAL
    if (packeta.load[X_BYTES] == 1): x = 1
    else:
        if (packeta.load[X_BYTES] == 255): x = -1
        else: x = 0
    
    # VERTICAL
    if (packeta.load[Y_BYTES] == 1): y = 1
    else:
        if (packeta.load[Y_BYTES] == 255): y = -1
        else: y = 0

    hid_datas.append({

        'left_btn_pressed' : packeta.load[BTN_BYTE],
        'x'         : x,
        'y'         : y
    })

wait = input('press enter when ready to be amazed')
time.sleep(5)

x_idx = 600     # shriruti
y_idx = 600     # shriruti
for hid_data in hid_datas:
    x_idx += hid_data['x']
    y_idx += hid_data['y']
    if (hid_data['left_btn_pressed']):
        pyautogui.click(x_idx, y_idx)
    



    
