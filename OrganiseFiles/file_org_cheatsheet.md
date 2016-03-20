# File Organisation Cheat sheet 
shutil - shell utilities module
send2trash - safe deletes 

## Easy copying and moving 
shutil.copy(src, dest)
shutil.move(src, dest)

## Permanent deletion 
os.unlink(path) - deletes file at path
os.rmdir(path) - delete folder at path (must be empty)
os.rmtree(path) - delete all files and folder at path

## Send stuff to recyling bin
send2trash.send2trash(path)

## Walking a directory tre
currentFolderName, listOfSubfolders, listOfFiles = os.walk()

## File compression
zipfile module
Make ZipFIle object - zipfile.ZipFile(zip file)
zipFile.extractall()
### Editing a zipped filed 
newZip = zipfile.ZipFile(file, 'w') - open the file in write mode 
newZip.write(file, options)