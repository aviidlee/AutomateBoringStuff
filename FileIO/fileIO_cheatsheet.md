os.getcwd()
os.path.join()

os.path.exists(<path>)
os.path.isfile(<path>)
os.path.isdir(<path>)

os.listdir(<path>)

## Saving binary files 
Module = shelve 

shelve.open(<file>)
shelve[<data label>] = <data; e.g., list>

## Using pprint to store variables as text files
Module = pprint  
pprint.pformat(<list or dict>) returns syntactically-correct string rep of the argument; save in a .py file as use the file like a module to reload data.