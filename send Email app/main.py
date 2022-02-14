import smtplib

sms=smtplib.SMTP("smtp.gmail.com",25)
try:
    m="this is tst"
    sms.sendmail("solllsara@gmail.com","solllsara@gmail.com",m)
    print("Sented")
except Exception as e:
    print("uh-oh",e)

sms.quit()