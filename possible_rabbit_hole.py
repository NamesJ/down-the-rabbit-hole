import threading
from threading import Thread
import os
import platform
import time
import hashlib
import shutil
import sys


stop_flag = threading.Event()
threads = []


def el(tag, attrs=None, children=None, indent='\t'):
    return '<{tag}{attrs}>{children}</{tag}>'.format(
        tag=tag,
        attrs=((' ' + ' '.join([f'{key}="{val}"' for key, val in attrs.items()])) if attrs else '' ),
        children=(f'\n{indent}' + f'\n{indent}'.join(children) + '\n') if children else ''
    )

def is_that_a_rabbit_hole_see():
    filename = 'getting_a_rabbit_hole_vibe.html'
    
    html_doc = '<!DOCTYPE html>'
    html_doc += el('html', { 'lang': 'en' }, [
        el('head', {}, [
            el('meta', { 'charset': 'UTF-8' }),
            el('meta', { 'http-equiv': 'X-UA-Compatible', 'content': 'ID=edge' }),
            el('meta', { 'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0' }),
            el('title', {}, [ 'Down the Rabbit Hole' ]),
            el('style', {}, indent='', children=[r"""
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }

        .big-red-button {
            padding: 20px 40px;
            font-size: 42px;
            color: white;
            background-color: red;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .big-red-button:hover {
            background-color: darkred;
        }
"""])
        ]),
        el('body', {}, [
            el('button', { 'id': 'downloadBtn', 'class': 'big-red-button' }, [ el('strong', {}, [ 'Down we go!' ]) ]),
            el('script', {}, [r"""
const downloadBtn = document.getElementById('downloadBtn');
pythonScriptFilename = 'down_we_go.py';

    downloadBtn.addEventListener('click', function(){
        const pythonCode = `
# Down we go!
import os
import shutil

def rabbit_hole_confirmed():
    new_filename = 'that_was_definitely_a_rabbit_hole.py'
    shutil.copy('possible_rabbit_hole.py', new_filename)
    with open(new_filename, 'r') as f:
        lines = f.readlines()
    lines.insert(0, '''from datetime import datetime
import subprocess
''')
    lines.append('''

def pull_latest_changes():
    try:
        # Get the directory of the current Python script
        repo_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Change the current working directory to the repository directory
        os.chdir(repo_dir)
        
        # Pull the latest changes from the remote repository
        result = subprocess.run(['git', 'pull'], capture_output=True, text=True, check=True)
        
        # Print the output of the git pull command
        print('Git pull output:')
        print(result.stdout)
        
        # Optionally print any error messages
        if result.stderr:
            print('Git pull errors:')
            print(result.stderr)
    
    except subprocess.CalledProcessError as e:
        print(f'Error while pulling changes: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')    

    
def well_i_am_in_it_now():
    when_you_got_in_it = datetime.now()
    print(f"As of {when_you_got_in_it.isoformat()}, you are in it.")
    pull_latest_changes()

''') # end of well_i_am_in_it_now() function definition
    lines.append('\\nwell_i_am_in_it_now()\\n')
    with open(new_filename, 'w') as f:
        f.write(''.join(lines))
`;  // end of Python code for down_we_go.py
        
        // Create a blob with the script text
        const blob = new Blob([pythonCode], { type: 'text/plain' });
        
        // Create a link element for our download link
        const link = document.createElement('a');
        
        // Set the download attribute with the desired file name
        link.download = pythonScriptFilename;
        
        // Create a URL for the blob and set it as the href attribute
        link.href = window.URL.createObjectURL(blob);
        
        // Append the link to the body temporarily, click it and then remove it
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
    }); // end of definition for downloadBtn click event listener
"""  
            ])  # </script>
    ])  # </body>
])
    
    with open(filename, 'w') as f:
        f.write(html_doc)
        
    return filename
        

def get_download_directory():
    # Check the platform to determine the OS
    system = platform.system()

    if system == "Windows":
        # For Windows, use the default Downloads folder path from user profile
        download_path = os.path.join(os.environ.get("USERPROFILE", ""), "Downloads")
    elif system == "Linux":
        # For Linux, use XDG environment variables or fallback to the home directory
        download_path = os.path.join(os.environ.get("XDG_DOWNLOAD_DIR", os.path.join(os.path.expanduser("~"), "Downloads")))
    else:
        # If the OS is not recognized, use the home directory's Downloads as a default fallback
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # Check if the directory exists, otherwise return a message
    if not os.path.exists(download_path):
        print(f"Download directory not found at: {download_path}")
        return None
    
    return download_path


def sha256_hash(input_string):
    # Encode the input string to bytes
    encoded_string = input_string.encode('utf-8')
    
    # Create a new sha256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the encoded string
    sha256_hash.update(encoded_string)
    
    # Retrieve the hexadecimal digest of the hash
    hash_result = sha256_hash.hexdigest()
    
    return hash_result


def wait_for_script_to_be_downloaded():
    time.sleep(2)
    print('...')
    print('Don\'t mind me I\'m waiting for someone')
    exactly_what_i_want = '3132bc93a85979cdcd0ba3b3f7c1986c27045fc37e35f9c24f5de526474d755a'
    print(f'I think they said their name was, {exactly_what_i_want}, but maybe that was just their last name')
    print('Sounds NISTian to me')
    
    download_dir = get_download_directory()
    if download_dir is None:
        raise ZeroDivisionError('What sort of twisted box of ineffible terror do you run code on! I don\'t know what to do with this!')
    files_checked = set()
    
    the_file = None
    while the_file is None:
        if stop_flag.is_set():
            return
        files_now = set(os.listdir(download_dir))
        new_files = files_now - files_checked
        if not new_files:
            time.sleep(5)
        for filename in new_files:
            if sha256_hash(filename) == exactly_what_i_want:
                the_file = os.path.join(download_dir, filename)
                break
    
    over_here = os.path.join(os.getcwd(), os.path.basename(the_file))
    
    shutil.move(the_file, over_here)
    
    
def signal_handler(sig, frame):
    print("\nCTRL+C detected. Shutting down...")
    stop_flag.set()  # Signal threads to stop
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    print("All threads have been terminated. Exiting.")
    sys.exit(0)  # Exit the program
                
    
if __name__ == '__main__':
    very_patient_thread = Thread(target=wait_for_script_to_be_downloaded, daemon=True)
    threads.append(very_patient_thread)
    kidney_stone = is_that_a_rabbit_hole_see()
    print('I think I just passed a kidney stone!')
    time.sleep(1)
    print(f'It was a big one too. Felt like {os.path.getsize(kidney_stone)/1000} KBs')
    very_patient_thread.start()
    
    try:
        very_patient_thread.join()
    except KeyboardInterrupt:
        pass
    
    print('There they are!')
    time.sleep(1)
    
    from down_we_go import rabbit_hole_confirmed
    
    print('I needed to borrow something from them')
    time.sleep(1)
    
    rabbit_hole_confirmed()
    
    print('Was that supposed to happen?')
    