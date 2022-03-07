from flask import Flask,render_template,request,redirect,url_for
import time
import server 

app = Flask(__name__)

@app.route("/")
def Index():
   return render_template('index.html')

@app.route('/template',methods=["POST"])
def template():
   error = None
   if request.method == 'POST':
      template = request.form['template']
      url = server.server(template)
      if url != None:
         return redirect(url)
      else:
         return "Error Server"
   else:
      return "seleect a template"
if "__main__"==__name__:
   print("Starter Server ...")
   time.sleep(1)
   app.run(debug=True,host="192.168.0.105",port=5555)



