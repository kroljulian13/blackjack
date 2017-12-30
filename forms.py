from flask_wtf import Form

from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import (DataRequired, Regexp, ValidationError, 
                                 Length, EqualTo)


class InputsForm(Form):
    balance = StringField(
        'Balance', 
        default="1000",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Balance should be only integer numbers")
            ])
    bet = StringField(
        'Bet', 
        default="10",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Bet should be only integer numbers")
            ])
    idlePlay = StringField(
        'IdlePlay', 
        default="5",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = " idlePlay should be only integer numbers")
            ])
    maxBet = StringField(
        'MaxBet', 
        default="100",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = " maxBet should be only integer numbers")
            ])
    strategy = RadioField(
        'Strategy',
        choices=[
            ("hiloActive", 'Hi-Lo'), 
            ("betStrategyActive",'Bet Strategy'),
            ("noStrategy", 'No strategy')],
        default="hiloActive", 
    )
    # hiloActive = BooleanField(
    #     'HiloActive',
    #     default="checked"
    #     )
    # betStrategyActive = BooleanField(
    #     'BetStrategyActive',
    #     ) 