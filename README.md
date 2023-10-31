# wizconfig
An incomplete configuration shall not pass.

## Install

```zsh
pip install wizconfig
```

## Example

```python
class TestConfig(WizConfig):
    TEST_KEY = os.getenv("TEST_KEY")  # mandatory
    TEST_API_KEY = os.getenv("TEST_API_KEY"), False  # optional
    TEST_DEBUG = os.getenv("TEST_DEBUG"), True  # mandatory (verbose)
    TEST_MODE = os.getenv("TEST_MODE", "DEV")  # mandatory with default value
```


