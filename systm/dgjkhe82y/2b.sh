script_full_path=$(dirname "$0")
#read -p "3Press [Enter] key to start backup..."
python $script_full_path/gf2.py $script_full_path
#read -p "4Press [Enter] key to start backup..."
python $script_full_path/gf3.py $script_full_path
#read -p "5Press [Enter] key to start backup..."
bash $script_full_path/3.sh
#read -p "6Press [Enter] key to start backup..."
python $script_full_path/gf9.py $script_full_path
#read -p "6Press [Enter] key to start backup..."