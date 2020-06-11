import json
from peewee import *
from models import db, Aircraft
from flask import (
    Flask, abort, render_template, 
    request, redirect, flash)
from forms import AircraftForm, UpdateForm, SearchForm
from db_manager import retrive_obj, create_obj, delete_obj, update_obj
from scraper.classes_task_3 import Aircraft

app = Flask(__name__)
# This is required for forms
app.config['SECRET_KEY'] = 'super secure key'

#AIRCFRATS_FILE = "global.json"


@app.route('/')
@app.route('/aircrafts')
def index():
    # Mode 1 to read one instance, mode 2 to read all instances, mode 3 to search by operator contains string
    aircrafts = retrive_obj(2,0,"")
    return render_template('aircrafts.html', aircrafts=aircrafts)


@app.route('/aircrafts/<int:aircraft_id>')
def aircraft(aircraft_id):
    try:
        # Mode 1 to read one instance, mode 2 to read all instances, mode 3 to search by operator contains string
        aircraft = retrive_obj(1, aircraft_id,"")
    except:
        abort(404)
    return render_template('aircraft.html', aircraft=aircraft)


@app.route('/aircrafts/new', methods=['GET', 'POST'])
def new_aircraft():
    form = AircraftForm()
    if request.method == 'POST' and form.validate():
        # Add new aircraft to DB
        operator = form.operator.data
        model = form.model.data
        registration = form.registration.data
        cn_fl = form.cn_fl.data
        create_obj(operator, model, registration, cn_fl)
        # Mode 1 to read one instance, mode 2 to read all instances, mode 3 to search by operator contains string
        aircrafts = retrive_obj(2,0,"")
        return redirect('/aircrafts')
    return render_template('aircraft_new_form.html', form=form)


@app.route('/aircrafts/<int:aircraft_id>/delete', methods=['GET', 'POST'])
def del_aircraft(aircraft_id):
    # Delete aircraft from DB
    try:
        delete_obj(aircraft_id)
    except:
        abort(404) 
    return redirect('/aircrafts')    


@app.route('/aircrafts/<int:aircraft_id>/update', methods=['GET', 'POST'])
def update_aircraft(aircraft_id):
    form = UpdateForm()
    if request.method == 'POST' and form.validate():
        # Add new aircraft to DB
        operator = form.operator.data
        model = form.model.data
        registration = form.registration.data
        cn_fl = form.cn_fl.data
        update_obj(aircraft_id, operator, model, registration, cn_fl)
        aircrafts = retrive_obj(2,0,"")
        return redirect('/aircrafts')
    return render_template('aircraft_update_form.html', form=form)


@app.route('/aircrafts/find', methods=['GET', 'POST'])
def find_aircraft():
    form = SearchForm()
    if request.method == 'POST' and form.validate():
        # Add new aircraft to DB
        operator = form.operator.data
        # Mode 1 to read one instance, mode 2 to read all instances, mode 3 to search by operator contains string
        aircrafts = retrive_obj(3,0,operator)
        return render_template('aircrafts.html', aircrafts=aircrafts)
    return render_template('aircraft_search_form.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
