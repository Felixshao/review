"""---------------------------------- with用法 -----------------------------------------------------------------"""
class Sample:
    def __enter__(self):

        return "Foo"

    def __exit__(self, type, value, trace):
        pass

def get_sample():
    return Sample()


if __name__ == '__main__':
    with open('../file/1234.txt', 'r', encoding='utf-8') as txt:
        print(txt)