import os
import subprocess

try:
    from google import genai
except ImportError:
    subprocess.check_call(["pip", "install", "google-genai"])
    from google import genai

def askOmi(error):

    api_key = "AIzaSyATDPGbokzoJaBm9CU56GbvJT-1rCd75ls"
    
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=error
    )
    return response.text

def html(error):
    answer = askOmi(error)

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>css</title>
</head>
<body>
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <p>{answer}</p>
</body>
</html>
"""

    with open("output.html", "w") as f:
        f.write(html_content)


def inline_html(error, filename="index.html"):
    """
    Generates HTML output in the same file from where it's called.
    If the file doesn't exist, creates a new one. If it exists, appends the content.
    """
    answer = askOmi(error)
    
    # Check if file exists
    file_exists = os.path.exists(filename)
    
    if file_exists:
        # Read existing content
        with open(filename, "r", encoding="utf-8") as f:
            existing_content = f.read()
        
        # Create new content with the AI response
        new_content = f"""
<!-- AI Response added by askOmi -->
<div style="border: 2px solid #007bff; padding: 20px; margin: 20px 0; border-radius: 8px; background-color: #f8f9fa;">
    <h3 style="color: #007bff; margin-top: 0;">AI Response:</h3>
    <p style="margin-bottom: 0; line-height: 1.6;">{answer}</p>
</div>
<!-- End AI Response -->
"""
        
        # Append to existing file
        with open(filename, "a", encoding="utf-8") as f:
            f.write(new_content)
    else:
        # Create new HTML file with the response
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>askOmi Response</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .response-container {{
            background-color: white;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .response-title {{
            color: #007bff;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        .response-content {{
            line-height: 1.6;
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="response-container">
        <h1 class="response-title">AI Response</h1>
        <div class="response-content">
            {answer}
        </div>
    </div>
</body>
</html>"""
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
    
    print(f"Response added to {filename}")


def get(error, style="inline"):
    """
    Returns HTML content as a string instead of writing to a file.
    Perfect for using directly in Python code!
    
    Parameters:
    - error (str): Your question or prompt
    - style (str): "inline" for appending style, "full" for complete HTML document
    
    Returns:
    - str: HTML content as string
    """
    answer = askOmi(error)
    
    if style == "inline":
        # Returns HTML content that can be appended to existing HTML
        html_content = f"""
<!-- AI Response added by askOmi -->
<div style="border: 2px solid #007bff; padding: 20px; margin: 20px 0; border-radius: 8px; background-color: #f8f9fa;">
    <h3 style="color: #007bff; margin-top: 0;">AI Response:</h3>
    <p style="margin-bottom: 0; line-height: 1.6;">{answer}</p>
</div>
<!-- End AI Response -->
"""
    else:  # style == "full"
        # Returns complete HTML document
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>askOmi Response</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .response-container {{
            background-color: white;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .response-title {{
            color: #007bff;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        .response-content {{
            line-height: 1.6;
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="response-container">
        <h1 class="response-title">AI Response</h1>
        <div class="response-content">
            {answer}
        </div>
    </div>
</body>
</html>"""
    
    return html_content


def destroy():
    packages = ["google-genai", "askOmi"]
    
    for package in packages:
        try:
            subprocess.check_call(["pip", "uninstall", "-y", package])
        except subprocess.CalledProcessError:
            pass
    
    # Delete output.html if it exists
    if os.path.exists("output.html"):
        os.remove("output.html")
    else:
        pass

