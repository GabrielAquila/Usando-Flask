from flask import Flask, request, render_template

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
            return render_template("resultado_soma.html", resultado_soma=soma)

        elif (request.args['ope'] == 'div'):
            div = float(request.args["a"]) / float(request.args["b"])
            return render_template("resultado_div.html", resultado_div=div)

        elif (request.args['ope'] == 'sub'):
            sub = int(request.args["a"]) - int(request.args["b"])
            return render_template("resultado_sub.html", resultado_sub=sub)

        elif (request.args['ope'] == 'mult'):
            mult = int(request.args["a"]) * int(request.args["b"])
            return render_template("resultado_mult.html", resultado_mult=mult)

    except ZeroDivisionError:
        return render_template('error_zero.html', error=('divisão por 0'))
    except ValueError:
        return render_template('erro_value.html', error_value=('Parametro passado nao é valido'))
    except Exception:
        return render_template('erro_exception.html', error=('Valor Invalido, Favor enviar o valor novamente'))

        # return ("os parametros preenchidos via form aparecem no dicionario request.args" +
        #         "<br>  Se voce acessou sem preencher o form, essa variavel é um dicionário" +
        #         "<br>  Vazio <br>" +
        #         str(request.args))  (MEU COMENTARIO: Rever return se é necessario mesmo, senao, tira fora!)


app.run(debug=True)
