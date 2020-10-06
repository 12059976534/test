import smtplib, ssl
import random
import string

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
# sender_email = "jekomontainugrah@gmail.com"
password = ""


# Create a secure SSL context


# Try to log in to server and send email

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str.upper()        


def log(subject,msg,sender_email):
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        message="subject: {}\n\n{}".format(subject,msg)
        # TODO: Send email here
        server.sendmail(sender_email, sender_email, message)
        print("berhasil")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    
