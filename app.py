from flask import Flask, g, render_template, flash, redirect, url_for, request
import forms
import script
import models
import os

DEBUG = True
PORT = 8001
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = "a;lkdjaf;lksjdf;laksjdfa;sk"

@app.before_request
def before_request():
    """Conect to db before each request"""
    g.db = models.DATABASE
    g.db.connect()
    
@app.after_request
def after_request(response):
    """Close db connection after each req"""
    g.db.close()
    return response

@app.route('/strategy', methods = ['GET','POST'])
def strategy():
    form=forms.BaseInputsForm()
    betForm = forms.BetStrategyForm()
    if form.validate_on_submit() and betForm.validate_on_submit():
        flash("Data analyzed scroll down to check results", category='success')
        # data processing
        strategyCoeff = { 
            "L" : {
                "bet" : int(betForm.L0.data),
                "L" : {
                    "bet" : int(betForm.L1.data),
                    "L" : { 
                        "bet" : int(betForm.L22.data),
                        "W" : { 
                            "bet" : int(betForm.W33.data),
                            "W" : {
                                "bet": int(betForm.W45.data)
                            },
                            "L" : {
                                "bet": int(betForm.L46.data)
                            }
                        },
                        "L" : {  
                            "bet" : int(betForm.L34.data),
                            "W" : {
                                "bet": int(betForm.W47.data)
                            },
                            "L" : {
                                "bet": int(betForm.L48.data)
                            }
                        }  
                    },
                    "W" : { 
                        "bet" : int(betForm.W21.data),
                        "W" : {
                            "bet" : int(betForm.W31.data),
                            "W" : {
                                "bet": int(betForm.W41.data)
                            },
                            "L" : {
                                "bet": int(betForm.L42.data)
                            }
                        },
                        "L" : {
                            "bet" : int(betForm.L32.data),
                            "W" : {
                                "bet": int(betForm.W43.data)
                            },
                            "L" : {
                                "bet": int(betForm.L44.data)
                            }
                        }
                    }
                }
            }
        }

        simulationResults=script.game(0, int(form.balance.data), int(form.bet.data), 
            int(form.idlePlay.data), int(form.maxBet.data), form.strategy.data, strategyCoeff)
        try:
            models.Results.create(
                balance = simulationResults[len(simulationResults)-1]["balance"], 
                total_win = simulationResults[len(simulationResults)-1]["totalWin"],
                numberOfPlays = simulationResults[len(simulationResults)-1]["no"],
                strategy = form.strategy.data)
        except models.IntegrityError:
            print(models.IntegrityError)
            flash("DB error", category='danger')
        else:
            pass

        return render_template('strategy.html',form=form, betForm=betForm, data=simulationResults)
    return render_template('strategy.html',form=form, betForm=betForm )

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/')
def index():
    results = models.Results.select()

    if results:
        #finding best, worst score
        best = float(results[0].balance)
        worst = float(results[0].balance)
        for result in results:
            if float(result.balance) > best:
                best=float(result.balance)
            if float(result.balance) < worst:
                worst=float(result.balance)

    else:
        best = 0
        worst = 0

    return render_template('index.html', results=results, metric = {"best":best, "worst":worst})

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__=='__main__':
    models.initialize()
    #app.run(debug=DEBUG, host=HOST, port=PORT)
    app.run(debug=DEBUG)