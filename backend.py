from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Checkout Service Backend v1.0.0 running...'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)