from flask import Flask, request, render_template, redirect, url_for, session


submitted_text = ""


app = Flask(__name__)

@app.route('/')
def home():
    print("Testing print HOME")
    return "Welcome to the Home Page!"


@app.route('/about')
def about():
    print("Testing print ABOUT")
    return "This is the About Page."


@app.route('/form')
def form():
    print("Testing print FORM")
    return render_template('form.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():

    global submitted_text
    
    if request.method == 'POST':
        submitted_text = request.form.get('data')
    else:
        submitted_text = request.args.get('data')

    return redirect(url_for('result'))


@app.route('/result')
def result():
    # eventually this will display the submitted text
    return render_template('results.html', my_text=submitted_text)



if __name__ == '__main__':
    app.run(debug=True)