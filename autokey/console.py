if window.wait_for_exist('Terminal', timeOut=0):
    window.activate('Terminal', False, False)
else:
    system.exec_command('xfce4-terminal', getOutput=False)
