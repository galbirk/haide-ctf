# script to extract all mouse pointer positions in pcap
#
# this challenge was recorded with logitech g602 mouse.

from scapy.all import *
import pyautogui
import time


BTN_BYTE  = -8
X_BYTE    = -6
Y_BYTE    = -4
SCRN_WIDTH, SCRN_HIGHT = pyautogui.size()

def main():
    
# ----- import pcap -----


    packets = rdpcap('<filename>.pcapng')
    hid_datas = []


# ----- make a list of all mouse movements -----


    for packeta in packets:

        # HORIZONTAL movement -
        if ():  # no movement
            pass
        else:   # movemenet
            pass
            if ():  # moved to the right
                pass
            else:   # moved to the left
                pass
        
        # VERTICAL movement -
        if ():  # no movement
            pass
        else:   # movemenet
            pass
            if ():  # moved up
                pass
            else:   # moved down
                pass

        hid_datas.append({
            'left_btn_pressed' : '',
            'x'         : '',
            'y'         : ''
        })

    

# ----- replay all captured activity -----


    x_idx = ''     # START X
    y_idx = ''     # START Y
    for hid_data in hid_datas:
        x_idx += hid_data['x']
        y_idx += hid_data['y']
    if (hid_data['left_btn_pressed']):
        pyautogui.click(x_idx, y_idx)



if __name__ == "__main__":
  main()

    
