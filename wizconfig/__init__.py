import inspect

from abc import ABC


class InvalidConfigException(ValueError):
    pass


class WizConfig(ABC):
    def __init__(self):
        """Validate config values.

        Raises:
            InvalidConfigException: Missing mandatory config value.
        """
        for k, v in self.__get_properties():
            if type(v) == tuple:
                if v[1] and v[0] is None:
                    raise InvalidConfigException(f"{k} value not set.")

                setattr(self, k, v[0])
            else:
                if v is None:
                    raise InvalidConfigException(f"{k} value not set.")

    def __str__(self):
        return str(self.__get_properties())

    def __get_properties(self):
        return [
            (k, v)
            for (k, v) in inspect.getmembers(self)
            if not (k.startswith("_") or inspect.ismethod(v))
        ]
