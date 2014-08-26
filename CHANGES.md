Changelog
=========

0.4 (dev)
---------

- Upgrade Python 3.3.x to 3.4.1

0.3.4 (2014/08/22)
------------------

- Updated instructions to run `bootstrap.bat` as administrator
- Fixed path quoting and condition check in `bootstrap.bat`

0.3.3 (2014/07/30)
------------------

- Added copies of binary installers to the server and GitHub
- Upgraded Python 2.7.6 to 2.7.8

0.3.2 (2014/04/10)
------------------

- Fixed serve high CPU utilization due to busy wait loop

0.3.1 (2014/04/10)
------------------

- Fixed Windows install error by removing pip dependency
- bootstrap.py is now downloaded to the current directory for offsite support

0.3 (2014/03/19)
----------------

- Updated from jacebrowning/template-pyhton
- Bumped bootstrap.bat Python versions to 2.7.6 and 3.3.5
- Explicity using 'pip==1.5.2' and 'virtualenv==1.10' in bootstrap.py
- Python's FTP location changed to "legacy.python.org"

0.2.2 (2014/02/07)
------------------

- Fixed 'install' command on Cygwin

0.2.1 (2014/02/07)
------------------

- Fixed expansion of package tuple

0.2 (2014/02/07)
----------------

- Added 'pylint', 'nose', and 'coverage' to bootstrap.py

0.1.2 (2014/01/16)
------------------

- Added PySVN to bootstrap.py

0.1.1 (2013/10/31)
------------------

- Now copying a default .pypirc file
- Added pauses to bootstrap.bat

0.1.0 (2013/10/30)
------------------

- First stable release

0.0.2 (2013/10/30)
------------------

- Improved Linux support
- Added '--port' argument to 'arnie serve'

0.0.1 (2013/10/28)
------------------

- Initial release
