from functools import wraps
from dataclasses import dataclass

NO_RETURN = object()


@dataclass
class Call:
    args: tuple
    kwargs: dict
    return_value: object
    exception: object


def record_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        try:
            return_value = func(*args, **kwargs)
        except (ValueError, TypeError) as err:
            wrapper.calls.append(Call(args, kwargs, NO_RETURN, err))
            raise
        else:
            wrapper.calls.append(Call(args, kwargs, return_value, None))
            return return_value
    wrapper.call_count = 0
    wrapper.calls = []

    return wrapper
