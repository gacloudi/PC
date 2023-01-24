from matplotlib.pyplot import step
from numpy import append
import pandas as pd
import math as m
#from regex import P
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(page_title="Personal Finance", page_icon="chart_with_upwards_trend", layout="centered")
with st.sidebar:
    selected = option_menu("Menu",["EMI","PPF","FD","EPF"],
        icons=['house','file','calculator','calculator-fill'], menu_icon="cast", default_index=0)
if selected=='EMI':
  st.subheader("blue:[EMI Calculator]")
  st.write("-----------------------")
  df=pd.DataFrame(columns=['Month','Interest','Principal','Loan_Remaining'])
  df11=pd.DataFrame(columns=['Month','Interest','Principal','Loan_Remaining'])
  def main():
    c1,c2,c3=st.columns(3)
    with c1:
      Loan = st.number_input('Enter Loan Amount', value=100000)
    #st.write("Loan amount:", Years)
    with c2:
      Years=st.number_input('Enter Tenure Period in Years', value=10)
    with c3:
      Rate=st.number_input('Enter Rate of Interest', 0.0,15.0,6.0,step=0.05)
    st.write("-----------------------")
    #Loan=Loan*100000
    PR=Rate/1200
    o=pow((1 + PR), Years*12)/(pow((1 + PR), Years*12)-1)
    EMI=o*Loan*PR
    Total_Interest=EMI * Years * 12 - Loan
    st.write("Monthly EMI:",m.ceil(EMI))
    st.write("-----------------------")
    st.subheader("Monthly Split")
    result=[]
    L2=Loan
    for i in range(1,Years*12+1):
      u=i
      In=m.ceil(L2 * PR)
      p=m.ceil(EMI-In)
      L2=L2-p
      result.append([u,In,p,L2])
    df1=df.append(pd.DataFrame(result,columns=df.columns)).reset_index(drop=True)
    st.dataframe(df1)
    return(Total_Interest,EMI,Loan,Years,Rate,df1)

  def fn(EMI,Years,Loan,Rate,Rem,Rate1,df3):
    if(Rate1>0):
      #Amount1 = m.ceil(Loan * (pow((1 + d/ 100), Years)))
      #st.write(Amount1)
      #Years=Years*12 -Rem
      #st.write(Years)
      d4=df3
      #st.dataframe(d4)
      #d4.iloc[:d4[d4.Month == Rem].index[0]]
      Remaining_Loan = d4.loc[(d4["Month"] == Rem+1), ["Loan_Remaining"]]
      #st.write((Remaining_Loan)) 
    #Remaining_Loan=int(Remaining_Loan[0:1]-500)
      #st.write(Remaining_Loan)
      #st.dataframe(d4)
      PR1=Rate1/1200
      Years=(Years*12)-Rem
      #st.write(PR1)
      #st.write(Years)
      o1=pow((1 + PR1), Years)/(pow((1 + PR1), Years)-1)
      #st.write(o1)
      EMI1=m.ceil(o1*(Remaining_Loan.iloc[0]['Loan_Remaining'])*PR1)
      
      #st.write("New EMI",EMI1)
      #Total_Paid=EMI * Years 
      #Amount1=Amount1-Total_Paid
      #st.write(Amount1)
      #EMI1=m.ceil((Amount1)/(Rem))
      #st.write(EMI1)
      Increase=m.ceil(EMI1-EMI)
      #New_Years_1=m.ceil(Amount1/(EMI))
      
      #st.write('It will take',New_Years_1,"months to complete the repayment under the new rate")
      if Increase >=0:
        st.write("Your EMI will increase by:",Increase, 'for the remaining tenure (',Years,'months)')
        st.write('Your new EMI will be:',EMI1)
      else:
        Increase=abs(Increase)
        st.write("Your EMI will decrease by:",Increase, 'for the remaining tenure (',Years,'months)')
        st.write('Your new EMI will be:',EMI1)
      result=[]
      L21=(Remaining_Loan.iloc[0]['Loan_Remaining'])* 1
      for i in range(1,Years+1):
        u=i
        In1=m.ceil(L21 * PR1)
        p1=m.ceil(EMI1-In1)
        L21=L21-p1
        result.append([u,In1,p1,L21])
      #L2=Loan-p
      df4=df11.append(pd.DataFrame(result,columns=df.columns)).reset_index(drop=True)
      st.dataframe(df4)
    else:
      st.info("Enter New Rate ")
  def fn2(AEMI,l,ti,EMI): 
    
    a1=l+ti    
    New_EMI=(EMI*(12+AEMI))/12
    New_Years=m.ceil(a1/(New_EMI))
    col1,col2=st.columns([2.5,1])
    with col1:
      st.write('If you pay',int(AEMI),'extra every year, you can pay-off the loan in (months):',New_Years)
    with col2:
      st.write('Total Savings:',m.ceil(EMI * (Years*12-New_Years)))
    #return(New_Years)
  if __name__=="__main__":
    #col1,col2=st.columns(2)
    #with col1:
      Total_Interest,EMI,Loan,Years,Rate,dataf=main()
      ti=Total_Interest
      e=EMI
      l=Loan
      y=Years
      r=Rate
      df3=dataf
      #st.dataframe(dataf)
      #st.write(ti,l)
      #c=c.append({'A':a,'B':b},ignore_index=True)
      #st.dataframe(c)
      #st.bar_chart(c[['A','B']])
      li=['Interest','Principal Amount']
      ti=m.ceil(ti)
      n=[ti,l]
      #n=[(a*100)/(CI+a),(CI*100)/(CI+a)]
      fig = go.Figure(
      go.Pie(
      labels = li,
      values = n,
      hoverinfo = "label+percent",
      textinfo = "value"
      ))

  st.subheader("Distribution of Payment")
  st.plotly_chart(fig)
  st.write("---------------------------------------------------")
    #st.write(a,b,c,d)
    #with col2:
  st.subheader("Rate-Analysis") 
  st.write("*Central Banks tend to increase/decrease lending rates which will impact your EMIs")
  st.write("*Rate Analysis helps you to check how your monthly EMI will get impacted")  
  form = st.form(key='my-form')
  #form.input
  Rate1=form.number_input('New Rate',step=0.25)
  Rem=form.number_input('Number of EMIs Completed',step=1)
  #r=form.number_input()
  #st.button('Analysis',on_click=fn(a,b,c,d,Rate1))
  submit = form.form_submit_button('Submit')
  if submit:
    fn(e,y,l,r,Rem,Rate1,df3)

  st.subheader("Additional-EMI")
  st.write("*Paying additional EMIs helps you to reduce your loan burden in a long run.")  
  st.write("*Additional-EMI Analysis provides an insight how paying additonal EMI is beneficial.")  
  form = st.form(key='my-form2')
  #form.input
  AEMI=form.number_input('# of Additional EMI Per Year',step=1)
  #st.button('Analysis',on_click=fn(a,b,c,d,Rate1))
  submit2 = form.form_submit_button('Submit')
  if submit2:
    fn2(AEMI,l,ti,e)
  #AEMI=form.number_input('Additional EMI Per Year')  
