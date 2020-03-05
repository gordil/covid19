from os import listdir, rename
from os.path import isfile, join
import string,re
printable = set(string.printable)
mypath_raw=r'C:\Users\u34472\Documents\covid19-master\daily_raw'
mypath_processed=r'C:\Users\u34472\Documents\covid19-master\daily_processed'
onlyfiles = [f for f in listdir(mypath_raw) if isfile(join(mypath_raw, f))]
skip_list=('Western Pacific Region','European Region','South-East Asia Region','Eastern Mediterranean Region','Region of the Americas','African Region')
replace_list={'the United Kingdom':'United Kingdom','the United States':'United States'}
for fname in onlyfiles:
	fr = open(mypath_raw+"/"+fname, "r")
	fp = open(mypath_processed+"/"+fname, "a")
	c=1
	out_line=''
	for line in fr:
		line=''.join(filter(lambda x: x in printable, line))
		if line.rstrip() in skip_list:
			continue
		if c==1:
			country_name=line.rstrip()
			if country_name in replace_list:
				country_name=replace_list[country_name]
			out_line=fname.split('.')[0]+','+country_name
		else:
			if c==2:
				val_arr=re.split('\(|\)',line.rstrip())
				out_line+=','+val_arr[0].strip()
				out_line+=','+val_arr[1].strip()
			elif c==7:
				val_arr=re.split('\(|\)',line.rstrip())
				out_line+=','+val_arr[0].strip()
				out_line+=','+val_arr[1].strip()
				out_line+=',,'
			# else:
				# out_line+=','+line.rstrip()
		c+=1		
		if c==8:
			fp.write(out_line+'\n')			
			c=1
	print('Completed processing '+fname)
	fr.close()
	fp.close()
	rename(mypath_raw+"/"+fname, mypath_raw+"/processed/"+fname)

	