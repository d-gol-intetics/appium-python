# appium-python

How to prepare and run tests of this solution on Windows 10 from scratch

1. Install Python and Pip
https://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/

2. Install PyCharm Community Edition

3. Install packages from command prompt - type
pip install selenium
pip install behave
pip install nose

4. Follow the guide from link below. Be attentive. Stop following the guide when you hit the line - 'Download a sample .apk file from APKPure'
https://www.swtestacademy.com/appium-tutorial/

5. Install Twitter app on emulator or phone - where you want to run tests

6. Navigate to webdriver/driver.py in framework. Leave the desired_caps variable initialisation you want depending on where you want to run tests - emulator/phone

7. In Command prompt cd to framework root directory

8. If you are running tests on emulator - make sure emulator is running

9. Type 'behave'

The tests should be running now on emulator or phone. 
