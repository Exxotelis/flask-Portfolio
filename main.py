from flask import Flask, render_template, request
from send_email import send_email  # Import the send_email function


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        user_name = request.form['contact_name']
        user_email = request.form['contact_email']
        message = request.form['contact_message']

        # Send email
        send_email(user_name, user_email, message)

        return 'Email sent successfully!'
    else:
        return render_template('contact.html')


@app.route('/projects')
def projects():  # Changed the function name to 'gallery'
    return render_template('projects.html')


@app.route('/gallery')
def gallery():  # Changed the function name to 'gallery'
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)
