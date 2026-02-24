import re

with open('index.css', 'r') as f:
    css = f.read()

# Variables
css = re.sub(r'--bg-color:.*?;', '--bg-color: #8C9EFF;', css)
# Keep text color readable vs blue
css = re.sub(r'--text-color:.*?;', '--text-color: #1A1A1A;', css)
css = re.sub(r'--primary-color:.*?;', '--primary-color: #D6F74C;', css)
css = re.sub(r'--secondary-color:.*?;', '--secondary-color: #F06038;', css)
css = re.sub(r'--accent-color:.*?;', '--accent-color: #FCD9BE;', css)

# Fix Cards that had solid white backgrounds
css = re.sub(r'\.booking-card \{\s*background:\s*#[a-fA-F0-9]+;', '.booking-card {\n    background: var(--accent-color);', css)
css = re.sub(r'\.package-card \{\s*background:\s*#[a-fA-F0-9]+;', '.package-card {\n    background: var(--accent-color);', css)
css = re.sub(r'\.addons-card \{\s*background:\s*#[a-fA-F0-9]+;', '.addons-card {\n    background: var(--accent-color);', css)
css = re.sub(r'\.scope-notes \{\s*background:\s*#[a-fA-F0-9]+;', '.scope-notes {\n    background: var(--accent-color);', css)
css = re.sub(r'\.service-card \{\s*background:\s*#[a-fA-F0-9]+;', '.service-card {\n    background: var(--accent-color);', css)

# Fix Primary Button Hover (use tomato)
css = re.sub(r'\.btn-primary:hover \{.*?\n\}', 
    '''.btn-primary:hover {
    background-color: var(--secondary-color);
    transform: translate(-2px, -2px);
    box-shadow: 8px 8px 0 rgba(0,0,0,0.25);
}''', css, flags=re.DOTALL)


# Fix Secondary Button (make it apricot)
css = re.sub(r'\.btn-secondary \{.*?\n\}', 
    '''.btn-secondary {
    background-color: var(--accent-color);
    color: var(--text-color);
    border: 3px solid #000;
    box-shadow: 6px 6px 0 rgba(0,0,0,0.15);
}''', css, flags=re.DOTALL)

# Fix Secondary Button Hover (make it tomato)
css = re.sub(r'\.btn-secondary:hover \{.*?\n\}', 
    '''.btn-secondary:hover {
    background-color: var(--secondary-color);
    transform: translate(-2px, -2px);
    box-shadow: 8px 8px 0 rgba(0,0,0,0.25);
}''', css, flags=re.DOTALL)

with open('index.css', 'w') as f:
    f.write(css)

print("Applied new color palette to index.css")
