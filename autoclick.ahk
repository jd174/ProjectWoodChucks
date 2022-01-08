PrintScreen::Reload

;Click simple

+Capslock::
Loop
{
if GetKeyState("Capslock", "T")
{
Click 10
}
}