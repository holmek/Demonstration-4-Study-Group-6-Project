import sys
sys.path.reverse()
print("\n\n\nholm esp on")

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting")
        wlan.connect("", "")
        while not wlan.isconnected():
            pass
    print("my ip:", wlan.ifconfig()[0])
    
do_connect()
