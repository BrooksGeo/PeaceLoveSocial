import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # Replace the text logo
    content = content.replace(
        '<div class="logo">Peace Love Social</div>',
        '<a href="index.html" class="logo-link"><img src="media/logo-horizontal.png" alt="Peace Love Social Logo" class="logo-img"></a>'
    )
    
    with open(file, 'w') as f:
        f.write(content)

print("Updated HTML files with logos.")
