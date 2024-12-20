from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config['SECRET_KEY']='1234'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'


@app.route('/')
def home():
    return render_template("main-real.html")

@app.route('/contact-us')
def contact_us():
    return render_template("contact-us-link.html")

@app.route('/general')
def general():
    return render_template("general-link.html")

@app.route('/one-apartment')
def one_apartment():
    return render_template("one-apartment.html")

@app.route('/two-apartment')
def two_apartment():
    return render_template("two-apartment.html")

@app.route('/parking')
def parking():
    return render_template("parking.html")

@app.route('/video-tour')
def video_tour():
    return render_template("video-tour.html")

@app.route('/see-fotos-1-1')
def see_fotos_1_1():
    return render_template("fotos-1-1.html")

@app.route('/see-fotos-2-1')
def see_fotos_2_1():
    return render_template("fotos-2-1.html")

@app.route('/see-fotos-3-1')
def see_fotos_3_1():
    return render_template("fotos-3-1.html")

@app.route('/see-fotos-4-1')
def see_fotos_4_1():
    return render_template("fotos-4-1.html")


@app.route('/see-fotos-1-2')
def see_fotos_1_2():
    return render_template("fotos-1-2.html")

@app.route('/see-fotos-2-2')
def see_fotos_2_2():
    return render_template("fotos-2-2.html")

@app.route('/see-fotos-3-2')
def see_fotos_3_2():
    return render_template("fotos-3-2.html")

