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

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/termsofuse')
def termsofuse():
    return render_template('termsofuse.html')

@app.route('/privacypolicy')
def privacypolicy():
    return render_template('privacypolicy.html')



# Guardrail Delineators 

@app.route('/akt/traffic_signal_lenses')
def traffic_signal_lenses():
    return render_template('/akt/traffic_signal_lenses.html')

@app.route('/akt/c1001az')
def c1001az():
    return render_template('/akt/c1001az.html')

@app.route('/akt/no18CenterMountDelineator')
def no18CenterMountDelineator():
    return render_template('/akt/no18CenterMountDelineator.html')

@app.route('/akt/567_guardrail_delineator')
def guardrail_delineator():
    return render_template('/akt/567_guardrail_delineator.html')

@app.route('/akt/181_guardrail_delineator')
def guardrail_delineator_181():
    return render_template('/akt/181_guardrail_delineator.html')



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





# emb series 

@app.route('/reflectors/EBMT')
def EBMT():
    return render_template('/reflectors/EBMT.html')

@app.route('/reflectors/EBM3x4')
def EBM3x4():
    return render_template('/reflectors/EBM3x4.html')

@app.route('/reflectors/EBM3x3')
def EBM3x3():
    return render_template('/reflectors/EBM3x3.html')

@app.route('/reflectors/EBM3x8')
def EBM3x8():
    return render_template('/reflectors/EBM3x8.html')



# GRD SERIES

@app.route('/reflectors/GRD_S')
def GRD_S():
    return render_template('/reflectors/GRD_S.html')

@app.route('/reflectors/GRD_C')
def GRD_C():
    return render_template('/reflectors/GRD_C.html')

@app.route('/reflectors/GRD_H')
def GRD_H():
    return render_template('/reflectors/GRD_H.html')

@app.route('/reflectors/GRD_ST')
def GRD_ST():
    return render_template('/reflectors/GRD_ST.html')

@app.route('/reflectors/GRD_FLEX')
def GRD_FLEX():
    return render_template('/reflectors/GRD_FLEX.html')




# reflective panels 

@app.route('/reflectivepanels/rivetpanel18x18')
def rivetpanel18x18():
    return render_template('/reflectivepanels/rivetpanel18x18.html')

@app.route('/reflectivepanels/rivetpanel5x11')
def rivetpanel5x11():
    return render_template('/reflectivepanels/rivetpanel5x11.html')

@app.route('/reflectivepanels/aluminum4x15')
def aluminum4x15():
    return render_template('/reflectivepanels/aluminum4x15.html')

@app.route('/reflectivepanels/panel3x12')
def panel3x12():
    return render_template('/reflectivepanels/panel3x12.html')

@app.route('/reflectivepanels/square4x4')
def square4x4():
    return render_template('/reflectivepanels/square4x4.html')


@app.route('/akt/WY_101285')
def WY_101285():
    return render_template('/akt/WY_101285.html')

@app.route('/akt/aluminumangle4x4')
def aluminumangle4x4():
    return render_template('/akt/aluminumangle4x4.html')

