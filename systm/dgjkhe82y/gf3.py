# gf3.py v210207.1
import os
import sys
import fnmatch
language = 'nolanguage'
comment = "x"
extension ="py"
fname='nofilename'
bannedstring=""
banned=[]
limitstring=""
limitlist=[]
limitword=[]
limitnum=[]
limitcount=[]
atleaststring=""
atleastlist=[]
atleastword=[]
atleastnum=[]
atleastcount=[]
requiredstring=""
requiredlist=[]
requiredcount=[]
functionmode="no"
functionlist=[]

currentdir=sys.argv[1]
tempstring=currentdir+"/tmp/"
casefname=tempstring+"cases.txt"
restrictoutfile=tempstring+"restrictout.txt"
sum1file=tempstring+"summary1.txt"
sum2file=tempstring+"summary2.txt"
###############################
#Use this for headings
###############################
goFlag=True
try:
    with open(casefname,"r") as infile:
        dummycount=0
except:
    goFlag=False
    with open (restrictoutfile,"w") as outfile:
        outfile.write('Error Code 15')
        outfile.write("\n+++++++++++++++++++++++++++++++++++\n")
        outfile.write("\nCHECK MODE HALTED...\n")
        outstring="\nReview Restrictions in Assignment\n"
        outfile.write(outstring)
        outfile.write("\nTests Passed: 0.0 %\n")
        with open (sum1file, "w") as out1file:
            outfile.write("")
        with open (sum2file, "w") as out1file:
            outfile.write("")
rname="restrictCheck.py"
fname=tempstring+rname
try:
    with open (fname,"r") as tryfile:
        dummycount=0
except:
    goFlag=False
    with open (restrictoutfile,"w") as outfile:
        outfile.write('Error Code 16')
        outfile.write("\n+++++++++++++++++++++++++++++++++++\n")
        outfile.write("\nCHECK MODE HALTED...\n")
        outstring="\nReview Restrictions in Assignment\n"
        outfile.write(outstring)
        outfile.write("\nTests Passed: 0.0 %\n")
        with open (sum1file, "w") as out1file:
            outfile.write("")
        with open (sum2file, "w") as out1file:
            outfile.write("")            

if goFlag:
  with open(casefname,"r") as infile:
      for line in infile:
          if line[:7]=='BANNED=':
              bannedstring = (line[7:].strip())
              banned.extend(bannedstring.split(","))
          if line[:7]=='LIMITS=':
              limitstring = (line[7:].strip())
              limitlist.extend(limitstring.split(","))
          if line[:8]=='ATLEAST=':
              atleaststring = (line[8:].strip())
              atleastlist.extend(atleaststring.split(","))
          if line[:9]=='REQUIRED=':
              requiredstring = (line[9:].strip())
              requiredlist.append(requiredstring)
          if line[:13]=="FUNCTIONMODE=":
              functionmode=line.strip()[13:]
          if line.strip()[0:10]=="FUNCTIONS=":
              functionlist=line.strip()[10:].split(",")
