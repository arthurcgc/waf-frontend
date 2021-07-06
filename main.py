from parse import parse
from forms import CreateWafForm, DeleteWafForm, UpdateWafForm
from flask import Flask, flash
from flask import render_template
import requests
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ['SECRET_KEY']
waf_api = os.environ['WAF_API_URL']

@app.route('/create', methods=["GET", "POST"])
def create():
    form = CreateWafForm()
    if form.validate_on_submit():
        payload = {
            "name": form.name.data,
            "namespace": form.namespace.data,
            "plan": form.planName.data,
            "bind": {
                "serviceName": form.bindSvcName.data,
                "namespace": form.bindNamespace.data,
            },
            "replicas": form.replicas.data
        }
        if form.customRules.data != None:
            filename = secure_filename(form.customRules.data.filename)
            path = 'uploads/' + filename
            form.customRules.data.save(path)
            customRulesList = parse(path)
            payload["rules"] = {
                "customRules": customRulesList
            }
            os.remove(path) 
        if form.removeRules.data != None:
            if "rules" in payload:
                payload["rules"]["removeAfter"] = {
                        "removeByTag": form.removeRules.data
                    }
            else:
                payload["rules"] = {
                    "removeAfter": {
                        "removeByTag": form.removeRules.data
                    }
                }
        r = requests.post(waf_api, json=payload)
        if r.status_code == 201:
            flash(f"Successfully created {form.name.data}!", "success")
        else:
            flash("Error: " + r.text, "danger")
    return render_template('create.html', form=form)

@app.route('/delete', methods=["GET", "POST"])
def delete():
    form = DeleteWafForm()
    if form.validate_on_submit():
        payload = {
            "name": form.name.data,
            "namespace": form.namespace.data
        }
        r = requests.delete(waf_api, json=payload)
        if r.status_code == 200:
            flash(f"Successfully deleted {form.name.data}!", "success")
        else:
            flash("Error: " + r.text, "danger")
    return render_template('delete.html', form=form)

@app.route('/update', methods=["GET", "POST"])
def update():
    form = UpdateWafForm()
    if form.validate_on_submit():
        payload = {
            "name": form.name.data,
            "namespace": form.namespace.data,
            "plan": form.planName.data,
            "bind": {
                "serviceName": form.bindSvcName.data,
                "namespace": form.bindNamespace.data,
            },
            "replicas": form.replicas.data
        }
        if form.customRules.data != None:
            filename = secure_filename(form.customRules.data.filename)
            path = 'uploads/' + filename
            form.customRules.data.save(path)
            customRulesList = parse(path)
            payload["rules"] = {
                "customRules": customRulesList
            }
            os.remove(path) 
        else:
            payload["rules"] = {
                "customRules": []
            }
        if form.removeRules.data != None:
            if "rules" in payload:
                payload["rules"]["removeAfter"] = {
                        "removeByTag": form.removeRules.data
                    }
            else:
                payload["rules"] = {
                    "removeAfter": {
                        "removeByTag": form.removeRules.data
                    }
                }
        r = requests.put(waf_api, json=payload)
        if r.status_code == 201:
            flash(f"Successfully updated {form.name.data}!", "success")
        else:
            flash("Error: " + r.text, "danger")
    return render_template('update.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)