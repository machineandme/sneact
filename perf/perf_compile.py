from sneact import Sneact, s, _
from sneact.html import div, p, img

scope = dict(
    title="Tiger",
    subtitle="About tigers",
    image='"tiger.png"',
    text= "Hello tigers. We love Tigers."
)

home_page = (+Sneact(scope)
    <<div>>_
        <<p>> s.title <<-p>>_
        <<p>> s.subtitle <<-p>>_
        <<div>>_
            <<p>> s.text <<-p>>_
            <<img(src=s.image)>>_
        <<-div>>_
    <<-div>>_
)

#?
home_page.compile()
