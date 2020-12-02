from sneact import Sneact, s, _
from sneact.loop import for_each, do, item
from sneact.html import div, img


# fmt: off

scope = dict(
    images=["cat.png", "dog.png", "frog.png"]
)
page = (+Sneact(scope)
    <<div>>_
        @for_each(s.images, +do
            <<img(src=item)>>_
        )
    <<-div>>_
).compile()

#?
page.as_html()
