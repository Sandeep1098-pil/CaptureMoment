from flask import Flask, flash, render_template, request, redirect, url_for,session

app = Flask(__name__)
app.secret_key = 'Sand110'


users = {
    "admin": "pass",
    "demo": "tusa"
}


photographers = [
    {"id": "p1", "name": "Amit Lensman", "skills": ["Wedding", "Portrait"], "image": "amit.jpg"},
    {"id": "p2", "name": "Sana Clickz", "skills": ["Fashion", "Event"], "image": "sana.jpg"},
    {"id": "p3", "name": "Aarna", "skills": ["Drone", "Event", "Traditional"], "image": "aarna.jpg"},
    {"id": "p4", "name": "Aditya", "skills": ["Wildlife", "Night"], "image": "aditya.jpg"}
    
]


availability_data = {
    "p1": ["2025-06-20", "2025-06-23"],
    "p2": ["2025-06-19", "2025-06-22"],
    "p3": ["2025-06-25", "2025-06-30"],
    "p4": ["2025-06-21", "2025-07-27"]
}


@app.route('/')
def index():
    return redirect(url_for('login'))

# Route: Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            flash('❌ Invalid username or password')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/submit-review", methods=["POST"])
def submit_review():
    name = request.form["photographer_name"]
    pid = request.form["photographer_id"]
    rating = request.form["rating"]
  
    return f"Review submitted for {name} (ID: {pid}) with {rating} stars!"



@app.route('/logout')
def logout():
    return redirect(url_for('login'))


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def info():
    return render_template('about.html')

# Route: Show Photographers
@app.route('/show-photographers')
def show_photographers():
    return render_template('photographers.html', photographers=photographers, availability_data=availability_data)


@app.route('/reset')
def reset():
    session.clear()  
    return redirect(url_for('login'))
@app.route('/book', methods=['GET','POST'])
def book_photographer():
    if request.method == 'POST':
        photographer_id = request.form['photographer_id']
        user_id         = request.form['user_id']
        date            = request.form['date']
        
        return redirect(url_for('booking_success')) 
    return render_template('book.html')


@app.route('/booking-success') 
def booking_success():
    return render_template('successful.html')  


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
