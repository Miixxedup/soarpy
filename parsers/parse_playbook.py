def parse_playbook(filepath):
    book = ingest_logic(filepath)
    return book

def ingest_logic(filepath):
    g = []
    with open(filepath, 'r') as f:
        g = f.read().split(" --> ")
    return g
    