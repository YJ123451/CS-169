import flask
from flask import Flask, render_template


app = Flask(__name__,
           template_folder='main',
            static_folder='main/static',
           static_url_path = '/static')

@app.route('/')
def welcome():
  return render_template('index.html')

@app.route('/mainpage')
def main_page():
  return render_template('mainpage.html')
  



if __name__ == '__main__':
  app.run(host = '0.0.0.0', port= 500, debug=True)