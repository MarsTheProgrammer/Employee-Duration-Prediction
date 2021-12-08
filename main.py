from flask import Flask, render_template, request

app = Flask(__name__)


# education, joiningYear, city, paymentTier, age, gender,
#   everBenched, experienceInCurrentDomain -> leaveornot

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("profile.html")

@app.route('/signin', methods=["GET", "POST"])
def sign_in():
    return render_template("signin.html")

@app.route('/data', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        first_name = request.form.get('fname')
        degree = request.form.get('degree')
        year_joined = request.form.get('year')
        city = request.form.get('city')
        salary = request.form.get('salary')
        age = request.form.get('age')
        gender = request.form.get('gender')
        benched = request.form.get('benched')
        experience = request.form.get('exp')

        return "Degree: " + degree + \
               " Year Joined: " + year_joined + \
               " City: " + city + \
               " Salary: " + salary + \
               " Age: " + age + \
               " Gender: " + gender + \
               " Benched: " + benched + \
               " Experience: " + experience

    return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)
