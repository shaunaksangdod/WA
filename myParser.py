import re
import pandas as pd

date,time,text,sender = [],[],[],[]

for f in open('_chat.txt').readlines():

    '''Get Date'''
    #re_date = '((?:[0]?[1-9]|[1][012])[-:\\/.](?:(?:[0-2]?\\d{1})|(?:[3][01]{1}))[-:\\/.](?:(?:\\d{1}\\d{1})))(?![\\d])'  # MMDDYY
    re_date = '^(\[[0-9]*/[0-3][0-9]/[0-9][0-9])'
    rg_date = re.compile(re_date, re.IGNORECASE | re.DOTALL)
    m_date = rg_date.search(f)
    if m_date:
        date.append(m_date.group(1).split('[')[1])
        #print "(" + date + ")" + "\n"

    '''Get Time'''
    re_time ='('+re_date+', (?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?)'	# HourMinuteSec
    rg_time = re.compile(re_time, re.IGNORECASE | re.DOTALL)
    m_time = rg_time.search(f)
    if m_time:
        time.append(m_time.group(1).split(', ')[1])
        #print "(" + time + ")" + "\n"
    '''Get Sender'''
    if m_time:
        #re_sender = '((?:[a-z][a-z]+:))'
        re_sender = '('+re_time+'] (?:.*:))'
        rg_sender = re.compile(re_sender, re.IGNORECASE | re.DOTALL)
        m_sender = rg_sender.search(f)
        if m_sender:
            sender.append(m_sender.group(1).split('] ')[1].split(':')[0])
            #print "(" + sender + ")" + "\n"
    #print text
    '''Get Message'''
    re_msg = '((: .*))'
    rg_msg = re.compile(re_msg, re.IGNORECASE | re.DOTALL)
    m_msg = rg_msg.search(f)

    if m_msg:
        text.append(m_msg.group(1).split(': ')[1])

    re_msg_newline = '(^[a-z0-9].*)'
    rg_msg_newline = re.compile(re_msg_newline, re.IGNORECASE | re.DOTALL)
    m_msg_newline = rg_msg_newline.search(f)

    if m_msg_newline:
        text[-1] = text[-1].__add__(m_msg_newline.group(1))

df = pd.DataFrame(list(zip(date,time,sender,text)),columns=['date','time','sender','text'])
df.to_csv('a.csv')
