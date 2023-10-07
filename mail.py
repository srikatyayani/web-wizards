from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    # Process the data and return a response
    response = {'message': 'Data received', 'data': data}
    return jsonify(response)

if _name_ == '_main_':
    app.run(debug=True)