# sphinx-c-autodoc-bug-mwe

MWE for a bug in sphinx-c-autodoc.

`sphinx-c-autodoc <= 1.4.0` does not document structs/typedefs/enums/unions when using `sphinx >= 8.2.0`, because of a
change introduced in https://github.com/sphinx-doc/sphinx/pull/13201.

## Testing

### Buggy behaviour
```bash
poetry install
poetry add sphinx^8.2.1
poetry run sphinx-build . build
firefox build/index.html
```

### Correct behaviour (pre sphinx 8.2.0)
To downgrade sphinx, do
```bash
poetry install
poetry add sphinx==8.1.3
poetry run sphinx-build . build
firefox build/index.html
```
