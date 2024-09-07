import os
import shutil


keep_these = {
    '.git',
    '.gitignore',
    'README.md',
    'possible_rabbit_hole.py',
    'cleanup.py'
}


def cleanup():
    for file in os.listdir('.'):
        if file in keep_these:
            continue
        print(f'Deleting {file}')
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)
        
        
if __name__ == '__main__':
    cleanup()