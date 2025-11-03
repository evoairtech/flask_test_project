from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from forms import TextForm

app = Flask(__name__)
app.secret_key = 'nekuv_kluch'  # Required for session and CSRF

# Home route
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# About route
@app.route('/about')
def about():
    return "This is the About Page."

# WTForms route (optional)
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = TextForm()
    if form.validate_on_submit():
        session['my_text'] = form.UserInput.data
        return redirect(url_for('result'))
    return render_template('form.html', form=form)

# Result route for WTForms (optional)
@app.route('/result')
def result():
    text = session.get('my_text', 'No data submitted yet.')
    session.pop('my_text', None)
    return render_template('results.html', my_text=text)

# Simple JSON GET route
@app.route('/api/info')
def api_info():
    return jsonify({"message": "Hello from Flask!", "status": "success"})

# Dynamic JSON route handling GET & POST
@app.route('/api/calc', methods=['GET', 'POST'])
def api_calc():
    if request.method == 'GET':
        x = request.args.get('x', type=int, default=0)
        y = request.args.get('y', type=int, default=0)
        name = request.args.get('name', default='Guest')
        total = x + y
        product = x * y
        return jsonify({
            "method": "GET",
            "greeting": f"Hello {name}!",
            "x": x,
            "y": y,
            "sum": total,
            "product": product
        })

    elif request.method == 'POST':
        data = request.get_json()
        if not data or 'x' not in data or 'y' not in data:
            return jsonify({"error": "JSON must include 'x' and 'y'"}), 400
        x = data['x']
        y = data['y']
        try:
            quotient = x / y
        except ZeroDivisionError:
            quotient = None
        return jsonify({
            "method": "POST",
            "x": x,
            "y": y,
            "sum": x + y,
            "difference": x - y,
            "product": x * y,
            "quotient": quotient
        })


if __name__ == '__main__':
    app.run(debug=True)
