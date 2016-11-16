import os
from flask import Flask, jsonify
from faker import Factory
from redis import StrictRedis

app = Flask(__name__)
fake = Factory.create()
redis_host = os.environ.get('REDIS_HOST', 'localhost')
r = StrictRedis(host=redis_host, port=6379, db=0)

def get_item_name(item_id):
    item_key = "item_master:{}".format(item_id)
    item_name = r.get(item_key)
    if not item_name:
        item_name = fake.word()
        r.set(item_key, item_name)
    else:
        item_name = item_name.decode('utf-8')
    return item_name


@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item_name = get_item_name(item_id)
    return jsonify(itemId=item_id, itemName=item_name)
