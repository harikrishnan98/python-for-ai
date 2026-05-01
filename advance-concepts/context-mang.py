from contextlib import contextmanager
import os

f = open('sample.txt','w')
f.write('Lorem this is a sample text for the sample txt file')
f.close()

with open('sample.txt','w') as f:
    f.write('Sample text for the sample file')


## Custom Context Manager

class Open_File():

    def __init__(self, filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


    
with Open_File('sample.txt', 'w') as f:
        f.write('Testing')


print('File closed:%s'% f.closed)

@contextmanager    
def open_file(file,mode):
     f = open(file,mode)
     yield f
     f.close()

with open_file('sample.txt','w') as f:
     f.write('Testing with context-manager')

print(f.closed)

@contextmanager    
def open_file_op(file,mode):
    try:
        f = open(file,mode)
        yield f
    finally:
        f.close()

with open_file_op('sample.txt','w') as f:
     f.write('Testing with context-manager')

print(f.closed)


## Real world example

cwd = os.getcwd()
# /Users/harikrishnanthangavelayutham/Documents/AIntelligence/Python Projects/python-for-ai/advance-concepts/
os.chdir('sample-dir-one')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('sample-dir-two')
print(os.listdir())
os.chdir(cwd)

# Saving the current directory and switching another dir 

# Switching again back to original cwd - teardown - __exit__

@contextmanager
def set_curr_dir(dest_dir):
    try:
        cwd = os.getcwd()
        os.chdir(dest_dir)
        yield # We don't want to yield anything here Unlike in open_file we are not going to use
        # the returned value from the yield like f.write

    finally:
        os.chdir(cwd) # Making sure its again setting the cwd when context exit (teardown)


with set_curr_dir('sample-dir-one'): # Since we are not returning anythin we don't need as f or some varname
    print(os.listdir())

with set_curr_dir('sample-dir-one'): # Since we are not returning anythin we don't need as f or some varname
    print(os.listdir())