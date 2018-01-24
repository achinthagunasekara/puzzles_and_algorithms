""" Print employee hierachy """

import urllib  # pylint: disable=unused-import
import json  # pylint: disable=unused-import

def get_emp_details(emp_id):
    """
    Get employee details from the API
    Args:
        emp_id (string): Employee ID
    Return:
        Directory: Directory of employee details
    """
    #try:
    #    url == "http://www.linkedin.corp/api//employee/%s" % emp_id
    #    resonse = urllib.urlopen(url)
    #    data = json.loads(response.read())
    #    return data
    #except Exception ex:
    #    print "something went wrong - %s" % ex.message

    # just return test data for testing
    if emp_id == 'A123456791':
        return {
            "name": "Flynn Mackie",
            "title": "Senior VP of Engineering",
            "reports": ["A123456793", "A1234567898"]
        }
    elif emp_id == 'A123456793':
        return {
            "name": "Bruce Wayne",
            "title": "SRE",
            "reports": []
        }
    elif emp_id == 'A1234567898':
        return {
            "name": "Peter Parker",
            "title": "Tester",
            "reports": []
        }
    else:
        return None


def get_emp_hierarchy(emp_id, print_spaces=0):
    """
    Print the employee details and get direct reports
    Args:
        emp_id (string): Employee ID
        print_spaces (int): Number of spaces to print before details
    Returns:
        None
    """
    emp_details = get_emp_details(emp_id=emp_id)

    if not emp_id:
        return None

    spaces = ''

    for each_space in xrange(print_spaces):  # pylint: disable=unused-variable
        spaces = "%s%s" % (spaces, ' ')

    print "%s%s - %s" % (spaces, emp_details['name'], emp_details['title'])

    for report in emp_details['reports']:
        get_emp_hierarchy(emp_id=report, print_spaces=(print_spaces + 2))


get_emp_hierarchy(emp_id='A123456791')
