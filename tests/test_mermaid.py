import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import json
from server.models import Diagram
from server.validator import validate
from server.mermaid import to_mermaid

EXAMPLES = [
    (
        "flowchart",
        "ir/examples/flowchart.json",
        """flowchart TD
A["Start"]
B["Step B"]
C["Step C"]
D["Decision?"]
E["Path E"]
F["Path F"]
A --> B
B --> C
C --> D
D -->|yes| E
D -->|no| F""",
    ),
    (
        "timeline",
        "ir/examples/timeline.json",
        """timeline
title Cosmic Timeline
13.8e9 years ago : Big Bang
300k years ago : First humans
2,000 years ago : Jesus born
1939-1945 : WWII""",
    ),
    (
        "mind_map",
        "ir/examples/mindmap.json",
        """mindmap
root((Computer Science))
ai(AI)
net(Networks)
sec(Security)
root --> ai
root --> net
root --> sec""",
    ),
]


@pytest.mark.parametrize("name, path, expected", EXAMPLES)
def test_mermaid(name, path, expected):
    with open(path) as f:
        data = json.load(f)
    d = validate(data)
    out = to_mermaid(d)
    assert out.strip() == expected.strip()
