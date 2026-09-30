import requests,time,datetime,threading
T="7956826718:AAG0Ldspgef4uO3os12byK3SF4j4Gdbi0lI"
C="554096902"
running=False
last_t=None
def send(txt):
 try:requests.post(f"https://api.telegram.org/bot{T}/sendMessage",data={"chat_id":C,"text":txt,"parse_mode":"HTML"},timeout=10)
 except:pass
def go():
 r=requests.get("https://query1.finance.yahoo.com/v8/finance/chart/GC=F",params={"interval":"15m","range":"1d"},headers={"User-Agent":"Mozilla/5.0"},timeout=15).json()
 d=r["chart"]["result"][0];q=d["indicators"]["quote"][0];o=[]
 for i in range(len(d["timestamp"])):
  a,h,l,c=q["open"][i],q["high"][i],q["low"][i],q["close"][i]
  if None not in(a,h,l,c):o.append({"t":d["timestamp"][i],"o":round(a,2),"h":round(h,2),"l":round(l,2),"c":round(c,2)})
 return o[-6:]
def chk():
 global last_t
 cs=go()
 if len(cs)<3:return
 c1,c2=cs[-2],cs[-3]
 if last_t==c1["t"]:return
 b1=abs(c1["c"]-c1["o"]);r1=c1["h"]-c1["l"];lw=min(c2["o"],c2["c"])-c2["l"];uw=c2["h"]-max(c2["o"],c2["c"]);r2=c2["h"]-c2["l"]
 bull=c1["c"]>c1["o"];bear=c1["c"]<c1["o"];p=dr=None
 if r2>0 and r1>0:
  if lw/r2>=0.4 and bull and b1/r1>=0.6 and c1["c"]>c2["h"]:p,dr="SFU","BUY"
  elif uw/r2>=0.4 and bear and b1/r1>=0.6 and c1["c"]<c2["l"]:p,dr="SFU","SELL"
  elif lw/r2>=0.4 and bull and b1/r1>=0.3 and c1["c"]<=c2["h"]:p,dr="AFU","BUY"
  elif uw/r2>=0.4 and bear and b1/r1>=0.3 and c1["c"]>=c2["l"]:p,dr="AFU","SELL"
 if p:
  e=c1["c"];ll=min(x["l"] for x in cs[-5:]);hh=max(x["h"] for x in cs[-5:])
  if dr=="BUY":sl=round(ll-0.5,2);tp=round(e+(e-sl)*2,2);ar="BUY";dn="BUQA"
  else:sl=round(hh+0.5,2);tp=round(e-(sl-e)*2,2);ar="SELL";dn="AYIQ"
  send(f"{'📈' if ar=='BUY' else '📉'} <b>FU SIGNAL XAU/USD</b>\nPattern:{p} {dn}\nKirish:{e}\nSL:{sl}\nTP:{tp}\nRR:1:2");last_t=c1["t"]
def loop():
 global running
 while running:
  try:chk()
  except:pass
  time.sleep(60)
def upd(off=None):
 try:return requests.get(f"https://api.telegram.org/bot{T}/getUpdates",params={"timeout":30,"offset":off},timeout=35).json().get("result",[])
 except:return[]
