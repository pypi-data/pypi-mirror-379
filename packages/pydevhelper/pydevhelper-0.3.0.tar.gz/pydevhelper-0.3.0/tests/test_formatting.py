import pytest
from dev_helper import print_table

def test_print_table_with_rich_renders_correct_data(capsys):
    """
    Verifica se a função print_table, usando 'rich', renderiza
    o título, os cabeçalhos e os dados corretamente no output.
    """
    # 1. Prepara os dados de teste
    test_banner = "E Corp Nodes"
    test_payload = [
        {"node_id": "0xDEADBEEF", "status": "COMPROMISED"},
        {"node_id": "0xCAFEBABE", "status": "ROOT"},
    ]

    # 2. Executa a função
    print_table(test_payload, banner=test_banner)
    captured_output = capsys.readouterr().out

    # 4. Verifica se os elementos essenciais estão no output
    # Verifica o título
    assert test_banner in captured_output

    # Verifica os cabeçalhos
    assert "node_id" in captured_output
    assert "status" in captured_output

    # Verifica os dados das linhas
    assert "0xDEADBEEF" in captured_output
    assert "COMPROMISED" in captured_output
    assert "0xCAFEBABE" in captured_output
    assert "ROOT" in captured_output


def test_print_table_with_rich_empty_payload(capsys):
    print_table([])
    captured_output = capsys.readouterr().out
    
    # O output deve ser uma string vazia
    assert captured_output == ""