from process import check_string_in_file

f1 = open("gistfile1.txt","r")
f2 = open("fileprces.txt","w+")
lines = f1.readlines()
sum_linefile = 0
for lps in lines:
    arr = lps.split('"')
    tma = arr[-2]
    tmb = tma.split(") ") #split into "Name_browser/version_number Safari/version_number"
    f2.write(tmb[-1])   
    f2.write('\n')
    sum_linefile = sum_linefile+1 #sum_line of file log 
f1.close()
f2.close()

#check string match first in line
chromefweb = check_string_in_file('fileprces.txt','Chrome')
chromefapp = check_string_in_file('fileprces.txt','CriOS')
coccoc = check_string_in_file('fileprces.txt','coc_coc_browser')
fbapp = check_string_in_file('fileprces.txt','Mobile')
firefox = check_string_in_file('fileprces.txt','Gecko')
ie = check_string_in_file('fileprces.txt','\)')
ie2 = check_string_in_file('fileprces.txt','Mozilla')
safari = check_string_in_file('fileprces.txt','Version')
other = check_string_in_file('fileprces.txt','-')

print("Chrome: ",(chromefapp+chromefweb))
print("CocCoc: ",coccoc)
print("Fbapp: ",fbapp)
print("Firefox: ",firefox)
print("IE: ",(ie+ie2))
print("Safari: ",safari)
print("Device other: ",other)
print("Sumline: ",sum_linefile)
print("-------------------------------------------------------")

#print rate of browser types
print("Rate of Chrome: "+format(float(chromefapp+chromefweb)/sum_linefile*100,".2f")+"%")
print("Rate of CocCoc: "+format(float(coccoc)/sum_linefile*100,".2f")+"%")
print("Rate of Fbapp: "+format(float(fbapp)/sum_linefile*100,".2f")+"%")
print("Rate of Firefox: "+format(float(firefox)/sum_linefile*100,".2f")+"%")
print("Rate of IE "+format(float(ie+ie2)/sum_linefile*100,".2f")+"%")
print("Rate of Safari: "+format(float(safari)/sum_linefile*100,".2f")+"%")
print("Rate of Other: "+format(float(other)/sum_linefile*100,".2f")+"%")




