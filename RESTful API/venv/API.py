##python -m venv venv
##source venv/bin/activate  # On Windows use `venv\Scripts\activate`


from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields  
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app, version='1.0', title='Flask API', description='A simple Flask API')
auth = HTTPBasicAuth()

users = {
    "admin": "password"
}

@auth.get_password
def get_pw(username):
    return users.get(username)

ns = api.namespace('items', description='Item operations')

item_model = api.model('Item', {
    'id': fields.Integer(required=True, description='The item identifier'),
    'name': fields.String(required=True, description='The item name')
})

items = []

@ns.route('/')
class ItemList(Resource):
    @ns.doc('list_items')
    @ns.marshal_list_with(item_model)
    def get(self):
        return items

    @ns.doc('create_item')
    @ns.expect(item_model)
    @ns.marshal_with(item_model, code=201)
    def post(self):
        item = api.payload
        items.append(item)
        return item, 201

@ns.route('/<int:id>')
@ns.response(404, 'Item not found')
@ns.param('id', 'The item identifier')
class Item(Resource):
    @ns.doc('get_item')
    @ns.marshal_with(item_model)
    def get(self, id):
        item = next((item for item in items if item['id'] == id), None)
        if item:
            return item
        api.abort(404)

    @ns.doc('delete_item')
    @ns.response(204, 'Item deleted')
    def delete(self, id):
        global items
        items = [item for item in items if item['id'] != id]
        return '', 204

    @ns.expect(item_model)
    @ns.marshal_with(item_model)
    def put(self, id):
        item = next((item for item in items if item['id'] == id), None)
        if item:
            data = api.payload
            item.update(data)
            return item
        api.abort(404)

@app.route('/secure-data')
@auth.login_required
def get_secure_data():
    return "This is protected data, {}!".format(auth.username())

if __name__ == '__main__':
    app.run(debug=True)
