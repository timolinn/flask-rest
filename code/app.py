from flask import Flask, jsonify, request, redirect, url_for

app = Flask(__name__)

stores = [
    {
        'name': 'My Store oh yeah',
        'items': [
            {
                'name': 'Nike Kits',
                'price': 17.59
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name': data['name'],
        'items': []
    }
    stores.append(new_store)
    # return jsonify(stores)
    return redirect(url_for('get_stores'))

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'store':store})
        else:
            return jsonify({'error': f'{name} not found in our database'})

@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})
    # pass

if __name__ == '__main__':
    app.run(debug=True)
