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

@app.route("/isAdmin")
def isAdmin():
    user_mail = request.args.get('mail')
    database = spanner_client.instance(instance_id).database(database_id)
    with database.snapshot() as snapshot:
        cursor = snapshot.execute_sql(
            "SELECT is_admin FROM user WHERE mail = @userMail;",
            params={"userMail": user_mail},
            param_types={"userMail": spanner.param_types.STRING})

    results_list=  list(cursor)
    is_admin = results_list[0][0] if results_list else False
    return jsonify(is_admin=is_admin)

# [END app]