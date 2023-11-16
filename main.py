# [START app]
import logging

# [START imports]
from flask import Flask, request
from flask import jsonify
from google.cloud import spanner
import google.oauth2.id_token
import google.auth.transport.requests
import os

# [END imports]

# [START create_app]
app = Flask(__name__)
HTTP_REQUEST = google.auth.transport.requests.Request()
# [END create_app]

# [START create_spanner]
spanner_client = spanner.Client()
instance_id = os.getenv("SPANNER_INSTANCE")
database_id = os.getenv("SPANNER_DATABASE")
# [END create_spanner]

def getMailFromToken(token):
    if(token == ""):
        return None
    token = token.split(" ").pop()
    try:
        claims = google.oauth2.id_token.verify_firebase_token(
            token, HTTP_REQUEST, audience=os.environ.get("GOOGLE_CLOUD_PROJECT")
        )
        return claims["email"] if claims else None
    except ValueError as e:
        logging.error(f'Error verifying token: {e}')
        return None

@app.route("/isAdmin")
def isAdmin():
    user_token = request.args.get('token')
    user_mail = str(getMailFromToken(user_token))
    if not user_mail:
        return jsonify(is_admin=False)
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