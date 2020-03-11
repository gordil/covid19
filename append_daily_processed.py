from os import listdir, rename
from os.path import isfile, join
from shutil import copyfile
from datetime import datetime

mypath_processed = "daily_processed"
onlyfiles = [f for f in listdir(mypath_processed) if isfile(join(mypath_processed, f))]
copyfile("covid19.csv", "full_bkp/covid19"+str(datetime.now().strftime("%d-%b-%Y-%H-%M-%S-%f"))+".csv")
ff = open("covid19.csv", "a")
for fname in onlyfiles:	
	fp = open(mypath_processed+"/"+fname, "r")
	ff.write(fp.read())
	print('Completed processing - '+fname)
	fp.close()
	rename(mypath_processed+"/"+fname, mypath_processed+"/processed/"+fname)
ff.close()