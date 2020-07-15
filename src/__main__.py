"""This module defines the behaviour of the package
in a top-level script environment.

The following command executes this script:

```bash
python -m picharsso
```
"""

from .cli import main

if __name__ == "__main__":
    main()
