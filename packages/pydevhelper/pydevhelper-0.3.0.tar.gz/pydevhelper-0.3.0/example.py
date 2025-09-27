from dev_helper import setup_logging, require_vars, timer, print_table

setup_logging()
require_vars(["PATH"])  # PATH sempre existe, só para teste

@timer
def main():
    data = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    print_table(data)

main()
