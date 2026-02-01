import functools

def validate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not (0 <= arg <=256):
                return 'Function call is not valid!'
        for value in kwargs.values():
            if not (0 <= value <=256):
                return 'Function call is not valid!'

        return func(*args, **kwargs)
    return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"



# set_pixel(0, 127, 300)
set_pixel(0,127,250)
