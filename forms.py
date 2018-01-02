from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import (DataRequired, Regexp, ValidationError, 
                                 Length, EqualTo)


class BaseInputsForm(FlaskForm):
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


class BetStrategyForm(FlaskForm):
    L0 = StringField(
        'L0', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    L1 = StringField(
        'L1', 
        default="4",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    W21 = StringField(
        'W21', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    L22 = StringField(
        'L22', 
        default="8",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    W31 = StringField(
        'W31', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    L32 = StringField(
        'L32', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    W33 = StringField(
        'W33', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    L34 = StringField(
        'L34', 
        default="16",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    W41 = StringField(
        'W41', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    L42 = StringField(
        'L42', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    W43 = StringField(
        'W43', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    L44 = StringField(
        'L44', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    W45 = StringField(
        'W45', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    L46 = StringField(
        'L46', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    W47 = StringField(
        'W47', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])
    L48 = StringField(
        'L48', 
        default="1",
        validators = [ 
            DataRequired(), 
            Regexp( r'^[0-9]+$', message = "Only integer numbers !")
            ])