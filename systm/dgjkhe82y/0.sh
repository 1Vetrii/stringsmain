# 0.sh ver 1.01
clear
#echo You are here1
script_full_path=$(dirname "$0")
#python $script_full_path/cup.py $script_full_path
STR="GO"
python $script_full_path/dtct.py $script_full_path
#read -p "Press [Enter] key to start backup..."
LANG=$?
echo $LANG
if [ $LANG = 101 ];then
  echo Going to run Python...
  bash $script_full_path/1.sh
elif [ $LANG = 102 ];then
  echo Going to run Java...
  bash $script_full_path/1j.sh
else
  echo error 500
fi




# if [ $? != 0 ]; then
#      STR="STOP"
#      #read -p "Press [Enter] key to start backup..."
# fi
# if [ $STR = "GO" ];then
#   #read -p "Press [Enter] key to start backup..."
#   python $script_full_path/gf.py $script_full_path
#   #read -p "Press [Enter] key to start backup..."
#   bash $script_full_path/2.sh
#   #read -p "Press [Enter] key to start backup..."
# else
#   echo Error 001
# fi