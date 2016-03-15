import StringIO
import sys
import xml.etree.ElementTree as ET
from eagle_http import *

aStrIO = StringIO.StringIO()
eagle = eagle_http('jjee@ucdavis.edu', 'pmohapatra', '002ab5')
saveout = sys.stdout


sys.stdout = aStrIO

eagle.get_instantaneous_demand()
sys.stdout = saveout

aStr = "<data>\n"
aStr = aStr + aStrIO.getvalue()
aStr = aStr + "\n</data>"
print aStr

tree = ET.fromstring(aStr)

macID      = tree[1][0].text
meterMacID = tree[1][1].text
timestamp  = int(tree[1][2].text, 16)
demand     = int(tree[1][3].text, 16)
multiplier = int(tree[1][4].text, 16)
divisor    = int(tree[1][5].text, 16)
digitsRight= int(tree[1][6].text, 16)
digitsleft = int(tree[1][7].text, 16)
supLeadZero= tree[1][8].text
print macID, meterMacID, timestamp, demand, multiplier, divisor, digitsRight, digitsleft, supLeadZero

