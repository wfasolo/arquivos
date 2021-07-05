import pyshark

# Open saved trace file
cap = pyshark.FileCapture('mycapture.cap')

# Sniff from interface
capture = pyshark.LiveCapture(interface='enp0s7')
capture.sniff(timeout=10)

