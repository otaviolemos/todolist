import pytest
from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
      with app.test_client() as client:
        yield client

def test_user_signup(client):
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST&'
    response = client.post('/api/users', json=
    {
      "name": user_name,
      "email": user_email,
      "password": user_password
    })
    assert response.status_code == 201
    assert response.json["name"] is not None
    assert response.json["email"] is not None

def test_user_signup_with_error(client):
    user_name = 'Joe Doe'
    user_email = 'joe@doe.com'
    user_password = 'test1234TEST'
    response = client.post('/api/users', json=
    {
      "name": user_name,
      "email": user_email,
      "password": user_password
    })
    assert response.status_code == 400
    assert response.json["error"] is not None