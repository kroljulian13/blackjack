from flask import Flask, render_template, flash, redirect, url_for
import forms
import script

DEBUG = True
PORT = 8001
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = "a;lkdjaf;lksjdf;laksjdfa;sk"



@app.route('/strategy', methods = ['GET','POST'])
def strategy():
    form=forms.InputsForm()
    if form.validate_on_submit():
        flash("Data analyzed", category='success')
        # data processing
        # print(form.strategy.data)
        data=script.game(0, int(form.balance.data), int(form.bet.data), 
            int(form.idlePlay.data), int(form.maxBet.data), form.strategy.data)

        return render_template('strategy.html',form=form, data=data)
    return render_template('strategy.html',form=form)


@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)