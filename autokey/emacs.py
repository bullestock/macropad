if window.wait_for_exist('.*Emacs', timeOut=0):
    window.activate('emacs', False, False)
else:
    system.exec_command('emacs', getOutput=False)
