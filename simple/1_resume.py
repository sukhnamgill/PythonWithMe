from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()
pdf.image("my2.jpg", x=107, y=32, w=50)  # Adjust 'x', 'y', and 'w' for positioning and size
pdf.set_line_width(0.5)  # Set the border line width
pdf.rect(x=110, y=35, w=40, h=40)
pdf.rect(x=5, y=5, w=200, h=290)

# Set title font
pdf.set_font("Arial", "B", 16)

# Title
pdf.cell(200, 10, txt="Resume", ln=True, align="C")

# Line break
pdf.ln(10)

# Set font for personal details
pdf.set_font("Arial", size=12)

# Personal Details
pdf.cell(200, 10, txt="Name: Sukhnam Gill", ln=True)
pdf.cell(200, 10, txt="Date of Birth: 23rd November 2003", ln=True)
pdf.cell(200, 10, txt="Email: your.email@example.com", ln=True)
pdf.cell(200, 10, txt="Phone: +91 12345 67890", ln=True)
pdf.cell(200, 10, txt="Address: Ludhiana, Punjab", ln=True)

# Line break
pdf.ln(10)

# Education
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, txt="Education", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="B.Tech in Computer Science Engineering, CT University, Ludhiana (2022 - Present)", ln=True)

# Line break
pdf.ln(10)

# Skills
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, txt="Skills", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Programming Languages: Python, C++", ln=True)
pdf.cell(200, 10, txt="Frameworks: PyQt", ln=True)
pdf.cell(200, 10, txt="Web Technologies: HTML, CSS, JavaScript", ln=True)

# Line break
pdf.ln(10)

# Projects
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, txt="Projects", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Project 1: A simple web app using Python and Flask", ln=True)
pdf.cell(200, 10, txt="Project 2: Desktop application using PyQt", ln=True)

# Line break
pdf.ln(10)

# Experience (if applicable)
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, txt="Experience", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Intern at XYZ Tech Solutions, Ludhiana (2023)", ln=True)

# Line break
pdf.ln(10)

# Extra-Curricular Activities
pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, txt="Extra-Curricular Activities", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Member of the coding club at CT University", ln=True)

# Save the PDF
pdf.output("Sukhnam_gill_Resume1.pdf")

print("Resume created successfully!")
