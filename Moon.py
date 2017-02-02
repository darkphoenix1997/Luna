
# coding: utf-8

# In[ ]:

#https://www.openprocessing.org/sketch/58012
import webbrowser
  
n = int(raw_input("Cifra del año en el que se encuentra su fecha de la fase lunar:\n"))
while n<0:
  print "No puedo calcular fases lunar a.c.\n"
  n = int(raw_input("Cifra del año en el que se encuentra su fecha de la fase lunar:\n"))

m = int(raw_input("Mes en el que se encuentra su fecha de la fase lunar:"))
while m<0 or m>12:
  print "Verifique su mes por favor.\n"
  m = int(raw_input("Mes en el que se encuentra su fecha de la fase lunar:"))
  
  
w = int(raw_input("Dia en el que se encuentra su fecha de la fase lunar:"))
while m<0 or m>30:
  print "Verifique su dia por favor.\n"
  w = int(raw_input("Dia en el que se encuentra su fecha de la fase lunar:"))
  


def Aureo(n):
  while n > 0:
      x = n+1
      return x%19
      return Aureo(n)
print Aureo(n),"es su número aureo dado por el año",n #10
an=Aureo(n)

#2.Cálculo de la Epacta
def Epacta(n):
  while n > 0:
    a = Aureo(n)-1 #10-1 Aureo-1
    return a*11 #99 n*11
c = Epacta(n)%30 #9 Modulo


#condicion de los meses
                      #enero
ww= c+12+w            #febrero
e= c+1+w              #marzo
r= c+2+w              #abril
t= c+3+w              #mayo
y= c+4+w              #junio
u= c+5+w              #julio
i= c+6+w              #agosto
p= c+7+w              #septiembre
b= c+8+w              #octubre
cc=c+9+w              #noviembre
a= c+10+w             #diciembre

def recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an):

  if  m==11:
    print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera",cc-1 , "dias desde la ultima luna nueva.\n"
    if cc==0 or cc==29 or 0<cc<=7:
      print "La fase de la luna en esta fecha es Luna Nueva"
    elif cc>7 and cc<=14:
      print "La fase de la luna en esta fecha es Cuarto Creciente"
    elif cc>14 and cc<=21:
      print "La fase de la luna en esta fecha es Luna Llena"
    elif cc>21 and cc<29:
      print "La fase de la luna en esta fecha es Cuarto menguante"
    else:
      cc-=30
      recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)

  elif m==12:
    print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", a-1, "dias desde la ultima luna nueva.\n"
    if a==0 or a==29 or 0<a<=7:
      print "La fase de la luna en esta fecha es Luna Nueva"
    elif a>7 and a<=14:
      print "La fase de la luna en esta fecha es Cuarto Creciente"
    elif a>14 and a<=21:
      print "La fase de la luna en esta fecha es Luna Llena"
    elif a>21 and a<29:
      print "La fase de la luna en esta fecha es Cuarto menguante"
    else:
      print a
      a-=30
      recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)

  elif m==1:
      print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", an, "dias desde la ultima luna nueva.\n"
      if an==0 or an==29 or 0<an<=7:
        print "La fase de la luna en esta fecha es Luna Nueva"
      elif an>7 and an<=14:
        print "La fase de la luna en esta fecha es Cuarto Creciente"
      elif an>14 and an<=21:
        print "La fase de la luna en esta fecha es Luna Llena"
      elif an>21 and an<29:
        print "La fase de la luna en esta fecha es Cuarto menguante"
      else:
        an-=30
        recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)
  

  elif m==2:
      print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", ww-1, "dias desde la ultima luna nueva.\n"
      if ww==0 or ww==29 or 0<ww<=7:
        print "La fase de la luna en esta fecha es Luna Nueva"
      elif ww>7 and ww<=14:
        print "La fase de la luna en esta fecha es Cuarto Creciente"
      elif ww>14 and ww<=21:
        print "La fase de la luna en esta fecha es Luna Llena"
      elif ww>21 and ww<29:
        print "La fase de la luna en esta fecha es Cuarto menguante"
      else:
        ww-=30
        recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)
  

  elif m==3:
      print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", e-1, "dias desde la ultima luna nueva.\n"
      if e==0 or e==29 or 0<e<=7:
        print "La fase de la luna en esta fecha es Luna Nueva"
      elif e>7 and e<=14:
        print "La fase de la luna en esta fecha es Cuarto Creciente"
      elif e>14 and e<=21:
        print "La fase de la luna en esta fecha es Luna Llena"
      elif e>21 and e<29:
        print "La fase de la luna en esta fecha es Cuarto menguante"
      else:
        e-=30
        recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)
  

  elif m==4:
    print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", r-1, "dias desde la ultima luna nueva.\n"
    if r==0 or r==29 or 0<r<=7:
        print "La fase de la luna en esta fecha es Luna Nueva"
    elif r>7 and r<=14:
        print "La fase de la luna en esta fecha es Cuarto Creciente"
    elif r>14 and r<=21:
        print "La fase de la luna en esta fecha es Luna Llena"
    elif r>21 and r<29:
        print "La fase de la luna en esta fecha es Cuarto menguante"
    else:
      r-=30
      recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)
  
  elif m==5:
      print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", t-1, "dias desde la ultima luna nueva.\n"
      if t==0 or t==29 or 0<t<=7:
          print "La fase de la luna en esta fecha es Luna Nueva"
      elif t>7 and t<=14:
          print "La fase de la luna en esta fecha es Cuarto Creciente"
      elif t>14 and t<=21:
          print "La fase de la luna en esta fecha es Luna Llena"
      elif t>21 and t<29:
          print "La fase de la luna en esta fecha es Cuarto menguante"
      else:
        t-=30
        recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)
  

  elif m==6:
      print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", y-1, "dias desde la ultima luna nueva.\n"
      if y==0 or y==29 or 0<y<=7:
          print "La fase de la luna en esta fecha es Luna Nueva"
      elif y>7 and y<=14:
          print "La fase de la luna en esta fecha es Cuarto Creciente"
      elif y>14 and y<=21:
          print "La fase de la luna en esta fecha es Luna Llena"
      elif y>21 and y<29:
          print "La fase de la luna en esta fecha es Cuarto menguante"
      else:
          y-=30
          recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)
  

  elif m==7:
      print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", u-1, "dias desde la ultima luna nueva.\n"
      if u==0 or u==29 or 0<u<=7:
          print "La fase de la luna en esta fecha es Luna Nueva"
      elif u>7 and u<=14:
          print "La fase de la luna en esta fecha es Cuarto Creciente"
      elif u>14 and u<=21:
          print "La fase de la luna en esta fecha es Luna Llena"
      elif u>21 and u<29:
          print "La fase de la luna en esta fecha es Cuarto menguante"
      else:
          u-=30
          recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)
  
  
  elif m==8:
      print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", i-1, "dias desde la ultima luna nueva.\n"
      if i==0 or i==29 or 0<i<=7:
          print "La fase de la luna en esta fecha es Luna Nueva"
      elif i>7 and i<=14:
          print "La fase de la luna en esta fecha es Cuarto Creciente"
      elif i>14 and i<=21:
          print "La fase de la luna en esta fecha es Luna Llena"
      elif i>21 and i<29:
          print "La fase de la luna en esta fecha es Cuarto menguante"
      else:
        i-=30
        recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)
  

  elif m==9:
      print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", p-1, "dias desde la ultima luna nueva.\n"
    
      if p==0 or p==29 or 0<p<=7:
          print "La fase de la luna en esta fecha es Luna Nueva"
      elif p>7 and p<=14:
          print "La fase de la luna en esta fecha es Cuarto Creciente"
      elif p>14 and p<=21:
          print "La fase de la luna en esta fecha es Luna Llena"
      elif p>21 and p<29:
          print "La fase de la luna en esta fecha es Cuarto menguante"
      else:
          p-=30
          recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)
  

  elif m==10:
      print "La edad de la luna el dia", w, "del mes", m, "del",n ,"sera", b-1, "dias desde la ultima luna nueva.\n"
      if b==0 or b==29 or 0<b<=7:
          print "La fase de la luna en esta fecha es Luna Nueva"
      elif b>7 and b<=14:
          print "La fase de la luna en esta fecha es Cuarto Creciente"
      elif b>14 and b<=21:
          print "La fase de la luna en esta fecha es Luna Llena"
      elif b>21 and b<29:
          print "La fase de la luna en esta fecha es Cuarto menguante"
      else:
          m-=30
          recursion(ww,e,r,t,y,u,i,p,b,an,cc,a,m)
recursion(ww,e,r,t,y,u,i,p,b,cc,a,m,an)

def si(x):
  webbrowser.open_new_tab("http://giphy.com/gifs/l0ExaDiZMJW9W8xOw/tile")
def Si(x):
  webbrowser.open_new_tab("http://giphy.com/gifs/l0ExaDiZMJW9W8xOw/tile")
def SI(x):
  webbrowser.open_new_tab("http://giphy.com/gifs/l0ExaDiZMJW9W8xOw/tile")
  
  
def no(x):
  print "Aquí termina su programa."
  try:
    webbrowser.get("chrome").open_new("http://giphy.com/gifs/l0ExaDiZMJW9W8xOw/tile")
  except webbrowser.Error:
    print "No se ha encontrado Chrome."

l=(raw_input("¿Desea ver la animación de las fases enteras de la luna?.\n"))

if l==si or l==Si or SI:
  try:
    webbrowser.get("chrome").open_new("http://giphy.com/gifs/l0ExaDiZMJW9W8xOw/tile")
  except webbrowser.Error:
    print "No se ha encontrado Chrome."
#if raw_input("¿Desea calcular alguna otra fase?").lower()=="si":
#  pass
#else:
 # exit=True
#Luis Manuel Garcia Valdivia

