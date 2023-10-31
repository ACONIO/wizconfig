from os import getenv
from context import wizconfig as wc
from dotenv import load_dotenv

load_dotenv()


class TestConfig(wc.WizConfig):
    TEST_KEY = getenv("TEST_KEY")  # mandatory
    TEST_API_KEY = getenv("TEST_API_KEY"), False  # optional
    TEST_DEBUG = getenv("TEST_DEBUG"), True  # mandatory (verbose)

    TEST_MODE = getenv("TEST_MODE", "DEV")  # mandatory (default)


if __name__ == "__main__":
    cfg = TestConfig()
    print(cfg)
