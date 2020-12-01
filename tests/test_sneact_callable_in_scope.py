from sneact import Sneact, s, _
from sneact._magic_tags import (
    MagicHTMLTag,
    magic_html_chain_method,
    magic_html_mod_method,
)

# fmt: off


def dummy_tiger_helloer():
    return str.join(" ", ["Hello tigers.", "We love Tigers."])


def test_callable_in_scope(smoke_sneact_expected_results):
	from sneact.html import div, p, img
	scope = dict(
	    title="Tiger",
	    subtitle="About tigers",
	    image='"tiger.png"',
        text=dummy_tiger_helloer,
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
	result = home_page.compile().as_html()
	assert result == smoke_sneact_expected_results
