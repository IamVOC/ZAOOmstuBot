from patterns import Singleton


class exceptionHandler(metaclass=Singleton):

    def exCatcher(self, func):
        def inner_function(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as ex:
                Logger.log(ex)
                self.exHandler(ex, func)
    
        return inner_function
    
    def exHandler(exception, func):
        pass
