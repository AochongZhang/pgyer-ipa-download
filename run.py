import requests
import re
import html
import urllib.parse
import sys

html_url = ''
if len(sys.argv) >= 2:
    html_url = sys.argv[1]
if len(html_url) == 0:
    html_url = input('>_ Please input pgyer url\n')
if len(html_url) == 0:
    exit()

html_text = requests.get(html_url).text
key = re.findall(r'aKeyForAdSense = \'(\S+)\'', html_text).pop()
url = f'https://www.pgyer.com/app/plist/{key}/install//s.plist'
plist = requests.get(url, headers={
    'User-Agent': 'com.apple.appstored/1.0 iOS/16.3 model/iPhone14,4 hwp/t8110 build/20D47 (6; dt:252) AMS/1'}).text
ipa_url = urllib.parse.unquote(html.unescape(re.findall(r'<string>(\S+).ipa</string>', plist).pop()))
filename = re.findall(r'filename=(\S+)', ipa_url).pop() + '.ipa'
print(f'Download {filename} ...')
open(filename, 'wb').write(requests.get(ipa_url).content)
print('finish!')
