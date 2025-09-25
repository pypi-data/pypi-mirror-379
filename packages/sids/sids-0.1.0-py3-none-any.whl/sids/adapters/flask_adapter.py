"""Flask integration for SIDS."""

from flask import Flask, render_template_string
import os


class FlaskAdapter:
    """Adapter for running SIDS apps with Flask."""
    
    def __init__(self):
        self.app = None
    
    def run(self, sids_app, host="127.0.0.1", port=5000, debug=True, **kwargs):
        """Run the SIDS app using Flask."""
        self.app = Flask(__name__, 
                        template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
        
        @self.app.route('/')
        def index():
            # Generate HTML for all pages
            html_content = ""
            for page in sids_app.pages:
                html_content += f"<div class='page'>"
                html_content += f"<h1 class='text-4xl font-bold mb-8'>{page.title}</h1>"
                for component in page.components:
                    html_content += component.render()
                html_content += "</div>"
            
            # Use inline template with Tailwind CDN
            template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SIDS App</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 p-8">
    <div class="max-w-4xl mx-auto">
        {{ content|safe }}
    </div>
</body>
</html>
            """
            
            return render_template_string(template, content=html_content)
        
        print(f"🚀 SIDS app running at http://{host}:{port}")
        self.app.run(host=host, port=port, debug=debug, **kwargs)
