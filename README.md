# femail
Python package which supports sending mail through different kinds of API's


## pepipost

    from femail.pepipost import Client

    # initialize client
    c = Client(api_key, "codewarsnl@pepisandbox.com", "codewarsnl")

    # Send mail
    c.send_mail(to=["codewars.nl@gmail.com"], subject="test", body="Hello this is a test from a python library made by https://codewars.nl")

    # Render jinja template and send mail
    c.send_html_mail(to=["codewars.nl@gmail.com"], subject="test jinja", jinja_template_absolute_path="D:\\Private\\femail\\test.html", what="world!")