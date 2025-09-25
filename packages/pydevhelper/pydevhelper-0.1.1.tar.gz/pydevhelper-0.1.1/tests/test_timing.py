import re
import logging
from dev_helper import timer, setup_logging

def test_timer_logs_execution_time(capsys):
    setup_logging(level=logging.INFO)

    @timer
    def dummy():
        return 42

    result = dummy()
    assert result == 42

    captured = capsys.readouterr()
    assert re.search(r"executed in \d+\.\d{4}s", captured.err)
