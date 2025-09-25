from typing import List, Dict

def print_table(data: List[Dict]) -> None:
    """Pretty print a list of dictionaries as a table."""
    if not data:
        print("(no data)")
        return

    headers = list(data[0].keys())
    col_widths = {h: max(len(h), *(len(str(row[h])) for row in data)) for h in headers}

    # Print header
    header_row = " | ".join(f"{h:{col_widths[h]}}" for h in headers)
    print(header_row)
    print("-" * len(header_row))

    # Print rows
    for row in data:
        print(" | ".join(f"{str(row[h]):{col_widths[h]}}" for h in headers))
