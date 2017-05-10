import sys
filename = sys.argv[1]
text = (open(filename, 'rb'), dialect="excel").read().replace('o', '\n')
open(filename, 'wb').write(text)
