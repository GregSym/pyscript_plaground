# Playing around with PyScript

## just tinkering with some new python toys

src found here:
* https://github.com/pyscript/pyscript

## importing scripts:
chrome doesn't like importing a file from a 'file://' origin so to do the file import test I recommend a quick server

open terminal in this dir and:
```
python -m http.server
```
and then import.html's import will work

the server should go to:
http://localhost:8000/

by default

(any other solution will also work - for help: https://stackoverflow.com/a/21608670/15002486)