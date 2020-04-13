import os

def get_path():

    current_path = os.path.split(os.path.realpath(__file__))[0]
    project_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + '.')
    print(project_path)


if __name__ == '__main__':

    get_path()