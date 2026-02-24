import re

with open('index.css', 'r') as f:
    css = f.read()

# Make sure .logo-img and .footer-logo are sized appropriately
# If they don't exist, we add them. If they do, we ensure they are visible.

logo_css = """.logo-img {
    height: 80px;
    width: auto;
    object-fit: contain;
}

.footer-logo {
    height: 120px;
    width: auto;
    object-fit: contain;
    margin-bottom: 2rem;
}"""

if '.logo-img' not in css:
    css += "\n" + logo_css + "\n"
else:
    css = re.sub(r'\.logo-img \{.*?\n\}', 
    '''.logo-img {
    height: 80px;
    width: auto;
    object-fit: contain;
}''', css, flags=re.DOTALL)

if '.footer-logo' not in css:
     css += "\n" + logo_css.split("\n\n")[1] + "\n"
else:
     css = re.sub(r'\.footer-logo \{.*?\n\}', 
    '''.footer-logo {
    height: 120px;
    width: auto;
    object-fit: contain;
    margin-bottom: 2rem;
}''', css, flags=re.DOTALL)


with open('index.css', 'w') as f:
    f.write(css)

print("Fixed logo sizes in index.css")
