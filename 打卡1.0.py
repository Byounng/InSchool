import requests
import json

UA="Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2893 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/9969 MicroMessenger/8.0.11.1980(0x28000B3B) Process/appbrand1 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram"
report="start!!!"+"\n"

class da_ka:
    def __init__(self,name,PhoneNum,Passwd,JWE):
        self.name=name
        self.un=PhoneNum
        self.pwd=Passwd
        self.JWE=JWE
        self.fla=0
        self.GetJWsessionUrl="https://student.wozaixiaoyuan.com/basicinfo/mobile/login/username"
    def GetJwSession(self):  #get cookie(jwsession)
        self.header={"Host":"student.wozaixiaoyuan.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "User-Agent":UA,
            "Content-Length": "29",
        }
        self.AskBody="{}"
        self.LoginUrl=self.GetJWsessionUrl + "?username=" + self.un+ "&password=" + self.pwd
        JW_res=requests.post(url=self.LoginUrl,data=self.AskBody,headers=self.header)
        parseText=json.loads(JW_res.text)
        if parseText["code"]==0:
            self.JWE=JW_res.headers["JWSESSION"]
            self.state1=1
        else:
            self.state1=0
    def SendData(self):
        global report1
        self.SendUrl = "https://student.wozaixiaoyuan.com/heat/save.json"
        self.SendDataHeaders = {
            'Host': 'student.wozaixiaoyuan.com',
            'Connection': 'keep-alive',
            'Content-Length': '162',
            'JWSESSION': self.JWE,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
            'content-type': 'application/x-www-form-urlencoded',
            'Referer': 'https://servicewechat.com/wxce6d08f781975d91/180/page-frame.html',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        self.senddata = r"answers=%5B%220%22%2C%22%E6%97%A0%22%5D&seq=1&temperature=36.1&userId=&latitude=&longitude=&country=&city=&district=&province=&township=&street=&myArea=&areacode="
        DataRes=requests.post(url=self.SendUrl,data=self.senddata,headers=self.SendDataHeaders)
        self.DateText=DataRes.text
    def IfSuccess(self):
        global report
        if self.DateText[8]==0:
            report=report+"{name}".format(name=self.name)+"was success---/"
            self.report=report
        else:
            da_ka.GetJwSession(self)
            da_ka.SendData(self)
            print(self.DateText) ##测试输出用
            if self.DateText[8] !=0:
                report=report+"{name}".format(name=self.name)+"was failure***!"
                self.report = report
                print(self.DateText)

'''
注意：
目前以手机号+密码登录方式不稳定，且登录失败5次账号会被冻结24h 故建议自行抓包JWsession

'''
u1=["YANGYANG","你的手机号","密码","你的JWESSION"]

newUser=da_ka(u2[0],u2[1],u2[2],u2[3]) #new一个实例
newUser.SendData() #调用newuser的打卡 ，使用jwession
newUser.IfSuccess()#打卡失败尝试使用手机号+pwd方式进行获取jwession并更新jwession
print(report) #日志
