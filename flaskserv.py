from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    open('Invoice1234.zip','wb').write(request.data)
    return {'code' : 200} 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
