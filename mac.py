import os
from datetime import datetime

ma = os.popen('wmic nic get macaddress').read().split()[3]
simdi = datetime.now()
t = simdi
result = datetime.strftime(t,'%d %m %Y %X')
f = open("myfile.txt", "w")
f.write(result) 
f.write("Mac Add  :" + ma)
f.close()
