# E26 IA Studio

git clone https://github.com/lLord/iastudio.git

cd iastudio

pip install -r requirements.txt


# To generate .exe

pip install pyinstaller

python -m PyInstaller --name AISTudio --windowed --collect-data gradio_client --add-data=./config:./config main.py
