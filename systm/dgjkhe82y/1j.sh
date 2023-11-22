#echo about to run Java now
clear
script_full_path=$(dirname "$0")
STR="GO"
#javac test.java
javac J200helloworld.java
if [ $? != 0 ]; then
     STR="STOP"
fi
if [ $STR = "GO" ];then
  #echo $script_full_path
  #java J200helloworld<$script_full_path/aaa/input.txt>$script_full_path/aaa/output.txt
  python $script_full_path/gfj.py $script_full_path
  bash $script_full_path/2.sh
else
  echo Execution Halted
fi