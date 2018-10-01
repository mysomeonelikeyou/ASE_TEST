# Changed this file directly on github using your web browser by commenting the python file

import pandas as pd

#read profile
f=open("soc-pokec-profiles.txt","r")
lines=f.readlines()
userid = []
gender = []
for x in lines:
	a = x.split('	')[0]
	b = x.split('	')[3]
	userid.append(a)
	gender.append(b)
	#print(gender)

   # userid.append(x.split('	')[0])
    #gender.append(x.split('	')[3])
    #1: man 0: woman

f.close()


raw_data = {"userid":userid,"gender":gender}
df = pd.DataFrame(raw_data)

df.to_csv('id_gender.csv', columns=['userid','gender'],header = None, index = None)

