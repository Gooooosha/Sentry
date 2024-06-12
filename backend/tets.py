import linecache
import sys


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка в функции: {func.__name__}")
            print(f"Подробности по ошибке:\n{e}")

            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            line = linecache.getline(filename, lineno, f.f_globals)
            print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

            return None

    return inner_function


@exception_handler
def test():
    x = 1 / 0
    print(x)


if __name__ == "__main__":
    test()
