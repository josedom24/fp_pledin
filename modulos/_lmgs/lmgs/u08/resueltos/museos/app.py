from flask import Flask, url_for,render_template,request,abort
from lxml import etree
app = Flask(__name__)   

@app.route("/")
def inicio():
	doc = etree.parse('museos.xml')
	museos=doc.xpath('//SimpleData[@name="NOMBRE"]/text()')
	ids=doc.xpath('//SimpleData[@name="FID"]/text()')
	datos=zip(ids,museos)
	return render_template("inicio.html",datos=datos)

@app.route('/museosinfo/<int:id>')
def info(id):
	doc = etree.parse('museos.xml')
	nombre=doc.xpath('//SimpleData[@name="FID" and text()="%s"]/../SimpleData[@name="NOMBRE"]/text()'%id)[0]
	telefono=doc.xpath('//SimpleData[@name="FID" and text()="%s"]/../SimpleData[@name="TELEFONO"]/text()'%id)[0]
	direccion=doc.xpath('//SimpleData[@name="FID" and text()="%s"]/../SimpleData[@name="DIRECCION"]/text()'%id)[0]
	return render_template("museos.html",nombre=nombre,direccion=direccion,telefono=telefono)

app.run(debug=True)

