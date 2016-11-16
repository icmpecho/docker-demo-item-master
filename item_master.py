from flask import Flask, jsonify
from faker import Factory

app = Flask(__name__)
fake = Factory.create()


@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item_name = fake.word()
    return jsonify(itemId=item_id, itemName=item_name)
