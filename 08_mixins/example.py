class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())

class ReprMixin:
    def __repr__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

class LogMixin:
    def log(self, msg):
        print(f"[{self.__class__.__name__}] {msg}")

class SaveMixin:
    def save(self, filename="data.txt"):
        with open(filename, "w") as f:
            for k, v in self.__dict__.items():
                f.write(f"{k}={v}\n")
        self.log(f"saved to {filename}")

class User(LogMixin, ReprMixin, SaveMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


u = User("Pedro", 38)
print(u)
u.log("hola")
u.save()

###############################


# Mini hands-on exercise

from datetime import datetime

class TimestampMixin:
    def add_timestamp(self, msg):
        return f"{datetime.now().isoformat()} - {msg}"

class FileLoggerMixin:
    filename = "log.txt"

    def log_to_file(self, msg):
        with open(self.filename, "a") as f:
            f.write(msg + "\n")

class ColorMixin:
    GREEN = "\033[92m"
    RESET = "\033[0m"

    def colorize(self, msg):
        return f"{self.GREEN}{msg}{self.RESET}"

class BaseLogger:
    def log(self, msg):
        print(msg)

#from timestamp_mixin import TimestampMixin
#from color_mixin import ColorMixin
#from file_logger_mixin import FileLoggerMixin
#from base_logger import BaseLogger

class SmartLogger(TimestampMixin, ColorMixin, FileLoggerMixin, BaseLogger):
    def log(self, msg):
        msg = self.add_timestamp(msg)
        msg = self.colorize(msg)
        self.log_to_file(msg)
        super().log(msg)

if __name__ == "__main__":
    logger = SmartLogger()
    logger.log("Hola Pedrin, logging inteligente!")



#### #########################
# anadimos otra nueva clase mixin
class BaseLogger:
    def log(self, msg):
        print(msg)

class TimestampMixin:
    def add_timestamp(self, msg):
        return "[TS] " + msg

class ColorMixin:
    def colorize(self, msg):
        return f"\033[92m{msg}\033[0m"

class FileLoggerMixin:
    def log_to_file(self, msg):
        with open("logs.txt", "a") as f:
            f.write(msg + "\n")

class StatsMixin:
    def __init__(self):
        self.log_count = 0
        super().__init__()

    def log(self, msg):
        self.log_count += 1
        super().log(msg)

class SmartLogger(StatsMixin,
                  TimestampMixin,
                  ColorMixin,
                  FileLoggerMixin,
                  BaseLogger):

    def log(self, msg):
        msg = self.add_timestamp(msg)
        msg = self.colorize(msg)
        self.log_to_file(msg)
        super().log(msg)

# Uso
logger = SmartLogger()
logger.log("Hola mundo")
logger.log("Segundo log")

print("Número de logs:", logger.log_count)

