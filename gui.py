from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="poonamsharma",
  database="mydatabase"
)
mycursor = mydb.cursor()


window=Tk()
window.title("Booking System")
window.configure(background="light green")
lbl=Label(window,text="Welcome...!",font=("Arial Bold", 10))
lbl.grid(column=3,row=0)



lbl_f=Label(window,text="From",font=("Arial Bold", 10))
lbl_f.grid(column=0,row=1)
txt_f=Combobox(window)
txt_f['values']=("Mumbai","Chennai","Delhi","Banglore")
txt_f.grid(column=1, row=1)
txt_f.focus()

lbl_t=Label(window,text="To",font=("Arial Bold", 10))
lbl_t.grid(column=2,row=1)
txt_t = Combobox(window)
txt_t['values']=("Mumbai","Chennai","Delhi","Banglore")
txt_t.grid(column=3, row=1)
txt_t.focus()


lbl_fn=Label(window,text="First Name",font=("Arial Bold", 10))
lbl_fn.grid(column=1,row=2)
txt_fn=Entry(window,width=10)
txt_fn.grid(column=2,row=2)


lbl_ln=Label(window,text="Last Name",font=("Arial Bold", 10))
lbl_ln.grid(column=3,row=2)
txt_ln=Entry(window,width=10)
txt_ln.grid(column=4,row=2)


lbl_ag=Label(window,text="Age",font=("Arial Bold", 10))
lbl_ag.grid(column=1,row=3)
txt_ag=Entry(window,width=10)
txt_ag.grid(column=2,row=3)


lbl_g=Label(window,text="Gender",font=("Arial Bold", 10))
lbl_g.grid(column=3,row=3)
txt_g = Combobox(window)
txt_g['values']=("Male","Female")
txt_g.grid(column=4, row=3)
txt_g.focus()


lbl_pn=Label(window,text="Phone number",font=("Arial Bold", 10))
lbl_pn.grid(column=1,row=4)
txt_pn=Entry(window,width=10)
txt_pn.grid(column=2,row=4)


lbl_s=Label(window,text="Slots",font=("Arial Bold", 10))
lbl_s.grid(column=3,row=4)
txt_s = Combobox(window)
txt_s['values']=("Morning","Evening")
txt_s.grid(column=4, row=4)
txt_s.focus()


