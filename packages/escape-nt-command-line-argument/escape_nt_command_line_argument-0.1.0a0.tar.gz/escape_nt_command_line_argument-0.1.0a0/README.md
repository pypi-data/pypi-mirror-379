# `escape-nt-command-line-argument`

A readable, reliable, reviewable solution for escaping NT command-line arguments with explicit, single-pass state
machine logic.

## Features

- Correctly escapes any argument for safe use with `CreateProcessW`, including all tricky cases (backslashes, quotes,
  whitespace, trailing slashes, etc.)
- Explicit, single-pass state machine logic: readable, reliable, reviewable.
- Immutable, functional programming style: each character is processed atomically, ensuring precise and predictable
  results.
- Supports Python 2+.

## Installation

```sh
pip install escape-nt-command-line-argument
```

## Usage

```python
# coding=utf-8
from __future__ import print_function

import sys
from typing import Text
from escape_nt_command_line_argument import escape_nt_command_line_argument

if sys.version_info < (3,):
    def raw_unicode_input(prompt):
        # type: (Text) -> Text
        return raw_input(prompt.encode(sys.stdout.encoding)).decode(sys.stdin.encoding)
else:
    def raw_unicode_input(prompt):
        # type: (Text) -> Text
        return input(prompt)

while True:
    to_escape = raw_unicode_input(u'Enter an NT command-line argument: ')
    print(escape_nt_command_line_argument(to_escape))
```

```
Enter an NT command-line argument: C:\Users
C:\Users

Enter an NT command-line argument: C:\Program Files
"C:\Program Files"

Enter an NT command-line argument: \
"\\"

Enter an NT command-line argument: \\
"\\\\"

Enter an NT command-line argument: \\\
"\\\\\\"

Enter an NT command-line argument: "
"\""

Enter an NT command-line argument: ""
"\"\""

Enter an NT command-line argument: \"
"\\\""

Enter an NT command-line argument: \\"
"\\\\\""

Enter an NT command-line argument: "\"
"\"\\\""

Enter an NT command-line argument: \\""
"\\\\\"\""

Enter an NT command-line argument: C:\Users\
"C:\Users\\"

Enter an NT command-line argument: "abc" & "def"
"\"abc\" & \"def\""

Enter an NT command-line argument: "a&"b"c"d""
"\"a&\"b\"c\"d\"\""
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).