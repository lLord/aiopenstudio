# E26 IA Studio

pip install -r requirements.txt


# To generate .exe

pip install pyinstaller

python -m PyInstaller --name AISTudio --windowed --collect-data gradio_client --add-data=./config:./config main.py
