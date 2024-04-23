from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    primer_f = StringField('Forward Primer', validators=[DataRequired()])
    primer_r = StringField('Reverse Primer', validators=[DataRequired()])
    guide_seq = StringField('Guide Sequence and context (>=15 bp)', validators=[DataRequired()])
    orientation = StringField('Orientation', validators=[DataRequired()])
    submit = SubmitField('Design Headloop Primers')