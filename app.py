from flask import Flask, render_template


#Generar el servidor (Front-end)
servidorFront = Flask(__name__)

#Colocar la IP de su instancia virtual y verificar el puerto
serverData={"ip":"52.54.162.201","port":8081}

@servidorFront.route("/formulario",methods=['GET'])
def formulario():
    return render_template('pagina.html',server=serverData)

if __name__ == '__main__':
    servidorFront.run(debug=False,host='0.0.0.0',port='8082')