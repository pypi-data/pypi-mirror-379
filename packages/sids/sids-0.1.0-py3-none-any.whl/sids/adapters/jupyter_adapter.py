"""Jupyter integration for SIDS."""

try:
    from IPython.display import HTML, display
except ImportError:
    HTML = None
    display = None


class JupyterAdapter:
    """Adapter for running SIDS apps in Jupyter notebooks."""
    
    def run(self, sids_app, **kwargs):
        """Display the SIDS app in Jupyter."""
        if HTML is None or display is None:
            raise ImportError("IPython not available. Install with: pip install sids[jupyter]")
        
        # Generate HTML for all pages
        html_content = """
<div style="font-family: system-ui, -apple-system, sans-serif;">
<script src="https://cdn.tailwindcss.com"></script>
<div class="bg-gray-50 p-8 rounded-lg">
        """
        
        for page in sids_app.pages:
            html_content += f"<div class='page mb-8'>"
            html_content += f"<h1 class='text-4xl font-bold mb-6'>{page.title}</h1>"
            for component in page.components:
                html_content += component.render()
                html_content += "<br>"
            html_content += "</div>"
        
        html_content += "</div></div>"
        
        display(HTML(html_content))
