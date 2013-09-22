# - * - encoding: utf-8 - * -

from web.helpers import name_gen, password_gen, register_reddit, get_captcha


if __name__ == "__main__":
    print ("\nHello, in order to register a random account please"
           "solve this captcha\n")

    iden = get_captcha()
    print "http://www.reddit.com/captcha/%s" % iden
    captcha = raw_input("Captcha: ")

    name = name_gen()
    passwd = password_gen()

    print "\nSending request to reddit"
    response = register_reddit(username=name, passwd=passwd,
                               iden=iden, captcha=captcha)

    if len(response) > 0:
        print "\nOups there were some errors"

        for e in response:
            print "\t%s - %s" % (e[0], e[1])
            if e[0].startswith("BAD_USE"):
                print "\t\tUsername: %s" % name
    else:
        print """
        Successful registration!
            Username: %s
            Password: %s
        """ % (name, passwd)
