from os import listdir, rename
from os.path import isfile, join
from shutil import copyfile
from datetime import datetime

mypath_processed = "C:\Users\gordi\Documents\covid\daily_processed"
mypath_full = "C:\Users\gordi\Documents\covid"
onlyfiles = [f for f in listdir(mypath_processed) if isfile(join(mypath_processed, f))]
copyfile(mypath_full+'/covid19.csv', mypath_full+"/full_bkp/covid19"+str(datetime.now().strftime("%d-%b-%Y-%H-%M-%S-%f"))+".csv")
ff = open(mypath_full+"/covid19.csv", "a")
for fname in onlyfiles:	
	fp = open(mypath_processed+"/"+fname, "r")
	ff.write(fp.read())
	print('Completed processing - '+fname)
	fp.close()
	rename(mypath_processed+"/"+fname, mypath_processed+"/processed/"+fname)
ff.close()