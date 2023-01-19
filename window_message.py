import smtplib

sender_email = "example@gmail.com"
receiver_email = "example2@gmail.com"
password = "take from gmail" #create app passwd from gmail not real passwd
message = "kisi ne window chalu kri h check kr."

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()
