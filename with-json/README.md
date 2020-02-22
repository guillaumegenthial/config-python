# Configuration and Dependency Injection with custom JSON serialization

Make each class inherit a special `Serializable` interface that implements 2 methods
- `from_params(cls, params: Dict)`: create instance of `cls` using parameters in `params`
- `from_dict(data: Dict)`: create instance, infer class from `data["type"]` use `from_params` on `data["params"]`

Using inspection and generic tests, it is easy to automate most serialization scenarios (nesting, etc.).

## Run

Run example with

```bash
python run.py
```

## Discussion

Notice that the two layers have different instances of the same vocab (the python `id`s are not the same).

There are ways to improve the `Serializable` interface to support singletons, scoping, but this goes beyond the scope of this dummy example.