if selected=='PPF':
    st.subheader("PPF Calculator")
    st.write("-----------------------")
    c1,c2,c3=st.columns(3)
    with c1:
        Amount = st.number_input('Enter Annual Invested Amount',format='%d',step=1,value=10000)
    with c2:
#st.write("Loan amount:", Years)
        Years=st.number_input('Enter Tenure Period in Years',format='%d',step=1,value=15)
    with c3:
        Rate=st.number_input('Enter Rate of Interest',value=7.10,step=0.05)
    st.write("-----------------------")
  
    Rate=Rate/100  
    Amount1=m.ceil(Amount*Years)
    Amt=Amount
    pwr=Amt*(pow((1+Rate),Years)-1)/Rate
    prr=(pwr*Rate)
    #pwr=Amt*(pow(Rate,Years)-1)/Rate
    TL=m.ceil(prr+pwr)
    #st.write(prr+pwr)
    #TL=m.ceil(Amt*pwr)
    ##TL=m.ceil(Amt * (pow(((1 + Rate / 100), Years)-1)/Rate))
    st.write('Maturity Amount:',TL)
    st.write("-----------------------")
    I=TL-Amount1
    li=['Interest','Amount']
    n=[Amount1,I]
    fig = go.Figure(
            go.Pie(
            labels = li,
            values = n,
            hoverinfo = "label+percent",
            textinfo = "value"
            ))  
    st.subheader("Distribution of Payment")
    st.plotly_chart(fig)
