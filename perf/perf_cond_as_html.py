from sneact import Sneact, s, _
from sneact.cond import when, when_not, then
from sneact.html import div, p


# fmt: off

scope = dict(
    text="Hello tigers. We love Tigers.",
    not_text="Hello not tigers. We love Tigers.",
    show_text=True
)
home_page = (+Sneact(scope)
    <<div>>_
        @when(s.show_text, +then
            <<p>> s.text <<-p>>_
        )
        @when_not(s.show_text, +then
            <<p>> s.not_text <<-p>>_
        )
    <<-div>>_
).compile()

#?
home_page.as_html()
