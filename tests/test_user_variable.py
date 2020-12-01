from sneact.web.user import User
from sneact import Sneact, s, _
from sneact.html import p


def test_user_scope():
    template_scope = {"hey": "default hey"}
    template = (+Sneact(template_scope) << p >> s.hey << -p >> _).compile()
    assert template.as_html() == "<p>default hey</p>\n"
    robert = User(intial_props={"hey": "Hey Robert"})
    assert template.show_for(robert) == "<p>Hey Robert</p>\n"
