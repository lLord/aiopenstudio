# AI Open Studio

![IA Studio Interface](https://imgur.com/a/fbGfIa3)

git clone https://github.com/lLord/aiopenstudio.git

cd aiopenstudio

pip install -r requirements.txt


# To generate .exe

pip install pyinstaller

python -m PyInstaller --name AiOpenStudio --onefile --windowed --collect-data gradio_client --add-data=./config:./config main.py
