from cx_Freeze import setup, Executable

# need to install visual studio c++
# pip install cx_Freeze-5.1.1.[...].whl
# python setup.py build


# On appelle la fonction setup
setup(
    name = "Tutorial",
    version = "1.0.0",
    description = "Starting Pyhton",
    executables = [Executable("../1_start/1_pythonrefresh.py")],
)
