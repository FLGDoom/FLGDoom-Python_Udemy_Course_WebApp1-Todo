# dashier ist jetzt ein module

# constances schreibt in der regel über den modulen und in CAPS
FILEPATH = r"saves\todos.txt"

DEFAULT_PRINTABLE = "test"
def test(printable = DEFAULT_PRINTABLE):
    """ This does shit """
    print(printable)

#print("Hello from functions") # alles was normal im script steht wird automatisch beim importen in main.py ausgeführt also beim importen wird das ganze modul ausgeführt

# man kann aber machen:

if __name__ == "__main__": # das heißt dass dieses directly gerunt wird, wenn man das von wo anders aus ausführt wird __name__ anders und stimmt die bedingung nicht mehr
    print("test, test")
# also beim indrekten ausführen passoirt nichts
# und dann kann man lokal in function.py testen ohne dass das beim importen ausgeführt wird

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos = file.readlines()

    return todos

def write_todos(todos, filepath = FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)
        file.close()