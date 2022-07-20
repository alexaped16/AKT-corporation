from app import app, db
from flask import redirect, render_template, url_for, flash


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',  title=title)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/product_line')
def product_line():
    return render_template('product_line.html')


@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/sister_companies')
def sister_companies():
    return render_template('sister_companies.html')



#AKT

@app.route('/akt/traffic_signal_lenses')
def traffic_signal_lenses():
    return render_template('/akt/traffic_signal_lenses.html')

@app.route('/akt/no18CenterMountDelineator')
def no18CenterMountDelineator():
    return render_template('/akt/no18CenterMountDelineator.html')

@app.route('/akt/567_guardrail_delineator')
def guardrail_delineator():
    return render_template('/akt/567_guardrail_delineator.html')

@app.route('/akt/181_guardrail_delineator')
def guardrail_delineator_181():
    return render_template('/akt/181_guardrail_delineator.html')

@app.route('/akt/aluminum_backer')
def aluminum_backer():
    return render_template('/akt/aluminum_backer.html')

@app.route('/akt/bituminous_pavement_marker_adhesive')
def bituminous_pavement_marker_adhesive():
    return render_template('/akt/bituminous_pavement_marker_adhesive.html')

@app.route('/akt/prismatic_retroreflective_pavement_marker')
def prismatic_retroreflective_pavement_marker():
    return render_template('/akt/prismatic_retroreflective_pavement_marker.html')

@app.route('/akt/concrete_barrier_wall_marker')
def concrete_barrier_wall_marker():
    return render_template('/akt/concrete_barrier_wall_marker')

@app.route('/akt/butyl_pads')
def butyl_pads():
    return render_template('/akt/butyl_pads.html')

@app.route('/akt/JD_1')
def JD_1():
    return render_template('/akt/JD_1.html')

@app.route('/akt/pavement_marker_921')
def pavement_marker_921():
    return render_template('/akt/pavement_marker_921.html')



# REFLECTORS 

@app.route('/reflectors/EBMT')
def EBMT():
    return render_template('/reflectors/EBMT.html')

@app.route('/reflectors/EBM3x4')
def EBM3x4():
    return render_template('/reflectors/EBM3x4.html')

@app.route('/reflectors/GRD-S')
def GRD_S():
    return render_template('/reflectors/GRD-S.html')


