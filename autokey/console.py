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
    return False;

if is_process_running('terminator'):
    window.activate('terminator', matchClass=True)
else:
    system.exec_command('terminator', getOutput=False)
