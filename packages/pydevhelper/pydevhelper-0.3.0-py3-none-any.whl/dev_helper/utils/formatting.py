# ----------------------------------------------------------------------------
# // Author: E. Alderson
# // Target: System Console Output
# // Mission: Expose the raw data. Make them see the truth behind the noise.
# // "Our democracy has been hacked." - fsociety
# ----------------------------------------------------------------------------

from typing import List, Dict, Any
from rich.console import Console
from rich.table import Table
from rich.style import Style


def print_table(payload: List[Dict[str, Any]], banner: str = "") -> None:

    if not payload:
        return  
    shell = Console()

    grid = Table(
        title=f"[bold red]>[/bold red] {banner}" if banner else "",
        title_justify="left",
        header_style=Style(color="red", bold=True),
        border_style=Style(color="bright_black"),
        show_lines=True,
    )
    headers = sorted(list(set(key for entity in payload for key in entity.keys())))

    # Construct the grid structure. Each column is a vulnerability.
    for header in headers:
        grid.add_column(header, style=Style(color="green"), no_wrap=False)

    for entity in payload:
        # Don't crash on their corrupted data. Use .get(). Stay hidden.
        values = [str(entity.get(h, "")) for h in headers]
        grid.add_row(*values)

    # Execute. Render the payload to the shell.
    shell.print(grid)
    # Now they have to look.

if __name__ == '__main__':
    # Sample payload. Could be anything. User credentials, process lists...
    # Let's say we've dumped E Corp's active network nodes.
    e_corp_nodes = [
        {"node_id": "0xDEADBEEF", "hostname": "nyc-prx-01.e-corp.com", "status": "COMPROMISED", "ping_ms": 12},
        {"node_id": "0xBADF00D", "hostname": "beijing-data-03.e-corp.com", "status": "UNKNOWN", "ping_ms": 210},
        {"node_id": "0xFEEDFACE", "hostname": "lon-auth-02.e-corp.com", "status": "SECURE", "ping_ms": 55},
        {"node_id": "0xCAFEBABE", "hostname": "local-dev-elliot", "status": "ROOT", "ping_ms": 0},
    ]

    # Run the visualization. Title it. Let them know who did this.
    print_table(e_corp_nodes, banner="E Corp Network Status (fsociety dump)")

# // Are you seeing this too?
# // Exit.