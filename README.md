# wizconfig
An incomplete configuration shall not pass.

![You_Shall_Not_Pass!_0-1_screenshot](https://github.com/ACONIO/wizconfig/assets/29633518/702cfbd6-de4f-4d40-9062-06cf8d8c8c55)

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


