from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf.file import FileField
from flask_wtf.file import FileAllowed
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length

class CreateWafForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=15)])
    namespace = StringField("Namespace", validators=[DataRequired(), Length(min=3, max=15)])
    replicas = IntegerField("Replicas", validators=[DataRequired()])
    planName = StringField("Plan", validators=[DataRequired(), Length(min=3, max=15)])
    bindSvcName = StringField("Service Name", validators=[DataRequired(), Length(min=3, max=15)])
    bindNamespace = StringField("Service Namespace", validators=[DataRequired(), Length(min=3, max=15)])
    bindProtocol = SelectField("Protocol",choices=["http", "https"], validators=[DataRequired()])
    customRules = FileField("Custom Rules", validators=[FileAllowed(["conf"], "Only .conf files allowed")])
    submit = SubmitField("Create")

class DeleteWafForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=15)])
    namespace = StringField("Namespace", validators=[DataRequired(), Length(min=3, max=15)])
    submit = SubmitField("Delete")

class UpdateWafForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=15)])
    namespace = StringField("Namespace", validators=[DataRequired(), Length(min=3, max=15)])
    replicas = IntegerField("Replicas", validators=[DataRequired()])
    planName = StringField("Plan", validators=[DataRequired(), Length(min=3, max=15)])
    bindSvcName = StringField("Service Name", validators=[DataRequired(), Length(min=3, max=15)])
    bindNamespace = StringField("Service Namespace", validators=[DataRequired(), Length(min=3, max=15)])
    bindProtocol = SelectField("Protocol",choices=["http", "https"], validators=[DataRequired()])
    customRules = FileField("Custom Rules", validators=[FileAllowed(["conf"], "Only .conf files allowed")])
    submit = SubmitField("Update")
