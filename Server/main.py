from flask import Flask, request
from flask_cors import CORS 
import subprocess
app = Flask(__name__) 
  

app = Flask(__name__)
CORS(app)

@app.route('/') 
def index(): 
    cmd = request.args.get('cmd')
    print(f"{request.environ.get('HTTP_X_REAL_IP', request.remote_addr)} ran command {cmd}")
    return subprocess.check_output([cmd])
  
if __name__ == '__main__': 
    app.run(debug=True, port=5000)
