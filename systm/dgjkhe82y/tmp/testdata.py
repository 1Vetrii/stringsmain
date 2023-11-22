fname="data/wordlist1.txt"
#fname="data/wordlistz.txt"
outname="output/wordsout.txt"
with open (fname) as infile, open (outname, "w") as outfile:
  for line in infile:
    if line[0]=='c':
      outfile.write(line)