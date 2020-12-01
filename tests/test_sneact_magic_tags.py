from sneact import Sneact, s, _
from sneact._magic_tags import (
    MagicHTMLTag,
    magic_html_chain_method,
    magic_html_mod_method,
)


# fmt: off

def test_smoke_sneact(smoke_sneact_expected_results):
	from sneact.html import div, p, img
	scope = dict(
	    title="Tiger",
	    subtitle="About tigers",
	    image='"tiger.png"'
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
	scope["text"] = "Hello tigers. We love Tigers."
	result = home_page.compile().as_html()
	assert result == smoke_sneact_expected_results


def test_magic_html_mod_method(fake_magic_class):
    mod_method = magic_html_mod_method("+")
    result = mod_method(fake_magic_class)
    assert isinstance(result, MagicHTMLTag)
    expected = ("+", "x")
    assert result.segments == expected


def test_magic_html_chain_method(fake_magic_class):
    chain_method = magic_html_chain_method("*")
    result = chain_method(fake_magic_class, fake_magic_class)
    assert isinstance(result, MagicHTMLTag)
    expected = ("x", "*", "x")
    assert result.segments == expected


def test_nested(nested_expected_results):
	from sneact.html import p, h1, header, footer
	scope = {}
	page = (+Sneact(scope)
	    <<header>>_
	    	**s.header
	    <<-header>>_
	    <<p>> "Lorem you know" <<-p>>_
	    <<footer>>_
	    	**s.footer
	    <<-footer>>_
	)
	page = page.compile()
	header = (+Sneact(scope)
	    <<h1>> "Page" <<-h1>>_
	)
	scope["header"] = header.compile()
	footer = (+Sneact(scope)
	    <<p>> "Copyright Kiselev Nikolay 2020" <<-p>>_
	)
	scope["footer"] = footer.compile()
	result = page.as_html()
	assert result == nested_expected_results
