## Package import:
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
#
from flask_mysqldb import MySQL

# PURPOSE: Explicitly define which columns are displayed per table
DISPLAY_COLUMNS = {
    "virus": [
        "virus_id",
        "name",
        "family",
        "genome_type",
        "ncbi_taxid",
        "ncbi_tax_url",   # will be hidden but used for linking
    ],
    "genome_sequence": [
        "sequence_id",
        "virus_id",
        "accession",
        "length",
        "sequence",
        "ncbi_nuccore_url",  # hidden but used for linking
    ],
}


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

# This shows example Flask routes that match the navbar links and templates.

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# PURPOSE:
# Render tables.html showing only selected columns per table.

@app.route("/tables")
def tables():
    cur = mysql.connection.cursor()

    allowed_tables = ["virus", "genome_sequence"]
    tables = []

    for table in allowed_tables:
        cols = DISPLAY_COLUMNS[table]
        col_sql = ", ".join(f"`{c}`" for c in cols)

        cur.execute(f"SELECT {col_sql} FROM `{table}`;")
        rows = cur.fetchall()

        tables.append({
            "name": table,
            "columns": cols,
            "rows": rows,
        })
    cur.close()

    return render_template("tables.html", tables=tables)



# PURPOSE: Add a simple Plotly bar chart showing the number of search hits per table.
# Install once: pip install plotly

import json
import plotly.graph_objects as go

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    scope = request.args.get("scope", "all").strip().lower()

    ALLOWED_TABLES = ["virus", "genome_sequence"]

    if scope in ALLOWED_TABLES:
        tables_to_search = [scope]
    else:
        tables_to_search = ALLOWED_TABLES

    tables = []
    chart_json = None  # will hold the Plotly figure JSON for the template

    if query:
        like_value = f"%{query}%"
        cur = mysql.connection.cursor()

        for table in tables_to_search:
            display_cols = DISPLAY_COLUMNS[table]

            search_cols = [c for c in display_cols if c not in ["ncbi_tax_url", "ncbi_nuccore_url"]]
            select_clause = ", ".join(f"`{c}`" for c in display_cols)
            where_clause = " OR ".join(f"`{c}` LIKE %s" for c in search_cols)

            sql = f"""
                SELECT {select_clause}
                FROM `{table}`
                WHERE {where_clause}
                LIMIT 100
            """
            cur.execute(sql, [like_value] * len(search_cols))
            rows = cur.fetchall()

            if rows:
                tables.append({
                    "name": table,
                    "columns": display_cols,
                    "rows": rows,
                })

        cur.close()

        # Build a minimal Plotly bar chart: number of hits per table
        if tables:
            labels = [t["name"] for t in tables]
            counts = [len(t["rows"]) for t in tables]

            fig = go.Figure(
                data=[go.Bar(x=labels, y=counts)]
            )
            fig.update_layout(
                title="Search hits per table",
                xaxis_title="Table",
                yaxis_title="Number of matches",
                margin=dict(l=40, r=20, t=50, b=40),
                height=320,
            )

            chart_json = fig.to_json()

    return render_template("search.html", q=query, scope=scope, tables=tables, chart_json=chart_json)


#http://127.0.0.1:5000//api/testing?q=sars

# This route tests your API setup by returning a very simple JSON object.
# Put it in app.py and make sure you import jsonify above.

# from flask import jsonify

# @app.route("/api/testing", methods=["GET"])
# def testing_api():
#     data = {
#         "status": "ok",
#         "message": "API is reachable",
#     }
#     return jsonify(data)


# but in JSON form for the REST API.
@app.route("/api/testing", methods=["GET"])
def testing_api():
    query = request.args.get("q", "").strip()

    # Example: same TABLE_CONFIG as your /testing route
    TABLE_CONFIG = {
        "virus": {
            "search":  ["virus_id", "name"],
            "display": ["virus_id", "name", "family"],
        },
        # add other tables...
    }

    results = []

    if query:
        like_value = f"%{query}%"
        cur = mysql.connection.cursor()  # dict rows → nicer JSON

        for table_name, cfg in TABLE_CONFIG.items():
            search_cols = cfg["search"]
            display_cols = cfg["display"]

            select_clause = ", ".join(f"`{col}`" for col in display_cols)
            where_clauses = " OR ".join(f"`{col}` LIKE %s" for col in search_cols)

            sql = f"SELECT {select_clause} FROM `{table_name}` WHERE {where_clauses} LIMIT 100"
            params = [like_value] * len(search_cols)
            cur.execute(sql, params)
            rows = cur.fetchall()   # rows is now a list of dicts

            if rows:
                results.append({
                    "table": table_name,
                    "columns": display_cols,
                    "rows": rows,
                })

        cur.close()

    # This is plain JSON-serializable data: dict → list → dicts → strings/ints/etc.
    payload = {
        "query": query,
        "results": results,
    }

    return jsonify(payload)



app.run(debug=True)
