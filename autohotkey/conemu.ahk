#F2::

WinGet, win, ID, ahk_class VirtualConsoleClass
WinActivate, ahk_id %win%
WinWaitActive, ahk_id %win%

return
