import os
import pytest
from dev_helper import require_vars, MissingEnvVarsError

def test_require_vars_pass(monkeypatch):
    monkeypatch.setenv("MY_ENV", "ok")
    # não deve lançar erro
    require_vars(["MY_ENV"])

def test_require_vars_fail(monkeypatch):
    monkeypatch.delenv("MISSING_ENV", raising=False)
    with pytest.raises(MissingEnvVarsError) as exc:
        require_vars(["MISSING_ENV"])
    assert "MISSING_ENV" in str(exc.value)
