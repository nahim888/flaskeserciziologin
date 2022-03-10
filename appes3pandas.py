from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import pandas as pd
regionicapoluoghi = pd.read_xlsx("regionicapoluoghi.xlsx")

@app.route('/risp', methods=['GET'])
def risp():
    return render_template('error.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)