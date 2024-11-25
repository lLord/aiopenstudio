# AI Open Studio

![[AI IOpen Studio Interface]](https://i.imgur.com/dY6nb3T.png)

git clone https://github.com/lLord/aiopenstudio.git

cd aiopenstudio

pip install -r requirements.txt


# To generate a executable

pip install pyinstaller

python -m PyInstaller --name AiOpenStudio --onefile --windowed --collect-data gradio_client --add-data=./config:./config main.py
