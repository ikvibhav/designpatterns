class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


if __name__ == "__main__":
    t = Singleton()
    print(t)
    s = Singleton.get_instance()
    print(s)
    t = Singleton.get_instance()
    print(t)
    s = Singleton()
    print(s)