import time

def log(fn):
     def wrapper(*args, **kwargs):
            start_time = time.time()

            result = fn(*args, **kwargs)

            end_time = time.time()

            execution_time = end_time - start_time
            param_names = fn.__code__.co_varnames

            args_str = ", ".join(
                f"{param_names[i]}={args[i]}"
                for i in range(len(args))
            )

            kwargs_str = ", ".join(
                f"{k}={v}" for k, v in kwargs.items()
            )

            with open('log.txt', 'a') as f:
                f.write(
                    f'{fn.__name__}; '
                    f'args: {args_str};'
                    f' kwargs: {kwargs_str}; '
                    f'execution time: {execution_time:.2f} sec.\n'
                )

            return result
     return wrapper


def foo(a, b, c):
    time.sleep(0.1)

foo(1, 2, c=3)

