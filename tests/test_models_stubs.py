
from app.models.user import User


def test_user_stub_defaults():
    u = User(userId="u1", name="Ada Lovelace")
    assert u.userId == "u1"
    assert u.name == "Ada Lovelace"
    assert u.email == ""
