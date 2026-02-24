import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # Replace the footer
    old_footer = """    <footer>
        <p>&copy; 2026 Peace Love Social. All rights reserved.</p>"""
    
    new_footer = """    <footer>
        <img src="media/logo-stacked.png" alt="Peace Love Social Logo" class="footer-logo">
        <p>&copy; 2026 Peace Love Social. All rights reserved.</p>"""
    
    content = content.replace(old_footer, new_footer)
    
    with open(file, 'w') as f:
        f.write(content)

with open('index.css', 'a') as f:
    f.write("\n.footer-logo {\n    height: 100px;\n    width: auto;\n    margin-bottom: 1.5rem;\n}\n")

print("Updated footers with logos.")
