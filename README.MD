# Health Mate App Appium BDD Framework

### Environment
- Install [Appium Desktop](https://github.com/appium/appium-desktop). (Check [this section](https://github.com/appium/appium-desktop#installing-on-macos) if you've met an error popup on mac.
- Install [Android Studio](https://developer.android.com/)
- Install [Java JDK 8](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html) or Java [JDK 11](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html)
- Specify `ANDROID_HOME` and `ANDROID_SDK_ROOT` in your PATH [Link](https://developer.android.com/studio/command-line/variables)
- Specify `JAVA_HOME` in your PATH [Link for Mac](https://stackoverflow.com/questions/15826202/where-is-java-installed-on-mac-os-x)
- Use Android device only. There is no implementation for iOS.
- Optional: Install Allure using Homebrew to open the detailed report after test: `brew install allure`

### All packages installation
Simply type `pip install -r requirements.txt` into the terminal.

### Main Dependencies
- Appium-Python-Client: `pip install appium-python-client`
- Behave: `pip install behave`
- Allure-Behave: `pip install allure-behave`

### Device setup
1. Open Settings on your Android device and scroll down to `About phone` option and tap on it `7 times`. You will unblock the developer options with this action.
2. Proceed to Developer options and enable `USD Debugging`
3. Type in the terminal `adb start-server`, attach your Android device with USB.
4. Type adb devices, you will see `numbers` and word `device` in front of it. These numbers are your `udid`, you will need it pretty soon.
5. Open `Appium GUI`  and click `Edit configurations`, specify your `ANDROID_HOME` and `JAVA_HOME` paths
6. Start the Appium server, remember your Appium's server Host, you need to pass it to the `capabilities` in the project. (You can start the server with commandline as well).
7. Open the `capabilities.json` file in the project's root folder.
8. Specify your `Appium server IP`, `Android version`, `Device name` and `udid` inside of this file.

### Almost ready
1. Make sure that Appium server is on, you've set capabilities, your phone is attached with usb cable and it is unlocked
2. You need to have the [Health Mate application](https://play.google.com/store/apps/details?id=com.withings.wiscale2&hl=en&gl=US) installed on your phone
3. **Important: That's the prod version of the app, and we cannot proceed through the email or two-factor auth with this framework. You need to log in and proceed to the Home screen first manually. After it, Appium won't clear app's cache and use your account to execute test.**

### Start the test
In project's root directory type `behave features/change_weight.feature` in terminal.

To get the report after test type `behave -f allure_behave.formatter:AllureFormatter -o ./features/artifacts/reports ./features`.

### After test
When the test would be finished, in the `features/artifacts` folder you can find screenshots for the successfully executed scenarios.

**If you have chosen an option with generating report:**
In the `features/artifacts/reports` folder, you can find an Allure report in JSON format.

If you want to open in the `html` format, just type `allure serve ./features/artifacts/reports`.

Note: Remember that `artifacts` folder (including screenshots and reports) would be cleared automatically when the next test run starts.
