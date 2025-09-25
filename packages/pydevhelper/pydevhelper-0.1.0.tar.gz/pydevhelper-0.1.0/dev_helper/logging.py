import logging

def setup_logging(level=logging.INFO) -> None:
    """Setup basic logging for terminal output."""

    root = logging.getLogger()
    root.setLevel(level)

    # Limpa handlers antigos
    for handler in list(root.handlers):
        root.removeHandler(handler)

    handler = logging.StreamHandler()  # padrão (stderr), compatível com caplog
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S"
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)
