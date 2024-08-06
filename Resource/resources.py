import os
import inspect


class Base:
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parent_dir = os.path.dirname(current_dir)
    HTML_Report_Path = parent_dir + "\Reports"

    desired_cap = dict(
        deviceName='emulator-5554',
        platformName='Android',
        automationName='UiAutomator2',
        app='C:\\Users\\dev\\Desktop\\HVIE APKS\\25 August\\25 Aug Dev.apk'

        # Other Capabilities
    )

    host = "http://127.0.0.1:4723"
