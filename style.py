mishtee_css = """
/* Import premium fonts */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Inter:wght@300;400&display=swap');

/* Main Container */
.gradio-container {
    background-color: #FAF9F6 !important;
    font-family: 'Inter', sans-serif;
    color: #333333;
}

/* Headings - Using Serif for the 'MishTee-Magic' identity */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    font-weight: 400 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase;
    color: #333333;
}

/* Buttons - Sharp, Terracotta, No Gradients */
button.primary {
    background: #C06C5C !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 0px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 400 !important;
    letter-spacing: 1px;
    padding: 12px 24px !important;
    transition: background 0.3s ease;
}

button.primary:hover {
    background: #A65D4F !important;
}

/* Inputs and Textboxes */
input, textarea {
    border: 1px solid #333333 !important;
    border-radius: 0px !important;
    background-color: transparent !important;
    box-shadow: none !important;
}

/* Tables - Lightweight Sans-Serif */
table, thead, th, td {
    font-family: 'Inter', sans-serif !important;
    font-weight: 300 !important;
    border-collapse: collapse !important;
    border: 1px solid #E0E0E0 !important;
}

/* Structural Spacing and Borders */
.gap, .form {
    padding: 2rem !important;
    gap: 2rem !important;
}

.block {
    border: 1px solid #E0E0E0 !important;
    border-radius: 0px !important;
    box-shadow: none !important;
    background: #FAF9F6 !important;
    margin-bottom: 20px !important;
}

/* Remove standard Gradio shadows and radii */
* {
    box-shadow: none !important;
    border-radius: 0px !important;
}
"""
