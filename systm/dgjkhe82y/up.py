# up.py v210223.1
# print(888)
# input()
import sys
import os
import fnmatch
import requests
currentdir=sys.argv[1]
mainsite="https://testingcases.davidhunter1.repl.co"
flog=currentdir+"/log.txt"
###################################
# Get project name from project.txt
###################################
fproject=currentdir+"/project.txt"
projectstring="unknown"
with open(fproject) as infile:
  for line in infile:
    if line.strip()[0:8]=="project=":
      projectstring=line.strip()[8:]
if projectstring=="unknown":
  print("Project Name not set in project.txt")
#input()
#projectstring="3C-01-Intro"
#############################
# check if update setting on
##############################
ulist=[]
update="no"   
with open ("settings.txt") as infile: #if user want to update a file
  for line in infile:
    if line.strip()[0:8]=="#update=":
      update=line.strip()[8:]
    if line.strip()[0:9]=="# update=":
      update=line.strip()[9:]
    if line.strip()[0:10]=="# update =":
      update=line.strip()[10:]
#print(update)
if update!="no" and update!="every" and len(update)>0:
  ulist=update.split(",")
#############################
# set location
##############################
folder="updates"
####################################
# copy update settings; get every list
####################################
#print("herea")
# input()
data_url = mainsite+"/"+projectstring+"/"+folder+"/"+"usettings.txt"
copyname=currentdir+"/usettings.txt"
try:
  r = requests.get(data_url, timeout=1)
  #print("here2")
  # input()
  with open(copyname, "w") as f:
    f.write(r.text)
except:
  print("error 001")
  # with open (logname, "w") as outfile:
  #   outfile.write("error 001")
  pass
setfile=copyname
everylist=[]
startlist=[]
every="none"
force="no"
starters="none"
with open(setfile) as infile:
  for line in infile:
    if line.strip()[0:6]=="EVERY=":
      every=line.strip()[6:]
    if line.strip()[0:6]=="FORCE=":
      force=line.strip()[6:]
    if line.strip()[0:9]=="STARTERS=":
      starters=line.strip()[9:]
everylist=every.split(",")
if starters!="none":
  startlist=starters.split(",")
#print(starters)
#print(startlist)
#input()
#############################
# update from user
##############################
if update !="no" and update!="every" and force!="YES":
  #print("Updating some")
  for fname in ulist:
    file_url = mainsite+"/"+projectstring+"/"+folder+"/"+fname
    copyname=currentdir+"/"+fname
    r = requests.get(file_url, timeout=1)
    print ("here3")
    with open(copyname, "w") as f:
      f.write(r.text)

#############################
# update every
##############################
if force=="YES":
  update="every"
if update=="every" and every!="none":
  #print("Updating every")
  for fname in everylist:
    file_url = mainsite+"/"+projectstring+"/"+folder+"/"+fname
    copyname=currentdir+"/"+fname
    r = requests.get(file_url, timeout=1)
    with open(copyname, "w") as f:
      f.write(r.text)
#input()
###########################
# copy starter files
###########################
for f in startlist:
  if os.path.exists(f):
    pass
    #print (f"{f} already exits")
  else:
    #print (f"{f} does not exist")
    try:
      start_url = mainsite+"/"+projectstring+"/starters/"+f
      copyname=f
      r = requests.get(start_url, timeout=1)
      with open(copyname, "w") as f:
        f.write(r.text)
    except:
      Print("Error: Issue with Starter File")
#print("here4")