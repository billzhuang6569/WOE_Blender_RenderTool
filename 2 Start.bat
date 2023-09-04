echo Running...
echo ---------------

start "BlenderRenderTool" /D "%~dp0\py" python "Render_Blender.py"


@echo Render Completed!
@echo Press any key to exit!
@echo See you next time!
pause
taskkill /FI "WINDOWTITLE eq BlenderRenderTool*" /T /F