if window.wait_for_exist('terminator', timeOut=0):
    window.activate('terminator', False, False)
else:
    system.exec_command('terminator', getOutput=False)
