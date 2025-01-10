import psutil

def is_process_running(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

print('console.py check')

if is_process_running('terminator'):
    print('console.py activate')
    window.activate('terminator', matchClass=True)
else:
    print('console.py exec')
    system.exec_command('(cd && terminator)', getOutput=False)

#print("terminator: %s" % is_process_running('terminator'))
