echo about to run Java now
clear
#javac -classpath .:target/dependency/* -d . $(find . -type f -name '*.java')
#java -classpath .:target/dependency/* Main

script_full_path=$(dirname "$0")
#python $script_full_path/pytest01.py $script_full_path
#python pytest02.py
STR="GO"
javac -classpath .:target/dependency/* -d . $(find . -type f -name '*.java')
#read -p "Press [Enter] key to start backup..."
if [ $? != 0 ]; then
     STR="STOP"
     #read -p "Press [Enter] key to start backup..."
fi
if [ $STR = "GO" ];then
  #read -p "Press [Enter] key to start backup..."
  java -classpath .:target/dependency/* Main
  #read -p "Press [Enter] key to start backup..."
  #bash $script_full_path/2.sh
  #read -p "Press [Enter] key to start backup..."
else
  echo Execution Halted
fi