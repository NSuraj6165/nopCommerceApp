pytest -v -s -m "sanity" testCases/ --browser chrome
REM pytest -v -s -m "sanity or regression" testCases/ --browser chrome
REM pytest -v -s -m "sanity and regression" testCases/ --browser chrome
REM pytest -v -s -m "regression" testCases/ --browser chrome