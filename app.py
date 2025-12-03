## Package import:
from flask import Flask, render_template, request
from flask_mysqldb import MySQL


# initialize flask
app = Flask(__name__)
app.debug = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'viral_user'
app.config['MYSQL_PASSWORD'] = 'B%$RYNGQNq4$kJ%'
app.config['MYSQL_DB'] = 'viral_db'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)


@app.route("/")
def home():
    # Renders templates/home.html
    return render_template("home.html")


@app.route("/results")
def results():
    cur = mysql.connection.cursor()

    # 1. Get all table names
    cur.execute("SHOW TABLES;")
    table_names = [row[0] for row in cur.fetchall()]

    tables = []

    for table in table_names:
        # 2. Query each table
        cur.execute(f"SELECT * FROM `{table}`;")
        rows = cur.fetchall()

        # 3. Get column names for that table
        colnames = [desc[0] for desc in cur.description]

        tables.append({
            "name": table,
            "columns": colnames,
            "rows": rows
        })

    cur.close()

    # 4. Send everything to the template
    return render_template("results.html", tables=tables)


@app.route("/testing")
def testing():
    cur = mysql.connection.cursor()

    table_names = [
        "virus",
        "protein_sequence",
        "genome_sequence",
        "enzyme_annotation",
    ]

    tables = []

    for name in table_names:
        cur.execute(f"SELECT * FROM `{name}`;")
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]

        tables.append({
            "name": name,
            "columns": colnames,
            "rows": rows
        })

    cur.close()

    return render_template("testing.html", tables=tables)
