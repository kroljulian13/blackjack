from flask import Flask, render_template, flash, redirect, url_for, request
import forms
import script

DEBUG = True
PORT = 8001
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = "a;lkdjaf;lksjdf;laksjdfa;sk"

@app.route('/strategy', methods = ['GET','POST'])
def strategy():
    form=forms.BaseInputsForm()
    betForm = forms.BetStrategyForm()
    if form.validate_on_submit() and betForm.validate_on_submit():
        flash("Data analyzed scroll down to check results", category='success')
        # data processing
        playerStrategy = { 
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
            int(form.idlePlay.data), int(form.maxBet.data), form.strategy.data, playerStrategy)

        return render_template('strategy.html',form=form, betForm=betForm, data=simulationResults)
    return render_template('strategy.html',form=form, betForm=betForm )

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)