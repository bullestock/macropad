#F3::

WinGet, win, List, ahk_class MozillaWindowClass

Loop %win%
{
   myid := win%A_Index%
   WinGetTitle title, ahk_id %myid%
   if title contains Mozilla Firefox
      WinActivate, ahk_id %myid%
      Break
}
return
