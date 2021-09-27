import smtplib, os, pickle  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase    # 파일을 전송할 때 사용되는 모듈
from openpyxl import Workbook
from openpyxl import load_workbook
import datetime

class mail():
    def __init__(self):
        self.toAddr=["soo_cheol@seoreu.com"]
        pickle_file = os.path.join(os.pardir,"mail.pickle")
        ## Load pickle
        with open(pickle_file,"rb") as fr:
            data = pickle.load(fr)
        self.email = data["email"]
        self.pw = data["pw"]

    def send_mail(self,name,start_day,end_day):
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
        msg = MIMEMultipart()
        if start_day == end_day:
            msg['Subject'] = f"연차신청서_{start_day}_{name}"
        elif start_day != end_day:
            msg['Subject'] = f"연차신청서_{start_day},{end_day[-1]}_{name}"
        msg['From'] = "seoreu@seoreu.com"
        msg['to'] = "soo_cheol@seoreu.com"
        msg['Cc'] = "choi_th@seoreu.com"
        msg.preamble="?"
        file = f"{os.path.join(os.pardir,'연차신청서.xlsx')}"

        part = MIMEBase("application","octet-stream")
        part.set_payload(open(file,"rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment',filename="연차신청서.xlsx")
        msg.attach(part)
        smtp.sendmail(self.email,"soo_cheol@seoreu.com",msg.as_string())
        smtp.quit()

    def make_report(self,in_name,part,position,start_day,end_day,start_time,end_time,in_kind,annual_txt,number):
        load_wb = load_workbook(os.path.join(os.pardir,"연차신청서.xlsx"), data_only=True)
        load_ws = load_wb['근태계']
        load_ws["H5"] = in_name
        load_ws["B10"] = part
        load_ws["B11"] = position
        load_ws["B12"] = in_name
        load_ws["B13"] = f"{start_day}~{end_day}"
        load_ws["B14"] = f"{start_time}~{end_time}"
        load_ws["G12"] = number
        if in_kind == "연차":
            load_ws["E15"]="O"
        elif in_kind == "반차":
            load_ws["E16"]="O"
        elif in_kind == "경조휴가":
            load_ws["I15"]="O"
        elif in_kind == "병가":
            load_ws["I16"]="O"
        elif in_kind == "조퇴":
            pass
        load_ws["B18"] = annual_txt
        today = datetime.datetime.now()
        load_ws["A24"] = f"{today.year}년 {today.month}월 {today.day}일"
        load_wb.save(os.path.join(os.pardir,"연차신청서.xlsx"))
        
# if __name__=="__main__":
#     mail = mail()
#     #mail.email_login()
#     mail.make_report()