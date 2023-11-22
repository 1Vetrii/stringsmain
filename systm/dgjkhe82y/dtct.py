# v220929.1
#print ("detecting...")
import sys
# import os
# import fnmatch
# import requests
currentdir=sys.argv[1]
#################################
## Reset language to unknown
#################################
lang="unknown1"
ftype=currentdir+"/type.txt"
with open (ftype,"w") as outfile:
  outstring="unknown1"
  outfile.write(outstring)
#################################
## Detect language from settings.txt
#################################
fname="Filename_Missing"
fileFlag=False
fnamestring="Filename:     Unknown"
with open ("settings.txt") as infile:
  for line in infile:
    if line.strip()[0:6]=="#file=":
      fname=line.strip()[6:]
    if line.strip()[0:7]=="# file=":
      fname=line.strip()[7:]
    if line.strip()[0:8]=="# file =":
      fname=line.strip()[8:]
if fname == "":
  fname="Filename_Missing"
if fname!="Filename_Missing":
  fnamestring="Filename:     "+fname
  if ".py" in fname:
    lang="python"
    fileFlag=True    
  elif ".java" in fname:
    lang="java"
    fileFlag=True
  else:
    lang="unknown2"
  # infofile=tempstring+"info.txt"
  # print (infofile)
  # with open(infofile,"w") as outfile:
  #   outfile.write(fnamestring)
  # with open ()
else:
  outstring="echo '#file=' line missing or incomplete in settings.txt"
  # with open (fname2bash,"w") as outfile:
  #   outfile.write(outstring)
#print ("Filename is",fname)
#print ("Language is",lang)
with open (ftype,"w") as outfile:
  outstring=lang
  outfile.write(outstring)
if lang=="python":
  exit(101)
elif lang=="java":
  shortfname=fname[:-5]
  #print(shortfname)
  #print ("jjjjjjj")
  ftemplate1=currentdir+"/1jtemplate.sh"
  fdestination=currentdir+"/1j.sh"
  # with open(ftemplate1) as infile:
  #   for line in infile:
  #     print(line.strip())
  with open(ftemplate1) as infile:
    fstring=infile.read()
  #print("777")
  #print(fstring)
  #print("778")
  fstring2=fstring.replace("filenamehere",fname)  
  fstring3=fstring2.replace("shortnamehere",shortfname)
  #print(fstring3)
  with open(fdestination,"w") as outfile:
    outfile.write(fstring3)
  #input()
  exit(102)
else:
  exit(99)
  