# v221001.1
# To Do Next
# print("here 51")
# input()
# Backup again
# options on reports details:
# (turn off reporting maybe???!)
# Advice if program won't run (comment out options one at a time until you find the one that is causing the error)
# Hidden test cases if output is to a file...
# (currently hides output to screen, but
# still need to delete both the input file from  the data folder and the output file from the output folder after the report is generated)
# 
# Clean up files at beginning and end
# autogenerate redherring folders/files
# different weights for test cases!!!

#print ("starting gfj...")
#input()
import sys
import os
import glob
import fnmatch
import requests
import datetime
from gfz import makebkup,timeshift
currentdir=sys.argv[1]
tempstring=currentdir+"/tmp/"
mainsite="https://testingcases.davidhunter1.repl.co"
#################################
# Get projectname and codename from Replit
#################################
projectname1="Project Unknown"
codename1="Codename Unknown"
accountname1=os.environ["REPL_SLUG"]
lasthyphen=accountname1.rfind("-")
projectname1=accountname1[:lasthyphen]
codename1=accountname1[lasthyphen+1:]
###################################
# Get folder name for testing from project.txt
###################################
fproject=currentdir+"/project.txt"
projectstring="unknown"
with open(fproject) as infile:
  for line in infile:
    if line.strip()[0:8]=="project=":
      projectstring=line.strip()[8:]
if projectstring=="unknown":
  print("Project Name not set in project.txt")
######################################
#projectstring="3C-01-Intro"
fname1abash=currentdir+"/1a.sh"
fname2bash=currentdir+"/2.sh"
fname2bbash=currentdir+"/2b.sh"
fname3bash=currentdir+"/3.sh"
checksFlag=False
goCases=False
today = datetime.datetime.now()
timeshiftnum=timeshift()
adjust = datetime.timedelta(hours=timeshiftnum)
today = today-adjust
#print(today)
timestring=f'{today.strftime("%x"):13} {today.strftime("%X")}'
#print (timestring)
month=timestring[:2]
day=timestring[3:5]
year=timestring[6:8]
hour=timestring[14:16]
mins=timestring[17:19]
sec=timestring[20:23]
timestring2=year+month+day+"-"+hour+mins+sec
# print(timestring)
# input()
codeFlag=False
codestring="Codename:     Unknown"
cname="error:missing codename"
with open ("settings.txt") as infile:
  for line in infile:
    if line.strip()[0:10]=="#codename=":
      cname=line.strip()[10:]
    if line.strip()[0:11]=="# codename=":
      cname=line.strip()[11:]
    if line.strip()[0:12]=="# codename =":
      cname=line.strip()[12:]
if cname == "":
  cname="error:missing codename"
if cname!="error:missing codename":
  codestring="Username:     "+cname
  codeFlag=True
else:
  outstring="echo '#codename=' line missing or incomplete in settings.txt"
  with open (fname2bash,"w") as outfile:
    outfile.write(outstring)
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
  fileFlag=True
  # infofile=tempstring+"info.txt"
  # print (infofile)
  # with open(infofile,"w") as outfile:
  #   outfile.write(fnamestring)
  # with open ()
else:
  outstring="echo '#file=' line missing or incomplete in settings.txt"
  with open (fname2bash,"w") as outfile:
    outfile.write(outstring)
#get mode= from main
mode="normal"   
with open ("settings.txt") as infile:
  for line in infile:
    if line.strip()[0:6]=="#mode=":
      mode=line.strip()[6:]
    if line.strip()[0:7]=="# mode=":
      mode=line.strip()[7:]
    if line.strip()[0:8]=="# mode =":
      mode=line.strip()[8:]
hstring="+++++++++++++++++++++++++++++++++++\n"+timestring+"\n"+codestring+"\n"+fnamestring+"\n+++++++++++++++++++++++++++++++++++\n"
#input()
#check mode
if codeFlag and fileFlag:
  checksFlag=True
##################################
# create lastrun file
#################################
infofile=tempstring+"lastrun.txt"
timestring3="Time:"+timestring
codestring2="Codename:"+codename1
hstring=hstring.replace(cname,codename1)
projectstring2="Project:"+projectname1
fstring2="File:"+fname
modestring="Mode:"+mode
with open(infofile,"w") as outfile:
  outfile.write(timestring3+"\n")
  outfile.write(codestring2+"\n")
  outfile.write(projectstring2+"\n")
  outfile.write(fstring2+"\n")
  outfile.write(modestring+"\n")
