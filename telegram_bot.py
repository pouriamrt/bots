import json
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote#, unquote
import time
from os.path import basename

def aux_dec2utf8(resp):
    decoded = ''

    for line in resp:
        decoded += line.decode('utf-8')
    return decoded


token = ''
cmd = 'getme'

url = f'https://api.telegram.org/bot{token}/'

resp = urlopen(url + cmd)
line = aux_dec2utf8(resp) # resp.read().decode('utf-8')
gtm = json.loads(line)

i = 0

flag = True
try:
    while flag:
        cmd = 'getUpdates'
        
        resp = urlopen(url + cmd)
        line = aux_dec2utf8(resp)
        upds = json.loads(line)
        
        NoM = len(upds['result'])
        if NoM:
            msg = upds['result'][0]['message']
            chat_id = msg['chat']['id']
            
            if 'text' in msg:
                str_txt = msg['text']
                txt = quote(msg['text'].encode('utf-8'))
                
                if txt.lower() in [s.lower() for s in ['hi', 'hello', 'hey']]:
                    txt = quote((msg['text'] + ' Jigar').encode('utf-8'))
                
                cmd = 'sendMessage'
                
                resp = urlopen(url + cmd + f'?chat_id={chat_id}&text={txt}')
                line = aux_dec2utf8(resp)
                check = json.loads(line)
                
                if check['ok']:
                    uid = upds['result'][0]['update_id']
                    cmd = 'getUpdates'
                    urlopen(url + cmd + '?offset={}'.format(uid + 1))
                    print(str_txt, ' -> ', msg['from']['username'])
                    
            elif 'emoji' in msg:
                emoji = quote(msg['emoji'].encode('utf-8'))
                
                cmd = 'sendMessage'
                
                resp = urlopen(url + cmd + f'?chat_id={chat_id}&emoji={emoji}')
                line = aux_dec2utf8(resp)
                check = json.loads(line)
                
                if check['ok']:
                    uid = upds['result'][0]['update_id']
                    cmd = 'getUpdates'
                    urlopen(url + cmd + '?offset={}'.format(uid + 1))
                    print(str_txt, ' -> ', msg['from']['username'])
                    
            elif 'sticker' in msg:
                sticker = quote(msg['sticker']['file_id'].encode('utf-8'))
                
                cmd = 'sendSticker'
                
                resp = urlopen(url + cmd + f'?chat_id={chat_id}&sticker={sticker}')
                line = aux_dec2utf8(resp)
                check = json.loads(line)
                
                if check['ok']:
                    uid = upds['result'][0]['update_id']
                    cmd = 'getUpdates'
                    urlopen(url + cmd + '?offset={}'.format(uid + 1))
                    
            elif 'photo' in msg:
                photo = quote(msg['photo'][0]['file_id'].encode('utf-8'))
                
                cmd = 'sendPhoto'
                
                resp = urlopen(url + cmd + f'?chat_id={chat_id}&photo={photo}')
                line = aux_dec2utf8(resp)
                check = json.loads(line)
                
                if check['ok']:
                    cmd = 'getFile'
                    resp = urlopen(url + cmd + f'?file_id={photo}')
                    line = aux_dec2utf8(resp)
                    check0 = json.loads(line)
                    
                    file_path = quote(check0['result']['file_path'].encode('utf-8'))
                    img_url = f'https://api.telegram.org/file/bot{token}/{file_path}'
                    suffix = basename(file_path).split('.')[1]
                    urlretrieve(img_url, f'D:/img.{suffix}')
                    
                    uid = upds['result'][0]['update_id']
                    cmd = 'getUpdates'
                    urlopen(url + cmd + '?offset={}'.format(uid + 1))
                    
                    
            elif 'animation' in msg:
                animation = quote(msg['animation']['file_id'].encode('utf-8'))
                
                cmd = 'sendAnimation'
                
                resp = urlopen(url + cmd + f'?chat_id={chat_id}&animation={animation}')
                line = aux_dec2utf8(resp)
                check = json.loads(line)
                
                if check['ok']:
                    uid = upds['result'][0]['update_id']
                    cmd = 'getUpdates'
                    urlopen(url + cmd + '?offset={}'.format(uid + 1))
                
            else:
                uid = upds['result'][0]['update_id']
                cmd = 'getUpdates'
                urlopen(url + cmd + '?offset={}'.format(uid + 1))
                
        if i%7 == 0:
            print('waiting ...')
            
        time.sleep(1)
        i += 1

except KeyboardInterrupt:
    print('exit')
