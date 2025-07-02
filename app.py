from flask import Flask, flash, render_template, request, redirect, url_for,session

app = Flask(__name__)
app.secret_key = 'Sand110'

# Dummy login users
users = {
    "admin": "pass",
    "demo": "tusa"
}

# Dummy photographer data
photographers = [
    {"id": "p1", "name": "Amit Lensman", "skills": ["Wedding", "Portrait"], "image": "amit.jpg"},
    {"id": "p2", "name": "Sana Clickz", "skills": ["Fashion", "Event"], "image": "sana.jpg"},
    {"id": "p3", "name": "Aarna", "skills": ["Drone", "Event", "Traditional"], "image": "aarna.jpg"},
    {"id": "p4", "name": "Aditya", "skills": ["Wildlife", "Night"], "image": "aditya.jpg"}
    
]

# Dummy availability data
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
    # Process/store data here
    return f"Review submitted for {name} (ID: {pid}) with {rating} stars!"


# Route: Logout (just redirects)
@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# Route: Signup Page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Route: Home Page (no session needed)
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
    session.clear()  # Correct syntax to clear session
    return redirect(url_for('login'))


  
@app.route('/bookings')
def show_bookings():
    user_bookings = [
        {"id": "p4", "name": "Aditya", "Date-booked": "29-8-2025","Image":"aditya.jpg"},
        {"id": "p3", "name": "Sana", "Date-booked": "26-7-2025","Image":"sana.jpg"}
    ]
    return render_template('bookings.html', bookings=user_bookings)

# Route: Book Photographer
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        photographer_id = request.form.get('photographer_id')
        date = request.form.get('date')
        return f"<h2 style='color:green'>Booking Confirmed! For {photographer_id} on {date}.</h2>"

    return render_template('book.html', photographers=photographers)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
