import re

with open('index.css', 'r') as f:
    css = f.write

with open('index.css', 'r') as f:
    css = f.read()

# Variables
css = re.sub(r'--bg-color:.*?;', '--bg-color: #F4F1E9;', css)
css = re.sub(r'--text-color:.*?;', '--text-color: #1A1A1A;', css)
css = re.sub(r'--primary-color:.*?;', '--primary-color: #000000;', css)
css = re.sub(r'--secondary-color:.*?;', '--secondary-color: #000000;', css)
css = re.sub(r'--accent-color:.*?;', '--accent-color: #000000;', css)

# Fix Header Gradient
css = re.sub(
    r'\.glass-header \{.*?\n\}', 
    '''\.glass-header {
    position: fixed;
    top: 0;
    width: 100%;
    padding: 1rem 5%;
    display: flex;
    justify-content: center;
    z-index: 1000;
    background-color: var(--bg-color);
    border-bottom: 3px solid #000;
}''', css, flags=re.DOTALL)

# Fix Nav
css = re.sub(r'nav \{.*?\n\}', 
    '''nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    max-width: 1200px;
    background: transparent;
    padding: 0.5rem 0;
}''', css, flags=re.DOTALL)

# Add Logo Image Class
css += "\n.logo-img { height: 60px; width: auto; }\n"

# Hide text logo if any leftovers
css = re.sub(r'\.logo \{.*?\n\}', 
    '''.logo {
    display: none;
}''', css, flags=re.DOTALL)

# Fix Nav Links
css = re.sub(r'\.nav-links a \{.*?\n\}', 
    '''.nav-links a {
    text-decoration: none;
    color: var(--text-color);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: transform var(--transition-speed);
    font-family: var(--font-body);
}''', css, flags=re.DOTALL)

css = re.sub(r'\.nav-links a:hover,\s*\.nav-links a\.active \{.*?\n\}', 
    '''.nav-links a:hover,
.nav-links a.active {
    transform: translateY(-2px);
    text-decoration: underline;
    text-decoration-thickness: 3px;
    text-underline-offset: 6px;
}''', css, flags=re.DOTALL)


# Fix H1 Text Shadow
css = re.sub(r'text-shadow: 4px 4px 0 #000;', '', css)

# Fix Gradient Text
css = re.sub(r'\.gradient-text \{.*?\n\}', 
    '''.gradient-text {
    color: var(--primary-color);
}''', css, flags=re.DOTALL)

# Disable Animation
css = re.sub(r'@keyframes glowShift \{.*?\n\}', '', css, flags=re.DOTALL)

# Fix Cards and Borders
css = re.sub(r'background:\s*rgba\(0, 0, 0, 0\.\d+\);', 'background: #ffffff;', css)
css = re.sub(r'border: 2px solid var\(--[a-zA-Z-]+\);', 'border: 3px solid #000;', css)
css = re.sub(r'box-shadow: \d+px \d+px 0 var\(--[a-zA-Z-]+\);', 'box-shadow: 6px 6px 0 #000;', css)

# Fix colors in sections
css = css.replace('color: #fff;', 'color: var(--text-color);')
css = css.replace('color: #eee;', 'color: var(--text-color);')
css = css.replace('color: #f4f4f4;', 'color: var(--text-color);')

# Fix Inputs
css = re.sub(r'background:\s*rgba\(255, 255, 255, 0\.08\);', 'background: #ffffff;', css)

# Package Grid Specific Fix
css = css.replace('border-color: var(--primary-color);', 'border-color: #000;')
css = css.replace('box-shadow: 7px 7px 0 var(--primary-color);', 'box-shadow: 8px 8px 0 #000;')

# Final CTA Text Shadow
css = css.replace('text-shadow: 2px 2px 0 #000;', '')
css = css.replace('text-shadow: 3px 3px 0 #000;', '')

# Fix Buttons
css = re.sub(r'\.btn-primary \{.*?\n\}', 
    '''.btn-primary {
    background-color: var(--primary-color);
    color: var(--bg-color);
    box-shadow: 6px 6px 0 rgba(0,0,0,0.15);
    border: 3px solid #000;
}''', css, flags=re.DOTALL)

css = re.sub(r'\.btn-primary:hover \{.*?\n\}', 
    '''.btn-primary:hover {
    transform: translate(-2px, -2px);
    box-shadow: 8px 8px 0 rgba(0,0,0,0.25);
}''', css, flags=re.DOTALL)

css = re.sub(r'\.btn-secondary \{.*?\n\}', 
    '''.btn-secondary {
    background-color: #ffffff;
    color: var(--primary-color);
    border: 3px solid var(--primary-color);
    box-shadow: 6px 6px 0 rgba(0,0,0,0.15);
}''', css, flags=re.DOTALL)

css = re.sub(r'\.btn-secondary:hover \{.*?\n\}', 
    '''.btn-secondary:hover {
    background-color: #f0f0f0;
    transform: translate(-2px, -2px);
    box-shadow: 8px 8px 0 rgba(0,0,0,0.25);
}''', css, flags=re.DOTALL)

# Hide tech grid and sphere
css = css.replace("mask-image: linear-gradient(to bottom, black 40%, transparent 100%);", "display: none;")
css = css.replace("background: radial-gradient(circle, rgba(255, 0, 128, 0.3) 0%, rgba(0, 0, 0, 0) 70%);", "display: none;")


# Remove text-shadow from h1
css = re.sub(r'h1 \{\s*font-family([^}]+)color: #fff;\s*text-shadow: 4px 4px 0 #000;\s*\}', r'h1 {\n    font-family\1color: var(--primary-color);\n}', css)

with open('index.css', 'w') as f:
    f.write(css)

print("Refactored index.css")
