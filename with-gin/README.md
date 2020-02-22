# Configuration and Dependency Injection with gin-config

Use [gin-config](https://github.com/google/gin-config) to define our pipeline.

## Run

Run example with

```bash
python run.py
```

## Discussion

Notice how we use scoping to define dependencies for the different classes only in those scopes (meaning that we can create different instances of the same class with different dependencies as they are in separate scopes).
Also, we use the singleton functionality to shared the vocab across the different layers.
