#import modules
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests 

#make a flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set a secret key to use when validating form data
app.config["SECRET_KEY"] = "your secret key"

#define a constant variable for url
URL = "http://127.0.0.1:5010/api/students/all"

#function to request student data from the api
#input: URL
#output: JSON student data
def get_student_data(url):
    #MAKE A REQUEST 
    response = requests.get(url)

    #convert format to JSON
    response_json = response.json()

    return response_json

#function to get a list of unique majors
#input:url
#output: list of unique majors
def get_unique_majors():

    #get a list of students from the student api
    student_data = get_student_data(URL)

    #produce a list of unique majors
    major_list = []

    for student in student_data:
        if student["major"] in major_list:
            continue
        major_list.append(student["major"])
    major_list.sort()
    return major_list

#create a route for the site index page that will display all student data
@app.route("/", methods  = ["GET"])
def index():
    #get the student data
    #make a request to the student data api url
    
    student_data = get_student_data(URL)    

    #send the student data to the index.html page
    return render_template('index.html', student_data = student_data)

@app.route("/majors", methods = ["GET"])
def majors():
    #write code that gets a unique list of majors from student data
    major_list = get_unique_majors()
    
    return render_template("majors.html", major_list=major_list)

@app.route('/majors',methods=['POST'])
def majors_post():
    major_list = get_unique_majors()
    result_list = []
    #get the form data that was submitted
    major = request.form.get('major')

    #validate our form data. If invalid form data, then show error message
    if not major:
        flash("You must select a major")
    else:
        #find students with the selected major and return to the majors.html page
        #get the student data
        student_list = get_student_data(URL)
        
        #loop through list of students. if student major == major, place student in a result list
        for student in student_list:
            if student["major"] == major:
                result_list.append(student)

        #send the result list to majors.html page


    return render_template("majors.html",major_list=major_list,result_list = result_list)


app.run(port = 5005)