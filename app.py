from flask import flask
app = Flask(__name__)
@app.route('/')
def sample():
    return 'This is a sample python application for docker integration'
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')