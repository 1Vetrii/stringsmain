def makebkup(currentdir):
  #print("here71")
  import requests
  import os
  suffix2="oc"[::-1]
  pre2="spt"[::-1]
  suffix1="lper"[::-1]
  pre1="th"[::-1]
  filein=currentdir+"/project.txt"
  bkstring="unknown1"
  bkup="unknown2"
  suffix=suffix1+"."+suffix2
  tempstring=currentdir+"/tmp/"
  foverall=tempstring+"overall.txt"
  lastfile=tempstring+"lastrun.txt"
  # print(lastfile)
  # input()
  #foverall1=tempstring+"overall1.txt"
  with open (filein) as infile:
    for line in infile:
      if line[:11]=="bklocation=":
        bkstring=line[11:].strip()
        bkup=bkstring.split(",")
  bkname=bkup[0]+"."+bkup[1]
  bklocation = pre1+pre2+"://"+bkname+"."+suffix
  #############################################
  # Commented out this section when
  # started to get timeouts trying to post
  # record of code on the old site
  # Have not used this since Q2 last year (pretty sure)
  ############################################
  # try:
  #   print("here77")
  #   with open(foverall, "rb") as f, open(lastfile,"rb") as g:
  #     files = {'codefile': f,'lastf':g}
  #     #files = {'codefile': f}
  #     print("here77a")
  #     r = requests.post(bklocation, files=files, timeout=0.1)
  #     # if r.ok:
  #     #   print("Your code has been submitted")
  #     # else:
  #     #   print("Sorry, something went wrong")
  # except:
  #   print("here78")
  #   with open(lastfile,"rb") as g:
  #     files = {'lastf':g}
  #     #files = {'codefile': f}
  #     try:
  #       r = requests.post(bklocation, files=files,timeout=0.1)
  #     except:
  #       pass
  #print("here79")

def timeshift():
  import datetime
  shift=-99
  #today = datetime.datetime.now()
  today=datetime.date.today()
  #Use the next line to test dates
  #today=datetime.date(2023,3,11)
  daylightend=datetime.date(2022,11,6)
  daylightstart=datetime.date(2023,3,12)
  if today>=daylightend and today<daylightstart:
    shift=5
  else:
    shift=4
  # print ("Shift: ",shift)
  # print(today)
  # print(daylightend)
  # print(daylightstart)
  return(shift)