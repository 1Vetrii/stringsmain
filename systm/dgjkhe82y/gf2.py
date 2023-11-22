# gf2.py v210207.1
#print("here85")
########################
#comparecases
########################
#print("starting compare cases")
import os
import sys
import fnmatch
import requests
currentdir=sys.argv[1]
mainsite="https://testingcases.davidhunter1.repl.co"
#projectstring="3C-01-Intro"
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
  print("Project Name not set in ??.txt")
######################################
tempstring=currentdir+"/tmp/"
casefname=tempstring+"cases.txt"
casenames=[]
calls=[]
ncases=0
linenum=0
functionmode="no"
tfname="none"
outmode="screen"
studentoutfiles=[]
nstudentouts=0
maxlines="1,10"
##########################
# get info from settings.txt
##########################
with open ("settings.txt") as infile:
  for line in infile:
    if line.strip()[0:6]=="#file=":
      fname=line.strip()[6:]
    if line.strip()[0:7]=="# file=":
      fname=line.strip()[7:]
    if line.strip()[0:8]=="# file =":
      fname=line.strip()[8:]
    if line.strip()[0:13]=="#reportlines=":
      maxlines=line.strip()[13:]
    if line.strip()[0:14]=="# reportlines=":
      maxlines=line.strip()[14:]
    if line.strip()[0:15]=="# reportlines =":
      maxlines=line.strip()[15:]
dot=fname.find(".")
shortfname=fname[:dot]
##########################
# check line #'s are valid
##########################
# print (maxlines)
# print (type(maxlines))
if maxlines=="all":
  maxlines=[1,10000]
else:
  try:
    maxlines=maxlines.split(",")
  except:
    maxlines=[1,10]
if len(maxlines)!=2:
  maxlines=[1,10]
maxlines[0]=int(maxlines[0])
maxlines[1]=int(maxlines[1])
if maxlines[0]<1:
  maxlines[0]=1
if maxlines[1]<maxlines[0]+1:
  maxlines[1]=maxlines[0]+10
minline=maxlines[0]
maxline=maxlines[1]
# print(minline)
# print(maxline)
#input()
###############################
#examine case file
###############################
with open(casefname) as infile:
  for line in infile:
    if line.strip()[0:5]=="case=":
      casenames.append(line.strip()[5:])
      ncases=ncases+1
      studentoutfiles.append('p') 
    if line[:13]=="FUNCTIONMODE=":
              functionmode=line.strip()[13:]
    if line.strip()[0:8]=="OUTMODE=":
        outmode=line.strip()[8:]
    if line.strip()[0:15]=="studentoutfile=":
        studentoutfiles[ncases-1]=line.strip()[15:]
        nstudentouts=nstudentouts+1    
    # if line.strip()[0:6]=="TFILE=":
    #     tfname=line.strip()[6:]   
if len(outmode)==0 or outmode!="file":
  outmode="screen"
  minline=1
  maxline=10000

#print(studentoutfiles)
#input()
###############################
# getcalls function
###############################
def getcalls(x):
  callsfname=tempstring+"teacher.py"
  callstring="none"
  with open(callsfname) as infile:
    all=infile.read()
    lookingfor="case=="+str(x)
    start=all.find(lookingfor)
    if start!=-1:
      start=start+len(lookingfor)+1
    end=all.find("elif case=="+str(x+1))
    if end==-1:
      end=len(all)
    callstring=all[start:end].strip("\n")
    return(callstring)
###################################
# get expected files (if file mode)
###################################
if outmode=="file":
  #print ("copying files")
  url_stem = mainsite+"/"+projectstring+"/"+"expectedfiles/"+shortfname+"/"
  #print (url_stem)
  #copyname=tempstring+fname
  for i in range(ncases):
    expfname="expected"+str(i+1)+".txt"
    data_url=url_stem+expfname
    #print(data_url)
    copyfname=tempstring+"z"+expfname
    #print(copyfname)
    r = requests.get(data_url)
    with open(copyfname, "w") as f:
      f.write(r.text)

#input()


    
# print(getcalls(3))  #     print(line.rstrip())
# input()
#print (functionmode)
#input()
countf=0
countp=0
# nInput=len(fnmatch.filter(os.listdir(tempstring), 'input*.txt'))
# print(nInput)
# print(ncases)
# with open(callsfname) as infile:
#   for line in infile:
#     print(line)

