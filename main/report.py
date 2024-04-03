#CYBER NAME BLACK-KILLER
#INSTAGRAM : https://www.instagram.com/me_rt7598
#CYBER NAME BLACK-KILLER
# coding=utf-8
#!/usr/bin/env python3

__author__ = "@merto1603"
__license__ = "GPLv3"
__version__ = "0.2"
__status__ = "being developed"

from time import time, sleep
from random import choice
from multiprocessing import Process

from libs.utils import CheckPublicIP, IsProxyWorking
from libs.utils import PrintStatus, PrintSuccess, PrintError
from libs.utils import PrintBanner, GetInput, PrintFatalError
from libs.utils import LoadUsers, LoadProxies, PrintChoices

from libs.instaclient import InstaClient

USERS = []
PROXIES = []

def MultiThread(username, userid, loginuser, loginpass, proxy, reasonid):
    client = None
    if (proxy != None):
        PrintStatus("[" + loginuser + "]", "Hesaba Giriş Yapılıyor!")
        client = InstaClient(
            loginuser,
            loginpass,
            proxy["ip"],
            proxy["port"]
        )
    else:
        PrintStatus("[" + loginuser + "]", "Hesaba Giriş Yapılıyor!")
        client = InstaClient(
            loginuser,
            loginpass,
            None,
            None
        )
        
    client.Connect()
    client.Login()
    client.Spam(userid, username, reasonid)
    print("")

def NoMultiThread():
    for user in USERS:
        client = None
        if (useproxy):
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Hesaba Giriş Yapılıyor!")
            client = InstaClient(
                user["user"],
                user["password"],
                proxy["ip"],
                proxy["port"]
            )
        else:
            proxy = choice(PROXIES)
            PrintStatus("[" + user["user"] + "]", "Hesaba Giriş Yapılıyor!")
            client = InstaClient(
                user["user"],
                user["password"],
                None,
                None
            )
        
        client.Connect()
        client.Login()
        client.Spam(userid, username, reasonid)
        print("")


if __name__ == "__main__":
    PrintBanner()
    PrintStatus("Kullanıcılar yükleniyor!")
    USERS = LoadUsers("./users.txt")
    PrintStatus("Proxyler Yükleniyor!")
    PROXIES = LoadProxies("./proxy.txt")
    print("")

    username = GetInput("şikayet etmek istediğiniz hesabın kullanıcı adını girin :")
    userid = GetInput("Şikayet etmek istediğiniz rapor numarası :")
    useproxy = GetInput("Proxy kullanmak ister misin? [evet / hayır]:")
    if (useproxy == "evet"):
        useproxy = True
    elif (useproxy == "hayır"):
        useproxy = False
    else:
        PrintFatalError("Lütfen sadece 'evet' veya 'hayır' yazınız!")
        exit(0)
    usemultithread = GetInput("Çoklu iş parçacığı kullanmak istiyor musunuz? [evet / hayır] (Çok fazla kullanıcınız varsa veya bilgisayarınız yavaşsa bu özelliği kullanmayın!):")
    
    if (usemultithread == "evet"):
        usemultithread = True
    elif (usemultithread == "hayır"):
        usemultithread = False
    else:
        PrintFatalError("Lütfen sadece 'evet' veya 'hayır' yazınız!")
        exit(0)
    
    PrintChoices()
    reasonid = GetInput("Lütfen yukarıdaki şikayetin nedenlerinden birini seçin (ör. spam için 1):")

    
    
    
    print("")
    PrintStatus("Başlıyor!")
    print("")

    if (usemultithread == False):
        NoMultiThread()
    else:
        for user in USERS:
            p = Process(target=MultiThread,
                args=(username,
                    userid,
                    user["user"],
                    user["password"],
                    None if useproxy == False else choice(PROXIES),
                    reasonid
                )
            )
            p.start() 
   

