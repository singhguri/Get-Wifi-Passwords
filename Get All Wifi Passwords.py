import os

f = open("abc.txt", "w")
f.write(os.popen("netsh wlan show profiles").read())
f.close()
f = open('abc.txt', 'r')
rawContent = f.readlines()

profileList = []

for content in rawContent:
    if (content.strip().startswith('All')):
        profileList.append(content.split(':')[1].strip().replace('\n', ''))

f.close()

for profile in profileList:
    fw = open(profile + ".txt", "w")
    fw.write(os.popen('netsh wlan show profile name = "' +
                      profile + '" key = clear').read())
    fw.close()

    fr = open(profile + '.txt', "r")
    rawContent = fr.readlines()
    fr.close()

    fw = open(profile + ".txt", "w")
    for content in rawContent:
        if (content.strip().startswith('Key')):
            fw.write("Password:" + content.strip().split(':')[1])

    fw.close()

os.remove('abc.txt')
