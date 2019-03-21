from flask import Flask, url_for,render_template,request,abort
app = Flask(__name__)   


	
@app.route("/calculadora",methods=["GET","POST"])
def calculadora():
	if request.method=="GET":
		return render_template("inicio.html")
	else:
		try:
			num1=int(request.form["num1"])
			num2=int(request.form["num2"])
		except:
			abort(404)
		op=request.form["operacion"]
		if op=="sumar":
			resultado=num1+num2
			signo="+"
		elif op=="restar":
			resultado=num1-num2
			signo="-"
		elif op=="multiplicar":
			resultado=num1*num2
			signo="*"
		elif op=="dividir" and num2!=0:
			resultado=num1/num2
			signo="/"
		else:
			abort(404)
		return render_template("operar.html",numero1=num1,numero2=num2,operacion=op,signo=signo,resultado=resultado)		





app.run(debug=True)

