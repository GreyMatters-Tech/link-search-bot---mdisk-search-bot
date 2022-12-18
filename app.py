from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'GreyMatters'


if __name__ == "__main__":
    app.run()

os.system("git clone -b test https://github.com/Greymattersbot/link-search-bot---mdisk-search-bot okk && cd okk && pip3 install -U -r requirements.txt && gunicorn app:app && python3 main.py &")
