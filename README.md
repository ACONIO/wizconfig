# magiconfig
An easy way to validate if your config's completeness

## Install

```zsh
pip install git+https://github.com/ACONIO/magiconfig.git
```

## Example

```python
class TestConfig(mc.MagicConfig):
    TEST_KEY = os.getenv("TEST_KEY")  # mandatory
    TEST_API_KEY = os.getenv("TEST_API_KEY"), False  # optional
    TEST_DEBUG = os.getenv("TEST_DEBUG"), True  # mandatory (verbose)
    TEST_MODE = os.getenv("TEST_MODE", "DEV")  # mandatory with default value
```


