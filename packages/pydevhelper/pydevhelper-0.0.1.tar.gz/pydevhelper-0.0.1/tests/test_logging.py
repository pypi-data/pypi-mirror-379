import logging
from dev_helper import setup_logging

def test_setup_logging_configures(capsys):
    setup_logging(level=logging.DEBUG)
    logging.debug("debug message")

    captured = capsys.readouterr()
    assert "debug message" in captured.err
