STR="GO"
python systm/dgjkhe82y/tmp/check1.py > systm/dgjkhe82y/tmp/output1.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check2.py > systm/dgjkhe82y/tmp/output2.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check3.py > systm/dgjkhe82y/tmp/output3.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check4.py > systm/dgjkhe82y/tmp/output4.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check5.py > systm/dgjkhe82y/tmp/output5.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check6.py > systm/dgjkhe82y/tmp/output6.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check7.py > systm/dgjkhe82y/tmp/output7.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
if [ $STR = "GO" ];then
   bash systm/dgjkhe82y/2b.sh
else
   clear
cat systm/dgjkhe82y/tmp/summary0.txt >systm/dgjkhe82y/tmp/summary.txt
cat systm/dgjkhe82y/tmp/summary1.txt >>systm/dgjkhe82y/tmp/summary.txt
cat systm/dgjkhe82y/tmp/summary.txt > reports/415paragraph.txt
cat systm/dgjkhe82y/tmp/summary.txt > systm/dgjkhe82y/zbkupc/415paragraph/415paragraph.txt
cat systm/dgjkhe82y/tmp/summary.txt > systm/dgjkhe82y/zbkupc/415paragraph/231122-111342.txt
cat 415paragraph.py > systm/dgjkhe82y/zbkupc/415paragraph/231122-111342.bkp
cat systm/dgjkhe82y/tmp/summary.txt

fi