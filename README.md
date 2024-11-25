# AI Open Studio

![IA Studio Interface](https://i.imgur.com/QK4nurC.png)

git clone https://github.com/lLord/iastudio.git

cd iastudio

pip install -r requirements.txt


# To generate .exe

pip install pyinstaller

python -m PyInstaller --name AiSTudio --onefile --windowed --collect-data gradio_client --add-data=./config:./config main.py
