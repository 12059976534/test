from flask import Flask,escape,request,render_template, redirect, url_for,flash
from flask import jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource,Api
from flask_cors import CORS
import gmailouth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:wahyu355@localhost/json'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# inisisasi objek resfull
api = Api(app)
# inisiasi objeck cors
CORS(app)




class Content(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(80),nullable=False)
    ket = db.Column(db.Text())
    isi = db.Column(db.Text())
    status = db.Column(db.Integer)


   


# global pariable untuk POST method
identitas={}

@app.route('/index',methods=['POST','GET'])
def index():
   if request.method=='POST':

      judul=request.form['judul']
      keterangan=request.form['keterangan']
      isi=request.form['isi']
      save=Content(
         judul=judul,
         ket=keterangan,
         isi=isi,
         status=1
      )
      db.session.add(save)
      db.session.commit()
      flash("berhasil upload data")
      return redirect(url_for('index'))
   return render_template('index.html')

# class resource
class Exampleresource(Resource):

   data=Content.query.all()
   lis=[]
   for data in data:
      lis.append({"id":data.id,"judul":data.judul,"ket":data.ket,"isi":data.isi})
   
   # method 'GET' dan 'POST'
   def get(self):
      return self.lis

   def post(self):
      judul=request.form["judul"]   
      ket=request.form["ket"]
      isi=request.form["isi"]

      identitas['judul']=judul
      identitas['ket']=ket
      identitas['isi']=isi

      respons={"msg":"berhasil"}
      return respons
   
api.add_resource(Exampleresource, "/api", methods=['GET','POST'])          
   



@app.route('/',methods=['GET','POST'])
def method_name():
    return redirect(url_for('index'))

d={}
def post():
   judul=request.form["judul"]   
   ket=request.form["ket"]
   isi=request.form["isi"]
   
   d['judul']=judul
   d['ket']=ket
   d['isi']=isi

   save=Content(judul=judul,ket=ket,isi=isi,status=1)
   db.session.add(save)
   db.session.commit()

   print("judul=",judul)
   print("ket=",ket)
   print("judul=",isi)

   a={"selamat":"you can acces my data "}
   return jsonify(a)

@app.route('/json', methods=['POST','GET'])
def json():
   js=Content.query.all()
   dat=[]
   b={"da":"imissyou","beri":"foryou"}
   for i in js:
      dat.append({"id":i.id,"judul":i.judul,"ket":i.ket,"isi":i.isi})
   if request.method=='POST':
      return post()

   return jsonify(dat)

@app.route('/auth',methods=['POST','GET'])
def auth():
   if request.method=='POST':
      email = request.form['email']

                 
      for a in range(5):
         su="FUTUR.COM/COMFIRMATION"
         t='harap tidak membagi token anda ke siapapun Komfirmasi token untuk mempalidasi acount ' + gmailouth.get_random_string(4) +' Adalah token akun anda '
         e="jekomontainugrah@gmail.com"
         a=gmailouth.log(su,t,e)
      print(email)
      
      return redirect(url_for("auth"))
      
   return render_template('auth.html')   

   

app.run(debug=True,port=5000,host='0.0.0.0')