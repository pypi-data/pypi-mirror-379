"""Tkinter integration for SIDS."""

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    tk = None
    ttk = None


class TkinterAdapter:
    """Adapter for running SIDS apps with Tkinter."""
    
    def __init__(self):
        self.root = None
    
    def run(self, sids_app, **kwargs):
        """Run the SIDS app using Tkinter."""
        if tk is None:
            raise ImportError("Tkinter not available")
        
        self.root = tk.Tk()
        self.root.title("SIDS App")
        self.root.geometry("800x600")
        
        # Create scrollable frame
        canvas = tk.Canvas(self.root)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Add components
        for page in sids_app.pages:
            # Page title
            title_label = tk.Label(scrollable_frame, text=page.title, 
                                 font=("Arial", 18, "bold"))
            title_label.pack(pady=10)
            
            for component in page.components:
                self._render_component(scrollable_frame, component)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        print("🚀 SIDS app running in Tkinter window")
        self.root.mainloop()
    
    def _render_component(self, parent, component):
        """Render a component in Tkinter."""
        if "text-3xl" in component.classes:  # H1
            label = tk.Label(parent, text=component.content, 
                           font=("Arial", 16, "bold"))
            label.pack(pady=5)
        elif "bg-blue-500" in component.classes:  # Button
            def on_click():
                if component.props.get('on_click'):
                    component.props['on_click']()
            
            button = tk.Button(parent, text=component.content, 
                             command=on_click, bg="#3B82F6", fg="white",
                             font=("Arial", 10), padx=10, pady=5)
            button.pack(pady=5)
        else:  # Generic component/Card
            label = tk.Label(parent, text=component.content, wraplength=400)
            label.pack(pady=5)
