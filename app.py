import os
import boto3
import hashlib

from chalice import Chalice, Response, BadRequestError
from chalice import NotFoundError

# Setup
app = Chalice(app_name='url-shortener')
app.debug = True

DDB = boto3.client('dynamodb')

@app.route('/', methods=['POST'], content_types=['application/json'])
def index():
   # Grab request url
    url = app.current_request.json_body.get('url', '')
    if not url:
        raise BadRequestError("Missing URL")

    # Generate unique 6 character token
    token = hashlib.md5(url.encode('utf-8')).hexdigest()[:6]

    # Store in dynamodb
    DDB.put_item(TableName=os.environ['APP_TABLE_NAME'],
                 Item={'token': {'S': token},
              'url': {'S': url}})

    return {'shortened': token, "url": url}

@app.route('/{token}', methods=['GET'])
def retrieve(token):
    # Retrieve url from dynamodb
    try:
        record = DDB.get_item(Key={'token': {'S': token}},
                              TableName=os.environ['APP_TABLE_NAME'])
    except Exception as e:
        raise NotFoundError(token)

    return Response(status_code=301,
                    headers={'Location': record['Item']['url']['S']},
                    body='')
 