global seat
seat=40
def clicked_b():
    global seat
    seat=seat-1
    
    f=""
    def check_fbox(event):
        global f
        if txt_f.get() == 'Mumbai':
            f = txt_f.get() # this will assign the variable c the value of cbox
        if txt_f.get() == 'Chennai':
            f = txt_f.get()
        if txt_f.get() == 'Delhi':
            f = txt_f.get()
        if txt_f.get() == 'Banglore':
            f = txt_f.get()
    txt_f.bind("<<ComboboxSelected>>", check_fbox)

    t=""
    def check_tbox(event):
        global t
        if txt_t.get() == 'Mumbai':
            t = txt_t.get() # this will assign the variable c the value of cbox
        if txt_t.get() == 'Chennai':
            t = txt_t.get()
        if txt_t.get() == 'Delhi':
            t = txt_t.get()
        if txt_t.get() == 'Banglore':
            t = txt_t.get()
    txt_t.bind("<<ComboboxSelected>>", check_tbox)

    if txt_f.get()==txt_t.get():
        messagebox.showerror("Error","Same cities selected")
    
    else:
        r=""
        def check_rbox(event):
            global r
            if txt_g.get() == 'Male':
                r = txt_g.get() # this will assign the variable c the value of cbox
            if txt_g.get() == 'Female':
                r = txt_g.get()
        txt_g.bind("<<ComboboxSelected>>", check_rbox)

        s=""
        def check_sbox(event):
            global s
            if txt_s.get() == 'Morning':
                s = txt_s.get() # this will assign the variable c the value of cbox
            if txt_s.get() == 'Evening':
                s = txt_s.get()
        txt_s.bind("<<ComboboxSelected>>", check_sbox)
    
        a=txt_fn.get()
        b=txt_ln.get()
        c=txt_ag.get()
        d=txt_pn.get()
        f=txt_f.get()
        t=txt_t.get()
        r=txt_g.get()
        s=txt_s.get()
        p=random.randrange(100,900,1)
        sql_insert_query = """ INSERT INTO `pass_detail`
                       (`pnr`, `fname`, `lname`, `age`, `gender`, `phone_no`, `bpoint`, `dpoint`, `slot`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        insert_tuple = (p,a,b,c,r,d,f,t,s)
        result  = mycursor.execute(sql_insert_query,insert_tuple)
        mydb.commit()

        
        global rt
        mycursor.execute("""SELECT * FROM pass_detail WHERE phone_no = '%s'""" % (d))
        myresult1=mycursor.fetchall()
        for x in myresult1:
            rt=x[0]
        global z
        global tv
        mycursor.execute("""SELECT * FROM transport WHERE initial_city = '%s' AND final_city = '%s'""" % (f, t))
        myresult2=mycursor.fetchall()
        for y in myresult2:
            tv=y[4]
            z=y[5]

        mycursor.execute ("""UPDATE transport SET avail='%s' WHERE initial_city='%s' AND final_city='%s'""" % (seat,f,t))
        mydb.commit()

        rt=str(rt)
        tvs=str(tv)
        str1="PNR:"
        str4="Bus no:"
        str6="Ticket booked....!"
        strf=str1 + "\t" + rt + "\n" + str4 + "\t" + tvs + "\n" + str6
        messagebox.showinfo("Ticket details" , strf)

        
def toplevel():
    top = Toplevel()
    top.title('Ticket details')
    top.wm_geometry("400x400")

    def viewre():
        a=txt_fn.get()
        b=txt_ln.get()
        c=txt_ag.get()
        d=txt_pn.get()
        f=txt_f.get()
        t=txt_t.get()
        r=txt_g.get()
        s=txt_s.get()
        lbl=Label(top, text="PNR: ")
        lbl.grid(column=1,row=2)
        lbl=Label(top, text=rt)
        lbl.grid(column=2,row=2)
        lbl=Label(top, text="Boarding point: ")
        lbl.grid(column=0,row=3)
        lbl=Label(top, text=f)
        lbl.grid(column=1,row=3)
        lbl=Label(top, text="Destination: ")
        lbl.grid(column=2,row=3)
        lbl=Label(top, text=t)
        lbl.grid(column=3,row=3)
        lbl=Label(top, text="Name: ")
        lbl.grid(column=0,row=4)
        lbl=Label(top, text=a)
        lbl.grid(column=1,row=4)
        lbl=Label(top, text="Age: ")
        lbl.grid(column=2,row=4)
        lbl=Label(top, text=c)
        lbl.grid(column=3,row=4)
        lbl=Label(top, text="Gender: ")
        lbl.grid(column=0,row=5)
        lbl=Label(top, text=r)
        lbl.grid(column=1,row=5)
        lbl=Label(top, text="Slot: ")
        lbl.grid(column=2,row=5)
        lbl=Label(top, text=s)
        lbl.grid(column=3,row=5)
        lbl=Label(top, text="Bus no:")
        lbl.grid(column=0,row=6)
        lbl=Label(top, text=tv)
        lbl.grid(column=1,row=6)
        lbl=Label(top, text="Driver name:")
        lbl.grid(column=2,row=6)
        lbl=Label(top, text=z)
        lbl.grid(column=3,row=6)

    def viewpnr():
        topv = Toplevel()
        topv.title('PNR view')
        topv.wm_geometry("400x400")
        lbl=Label(topv, text="PNR: ")
        lbl.grid(column=1,row=0)
        txt_u=Entry(topv,width=10)
        txt_u.grid(column=2,row=0)
        def view():
            topq = Toplevel()
            topq.title('PNR view')
            topq.wm_geometry("400x400")
            pnrv=txt_u.get()
            mycursor.execute("""SELECT * FROM pass_detail WHERE pnr='%s'""" % (pnrv))
            myresult=mycursor.fetchall()
            for j in myresult:
                a=j[1]
                c=j[4]
                f=j[6]
                t=j[7]
                r=j[3]
                s=j[8]
            mycursor.execute("""SELECT * FROM transport WHERE initial_city='%s' AND final_city='%s'""" % (f,t))
            myresult=mycursor.fetchall()
            for j in myresult:
                tv=j[4]
                z=j[5]
            lbl=Label(topq, text="PNR: ")
            lbl.grid(column=1,row=0)
            lbl=Label(topq, text=pnrv)
            lbl.grid(column=2,row=0)
            lbl=Label(topq, text="Boarding point: ")
            lbl.grid(column=0,row=1)
            lbl=Label(topq, text=f)
            lbl.grid(column=1,row=1)
            lbl=Label(topq, text="Destination: ")
            lbl.grid(column=2,row=1)
            lbl=Label(topq, text=t)
            lbl.grid(column=3,row=1)
            lbl=Label(topq, text="Name: ")
            lbl.grid(column=0,row=2)
            lbl=Label(topq, text=a)
            lbl.grid(column=1,row=2)
            lbl=Label(topq, text="Age: ")
            lbl.grid(column=2,row=2)
            lbl=Label(topq, text=c)
            lbl.grid(column=3,row=2)
            lbl=Label(topq, text="Gender: ")
            lbl.grid(column=0,row=3)
            lbl=Label(topq, text=r)
            lbl.grid(column=1,row=3)
            lbl=Label(topq, text="Slot: ")
            lbl.grid(column=2,row=3)
            lbl=Label(topq, text=s)
            lbl.grid(column=3,row=3)
            lbl=Label(topq, text="Bus no:")
            lbl.grid(column=0,row=4)
            lbl=Label(topq, text=tv)
            lbl.grid(column=1,row=4)
            lbl=Label(topq, text="Driver name:")
            lbl.grid(column=2,row=4)
            lbl=Label(topq, text=z)
            lbl.grid(column=3,row=4)

        btn=Button(topv,text='View Ticket using PNR',command=view)
        btn.grid(column=1,row=1)
    
    btn=Button(top,text='View Ticket using PNR',command=viewpnr)
    btn.grid(column=0,row=1)

    btn=Button(top,text='View recent ticket',command=viewre)
    btn.grid(column=1,row=1)

    
def toplevel_1():
    top_1=Toplevel()
    top_1.title('Update')
    lbl=Label(top_1, text="PNR: ")
    lbl.grid(column=1,row=0)
    txt_u=Entry(top_1,width=10)
    txt_u.grid(column=2,row=0)
    lbl=Label(top_1, text="Phone no: ")
    lbl.grid(column=3,row=0)
    txt_ph=Entry(top_1,width=10)
    txt_ph.grid(column=4,row=0)
    def update_p():
        phnu=txt_ph.get()
        pnru=txt_u.get()
        mycursor.execute ("""UPDATE pass_detail SET phone_no='%s' WHERE pnr='%s'""" % (phnu,pnru))
        mydb.commit()

    btn=Button(top_1,text='Update',command=update_p)
    btn.grid(column=4,row=1)

def toplevel_2():
    global seat
    seat=seat+1
    top_2=Toplevel()
    top_2.title('Cancel')
    top_2.geometry("300x100")
    lbl=Label(top_2, text="PNR: ")
    lbl.grid(column=4,row=0)
    txt_u=Entry(top_2,width=10)
    txt_u.grid(column=5,row=0)
    
    
    def delete():
        pnru=txt_u.get()
        mycursor.execute("""SELECT * FROM pass_detail WHERE pnr = '%s'""" % (pnru))
        myresult1=mycursor.fetchall()
        for x in myresult1:
            bp=x[6]
            dp=x[7]
        mycursor.execute ("""UPDATE transport SET avail='%s' WHERE initial_city = '%s' AND final_city = '%s'""" % (seat,bp,dp))
        mydb.commit()
        mycursor.execute("""DELETE FROM pass_detail WHERE pnr='%s'""" % (pnru))
        mydb.commit()
        messagebox.showinfo("Cancellation","Ticket cancelled...!")

    btn=Button(top_2,text='Cancel Ticket',command=delete)
    btn.grid(column=5,row=1)

def check():
    fa=txt_f.get()
    ta=txt_t.get()
    mycursor.execute("""SELECT * FROM transport WHERE initial_city='%s' AND final_city='%s'""" % (fa,ta))
    result=mycursor.fetchall()
    for z in result:
        av=z[3]
    str1="Available seats:"
    str2=str(av)
    strf=str1 + "\t" + str2
    messagebox.showinfo("Availability" , strf)    

btn=Button(window,text='View Ticket',command=toplevel)
btn.grid(column=1,row=6)

btn=Button(window,text='Book',command=clicked_b)
btn.grid(column=3,row=5)

btn=Button(window, text="Update",command=toplevel_1)
btn.grid(column=3,row=6)

btn=Button(window, text="Cancel Ticket",command=toplevel_2)
btn.grid(column=5,row=6)

btn=Button(window, text="Check Seats",command=check)
btn.grid(column=5,row=1)
window.mainloop()
