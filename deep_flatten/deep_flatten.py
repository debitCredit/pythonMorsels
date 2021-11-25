from collections.abc import Iterable


def deep_flatten(iterable):
    """Flatten an iterable of iterables."""
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from deep_flatten(item)
        else:
            yield item
