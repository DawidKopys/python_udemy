import time
from datetime import datetime as dt
hosts_path = r'c:\Windows\System32\drivers\etc\hosts'
hosts_temp = r'd:\python_workspace\web_blocker\hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'https://www.youtube.com/', 'youtube.com', 'http://joemonster.org/', 'joemonster.org']

while True:
    if 18 < dt.now().hour < 20:
        print('Working hours...')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Have fun!')
    time.sleep(5)


            # for line in content:
            #     written = False
            #     for website in website_list:
            #         if website in line:
            #             pass
            #         else:
            #             if written == False:
            #                 written = True
            #                 file.write(line)
