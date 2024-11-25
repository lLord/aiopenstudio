# AI Open Studio

!([https://imgur.com/a/fbGfIa3](https://i.imgur.com/dY6nb3T.png))

git clone https://github.com/lLord/aiopenstudio.git

cd aiopenstudio

pip install -r requirements.txt


# To generate .exe

pip install pyinstaller

python -m PyInstaller --name AiOpenStudio --onefile --windowed --collect-data gradio_client --add-data=./config:./config main.py
