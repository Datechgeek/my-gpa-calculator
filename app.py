from flask import Flask, render_template, redirect, url_for, request, send_file, session
from weasyprint import HTML
import tempfile
import os
from flask import make_response

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('courses'))

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        # Retrieve the course data from the form
        course_data = request.form.getlist('course_data')

        # Create lists to store course information
        course_codes = []
        course_titles = []
        credit_loads = []
        grades = []

        # Iterate over the course data in steps of 4
        for i in range(0, len(course_data), 4):
            # Extract course information
            code = course_data[i].strip()
            title = course_data[i + 1].strip()
            credit_load = int(course_data[i + 2].strip())
            grade = course_data[i + 3].strip()

            # Add course information to respective lists
            course_codes.append(code)
            course_titles.append(title)
            credit_loads.append(credit_load)
            grades.append(grade)

        # Calculate the GPA based on the provided grades and credit loads
        gpa = calculate_gpa(course_codes, credit_loads, grades)

        # Render the HTML template with the course data and the calculated GPA
        rendered = render_template('gpa_result.html', course_codes=course_codes, course_titles=course_titles, credit_loads=credit_loads, grades=grades, gpa=gpa)

        # Generate the PDF using WeasyPrint
        pdf_bytes = HTML(string=rendered).write_pdf()

        # Create a temporary file to store the PDF
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(pdf_bytes)
        temp.close()

        # Create a response and set the Content-Disposition header
        response = make_response(send_file(temp.name, as_attachment=True, mimetype='application/pdf'))
        response.headers['Content-Disposition'] = 'attachment; filename=gpa_result.pdf'

        return response
    else:
        # Handle the GET request
        return render_template('courses.html')
    
def calculate_gpa(course_codes, credit_loads, grades):
    total_points = 0
    total_credits = 0

    for i in range(len(course_codes)):
        grade = grades[i]
        credit_load = credit_loads[i]

        if grade == 'A':
            points = 5.0
        elif grade == 'B':
            points = 4.0
        elif grade == 'C':
            points = 3.0
        elif grade == 'D':
            points = 2.0
        elif grade == 'E':
            points = 1.0
        elif grade == 'F':
            points = 0.0
        else:
            points = 0.0

        course_points = points * credit_load

        total_points += course_points
        total_credits += credit_load

    gpa = total_points / total_credits
    return gpa

if __name__ == '__main__':
    app.run(debug=True)
