

def test_app_is_created(app):
    assert app.name == 'core.app'


def test_config_debug(config):
    assert config['DEBUG'] is True


def test_config_app_settings(config):
    assert config['APP_SETTINGS'] == 'config.DevelopmentConfig'


def test_request_returns_404(client):
    assert client.get('/status').status_code == 404
