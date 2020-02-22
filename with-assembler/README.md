# Configuration and Dependency Injection with `Assembler`

We create a special `Assembler` that parses information from a dictionary and creates the different objects, dealing with all the dependencies.

## Run

Run example with

```bash
python run.py
```

## Discussion

While this works well for our use-case, in some cases it might be limiting, as the `Assembler` does one thing only (what if we only want to create a `Vocab` for instance?).
