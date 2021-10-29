import datetime
import os
import subprocess
def conver2time(strs):
    return datetime.datetime.strptime(strs, '%d/%b/%Y:%H:%M:%S')

# strs = '28/Sep/2015:09:58:23'

# print(conver2time(strs))
rels = []
try:
    f1 = open('access.log','r')
    rlines = f1.readlines()
    if len(rlines) <= 0 :
        print("File Empty")
        
except:
    print("File Not Found")

try:
    ip_address = rlines[0].split(" ")[0]
    #print(ip_address)
    time_start = conver2time(rlines[0].split(" ")[3].split("[")[1])

    time_end  = time_start + datetime.timedelta(seconds=60)
    # print(time_end)
    count = 1

    # print(type(rlines)) 
    for i in range(1 , len(rlines)):
        # check dia chi IP
        if ip_address in rlines[i]:
            # lay ra thoi gian IP request
            time_req = conver2time(rlines[i].split(" ")[3].split("[")[1])
            # check xem het han 1 phut chua
            if time_req <= time_end:
                count += 1
                # khi het han 1 phut => kiem tra so request
                if count > 120 and ip_address not in rels:
                    rels.append(ip_address)
            # neu trong 1 phut thoa man < 120 req => reset time
            else : 
                count = 1 
                time_start = time_end
                time_end = time_start + datetime.timedelta(seconds=60)  
        # neu khac ip => dat lai cac gia tri do  
        else :
            ip_address = rlines[i].split(" ")[0]
            time_start = conver2time(rlines[i].split(" ")[3].split("[")[1])
            time_end  = time_start + datetime.timedelta(seconds=60)
            count = 1
    print(rels)

    os.system('sudo iptables -F INPUT')
    for liad in rels:
        os.system('sudo iptables -A INPUT --src {} -j DROP'.format(liad))

except:
    print("File Not Data")
