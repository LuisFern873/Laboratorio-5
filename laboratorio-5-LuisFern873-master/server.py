from flask import Flask, render_template

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/name/<name>', methods=['GET'])
def ejemplo(name):
    return f"Hola, {name}"

def invert(x):
    n = str(x)
    Newn = ''
    for i in range(len(n)-1,-1,-1):
        Newn += n[i]
    return Newn

@app.route('/palindromo/<palabra>', methods=['GET'])
def ejercicio1(palabra):
    if palabra == invert(palabra):
        return f"{palabra} es palíndromo"
    return f"{palabra} no es palíndromo"

@app.route('/operaciones/<a>/<b>', methods=['GET'])
def ejercicio2(a,b):
    sum = int(a)+int(b)
    res = int(a)-int(b)
    mul = int(a)*int(b)
    div = int(a)//int(b)
    return f"{a}+{b}={sum}____{a}-{b}={res}____{a}*{b}={mul}____{a}/{b}={div}"  

@app.route('/ordenar/<a>/<b>/<c>', methods=['GET'])
def ejercicio3(a,b,c):
    list = [a,b,c]
    list.sort()
    return f"{list[0]},{list[1]},{list[2]}"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))

# cd C:\c++\laboratorio-5-LuisFern873-master> python server.py