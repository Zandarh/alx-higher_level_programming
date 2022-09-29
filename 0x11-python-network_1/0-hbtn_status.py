#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urlib.request

    with urlib,request.urlopen('https://alx-intranet.hbtn.io/status') as result:
        content = result.read()
        print("Body response")
        print ("\t- typr: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
