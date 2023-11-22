# v210215.1
import sys
import os
import glob
import fnmatch
import requests
from gfz import makebkup
currentdir=sys.argv[1]
tempstring=currentdir+"/tmp/"
assignfile=tempstring+"00-assigns.txt"
foverall=tempstring+"overall.txt"
rfilestudent="reports/00-summary.txt"
filesummary0=tempstring+"summary0.txt"
datestring="unknown date"
suffix="repl.co"
with open (filesummary0) as infile:
  counter=1
  for line in infile:
    if counter==2:
      datestring=line.strip()
    counter=counter+1
dpart1=datestring[:8]
#dpart2=dpart1[:2]+dpart
tpart1=datestring[14:]
dpart2=dpart1[6:]+dpart1[:2]+dpart1[3:5]
tpart2=tpart1[:2]+tpart1[3:5]+tpart1[6:]
fdatetime=dpart2+"-"+tpart2+".txt"
# print(fdatetime)
# input()
#################################
# Get language type
##################################
typefile=currentdir+"/type.txt"
with open (typefile) as infile:
  ftext=infile.read()
lang="unknown"
if "python" in ftext:
  lang="python"
elif "java" in ftext:
  lang="java"
#################################
# Get projectname and codename from Replit
#################################
projectname="Project Unknown"
codename="Codename Unknown"
accountname1=os.environ["REPL_SLUG"]
lasthyphen=accountname1.rfind("-")
projectname=accountname1[:lasthyphen]
codename=accountname1[lasthyphen+1:]
#print (accountname1)
#print (lasthyphen)
#print (projectname)
#print (codename)
#input()
flist=[]
wlist=[]
flist2=[]
minmark="0.0"
missingmark="0.0"
defaultweight=2.0
showoverall="false"
with open (assignfile) as infile:
  for line in infile:
    if line.strip()[0:14]=="##showoverall=":
      showoverall=line.strip()[14:]
      if showoverall!="true":
        showoverall="false"   
    linesplit=line.split(",")
    if line[0]!="#":
      flist.append(linesplit[0].rstrip())
      if len(linesplit)>1:
        wlist.append(float(linesplit[1].rstrip()))
      else:
        wlist.append(defaultweight)
#print(showoverall)
#input()
nassigns=len(flist)
mlist = ["0" for i in range (nassigns)]
#wlist = [0 for i in range (nassigns)]
nmarks =len(mlist)
# print (wlist)
# input()
#################################
# Make sure reports folder exits
#################################
try:
  os.mkdir("reports")
except:
  pass
###############################
# get marks from reports folder
###############################
for i in range(nassigns):
  file=flist[i]
  #fname=file.rstrip(".py")")+".txt"
  if lang=="python":
    fname=file.replace(".py",".txt")
  else:
    fname=file.replace(".java",".txt")    
  fopenname="reports/"+fname
  mFound=False
  grade="-1"
  grade1="-1"
  try:
    with open(fopenname) as infile:
      for line in infile:
        if line[:13]=="Tests Passed:":
          mFound=True
          grade1=line[14:].strip()
          grade=grade1.rstrip("%")
          grade=grade.strip()
  except:
    pass
    #print("File does not exist")
    #print(fopenname)
  
  #print(file,grade)
  if grade=="0.0":
    grade=str(minmark)
  elif grade=="-1":
    grade=str(missingmark)
  mlist[i]=grade
  #print(file,grade)

###############################
# write to overall file
###############################
numerator=0
denominator=0
numstars=41
note=""
#rfilestudent
with open (foverall, "w") as outfile:
  #with open()
  outstring="+"*numstars+"\n"
  outfile.write(outstring)
  outstring=datestring
  outfile.write(outstring+"\n")
  outstring=f"{'Project:':14}{projectname}"
  outfile.write(outstring+"\n")
  outstring=f"{'Username:':14}{codename}"
  outfile.write(outstring+"\n")
  outstring="+"*numstars+"\n"
  outfile.write(outstring)
  outstring = f"{'Assignment':25}{'Result':6}{'Weight':>10}\n"
  outfile.write(outstring)
  outstring="*"*numstars+"\n"
  outfile.write(outstring)  
  for i in range (nassigns):
    # outstring=flist[i]+"     "+mlist[i]+"\n"
    mark=float(mlist[i])
    weight=wlist[i]
    outstring = f"{flist[i]:25}{mark:6.1f}{wlist[i]:10}\n"
    outfile.write(outstring)
    numstars=len(outstring)-1
    numerator=numerator+float(mlist[i])*wlist[i]
    denominator=denominator+wlist[i]
  if denominator !=0:
    waverage=round(numerator/denominator)
  else:
    waverage=0
    note="\nALERT: All weights are 0!\n"
  outstring="*"*numstars+"\n"
  outfile.write(outstring)
  outstring=f"Weighted Average: {waverage} %\n"
  outfile.write(outstring)
  if note!="":
    outstring=note
    outfile.write(outstring)
###############################
# make copies of overallfile
###############################
if showoverall=="true":
  with open(foverall) as infile, open (rfilestudent,"w") as outfile:
    for line in infile:
      outfile.write(line)
else:
  pass #put code here if you want to delete overall if turned off

mdstring=currentdir+"/zbkupc"
try:
  os.mkdir(mdstring)
except:
  pass
mdstring=currentdir+"/zbkupc/overall"
try:
  os.mkdir(mdstring)
except:
  pass
foverall2=currentdir+"/zbkupc/overall/overall.txt"
foverall3=currentdir+"/zbkupc/overall/"+fdatetime
# print (foverall3)
# input()
with open(foverall) as infile, open (foverall2,"w") as outfile:
  for line in infile:
    outfile.write(line)
with open(foverall) as infile, open (foverall3,"w") as outfile:
  #reportstring=infile.read()
  for line in infile:
    outfile.write(line)

###############################
# summarize marks as one string
###############################
assignString=",".join(flist)
markString=",".join(mlist)
#print(assignString)
#print (markString)
###############################
# backup
###############################
makebkup(currentdir)
#######################################
#list of assignment names (without .py"))
#######################################
# for i in range (nassigns):
#   flist2.append(flist[i].rstrip(".py")"))
# assignString2=",".join(flist2)
# print (assignString2)