import streamlit as st
from openpyxl import load_workbook
import pandas as pd
st.set_page_config(page_title="Area 51 فقيسة ", layout= "wide")
st.markdown("<h5 style='text-align: left; color: rgb(0 151 240 / 38%);'>This Website is Made by the man the myth the legend Hanna John Alkhoury</h5>" , unsafe_allow_html=True)
scitable=load_workbook('table.xlsx')
activescitable=scitable.active
counter=1
Flist=[]
for loop in range(14):
    row=activescitable[str(counter)]
    counter=counter+1
    l=[]
    for item in row:
        value=item.value
        l.append(value)
    Flist.append(l)
def bubbleSort(arr):
    for i in range(13):
        swapped = False
        for j in range(0, 13-i):
            one=arr[j]
            two=arr[j + 1]
            if int(one[1]) > int(two[1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
bubbleSort(Flist)
st.markdown("<h1 style='text-align: right; color: #00B0F0;'>  ترتيب الفقيسين من الأفقس إلى الأقل فقساً </h1>" , unsafe_allow_html=True)
st.write("###")
counter=1
for bro in Flist:
    st.markdown("<h3 style='text-align: right; color: #000000;'>"+ " elo:" + str(bro[1]) + "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎"+ bro[0] +"‎ ‎ ("+str(counter) +"</h3>" , unsafe_allow_html=True)
    counter=counter+1
with st.form(key="1"):
    code=st.text_input("Password",type='password')
    h=st.form_submit_button("UPDATE THE LIST", type='primary')
if code=='Noteverymanis0:)':
    with st.form(key="2"):
        beeb=st.multiselect("الروحة",options=["حنا","أوبي","سيف","أيهم","مجد","فواز","زين","بشار","طارق","أحمد","أديب","قصي","فؤاد","يامن"])
        button=st.form_submit_button("UPDATE THE LIST", type='primary')
        if button==True:
            came=[]
            fqs=[]
            for goo in Flist:
                state=False
                for go in beeb:
                    if go == goo[0]:
                        came.append(goo)
                        state=True
                if state==False:
                    fqs.append(goo)
            afterlist=[]
            for sigma in came:
                for beta in fqs:
                    factor= int(sigma[1]) - int(beta[1])
                    power=factor/400
                    down=1+10**power
                    Ea=32/down
                    sigma[1]=int(sigma[1]) + int(Ea)
                    beta[1]=int(beta[1]) - int(Ea)
                afterlist.append(sigma)  
            for bad in fqs:
                afterlist.append(bad)
            pd.DataFrame(afterlist).to_excel('table.xlsx', header=False, index=False) 
elif code=="Obaiisurdaddy5":
    st.markdown("<h5 style='text-align: right; color: #00B0F0;'>Wrong Password+ you got trolled</h5>" , unsafe_allow_html=True)
else:
   st.markdown("<h5 style='text-align: left; color: #00B0F0;'>Wrong Password </h5>" , unsafe_allow_html=True) 
