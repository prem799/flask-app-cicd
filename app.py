from flask import Flask, render_template, request

app = Flask(__name__)

# Define a simple in-memory database
database = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    # Retrieve data from the request form
    name = request.form.get('name')
    description = request.form.get('description')

    # Create a new item and add it to the database
    item = {'name': name, 'description': description}
    database.append(item)

    return render_template('success.html')

@app.route('/items')
def items():
    return render_template('items.html', items=database)

if __name__ == '__main__':
    app.run(debug=True)