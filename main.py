from flask import Flask, request, redirect, url_for,render_template
from lib.commands import add_contact, delete_contact, get_contacts

app = Flask(__name__)

@app.route('/')
def index():
    contacts = get_contacts()
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        add_contact(name, phone, email)
        return redirect(url_for('index'))
    return render_template('add_contact.html')

if __name__ == '__main__':
    app.run(debug=True)
