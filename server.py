from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

#ceļš uz about
@app.route('/about',methods = ['POST', 'GET'])
def about():
    return render_template("about.html")

#testiņš
@app.route('/tets',methods = ['POST', 'GET'])
def tets():
    parametri=["IQ","Augums","Kājas izmērs"]
    return render_template("tets.html", parametri=parametri)
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "Viss labii"

if __name__ == '__main__':
  app.run(debug="true")
