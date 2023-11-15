# [START app]
import logging

# [START imports]
from flask import Flask, request
from flask import jsonify
from google.cloud import spanner
import os
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]

# [START create_spanner]
spanner_client = spanner.Client()
instance_id = os.getenv("SPANNER_INSTANCE")
database_id = os.getenv("SPANNER_DATABASE")
# [END create_spanner]

@app.route("/")
def main():
    database = spanner_client.instance(instance_id).database(database_id)
    with database.snapshot() as snapshot:
        cursor = snapshot.execute_sql("SELECT * FROM user;")
    results = list(cursor)

    return results

