import email
def test_index(client):
    rv = client.get("/")
    assert "login" in rv.data.decode()
    assert "upload" in rv.data.decode()
    
def signup(client, username, password):
    data = dict(username=username, email=email, password=password)
    return client.post("/auth/signup", data=data, follow_redirects=True)

def test_index_signup(client):
    rv = signup(client, "admin", "flaskbook@example.com", "password")
    
    rv = client.get("/")
    assert "logout" in rv.data.decode()
    assert "upload" in rv.data.decode()