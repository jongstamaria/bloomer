from flask import Flask, request, jsonify, url_for
import pymysql, pymysql.cursors, dbconnect
import simplejson as json

app = Flask(__name__)
app.config["DEBUG"] = True
application = app # our hosting requires application in passenger_wsgi

#--- display tour_trips base on google place id ----#
@app.route('/menucategories', methods=['GET'])
def menucategories():

    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    
    try:
        conn = dbconnect.getConnection()
        cur = conn.cursor()
        cur.execute("SELECT * 
            FROM menu_categories 
            WHERE client_id = %s", id)
        result = cur.fetchall()
        #return jsonify(result)
        return json.dumps(result)
        
    except Exception as e:
        return(str(e))
