# My Project Title
GPA Calculator

## Video Demo
[Link to my video demo](https://youtu.be/Kwn1A_PISX0)

## Description
The GPA Calculator is a web application designed to help students calculate their Grade Point Average (GPA) based on their course grades and credit loads. The application is built using Flask, a Python web framework, and uses HTML and CSS for the front-end interface.

The application provides a form where users can input their course details, including the course code, course title, credit load, and grade. Users can add as many courses as they need, and the application will calculate the GPA based on the provided data.

The calculated GPA is then displayed on a new page, along with a table showing the details of the courses entered by the user. The application also generates a PDF of this page, which users can download for their records.

The project consists of several Python and HTML files:

## Files
 `app.py`: This is the main application file. It handles the routing and logic for the application.
- `courses.html`: This file contains the HTML for the course input form.
- `gpa_result.html`: This file contains the HTML for the GPA result page.
- `layout.html`: This is a base HTML file that other HTML files extend.



## Design Choices
## Design Choices
I chose to use Flask for this project because it's a lightweight and flexible framework that's well-suited for small applications like this GPA Calculator. Flask allowed me to quickly set up routing and form handling with minimal configuration.

For the front-end, I used basic HTML and CSS to keep the interface simple and user-friendly. I decided to include a table in the GPA result page to clearly display the details of the courses entered by the user. This makes it easy for users to verify their input and understand how their GPA was calculated.

In terms of code structure, I separated the application logic and the HTML templates into different files. This separation of concerns makes the code easier to maintain and understand.

I also decided to include a feature to generate a PDF of the GPA result page. I thought this would be a useful feature for users who want to keep a record of their GPA calculation. I used the pdfkit library to implement this feature because it provides a straightforward way to convert HTML to PDF.


## Conclusion

The GPA Calculator web application serves as a practical tool for students to easily calculate their Grade Point Average (GPA) based on their course grades and credit loads. With its user-friendly interface and the ability to generate a PDF for record-keeping, it aims to simplify the often tedious process of GPA calculation.

This project has been a great opportunity to apply and enhance my skills in Flask, HTML, CSS, and Python. It has also been a rewarding experience to create a tool that can potentially benefit many students.

Looking forward, there are several enhancements that could be made to the GPA Calculator. These include adding support for different GPA scales, implementing user accounts to save GPA calculations, and improving the PDF generation feature.

Thank you for taking the time to explore this project. I hope you find the GPA Calculator useful and I welcome any feedback or suggestions.