if selected=='FD':
    st.subheader("Fixed Deposit Calculator")
    st.write("-----------------------")
    c1,c2,c3=st.columns(3)
    with c1:
        Amount = st.number_input('Enter Principal Amount',format='%d',step=1,value=10000)
    with c2:
#st.write("Loan amount:", Years)
        Years=st.number_input('Enter Tenure Period in Months',format='%d',step=1,value=1)
    with c3:
        Rate=st.number_input('Enter Rate of Interest',value=6.00,step=0.05)
    st.write("-----------------------")
    #Amount=Amount*100000
    if Years > 3:
    #st.write(Years)
        MAmount = round(Amount * (pow((1 + (Rate) / 400), (Years*4/12))))
        #st.info(MAmount)
    else:
        MAmount = round(Amount * (pow((1 + (Rate) / 100), (Years/12))))
    
    st.write('Maturity Amount:',MAmount)
    st.write("-----------------------")
    li=['Interest','Principal Amount']
    n=[MAmount-Amount,Amount]
    #n=[(a*100)/(CI+a),(CI*100)/(CI+a)]
    fig = go.Figure(
    go.Pie(
    labels = li,
    values = n,
    hoverinfo = "label+percent",
    textinfo = "value"
    ))
    st.subheader("Distribution of Maturity Amount")
    st.plotly_chart(fig)
    #st.write("Loan amount:", Years)
if selected=='EPF':
  #Amount = st.slider('Select Basic Salary',0,500,10)
  st.subheader("EPF Calculator")
  st.write("-----------------------")
  col1,col2,col3=st.columns(3)
  with col1:
      Amount=st.number_input('Select Basic Salary',value=10000)
      Rate=st.number_input('Select Rate of Interest', 0.0,10.0,8.1,step=0.05)
  with col2:
      Age1=st.number_input('Select Current Age',0,60,22)
      Age2=st.number_input('Select Retirement Age',0,70,60)
  with col3:
      CEPF=st.number_input('Enter current EPF Balance')
      H=st.number_input('Enter Annual Hike %',5,20,8,step=1)
      
  Age3=Age2-Age1
  st.write("-----------------------")
  result=[]
  df=pd.DataFrame(columns=['Year','Opening','Salary','Contribution','Interest','Total'])
  C2=CEPF
  
  #Amount=Amount *1000
  for i in range(Age1,Age2+1):
          C=Amount*12*0.1567
          I=(C+C2)*Rate/100
          T=C+I+C2
          result.append([Age1,m.ceil(C2),m.ceil(Amount),m.ceil(C),m.ceil(I),m.ceil(T)])
          Age1=Age1 +1
          Amount=Amount*(1+H/100)
          C2=T
          #T=C2+C+I
          #L2=Loan-p
  df1=df.append(pd.DataFrame(result,columns=df.columns)).reset_index(drop=True)
  
  st.write("Maturity Amount:",m.ceil(T))
  st.write("-----------------------")
  st.subheader("Yearly Projection")
  st.dataframe(df1)
st.markdown("""
<style>


/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
