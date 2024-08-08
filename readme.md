## Use Chromedriver

You'll need ChromeDriver to control the Chrome browser. You can download it from the official chrome site. Make sure the version matches your installed version of Chrome.

* **Unzip the file** and place the executable in a directory included in your system's `PATH`, or specify the path directly in your script.

https://developer.chrome.com/docs/chromedriver/downloads

In voteSimulate.py code,  
Use the Path to the Executable: Make sure the chrome_driver_path points directly to the chromedriver file inside the extracted directory.
File Permissions: If the issue persists, ensure the chromedriver file has execute permissions (chmod +x chromedriver).

chrome_driver_path = 'PATH-TO-CHROME-DRIVER-IN-COMPUTER'

## Dependencies Install

you can install all the dependencies listed in the requirement file using:

pip install -r requirements.txt

## Run

`python voteSimulate.py`

terminal log

```python3 voteSimulate.py
Running iteration 1
Voted successfully!
wait .. for math
math: [1, 8]
Voted successfully, including solving the CAPTCHA! ->  9
Running iteration 2
Voted successfully!
wait .. for math
math: [10, 3]
Voted successfully, including solving the CAPTCHA! ->  13
Running iteration 3
Voted successfully!
wait .. for math
math: [1, 5]
Voted successfully, including solving the CAPTCHA! ->  6
Running iteration 4
Voted successfully!
wait .. for math
math: [1, 6]
Voted successfully, including solving the CAPTCHA! ->  7
Running iteration 5
Voted successfully!
wait .. for math
math: [4, 8]
Voted successfully, including solving the CAPTCHA! ->  12

```
