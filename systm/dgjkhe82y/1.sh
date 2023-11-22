# 1.sh ver 3.01
clear
script_full_path=$(dirname "$0")
#python $script_full_path/cup.py $script_full_path
STR="GO"
python $script_full_path/up.py $script_full_path
#read -p "Press [Enter] key to start backup..."
if [ $? != 0 ]; then
     STR="STOP"
     #read -p "Press [Enter] key to start backup..."
fi
if [ $STR = "GO" ];then
  #read -p "Press [Enter] key to start backup..."
  python $script_full_path/gf.py $script_full_path
  #read -p "Press [Enter] key to start backup..."
  bash $script_full_path/2.sh
  #read -p "Press [Enter] key to start backup..."
else
  echo Error 001
fi

