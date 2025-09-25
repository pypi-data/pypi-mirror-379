from dev_helper import print_table

def test_print_table_output(capsys):
    data = [{"id": 1, "name": "Alice"}]
    print_table(data)
    captured = capsys.readouterr()
    assert "id" in captured.out
    assert "Alice" in captured.out

def test_print_table_no_data(capsys):
    print_table([])
    captured = capsys.readouterr()
    assert "(no data)" in captured.out
