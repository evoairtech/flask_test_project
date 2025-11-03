from flask import Flask, request, render_template, redirect, url_for, session



app = Flask(__name__)
app.secret_key = 'nekuv_kluch'  # Required for session to work


@app.route('/')
def home():
    print("Testing print HOME")
    return "Welcome to the Home Page!"


@app.route('/about')
def about():
    print("Testing print ABOUT")
    return "This is the About Page."


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        session['my_text'] = request.form.get('data')
        return redirect(url_for('result'))
    
    # If it's a GET request → just show the form
    return render_template('form.html')

@app.route('/result')
def result():
    # eventually this will display the submitted text
    text = session.get('my_text', 'No data submitted yet.')
    # Clear the session after reading
    session.pop('my_text', None)
    return render_template('results.html', my_text=text)



if __name__ == '__main__':
    app.run(debug=True)