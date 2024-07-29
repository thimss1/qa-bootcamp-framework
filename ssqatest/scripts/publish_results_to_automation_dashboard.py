"""
Script to parse given junit xml file and sne test result to 'automation-dasshboard'.
The xml fle must be passed in as first parameter to the script.

Uses api to send the test result to automation-dashboard.
Automation-dashboard is a ui to see test results.

Example command:
$ python3 publish_results_to_automation_dashboard.py ./qa-bootcamp-framework/ssqatest/my_junit_report.xml


Example of calling the api to send the result:

    url = "http://automationdashboard.supersqa.com/postResult"

    payload = json.dumps({
      "startDateTime": "2022-12-12 00:00:00",
      "endDateTime": "2022-12-11 00:00:05",
      "numberOfTestCasesPassed": 10,
      "numberOfTestCasesFailed": 2,
      "testGroupName": "Regression FE Smoke",
      "resultStatus": "PASS"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    rs = requests.post(url=url, data=payload, headers=headers)
"""
# junit_xml_path = './qa-bootcamp-framework/ssqatest/my_junit_report.xml'


import sys
import xml.etree.ElementTree as ET
import pdb
from dateutil.parser import parse
from datetime import timedelta
import requests
import json
# get the file path from command line argument
# TODO: should take list of xml or check a folder for list of files and report all of them.
# TODO: exercise
junit_xml_path = sys.argv[1]
environment = 'prod'

if environment.upper() == 'STAGING':
    endpoint = 'http://staging.automationdashboard.supersqa.com/postResult'
elif environment.upper() == 'PROD':
    endpoint = 'http://automationdashboard.supersqa.com/postResult'
else:
    raise Exception(f"unknown environment '{environment}'")


# parse the xml
tree = ET.parse(junit_xml_path)
root = tree.getroot()

test_suite = root.find('testsuite')
name = test_suite.attrib['name']
errors = test_suite.attrib['errors']
failures = test_suite.attrib['failures']
skipped = test_suite.attrib['skipped']
total_number_of_tests = test_suite.attrib['tests']
duration = test_suite.attrib['time']
timestamp = test_suite.attrib['timestamp']

# calculate passed tests
failed_tests = int(errors) + int(failures)
passed_tests = int(total_number_of_tests) - failed_tests


# double check those values match
all_test_cases = test_suite.findall('testcase')
assert len(all_test_cases) == int(total_number_of_tests), f"Total qty test case = {len(all_test_cases)}, 'total' attribute = {total_number_of_tests}"

# calculate start and end time
timestamp = parse(timestamp)
star_time = timestamp - timedelta(seconds=float(duration))
start_time_formatted = star_time.strftime("%Y-%m-%d %H:%M:%S")
end_time_formatted = timestamp.strftime("%Y-%m-%d %H:%M:%S")

# create payload and make the call
payload = {
    "startDateTime": start_time_formatted,
    "endDateTime": end_time_formatted,
    "numberOfTestCasesPassed": passed_tests,
    "numberOfTestCasesFailed": failed_tests,
    "testGroupName": name,
    "resultStatus": "FAIL" if int(failed_tests) > 0 else "PASS"

}
print(f"Calling: {endpoint}")
print(f"Payload: {payload}")
rs_api = requests.post(url=endpoint, data=json.dumps(payload), headers={"Content-Type": "application/json"})
print(rs_api.json())
assert rs_api.status_code == 200

