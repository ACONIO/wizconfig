from os import getenv
from context import magiconfig as mc
from dotenv import load_dotenv

load_dotenv()


class TestConfig(mc.MagicConfig):
    TEST_KEY = getenv("TEST_KEY")  # mandatory
    TEST_API_KEY = getenv("TEST_API_KEY"), False  # optional
    TEST_DEBUG = getenv("TEST_DEBUG"), True  # mandatory (verbose)

    TEST_MODE = getenv("TEST_MODE", "DEV")  # mandatory (default)


if __name__ == "__main__":
    cfg = TestConfig()
    print(cfg)
