import pytest
from lesson19.app.application import Application

@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.quit)
    return app