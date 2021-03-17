# moodle_autouploader
auto upload files to moodle drag'n'drop fields

# System Requirements
  - Python 3.8+
  - Selenium
  - Helium
  - Google Chrome

# Installation
  - `pip install selenium`
  - `pip install helium`

# Run
  - open console and cd into code directory
  - `python.exe .\uploader.py`

# Restrictions and improvement plans
  - [ ] only works with same formatted Link on moodle page ("Anwesenheit dd.mm.yyyy") &#8594; add dynamic feature
  - [ ] get username AND password from file
  - [ ] run file continously and check if already a file has been uploaded &#8594; ignore already uploaded pages
  - [ ] improve page reloads with loops instead of try-except and function calls
