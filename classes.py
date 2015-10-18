class ReadOnly(object):
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise Exception("Changing read only attribute")
        else:
            self.__dict__[key] = value


def read_only_test():
    a = ReadOnly()

    a.a = 1
    print(a.a)
    a.a = 2
    print(a.a)


if __name__ == "__main__":
    read_only_test()