##################################
# checkmode
################################# 
if mode=="check" and checksFlag:
  shortfname=fname[:-5]
  #tempstring=currentdir+"/tmp/"
  data_url = mainsite+"/"+projectstring+"/"+shortfname+".cas"
  assignsname="00-assigns.txt"
  copyname=tempstring+fname
  
  ####### I think-> make copy of student file in temp dir
  # print(fname)
  # print(copyname)
  # input()
  try:
    with open (fname) as infile, open (copyname,"w") as outfile:
      for line in infile:
        outfile.write(line)
  except:
    #print(fname+" is missing")
    exit()
    #input()
  assigns_url = mainsite+"/"+projectstring+"/"+assignsname
  casefname=tempstring+"cases.txt"
  assignstempname=tempstring+"/"+assignsname
  #print("hey1")
  #input()
  r = requests.get(data_url, timeout=1)
  #print("hey2")
  #input()
  with open(casefname, "w") as f:
    f.write(r.text)
  a = requests.get(assigns_url, timeout=1)
  with open(assignstempname, "w") as f:
    f.write(a.text)
  with open (assignstempname) as atemp, open (assignsname, "w") as outfile:
    for line in atemp:
      linesplit=line.split(",")
      if line[0]!="#":
        #linesplit=line.split(",")
        outstring="## file="+linesplit[0]
        outfile.write(outstring)
      else:
        if line[1]!="#":
          outstring="## No Case file yet for: "+linesplit[0][1:]
          outfile.write(outstring)        

  ##################################
  # If want to check for missing functions I think
  # you could do it here
  # as long as copy of student file has been made 
  # and copy of cases file have been made
  # you should be able to do it
  #################################
  # print ("stopping")
  # input()
  ##################################
  #check if casefile is good to use
  #################################
  caseProblem=False
  caseProbString="Case File Error z"
  nfcases=0
  ninput=0
  nexpected=0
  casefileline=[]
  casenames=[]
  inputs=[]
  expected=[]
  casestart=[]
  instart=[]
  expectedstart=[]
  funcfiles=[]
  funcfiles2=set()
  linenum=0
  functionmode="no"
  tfname="none"
  datafiles=[]
  expectedfiles=[]
  studentoutfiles=[]
  outmode="screen"
  nstudentouts=0
  #input()
  with open(casefname) as infile:
    for line in infile:
      casefileline.append(line.strip('\n'))
      linenum=linenum+1
      if line.strip()[0:5]=="case=":
        casenames.append(line.strip()[5:])
        casestart.append(linenum)
        expectedfiles.append('p')
        studentoutfiles.append('pppp') 
        nfcases=nfcases+1
      if line.strip()[0:13]=="expectedfile=":
        expectedfiles[nfcases-1]=line.strip()[13:]
      if line.strip()[0:15]=="studentoutfile=":
        studentoutfiles[nfcases-1]=line.strip()[15:]
        #nstudentouts=nstudentouts+1
      if line.strip()[0:6]=="input=":
        inputs.append(line.strip()[6:])
        instart.append(linenum)    
        ninput=ninput+1
      if line.strip()[0:7]=="output=":
        expected.append(line.strip('\n')[7:])
        expectedstart.append(linenum)   
        nexpected=nexpected+1
      # if line.strip()[0:10]=="FUNCTIONS=":
      #   functionlist=line.strip()[10:].split(",")
      if line.strip()[0:13]=="FUNCTIONMODE=":
        functionmode=line.strip()[13:]
      if line.strip()[0:6]=="TFILE=":
        tfname=line.strip()[6:]
      if line.strip()[0:14]=="FUNCTIONFILES=":
        funcfiles=line.strip()[14:].split(",")
      if line.strip()[0:10]=="DATAFILES=":
        datafiles=line.strip()[10:].split(",")
      if line.strip()[0:8]=="OUTMODE=":
        outmode=line.strip()[8:]          
      if ((nfcases-ninput)>1) or ((nfcases-nexpected)>1):
        caseProblem=True
        print ("case file error 1")



  # print (datafiles)
  # input()
  # print (funcfiles)
  # print (len(funcfiles))
  ########################################
  # Scan student file for imported modules DEACTIVATED FOR JAVA
  ########################################
  # #funcignore={"math","random","matplotlib","os","csv","time"}
  # with open (copyname) as infile:
  #   start=0
  #   for line in infile:
  #     #print(line)
  #     if "from" in line and "import" in line:
  #       if line[0]!="#":
  #         start=line.find("from ")+5
  #         end=line.find("import")-1
  #         funcfiles2.add(line[start:end])
  #     elif "import" in line:
  #       if line[0]!="#":
  #         start=line.find("import ")+7
  #         end=line.find(" ",start)
  #         funcfiles2.add(line[start:end])
  # # print(funcfiles2)
  # funcscopy=funcfiles2-funcignore
  # # print(funcscopy)
  
  ##### Copy function files to temp folder ######### DEACTIVATED FOR JAVA
  # if len(funcscopy)>0:
  #   for f in funcscopy:
  #     funcin=f+".py"
  #     funcout=tempstring+f+".py"
  #     # print (funcin)
  #     # print (funcout)
  #     with open (funcin) as infile, open(funcout,"w") as outfile:
  #       for line in infile:
  #         outfile.write(line)
  
  ##### Copy my py file to test functions #########
  if functionmode=="output":
    my_url = mainsite+"/"+projectstring+"/"+tfname
    myfname=tempstring+"teacher.py"
    my = requests.get(my_url,timeout=1)
    with open(myfname, "w") as f:
      f.write(my.text)
  ######################################
  ##### Copy data files to data folders 
  ######################################
  #print(datafiles)
  #input()
 
  if len(datafiles)>0:
    # try:
    #   os.mkdir(currentdir+"/tmp/data")
    # except:
    #   pass
    try:
      os.mkdir("data")
    except:
      pass
    try:
      os.mkdir("output")
    except:
      pass
    for f in datafiles:
      data_url = mainsite+"/"+projectstring+"/data/"+f
      datafname2="data/"+f
      d = requests.get(data_url,timeout=1)
      with open(datafname2, "w") as outfile:
        outfile.write(d.text)
    # datastring=",".join(datafiles)
    # print(datafiles)
    # input()
    #for f in datafiles:
  npppp=studentoutfiles.count('pppp')
  nstudentoutfiles=len(studentoutfiles)-npppp
  if nstudentoutfiles>0:
    try:
      os.mkdir("output")
    except:
      pass
    file_list = glob.glob("output/*.txt")
    #print(file_list)
    for g in range(len(file_list)):
      file_list[g]=file_list[g][7:]
    #print(file_list)
    #print("---------")
    ##### Working Here!!!! ####
    for f in studentoutfiles:
      if f in file_list:
        #print (f)
        fremove="output/"+f
        #print (fremove)
        os.remove(fremove)
    #input()
  ###################################################
  if nfcases==0 and ninput==0 and nexpected==0:
    caseProblem=True
    caseProbString="Case File Error 0"
    print ("Error:\nCould not find case file for "+fname)
    print ()
    print ("Case files only exist for assignments listed below\n")
    print ("If appropriate, rename you file")
    print ()
    print ("+++++++++++++++++++++++++++")
    print ("Assignments with Case Files")
    print ("+++++++++++++++++++++++++++")    
    #print (a.text) # change this so prints 00-assigns
    #print ("Here")
    with open (assignsname) as infile:
      for line in infile:
        if line[:4]=="## f":
          print (line.strip()[8:])
        elif line[:5]=="## No":        
          print (line.strip()[3:])
        else:
          pass
  elif nfcases!=ninput or nfcases!=nexpected:
    caseProblem=True
    print ("case file error 2")
    print (str(nfcases)+"/"+str(ninput)+str+"/"+str(nexpected))
  else:
    pass
  ##################################
  #build input strings
  ##################################
  for i in range (ninput):
    inlength=expectedstart[i]-instart[i]
    for j in range (inlength-1):
      inputs[i]=inputs[i]+"\n"+casefileline[instart[i]+j]
  ##################################
  #build expected output strings
  ##################################
  for i in range (nexpected):
    if i < nexpected-1:
      outlength=casestart[i+1]-expectedstart[i]-1
      for j in range (outlength-1):
        expected[i]=expected[i]+"\n"+casefileline[expectedstart[i]+j]
    else:
      outlength=linenum-expectedstart[i]+1
      for j in range (outlength-1):
        expected[i]=expected[i]+"\n"+casefileline[expectedstart[i]+j] 
  
  ##################################
  # Create inputfiles
  ##################################
  for i in range (ninput):
    outfilename=tempstring+"input"+str(i+1)+".txt"
    #print (outfilename)
    with open (outfilename, "w") as outfile:
      outfile.write(inputs[i])
  ##################################
  # Create expected output files
  ##################################
  for i in range (nexpected):
    outfilename=tempstring+"zexpected"+str(i+1)+".txt"
    with open (outfilename, "w") as outfile:
      outfile.write(expected[i])
  
  if caseProblem==False:
    goCases=True
  try:
    with open (fname):
      pass
  except:
     print ("\nThere is no file with the name:",fname)
     print ("\nCheck file= line in settings.txt")
     goCases=False
   
  if goCases:
    noFileExistsFlag=False
    ncases=ninput
  #################################
  # Create dirs if don't exist
  ##################################
    try:
      os.mkdir(currentdir+"/tmp")
    except:
      pass
    # try:
    #   os.mkdir(currentdir+"/tmp/data")
    # except:
    #   pass
    # try:
    #   os.mkdir(currentdir+"/tmp/output")
    # except:
    #   pass
    try:
      os.mkdir("reports")
    except:
      pass

    mdstring=currentdir+"/zbkupc"
    try:
      os.mkdir(mdstring)
    except:
      pass
    mdstring=currentdir+"/zbkupc/"+shortfname
    try:
      os.mkdir(mdstring)
    except:
      pass
    sum0string=tempstring+"summary0.txt"
    with open (sum0string,"w") as sumfile0:
      sumfile0.write (hstring)
    restrictfile=tempstring+"restrictCheck.py"
    with open (fname) as infile, open (restrictfile,"w") as outfile:
      for line in infile:
        outfile.write(line) 
    for i in range (nfcases):
      checkfile=tempstring+"check"+str(i+1)+".py"
      incasefile=tempstring+"input"+str(i+1)+".txt"
      expectedfile=tempstring+"zexpected"+str(i+1)+".txt"
      outcasefile=tempstring+"output"+str(i+1)+".txt"
      with open (checkfile,"w") as outfile:
        outfile.write("import sys\n")
        outstring='infile = "'+incasefile+'"'
        outfile.write(outstring+"\n")
        outfile.write("sys.stdin = open (infile)\n") 
        outfile.write("#----------------------------------\n")    ######## if function output mode use my py file for code #######
        if functionmode=="output":
          try:
            with open (myfname) as infile:
              for line in infile:
                outfile.write(line)
          except:
            noFileExistsFlag=True
        else:
          try:
            with open (fname) as infile:
              for line in infile:
                outfile.write(line)
          except:
            noFileExistsFlag=True
    with open (fname2bash,"w") as outfile:
      outstring='STR="GO"\n'
      outfile.write(outstring)
      # outstring='echo $STR\n'
      # outfile.write(outstring)
      # outstring='read -p "Press any key to resume ..."\n'
      # outfile.write(outstring)
      for i in range (nfcases):
        checkfile=shortfname
        inputfile=tempstring+"input"+str(i+1)+".txt"
        outputfile=tempstring+"output"+str(i+1)+".txt"
        #outstring="python "+checkfile+" > "+outputfile+"\n"
        outstring="java "+shortfname+"<"+inputfile+">"+outputfile+"\n"
        outfile.write(outstring)
        outstring="if [ $? != 0 ]; then\n"
        outfile.write(outstring)
        outstring='     STR="STOP"\n'
        outfile.write(outstring)
        outstring="fi\n"
        outfile.write(outstring)
        # print (outmode)
        # input()
        if outmode=="file":
          studentstring="output/"+studentoutfiles[i]
          outstring="cat "+studentstring+">"+outputfile+"\n"
          outfile.write(outstring)

          outstring="if [ $? != 0 ]; then\n"
          outfile.write(outstring)
          outstring="     clear"+"\n"
          outfile.write(outstring)
          outstring="     echo Error: File Does Not Exist"+">"+outputfile+"\n"
          outfile.write(outstring)
          outstring="fi\n"
          outfile.write(outstring)
        #outfile.write(outstring)
        # outstring='echo $STR\n'
        # outfile.write(outstring)
        # outstring='read -p "Press any key to resume ..."\n'
        # outfile.write(outstring)
      #input()
      #if [ $STR = "STOP" ]; then
      outfile.write('if [ $STR = "GO" ];')
      outfile.write("then\n")
      outstring="   bash "+fname2bbash
      outfile.write(outstring)
      outfile.write("\nelse\n")
      outfile.write("   clear\n")
      outstring="cat "+tempstring+"summary0.txt >"+tempstring+"summary.txt\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary1.txt >>"+tempstring+"summary.txt\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary.txt > reports/"+shortfname+".txt\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary.txt > "+mdstring+"/"+shortfname+".txt\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary.txt > "+mdstring+"/"+timestring2+".txt\n"
      outfile.write(outstring)
      # #### adding backup file here
      # outstring="echo here1\n"
      # outfile.write(outstring)
      # outstring="read -p\n"
      # outfile.write(outstring)         
      outstring="cat "+fname+" > "+mdstring+"/"+timestring2+".bkp\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary.txt\n"
      outfile.write(outstring) 
      # outstring="echo here9\n"
      # outfile.write(outstring)
      outfile.write("\nfi")
      sum1string=tempstring+"summary1.txt"
      with open (sum1string,"w") as sumoutfile:
        outstring="\nTests Passed: 0.0%\n\n------------------------------\n"
        sumoutfile.write(outstring)
        sumoutfile.write('Error running "'+fname+'"')
        if functionmode!="no":
          outstring="\n\n1)Check function names are correct\n\nIf the issue persists...\n\n2)Disable 'check mode'\n3)Create your own program to test\n  your functions\n"
          sumoutfile.write(outstring)
        else:
          outstring="\n\nDisable 'check' mode to see\nregular error messages\n"
          sumoutfile.write(outstring)
        # if functionmode=="no":
        #   outstring="\n Check that function names are correct"
        #   sumoutfile.write(outstring)
        
    with open (fname3bash,"w") as outfile:
      outstring="cat "+tempstring+"summary0.txt >"+tempstring+"summary.txt\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"restrictout.txt >>"+tempstring+"summary.txt\n"
      outfile.write(outstring)      
      outstring="cat "+tempstring+"summary2.txt >>"+tempstring+"summary.txt\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary1.txt >>"+tempstring+"summary.txt\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary.txt > reports/"+shortfname+".txt\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary.txt > "+mdstring+"/"+shortfname+".txt\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary.txt > "+mdstring+"/"+timestring2+".txt\n"
      outfile.write(outstring)
      # Make backup file
      outstring="cat "+fname +" > "+mdstring+"/"+timestring2+".bkp\n"
      outfile.write(outstring)
      outstring="cat "+tempstring+"summary.txt\n"
      outfile.write(outstring) 
    if noFileExistsFlag:
      print ("/////////////////////////////////////////////")
      print ("ERROR: No file exists with the name "+fname)
      print ("/////////////////////////////////////////////")
  else:
    print ("\n*** Problem running cases ***\n")
    outstring="#Problem running cases"
    with open (fname2bash,"w") as outfile:
      outfile.write(outstring)
# Normal mode 
else:
  shortfname=fname[:-5]
  mdstring=currentdir+"/zbkupc/"+shortfname
  try:
    os.mkdir(mdstring)
  except:
    pass
  if codeFlag==False:
    pass
  elif fileFlag==False:
    pass
  elif mode=="normal":
    try:
      makebkup(currentdir)
    except:
      print("Error 55. Let your teacher know")
    try:
      try:
        with open (fname) as outfile:
          pass
      except:
        Print(f"{fname} does not exist")    
      with open (fname2bash,"w") as outfile:
        # Make backup file
        outstring="cat "+fname +" > "+mdstring+"/"+timestring2+".bkp\n"
        outfile.write(outstring)
        #outstring = "python "+fname
        outstring = "java "+shortfname        
        outfile.write(outstring)
    except:
      print (f"Error Running {fname}")
      print ("Check the file exists")
      print ("Output below may be from a previous file")
