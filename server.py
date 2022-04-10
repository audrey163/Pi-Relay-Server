from relay import Relay
from flask import Flask, request

app = Flask(__name__) #init flask app
r = Relay() #init GPIO-Relay handler

@app.route('/')
def index(): #this is good just to make sure the server is up
    return 'ready'

@app.route('/high', methods = ['GET'])
def high():
    ch = request.args.get('ch')
    if ch in [ str(i) for i in range(1,9) ]:
        r.high(ch)
        return 'success'
    return 'error'

@app.route('/low', methods = ['GET'])
def low():
    ch = request.args.get('ch')
    if ch in [ str(i) for i in range(1,9) ]:
        r.low(ch)
        return 'success'
    return 'error'

if __name__ == '__main__':
    app.run(debug=False, port=420, host='0.0.0.0')
