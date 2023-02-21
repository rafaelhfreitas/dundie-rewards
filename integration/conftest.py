MARKER = """\n
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""

def pytest_configure(config):
    map(config.addinivalue_line, MARKER.split("\n"))