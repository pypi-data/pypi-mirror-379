import pytest
from dev_helper import (
    slugify,
    camel_to_snake,
    snake_to_camel,
    normalize_whitespace,
    remove_html_tags,
    extract_emails,
    extract_urls,
)

@pytest.mark.parametrize("inp, out", [
    ("Olá Mundo!", "ola-mundo"),
    ("  espaços  ", "espacos"),
    ("Título com Acentuação", "titulo-com-acentuacao"),
    (" caracteres---especiais_!?#@ ", "caracteres-especiais"),
])
def test_slugify(inp, out):
    assert slugify(inp) == out

@pytest.mark.parametrize("inp, out", [
    ("CamelCase", "camel_case"),
    ("MyVariableName", "my_variable_name"),
    ("HTTPRequest", "http_request"),
    ("already_snake", "already_snake"),
])
def test_camel_to_snake(inp, out):
    assert camel_to_snake(inp) == out

@pytest.mark.parametrize("inp, out", [
    ("snake_case", "SnakeCase"),
    ("my_variable_name", "MyVariableName"),
    ("a_b_c", "ABC"),
])
def test_snake_to_camel(inp, out):
    assert snake_to_camel(inp) == out

@pytest.mark.parametrize("inp, out", [
    ("  muitos   espaços  ", "muitos espaços"),
    ("uma\nlinha\tnova", "uma linha nova"),
])
def test_normalize_whitespace(inp, out):
    assert normalize_whitespace(inp) == out

@pytest.mark.parametrize("inp, out", [
    ("<p>Olá</p> <b>Mundo</b>", "Olá Mundo"),
    ("Texto <a href='#'>com link</a>.", "Texto com link."),
])
def test_remove_html_tags(inp, out):
    assert remove_html_tags(inp) == out

def test_extract_emails():
    text = "Contacte info@example.com ou, para suporte, support@devhelper.dev."
    expected = ["info@example.com", "support@devhelper.dev"]
    assert extract_emails(text) == expected

def test_extract_urls():
    text = "Visite http://example.com e também https://www.google.com/search"
    expected = ["http://example.com", "https://www.google.com/search"]
    assert extract_urls(text) == expected