send("Bot tayyor! /start yuboring")
off=None;th=None
while True:
 for u in upd(off):
  off=u["update_id"]+1;msg=u.get("message",{});txt=msg.get("text","");cid=str(msg.get("chat",{}).get("id",""))
  if cid!=C:continue
  if txt=="/start":
   if not running:running=True;th=threading.Thread(target=loop,daemon=True);th.start();send("Bot ishga tushdi! /stop bilan toxtatish mumkin")
   else:send("Allaqachon ishlayapti!")
  elif txt=="/stop":running=False;send("Toxtatildi. /start bilan qayta ishlatish mumkin")
  elif txt=="/status":send("Ishlayapti" if running else "Toxtatilgan /start yuimport requests,time,datetime,threading
T="7956826718:AAG0Ldspgef4uO3os12byK3SF4j4Gdbi0lI"
C="554096902"
running=False
last_t=None
def send(txt):
 try:requests.post(f"https://api.telegram.org/bot{T}/sendMessage",data={"chat_id":C,"text":txt,"parse_mode":"HTML"},timeout=10)
 except:pass
def go():
 r=requests.get("https://query1.finance.yahoo.com/v8/finance/chart/GC=F",params={"interval":"15m","range":"1d"},headers={"User-Agent":"Mozilla/5.0"},timeout=15).json()
 d=r["chart"]["result"][0];q=d["indicators"]["quote"][0];o=[]
 for i in range(len(d["timestamp"])):
  a,h,l,c=q["open"][i],q["high"][i],q["low"][i],q["close"][i]
  if None not in(a,h,l,c):o.append({"t":d["timestamp"][i],"o":round(a,2),"h":round(h,2),"l":round(l,2),"c":round(c,2)})
 return o[-6:]
def chk():
 global last_t
 cs=go()
 if len(cs)<3:return
 c1,c2=cs[-2],cs[-3]
 if last_t==c1["t"]:return
 b1=abs(c1["c"]-c1["o"]);r1=c1["h"]-c1["l"];lw=min(c2["o"],c2["c"])-c2["l"];uw=c2["h"]-max(c2["o"],c2["c"]);r2=c2["h"]-c2["l"]
 bull=c1["c"]>c1["o"];bear=c1["c"]<c1["o"];p=dr=None
 if r2>0 and r1>0:
  if lw/r2>=0.4 and bull and b1/r1>=0.6 and c1["c"]>c2["h"]:p,dr="SFU","BUY"
  elif uw/r2>=0.4 and bear and b1/r1>=0.6 and c1["c"]<c2["l"]:p,dr="SFU","SELL"
  elif lw/r2>=0.4 and bull and b1/r1>=0.3 and c1["c"]<=c2["h"]:p,dr="AFU","BUY"
  elif uw/r2>=0.4 and bear and b1/r1>=0.3 and c1["c"]>=c2["l"]:p,dr="AFU","SELL"
 if p:
  e=c1["c"];ll=min(x["l"] for x in cs[-5:]);hh=max(x["h"] for x in cs[-5:])
  if dr=="BUY":sl=round(ll-0.5,2);tp=round(e+(e-sl)*2,2);ar="BUY";dn="BUQA"
  else:sl=round(hh+0.5,2);tp=round(e-(sl-e)*2,2);ar="SELL";dn="AYIQ"
  send(f"{'📈' if ar=='BUY' else '📉'} <b>FU SIGNAL XAU/USD</b>\nPattern:{p} {dn}\nKirish:{e}\nSL:{sl}\nTP:{tp}\nRR:1:2");last_t=c1["t"]
def loop():
 global running
 while running:
  try:chk()
  except:pass
  time.sleep(60)
def upd(off=None):
 try:return requests.get(f"https://api.telegram.org/bot{T}/getUpdates",params={"timeout":30,"offset":off},timeout=35).json().get("result",[])
 except:return[]
send("Bot tayyor! /start yuboring")
off=None;th=None
while True:
 for u in upd(off):
  off=u["update_id"]+1;msg=u.get("message",{});txt=msg.get("text","");cid=str(msg.get("chat",{}).get("id",""))
  if cid!=C:continue
  if txt=="/start":
   if not running:running=True;th=threading.Thread(target=loop,daemon=True);th.start();send("Bot ishga tushdi! /stop bilan toxtatish mumkin")
   else:send("Allaqachon ishlayapti!")
  elif txt=="/stop":running=False;send("Toxtatildi. /start bilan qayta ishlatish mumkin")
  elif txt=="/status":send("Ishlayapti" if running else "Toxtatilgan /start yuboring")
  boring")

