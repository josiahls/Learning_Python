"""
Create an exe file


"""

from cx_Freeze import setup, Executable

setup(name='URLParser', version='0.1', description='Parse Stuff',
      executables=[Executable("/home/josiah/PycharmProjects/Learning_Python/test_file.py")])



