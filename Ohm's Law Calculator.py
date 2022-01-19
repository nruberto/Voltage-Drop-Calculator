import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
st.subheader("Ohm's Law Calculator")

a = []
v = float(st.number_input('What is the initial voltage?', step=1))
b=[]
numR = int(st.number_input('How many resistors does the circuit have?', step=1))

for i in range(numR):
    ohm = float(st.number_input('Enter the resistance for resistor ' + str( i+1) + '? '))
    a.append(ohm)
    b.append((i+1))

    
if sum(a) != 0:
    
    I = v/sum(a)
    st.write('The current is:')
    st.write(round(I,2))


    vv = []
    for i in range(numR):
        volt = I*a[i]
        vv.append(volt)
        st.write('The voltage drop at resistor ' + str( i+1 ) + ' is: ')
        st.write(round(volt,2))
    
    
    
    
    fig = plt.figure(figsize = (15,10))
    plt.bar(b, vv) 
    plt.xticks(np.arange(1, len(b)+1,1))
    
    plt.xlabel('Resistors')
    plt.ylabel('Voltage Drops')
    plt.title('Resistor Voltage Drops')
    
    
    st.pyplot(fig)
    st.write(b)
    
