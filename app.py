import sqlite3 as sql
from flask import Flask, render_template, g
from datetime import datetime, date, timedelta

app = Flask(__name__)

DATABASE = "flaskr/ferme_3_chenes.sqlite"


# connect to database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
        db.row_factory = sql.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# querying data
def query_db(query, args=(), one=False):
    cursor = get_db().execute(query, args)
    data = cursor.fetchall()
    cursor.close()
    return (data[0] if data else None) if one else data


@app.route('/')
def home():

    def chart1():
        data_graph = query_db("SELECT date, id FROM velages")
        labels = []
        for day in range(1, 29):
            labels.append(f'Jour {day}')
        values = [0] * 28
        total = 0
        epoch = datetime.utcfromtimestamp(0)
        for data in data_graph:
            tmp_date = int(((datetime.strptime(data['date'], "%d/%m/%Y") - epoch).total_seconds() // 86400) % 28)
            values[tmp_date] += 1
            total += 1
        for entry in range(len(values)):
            values[entry] = (values[entry] / total) * 100
        return labels, values
    labels_graph1, values_graph1 = chart1()

    def chart2():
        data_graph = query_db("SELECT date, id FROM velages WHERE id in (SELECT animal_id FROM animaux_velages WHERE animal_id in (SELECT id FROM animaux WHERE mort_ne is 1))")
        epoch = datetime.utcfromtimestamp(0)
        labels = [epoch - timedelta(days=x) for x in range(365)]
        for date_entry in range(len(labels)):
            labels[date_entry] = datetime.strftime(labels[date_entry], "%d/%m")
        labels.append("01/01")
        labels.pop(0)
        labels.reverse()
        values = [0] * 365
        for data in data_graph:
            tmp_date = int(((datetime.strptime(data['date'], "%d/%m/%Y") - epoch).total_seconds() // 86400) % 365)
            values[tmp_date] += 1
        return labels, values
    labels_graph2, values_graph2 = chart2()

    def chart3():
        data_graph = query_db("SELECT date,id FROM velages WHERE (id in (SELECT animal_id FROM animaux_velages WHERE velage_id in (SELECT id FROM velages WHERE pere_id is 5002))) or (id in (SELECT animal_id FROM animaux_velages WHERE velage_id in (SELECT id FROM velages WHERE id in (SELECT id FROM velages WHERE pere_id IS 2 or 4 or 38 or 40 or 44 or 48))))")
        epoch = datetime.utcfromtimestamp(0)
        values = [0] * 12
        for data in data_graph:
            tmp_date = int(((datetime.strptime(data['date'], "%d/%m/%Y") - epoch).total_seconds() // 1036800) % 12)
            values[tmp_date] += 1
        return values
    values_graph3 = chart3()

    def chart4():
        data_graph = query_db("SELECT date, id FROM velages WHERE id in (SELECT animal_id FROM animaux_velages WHERE animal_id in (SELECT id FROM animaux WHERE decede is 1))")
        epoch = datetime.utcfromtimestamp(0)
        labels = labels_graph2
        values = [0] * 365
        for data in data_graph:
            tmp_date = int(((datetime.strptime(data['date'], "%d/%m/%Y") - epoch).total_seconds() // 86400) % 365)
            values[tmp_date] += 1
        return labels, values
    labels_graph4, values_graph4 = chart4()

    return render_template("index.html",
                           labels=[labels_graph1, labels_graph2, labels_graph4],
                           values=[values_graph1, values_graph2, values_graph3, values_graph4])


if __name__ == '__main__':
    app.run()