#input()
nInput=ncases
resultfile=tempstring+"summary1.txt"
with open(resultfile,"w") as rfile:
  #print(nInput)
  for i in range(nInput):
    countout=0
    countexp=0
    expectedfile=tempstring+"zexpected"+str(i+1)+".txt"
    outputfile=tempstring+"output"+str(i+1)+".txt"
    inputfile=tempstring+"input"+str(i+1)+".txt"
    with open(inputfile,"r") as ifile, open(outputfile,"r") as ofile, open(expectedfile, "r")as efile:
      inputstring=ifile.readlines()
      outstring=ofile.readlines()
      noutlines=len(outstring)
      #print (outstring)
      outstring2=outstring.copy()
      outstring2.append("\n")
      expectedstring=efile.readlines()
      nexplines=len(expectedstring)
      lenexpected=len(expectedstring)
      expectedstring2=expectedstring.copy()
      expectedstring2[lenexpected-1]=expectedstring2[lenexpected-1]+"\n"
      hidden=False
      #print(noutlines)
      #print(nexplines)
      shownumlines=False
      linebad=["" for x in outstring]
      if noutlines!=nexplines:
        shownumlines=True
      else:
        #linebad=["" for x in outstring]
        #print (linebad)
        for k in range (noutlines):
          if outstring[k]!=expectedstring[k]:
            linebad[k]=" <---"
        if outstring[k]==expectedstring[k]+"\n":
            linebad[k]=""          
        # print(linebad)
        # input()
      #input()
      # print (casenames)
      # print (i)
      # print (casenames[0])
      # input()
      casename=casenames[i]
      if "Hidden" in casename or "hidden" in casename:
        hidden=True
        casename="Hidden Test Case"
      if outstring==expectedstring or outstring==expectedstring2:
        result ="PASS"
        countp=countp+1
        rstring="-----------------------------------\n"
        rfile.write(rstring)
        rstring=("Test "+str(i+1)+ " - "+result+"\n")
        rfile.write(rstring)
      else:
        result="FAIL"
        countf=countf+1
        rstring="-----------------------------------\n"
        rfile.write(rstring)
        if casename=="":
          rstring=("Test "+str(i+1)+ " - "+result+"\n")
        else:  
          rstring=("Test "+str(i+1)+ " - "+casename+" - "+result+"\n")
        rfile.write(rstring)
      if result=="FAIL" and hidden==False:
        if functionmode!="no":
          rstring="***** Function Calls *****\n"
          rfile.write(rstring)
          rfile.write(getcalls(i+1))          
        if functionmode=="no":
          rstring="***** Input *****\n"
          rfile.write(rstring)
          for line in inputstring:
            rfile.write(line)
        for line in outstring:
          countout=countout+len(line)

        if outmode=="file":
          sfilename=studentoutfiles[i]
          rstring="\n**** Output ("+sfilename+") "
          nstars=36-len(rstring)
          if nstars <0:
            nstars =0
          rstring=rstring+"*"*nstars+"\n"     
        else:
          rstring="\n**** Your Output (console) ********\n"
        rfile.write(rstring)
        if outmode=="file":
          rfile.write("**** Line "+str(minline)+" to Line "+str(maxline)+"   "+"*"*(12-len(str(maxline)))+"\n")
        if shownumlines==True:
          rfile.write("     [ "+str(noutlines)+" lines ]             <---\n")
        linenum=0
        for line in outstring:
          linenum=linenum+1
          ######if linenum>maxlines:
          if linenum>=minline and linenum<=maxline:
            rstring1=line.strip('\n')
            rstring2=" ("+str(len(line))+")"+linebad[linenum-1]              
            rstring=rstring1+rstring2+"\n"
            rfile.write(rstring)
           
        for line in expectedstring:
          countexp=countexp+len(line)
        rfile.write("-"*35+"\n")        
        if outmode=="file":
          rstring="**** Expected Output (file) *******\n"        
        else:
          rstring="**** Expected Output (console) ****\n"
        rfile.write(rstring)
        if outmode=="file":
          rfile.write("**** Line "+str(minline)+" to Line "+str(maxline)+"   "+"*"*(12-len(str(maxline)))+"\n")
        if shownumlines==True:        
          rfile.write("     [ "+str(nexplines)+" lines ]\n")
        linenum=0  
        for line in expectedstring:
          linenum=linenum+1
          if linenum>=minline and linenum<=maxline:
            rstring1=line.strip('\n')
            rstring2=" ("+str(len(line))+")" 
            rstring=rstring1+rstring2
            rfile.write(rstring+"\n")   
numtests=countp+countf
sum2file=tempstring+"summary2.txt"
with open(sum2file,"w") as sum2:
  wstring="\nTests Passed: "+str(round((countp/numtests),2)*100)+" %\n"
  sum2.write(wstring)
  wstring="Passed:       "+str(countp)+"/"+str(numtests)+" tests\n"
  sum2.write(wstring)
