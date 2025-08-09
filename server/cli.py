import json, sys
from .validator import validate
from .mermaid import to_mermaid


def main():
    data = json.load(sys.stdin) if len(sys.argv) == 1 else json.load(open(sys.argv[1]))
    d = validate(data)
    print(to_mermaid(d))


if __name__ == "__main__":
    main()
