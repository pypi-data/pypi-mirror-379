"""Core rendering engine for SIDS."""

from contextlib import contextmanager
from typing import List, Dict, Any, Callable, Optional
import uuid


class Component:
    """Base class for all SIDS components."""
    
    def __init__(self, content: str = "", classes: str = "", **props):
        self.content = content
        self.classes = classes
        self.props = props
        self.id = str(uuid.uuid4())[:8]
    
    def render(self) -> str:
        """Render component to HTML."""
        return f"<div class='{self.classes}'>{self.content}</div>"


class Page:
    """Represents a page in the app."""
    
    def __init__(self, title: str):
        self.title = title
        self.components: List[Component] = []
        self._current_page = None
    
    def add_component(self, component: Component):
        """Add a component to this page."""
        self.components.append(component)


# Global state for current page context
_current_page: Optional[Page] = None


class App:
    """Main SIDS application class."""
    
    def __init__(self):
        self.pages: List[Page] = []
        self._adapters = {}
    
    @contextmanager
    def page(self, title: str):
        """Context manager for creating pages."""
        global _current_page
        page = Page(title)
        self.pages.append(page)
        old_page = _current_page
        _current_page = page
        try:
            yield page
        finally:
            _current_page = old_page
    
    def run(self, backend: str = "flask", **kwargs):
        """Run the app with the specified backend."""
        if backend == "flask":
            from .adapters.flask_adapter import FlaskAdapter
            adapter = FlaskAdapter()
            return adapter.run(self, **kwargs)
        elif backend == "jupyter":
            from .adapters.jupyter_adapter import JupyterAdapter
            adapter = JupyterAdapter()
            return adapter.run(self, **kwargs)
        elif backend == "tkinter":
            from .adapters.tkinter_adapter import TkinterAdapter
            adapter = TkinterAdapter()
            return adapter.run(self, **kwargs)
        else:
            raise ValueError(f"Unsupported backend: {backend}")


# Component functions
def H1(content: str, classes: str = "text-3xl font-bold", **props) -> Component:
    """Create an H1 heading component."""
    component = Component(content, f"text-3xl font-bold {classes}", **props)
    component.render = lambda: f"<h1 class='{component.classes}'>{component.content}</h1>"
    if _current_page:
        _current_page.add_component(component)
    return component


def Button(content: str, color: str = "blue", on_click: Optional[Callable] = None, 
           classes: str = "", **props) -> Component:
    """Create a button component."""
    color_classes = {
        "blue": "bg-blue-500 hover:bg-blue-700 text-white",
        "red": "bg-red-500 hover:bg-red-700 text-white", 
        "green": "bg-green-500 hover:bg-green-700 text-white",
        "gray": "bg-gray-500 hover:bg-gray-700 text-white",
    }
    
    base_classes = "font-bold py-2 px-4 rounded"
    color_class = color_classes.get(color, color_classes["blue"])
    full_classes = f"{base_classes} {color_class} {classes}"
    
    component = Component(content, full_classes, on_click=on_click, **props)
    component.render = lambda: f"<button class='{component.classes}' onclick='{component.props.get('on_click', '')}'>{component.content}</button>"
    
    if _current_page:
        _current_page.add_component(component)
    return component


def Card(content: str, classes: str = "bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4", 
         **props) -> Component:
    """Create a card component."""
    component = Component(content, f"bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 {classes}", **props)
    component.render = lambda: f"<div class='{component.classes}'>{component.content}</div>"
    
    if _current_page:
        _current_page.add_component(component)
    return component
