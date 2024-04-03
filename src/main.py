from flask import Flask
from api import API
from mock_db import MockDB
from prize import Prize

db = MockDB()


app = Flask(__name__)

@app.route('/api/catalog/<int:catalog_id>/prizes')
def list_prizes(catalog_id):
    api = API(db)
    prizes = api.list_prizes(catalog_id)
    if not prizes:
        return 'No prizes found within catalog_id={}.'.format(catalog_id), 404
    return prizes

@app.errorhandler(404)
def page_not_found(e):
    return 'The resource could not be found.', 404

if __name__ == '__main__':
    app.run(debug=True)