#  print(functionlist)
#   input() 
  limitword=limitlist[::2]
  limitnum=limitlist[1::2]
  atleastword=atleastlist[::2]
  atleastnum=atleastlist[1::2]
  if extension == 'py':
      language='python'
      comment="#"
  elif extension == 'java':
      language='java'
      comment='//'
  bancount=0
  numlimits=len(limitword)
  overlimit=0
  numatleasts=len(atleastword)
  underlimit=0
  numrequired=len(requiredlist)
  missing=0
  for i in range(len(banned)):
    if banned[i]=="comma":
      banned[i]=","
  with open (restrictoutfile,"w") as outfile:
  #eeeeeeeeee---check student file for banned strings---eeeeeeeeee
      linenum=0
      clength=len(comment)
      with open (fname,"r") as infile:
          message="\n"
          for line in infile:
              linenum=linenum+1
              stripline=line.strip()
              if stripline[0:clength]!=comment:
                  for word in banned:
                      if word in stripline:
                          message = message+"Line "+str(linenum)+": "+line+"\n"
                          bancount=bancount+1
      if bancount>0:
          outfile.write("Banned Strings are:\n")
          outfile.write(str(banned)+"\n\n")
          outfile.write(str(bancount)+" banned string(s) found\n")
          outfile.write(message)
          outfile.write("\n+++++++++++++++++++++++++++++++++++\n")
          outfile.write("\nCHECK MODE HALTED...\n")
          outstring="\nReview Restrictions in Assignment\n"
          outfile.write(outstring)
          outfile.write("\nTests Passed: 0.0 %\n")
          with open (sum1file, "w") as out1file:
            outfile.write("")
          with open (sum2file, "w") as out1file:
            outfile.write("")
          exit(3)
  #ffffffff---check student file for limited strings---ffffffffffff
      for i in range(numlimits):
          limitcount.append(0)

      with open (fname,"r") as infile:
          linenum=0
          for line in infile:
              linenum=linenum+1
              stripline=line.strip()
              if stripline[0:clength]!=comment:
                  for i in range(numlimits):
                      checkString = stripline.count(limitword[i])
                      limitcount[i]=limitcount[i]+checkString

      for i in range(numlimits):
          numword = limitcount[i]
          limit = int(limitnum[i])
          if numword>limit:
              overlimit=overlimit+1
              outfile.write ("Limit of "+str(limit)+" exceeded: '"+limitword[i]+"' ("+str(numword)+" occurences)"+"\n")
      if overlimit>0:
          outfile.write("\n")
          outfile.write("\n+++++++++++++++++++++++++++++++++++\n")
          outfile.write("\nCHECK MODE HALTED...\n")
          outstring="\nReview Restrictions in Assignment\n"
          outfile.write(outstring)
          outfile.write("\nTests Passed: 0.0 %\n")
          with open (sum1file, "w") as out1file:
            outfile.write("")
          with open (sum2file, "w") as out1file:
            outfile.write("")   
          exit(4)
  #gggggg---check student file for at least strings---gggggggggggg
      for i in range(numatleasts):
          atleastcount.append(0)

      with open (fname,"r") as infile:
          linenum=0
          for line in infile:
              linenum=linenum+1
              stripline=line.strip()
              if stripline[0:clength]!=comment:
                  for i in range(numatleasts):
                      checkString = stripline.count(atleastword[i])
                      atleastcount[i]=atleastcount[i]+checkString

      for i in range(numatleasts):
          numword = atleastcount[i]
          minimum = int(atleastnum[i])
          if numword<minimum:
              underlimit=underlimit+1
              outfile.write ("Minimum of "+str(minimum)+" not met: '"+atleastword[i]+"' ("+str(numword)+" occurences)"+"\n")
      if underlimit>0:
          outfile.write("\n")
          outfile.write("\n+++++++++++++++++++++++++++++++++++\n")
          outfile.write("\nCHECK MODE HALTED...\n")
          outstring="\nReview Restrictions in Assignment\n"
          outfile.write(outstring)
          outfile.write("\nTests Passed: 0.0 %\n")
          with open (sum1file, "w") as out1file:
            outfile.write("")
          with open (sum2file, "w") as out1file:
            outfile.write("")      
          exit(5)
  #hhhhhh---check student file for required strings-----hhhhh
      for i in range(numrequired):
          requiredcount.append(0)

      with open (fname,"r") as infile:
          linenum=0
          for line in infile:
              linenum=linenum+1
              stripline=line.strip()
              if stripline[0:clength]!=comment:
                  for i in range(numrequired):
                      if requiredlist[i]==stripline:
                          requiredcount[i]=requiredcount[i]+1
      for i in range(numrequired):
          num = requiredcount[i]
          if num!=1:
              missing=missing+1
      if missing==1:
          outfile.write ("Required Line Missing: \n")
          for i in range(numrequired):
              num = requiredcount[i]
              if num!=1:
                  outfile.write (requiredlist[i]+"\n")
      if missing>1:
          outfile.write ("Required Lines Missing: \n")
          for i in range(numrequired):
              num = requiredcount[i]
              if num!=1:
                  outfile.write (requiredlist[i]+"\n")
      if missing>0:
          outfile.write("\n")
          outfile.write("\n+++++++++++++++++++++++++++++++++++\n")
          outfile.write("\nCHECK MODE HALTED...\n")
          outstring="\nReview Restrictions in Assignment\n"
          outfile.write(outstring)
          outfile.write("\nTests Passed: 0.0 %\n")
          with open (sum1file, "w") as out1file:
            outfile.write("")
          with open (sum2file, "w") as out1file:
            outfile.write("")   
          exit(6)
  #iiiii---check that only has definitions---iiiiii
      #print (functionmode)
      #input()
      if functionmode !="no":
        with open (fname,"r") as infile:
          AllGood=True
          for line in infile:
            lineGood=False
            if line[0:3]=="def" or line[0]=="#" or line[0]==" " or line=="\n":
              #print ("Line Good")
              lineGood=True
            else:
              pass
              #print ("Line Not Good")
              #print (line)  
            if lineGood==False:
              #print(line)
              AllGood=False
        if AllGood==False:
          #print("Error: File should contain only function definitions")
          outfile.write("\n")
          outfile.write("\n+++++++++++++++++++++++++++++++++++\n")
          outfile.write("\nCHECK MODE HALTED...\n")
          outstring="\nRemove all lines outside functions\n"
          outfile.write(outstring)
          outfile.write("\nTests Passed: 0.0 %\n")
          with open (sum1file, "w") as out1file:
            outfile.write("")
          with open (sum2file, "w") as out1file:
            outfile.write("")  
          exit(7)
  # #jjjjj---check that has required functions---jjjjj
  #     AllGood=True
  #     print(functionlist)
  #     numfuncs=len(functionlist)
  #     existfuncs= [0 for i in range (numfuncs)]
  #     deffuncs=["def "+x for x in functionlist]
  #     print (numfuncs)
  #     print (existfuncs)
  #     print (deffuncs)
  #     missinglist=[]
  #     #input()
  #     for lookfor in deffuncs:
  #       funcGood=False
  #       #print (lookfor)
  #       looklength=len(lookfor)
  #       #print(looklength)
  #       with open (fname,"r") as infile:
  #         for line in infile:
  #           if line[:looklength]==lookfor:
  #             funcGood=True  
  #       if funcGood==False:
  #         AllGood=False
  #         missinglist.append(lookfor)
        
  #       # AllGood=True
  #       # for line in infile:
  #     print (missinglist)
  #       #   pass
  #     input()
  #     if AllGood==False:
  #       #print("Error: File should contain only function definitions")
  #       outfile.write("\n")
  #       outfile.write("\n+++++++++++++++++++++++++++++++++++\n")
  #       outfile.write("\nCHECK MODE HALTED...\n")
  #       outstring="\nRemove all lines outside functions\n"
  #       outfile.write(outstring)
  #       outfile.write("\nTests Passed: 0.0 %\n")
  #       with open (sum1file, "w") as out1file:
  #         outfile.write("")
  #       with open (sum2file, "w") as out1file:
  #         outfile.write("")  
  #       exit(8)
      
      