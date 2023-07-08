from email.message import EmailMessage
from ps import password
from ps import sender
import ssl
import smtplib

e_sender=sender
e_password=password

e_receiver='bseevlo597@wemail.pics'

subject=" Interested in Joining your Research "
body="""
Respected sir,

      I hope this email finds you well. I am  Krishitha Dara , a second-year undergraduate at IIT KHARAGPUR, enrolled in the BS course of Mathematics and Computing, department of mathematics.        
      In order to learn more about Monte-Carlo Bayesian Reinforcement Learning and how it relates to cybersecurity,I wanted to participate in your research.Also interested in how stochastic processes might be used in the area of cyber security.
                        
         I truly hope you will give me this opportunity .You can count on me to  actively participate in the project and to be open to learning .

Best regards,
Krishtiha Dara.
21MA10019. 

"""

em=EmailMessage()
em['From']= e_sender
em['To']=e_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context ) as smtp:
    smtp.login(e_sender,e_password)
    smtp.sendmail(e_sender,e_receiver,em.as_string())
