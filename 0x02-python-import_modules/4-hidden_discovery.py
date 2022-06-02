#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for term in dir(hidden_4):
        if not (term.startswith('_')):
            print(term)
