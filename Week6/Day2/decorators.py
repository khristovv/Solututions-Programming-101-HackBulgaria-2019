def accepts(*types):
    """accepts decorator, validates if the given func arguments are of the desired type"""
    def acceptor(func):
        def decorated(*args):
            for i in range(len(args)):
                if not isinstance(args[i], types[i]):
                    raise TypeError(f"Error, expected type: {types[i]} \
                                    for argument {args[i]}, got {type(args[i])}")
            return func(*args)
        return decorated
    return acceptor


def encrypt(key):
    """Encrypt decorator, encrypts the given string using Caesar Cipher method."""
    def encrypt_wrapper(func):
        def func_wrapper(string):
            from string import ascii_lowercase as letters
            encrypted_str = ''
            for ch in string:
                if ch.isupper() and ch.lower() in letters:
                    encrypted_str += letters[(letters.index(ch.lower()) + key) % len(letters)].upper()
                elif ch in letters:
                    encrypted_str += letters[(letters.index(ch) + key) % len(letters)]
                else:
                    encrypted_str += ch
            return func(encrypted_str)
        return func_wrapper
    return encrypt_wrapper


def log(logs_file):
    """Logs to a file the date & time the function was called"""
    from datetime import datetime
    def log_wrapper(func):
        def func_wrapper(*args, **kwargs):
            date = datetime.now()
            func(*args, **kwargs)
            with open(logs_file, 'a') as f:
                f.write(f'{func.__name__} called, at {date}\n')
        return func_wrapper
    return log_wrapper


def performance(file):
    """Measure and save to a file the runtime of a func."""
    import time
    def performance_wrapper(func):
        def save_to_file(func_name, run_time):
                with open(file, 'a') as f:
                    f.write(f'{func_name} called, took {run_time:.2f} seconds to complete\n')
        def func_wrapper(*args, **kwargs):
            start = time.perf_counter()
            func(*args, **kwargs)
            run_time = time.perf_counter() - start
            save_to_file(func.__name__, run_time)
        return func_wrapper
    return performance_wrapper


def main():
    @performance('performance_log.txt')
    @log('logs.txt')
    def get_squares(lst):
        return [num**2 for num in lst]

    get_squares([i for i in range(10000)])
    # @accepts(str, int)
    # def say_hello(name, age):
    #     print(f'name: {name}, age: {age}')
    #
    # @encrypt(2)
    # def print_str(string):
    #     print(string)
    #
    # print_str('Get get get low  ')


if __name__ == '__main__':
    main()


