import os
import shutil

project_name = "studyorstarve_rebuild"

file_structure = {
    "index.html": """<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>StudyOrStarve</title>
  <link rel='stylesheet' href='styles.css'>
</head>
<body>
  <h1>Welcome to StudyOrStarve</h1>
  <p>This is a static rebuild of the site.</p>
  <script src='script.js'></script>
</body>
</html>""",

    "styles.css": "body { font-family: Arial, sans-serif; background: #f9f9f9; margin: 2em; }",

    "script.js": "console.log('StudyOrStarve JS Loaded');",

    "README.md": "# StudyOrStarve Rebuild\n\nThis is a basic static recreation of StudyOrStarve.com.\nDeploy using GitHub Pages or Netlify."
}

# Create folder and files
os.makedirs(project_name, exist_ok=True)
for filename, content in file_structure.items():
    with open(os.path.join(project_name, filename), "w", encoding="utf-8") as f:
        f.write(content)

# Zip it (optional)
shutil.make_archive(project_name, 'zip', project_name)
print(f"✔ Project folder and ZIP created at: {os.path.abspath(project_name)}.zip")
