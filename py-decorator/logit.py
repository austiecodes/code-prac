from functools import wraps


class Logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)

            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')

            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        pass


class EmailLogit(Logit):
    def __init__(self, email='admin@pornhub.com', *args, **kwargs):
        self.email = email
        super(EmailLogit, self).__init__(*args, **kwargs)

    def notify(self):
        pass


@Logit()
def addition_func(x):
    return x + x


@Logit(logfile='out2.log')
def add2(x):
    return x + 2


result = addition_func(4)
result2 = add2(3)

print(result)
print(result2)
