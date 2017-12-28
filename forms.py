from flask_wtf import Form

from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, 
                                 Length, EqualTo)



class InputsForm(Form):
    balance = StringField(
        'balance', 
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Balance should be only integer numbers")
            ])
    bet = StringField(
        'bet', 
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Bet should be only integer numbers")
            ])
    idlePlay = StringField(
        'idlePlay', 
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = " idlePlay should be only integer numbers")
            ])
    maxBet = StringField(
        'maxBet', 
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = " maxBet should be only integer numbers")
            ])