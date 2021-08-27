import smtplib, os, pickle  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase    # 파일을 전송할 때 사용되는 모듈

class mail():
    def __init__(self):
        toAddr=["soo_cheol@seoreu.com"]
        pickle_file = os.path.join(os.getcwd(),"mail.pickle")
        ## Load pickle
        with open(pickle_file,"rb") as fr:
            data = pickle.load(fr)
        self.email = data["email"]
        self.pw = data["pw"]

    def email_login(self):
        smtp = smtplib.SMTP('smtp.cafe24.com',587)   # 587: 서버의 포트번호
        #smtp.connect("www.webmail.seoreu.com",465)
        smtp.ehlo()
        smtp.starttls()   # tls방식으로 접속, 그 포트번호가 587
        smtp.ehlo()
        # smtp.login('hyeshinoh@gmail.com', pickle.load( open('../pw.pickle', 'rb') ))
        try:
            smtp.login(self.email, self.pw)
            print("login성공")
        except:
            print("loging실패")
if __name__=="__main__":
    mail = mail()
    mail.email_login()


# nslookup
# > set type=mx
# > webmail.seoreu.com
# Server:		210.220.163.82
# Address:	210.220.163.82#53