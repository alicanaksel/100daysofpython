import smtplib

my_email="pytestingcode@gmail.com"
app_password=""

with smtplib.SMTP("smtp.gmail.com",587) as connection:# for yahoo smtp.mail.yahoo.com # port 587
    connection.starttls()#transport layer security
    connection.login(user=my_email,password=app_password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="pytestingcode@yahoo.com",
        msg="Subject:Asking for a friend\n\n Hello, I'm just trying to automate email but it keeps going to unwanted.")
