from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''

# Create your views here.

def adminloginaction(request):
    global fn,ln,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="root123",database='isp')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from admin where emailid='{}' and pass='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t ==():
            return render(request,'error.html')
        else:
            return render(request,'AdminDash.html')
        
        
    return render(request,'adminlogin_page.html')
        