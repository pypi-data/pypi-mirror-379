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

def test_slugify_basic():
    assert slugify("Olá Mundo!") == "ola-mundo"
    assert slugify("Python_3 Pro!") == "python-3-pro"

def test_slugify_unicode():
    assert slugify("日本語 テキスト", allow_unicode=True) == "日本語-テキスト"

def test_camel_to_snake_and_back():
    assert camel_to_snake("CamelCaseText") == "camel_case_text"
    assert snake_to_camel("snake_case_text") == "SnakeCaseText"

def test_normalize_whitespace():
    assert normalize_whitespace("   hello   world   ") == "hello world"

def test_remove_html_tags():
    assert remove_html_tags("<p>Hello <b>World</b></p>") == "Hello World"

def test_extract_emails():
    text = "Contact us at support@example.com or admin@test.org"
    emails = extract_emails(text)
    assert "support@example.com" in emails
    assert "admin@test.org" in emails

def test_extract_urls():
    text = "Visit https://example.com or http://test.org"
    urls = extract_urls(text)
    assert "https://example.com" in urls
    assert "http://test.org" in urls
