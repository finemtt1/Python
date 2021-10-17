import email.message
msg=email.message.EmailMessage()
msg["From"]="寄件人地址"
msg["To"]="收件人地址"
msg["Subject"]="電子郵件主題"
# 加入HTML內容
msg.add_alternative("<h3>HTML內容</h3>",subtype="html")

import smtplib
#從網路找到主機名稱和連接埠號
server=smtplib.SMTP_SSL("主機名稱,",連接埠號)
server.login("帳號","密碼")
#msg變數存放上一個步驟準備好的訊息物件
server.send_message(msg)
server.close()#發送完成後關閉連線