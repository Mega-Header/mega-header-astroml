$py = 'C:\Users\MENDOS\AppData\Local\Programs\Python312\python.exe'
Set-Location 'c:\Users\MENDOS\Desktop\mega-header-astroml'

& $py -m interrogate mega-header-astroml api tests *> '_ci_interrogate2.txt'
"interrogate_exit=$LASTEXITCODE" | Out-File -Append '_ci_interrogate2.txt'

& $py -m mypy mega-header-astroml/tracking/model_registry.py *> '_ci_mypy2.txt'
"mypy_exit=$LASTEXITCODE" | Out-File -Append '_ci_mypy2.txt'
