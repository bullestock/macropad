if window.wait_for_exist('Double Commander', timeOut=0):
    window.activate('Double Commander', False, False)
else:
    system.exec_command('doublecmd', getOutput=False)
