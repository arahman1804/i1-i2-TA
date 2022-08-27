from flask import Flask, render_template, request, flash
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np


app = Flask(__name__)
app.secret_key = 'super secret'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        membaca		= request.form['membaca']
        ziadah		= request.form['ziadah']
        murajaah 	= request.form['murajaah']
        qiraah		= request.form['qiraah']
        tajwid		= request.form['tajwid']
        k 			= request.form['k']

        if not membaca:
            flash('Berapa kali anda membaca ?','warning')
            return render_template('base.html')
        if not ziadah:
            flash('Berapa kali anda ziadah ?','warning')
            return render_template('base.html')
        if not murajaah:
            flash('Berapa kali anda murajaah ?','warning')
            return render_template('base.html')
        if not qiraah:
            flash('Berapa kali anda qiraah ?','warning')
            return render_template('base.html')
        if not tajwid:
            flash('Berapa kali anda qiraah ?','warning')
            return render_template('base.html')
        if not k:
            flash('Silahkan tentukan jarak ke tetanggaan','warning')
            return render_template('base.html')

        membaca		= int(membaca)
        ziadah		= int(ziadah)
        murajaah    = int(murajaah)
        qiraah 		= int(qiraah)
        tajwid		= int(tajwid)
        k 			= int(k)

        x, y = read_dataset()
        knn=KNeighborsClassifier(n_neighbors=k, metric='euclidean')
        knn.fit(x,y)
        y_pred = knn.predict([[membaca,ziadah,murajaah,qiraah,tajwid]])

        return render_template('base.html',prediksi=y_pred)

    return render_template('base.html')

@app.route('/dataset')
def dataset():
	items = pd.read_csv('dataset.csv')
	items = pd.DataFrame(items)
	return render_template('dataset.html',items=items.to_html(classes='table table-striped table-hover table-bordered table-sm table-responsive-sm'))

def read_dataset():
    x = pd.read_csv('dataset.csv')

    datax = x.iloc[:, [0,1,2,3,4]].values
    datay = x.iloc[:, [-1]].values

    return datax, datay

if __name__ == '__main__':
	app.run(debug=True, port=5000)