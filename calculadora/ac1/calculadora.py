from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return "verifique a URL /calc e /resultado"

@app.route("/calc")
def exibe_calculadora():
    return render_template("calculadora.html")

@app.route("/resultado")
def resultado():
    try: 
            
        if (request.args['ope'] == 'soma'):
            soma = int(request.args["a"]) + int(request.args["b"])
            return render_template("resultado.html", resultado = soma )

        elif (request.args['ope'] == 'div'):
            div = float(request.args["a"]) / float(request.args["b"])
            return f'sua divisão é {div}'
   
        elif (request.args['ope'] == 'sub'):
            sub = int(request.args["a"]) - int(request.args["b"])
            return f'sua subtração é {sub}'
        
        elif (request.args['ope'] == 'mult'):
            mult = int(request.args["a"]) * int(request.args["b"])
            return f'sua multiplicação é {mult}' 

    except ZeroDivisionError:
        return render_template('error.html', error = ('divisão por 0'))
    except ValueError:
        return 'ERRO : Enviei um parametro inválido, esperava um ERRO'
    except Exception :
        return 'ERRO : Enviei dados incompletos (faltava ope) e esperava um ERRO'

        return ("os parametros preenchidos via form aparecem no dicionario request.args"+ 
            "<br>  Se voce acessou sem preencher o form, essa variavel é um dicionário" +
            "<br>  Vazio <br>" +  
            str(request.args))



app.run(debug=True) 
