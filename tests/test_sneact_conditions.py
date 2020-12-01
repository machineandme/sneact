from sneact import Sneact, s, when, then, _
from sneact.html import div, p, img


# fmt: off

def test_conditions(smoke_sneact_expected_results, conditions_expected_results):
    scope = dict(
        title="Tiger",
        subtitle="About tigers",
        image='"tiger.png"',
        text="Hello tigers. We love Tigers.",
        show_text=True
    )
    home_page = (+Sneact(scope)
        <<div>>_
            <<p>> s.title <<-p>>_
            <<p>> s.subtitle <<-p>>_
            <<div>>_
                @when(s.show_text, +then
                    <<p>> s.text <<-p>>_
                )
                <<img(src=s.image)>>_
            <<-div>>_
        <<-div>>_
    )
    result_with_text = home_page.compile().as_html()
    assert result_with_text == smoke_sneact_expected_results
    scope['show_text'] = False
    result_without_text = home_page.compile().as_html()
    assert result_without_text == conditions_expected_results
