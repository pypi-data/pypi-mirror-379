"""Tests for SIDS core functionality."""

def test_app_initialization():
    """Test that App can be initialized."""
    from sids.core import App
    app = App()
    assert app is not None
    assert hasattr(app, 'pages')

def test_app_import():
    """Test that SIDS can be imported."""
    import sids
    assert hasattr(sids, 'App')