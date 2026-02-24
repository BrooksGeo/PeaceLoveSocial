import re

with open('index.css', 'r') as f:
    css = f.read()

# Change h3 colors in cards to Black for better contrast against Apricot
css = re.sub(r'(\.package-card h3,\s*\.addons-card h3 \{.*?)color: var\(--primary-color\);', 
             r'\1color: #000;', css, flags=re.DOTALL)

css = re.sub(r'(\.service-card h3 \{.*?)color: var\(--primary-color\);', 
             r'\1color: #000;', css, flags=re.DOTALL)

with open('index.css', 'w') as f:
    f.write(css)

import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # Replace old logos with new logo
    content = content.replace('logo-horizontal.png', 'pls.png')
    content = content.replace('logo-stacked.png', 'pls.png')
    
    with open(file, 'w') as f:
        f.write(content)

print("Fixed contrast and updated logo to pls.png across the site.")
