from flask import Flask, request, render_template, redirect, url_for, session
from forms import TextForm



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
    form = TextForm()

    if form.validate_on_submit():
        session['my_text'] = form.UserInput.data
        return redirect(url_for('result'))

    return render_template('form.html', form=form)


@app.route('/result')
def result():
    # eventually this will display the submitted text
    text = session.get('my_text', 'No data submitted yet.')
    # Clear the session after reading
    session.pop('my_text', None)
    return render_template('results.html', my_text=text)



if __name__ == '__main__':
    app.run(debug=True)