import email.header
import imaplib, email
import requests
from bs4 import BeautifulSoup
from email import policy
from email.header import decode_header
import pytest
import pytest_dependency
from Common.TestBase import TestBase


id = 'TESTID'
pw = 'TESTPW'

with imaplib.IMAP4_SSL('imap.naver.com') as imap : 
    imap.login(id, pw)
    imap.select('INBOX')

    status, messages = imap.uid('search', None, 'ALL') #ALL 대신 '(FROM "somewhere@naver.com")' 같이 검색어 입력 가능
    all_email = messages[0].split() # 모든 이메일

    recent = all_email[-1:] # 마지막 메일


    for n, message in enumerate(messages) : #recent 를 all_email로 변경하면 모든 메일에 대해서 메읽 읽기 수행함
        print(f"Writing email on {n}")
        print('='*70)
        #'message' 번째의 메일을 fetch 함(가져옴)
        res, msg = imap.uid('fetch', message, "(RFC822)") #res : 메일 상태('OK'), msg : 읽어온 메일 full data 
        raw = msg[0][1] #메일 파싱 하기 전 상태의 메일 읽어옴
        # msg[0] = (b'12345 (UID 12345 RFC822 {3425}', b'raw_email_data_here') 이렇게 생겨서 [0][1] 을 읽어와야함
        email_message = email.message_from_bytes(raw) #raw 이메일을 파싱함

        subject, encoding = decode_header(email_message["Subject"])[0] 
        #decode_header 가 2개짜리 tuple을 return 함. 
        # 1번째 : decoded part. 이 경우 subject가 받음
        # 2번째 : endcoding 사용된 부분. endcoding이 받음
        if isinstance(subject, bytes): # subject가 여전히 파싱 되지 않았을 경우 파싱해줌
            subject = subject.decode(encoding if encoding else 'UTF-8')
        
        

        if email_message.is_multipart(): 
            # If it's multipart, we need to walk through each part
            for part in email_message.walk(): #walk() 메소드는 각 이메일이 multipart일 때 각각 파트에 대해서 진행함
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if "attachment" not in content_disposition:
                    # Decode the body
                    body = part.get_payload(decode=True) #get_payload() method retrieves the actual content of the email part

                    if body: 
                        body = body.decode(part.get_content_charset('UTF-8'))
                        
        else:
            # For non-multipart emails, just decode the payload directly
            body = email_message.get_payload(decode=True)

            if body:
                body = body.decode(email_message.get_content_charset('utf-8'))
                

        
        email_message['To'] #수신인
        email_message['From'] #발신인
        email_message['Subject'] #제목
        subject #제목
        body #이메일 내용. 안에 첨부파일, html, plain text 등의 multipart일 수도 있음.


    # 비밀번호 초기화 링크 같이 특정 링크를 가져오기
    soup = BeautifulSoup(body, 'html.parser')

    reset_links = soup.find_all('a', href=True)
    reset_link = None
    for a in reset_links : 
        pw_href = a.get('href')
        if "reset-password" in pw_href : #reset-password 가 href에 있을 경우 해당 주소를 반환함
            reset_link = pw_href.strip()
            break       

    if reset_link : #반환 받은 주소로 추후 테스트 시나리오에 따라 자동화 스크립트 작성에 활용 가능. ex : 비밀번호 초기화 하는 시나리오
        print(reset_link)
    else : 
        print("뭐임?")

    imap.logout()
