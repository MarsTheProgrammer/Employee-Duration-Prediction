from flask import Flask, render_template, request

import jupytermodel

app = Flask(__name__)

model_list = []
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
        model_list.clear()
        model_list.append(degree)
        model_list.append(year_joined)
        model_list.append(city)
        model_list.append(salary)
        model_list.append(age)
        model_list.append(gender)
        model_list.append(benched)
        model_list.append(experience)


        return "Degree: " + degree + \
               " Year Joined: " + year_joined + \
               " City: " + city + \
               " Salary: " + salary + \
               " Age: " + age + \
               " Gender: " + gender + \
               " Benched: " + benched + \
               " Experience: " + experience

    return render_template("input.html")

test_list = [2,2017, 1, 3, 23, 1, 0, 0]
jupytermodel.predict_list(test_list)

if __name__ == "__main__":
    app.run(debug=True)
