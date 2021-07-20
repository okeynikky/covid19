import streamlit as st
import pandas as pd
import numpy as np
import base64
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

## Page expands to full width
st.set_page_config(page_title='SEIR Model App',
    layout='wide')
st.write("""
# SEIR Model Appp
**(Construction of the SEIR model)**

The SEIR model divides the population into four categories, called "S", "E", "I", and "R".

Category **"S"** consists of individuals who are susceptible to the disease being modeled.

Category **"E"** consists of individuals who are exposed to the disease. Diseases (like COVID-19) often have an incubation period or a latency period and this category accommodates it. (The SIR model does not have this category.)

Category **"I"** consists of individuals infected with the disease and are capable of infecting others.

Category **"R"** consists of individuals who can be removed from the system, e.g., because they have gained immunity to the disease, or because they have succumbed to the disease.

""")
st.sidebar.header('Set initial assumption')
s = st.sidebar.slider('s % for proportion of individuals who are susceptible ', 0.0, 1.0)
e = st.sidebar.slider('e % for proportion of individuals who are exposed to the disease ', 0.0, 1.0)
i = st.sidebar.slider('i % for proportion of individuals infected with the disease and are capable of infecting others. ', 0.0, 1.0)
r = st.sidebar.slider('r % for proportion of individuals who can be removed from the system ', 0.0, 1.0)
y = st.sidebar.slider('Time to simulation', 0, 200, (10,50), 50)
# Sidebar - Specify parameter settings
st.sidebar.header('Set Parameters')
beta = st.sidebar.slider('beta % for transmission rate (or the rate of contact)', 0.0, 1.0)
sigma = st.sidebar.slider('sigma % for incubation rate or the rate at which exposed hosts become infected', 0.0, 1.0)
gamma = st.sidebar.slider('gamma % for recovery rate or the rate at which infected individuals move to the R category', 0.0, 1.0)

# Displays the dataset
st.subheader('Dynamics system')



def seir_f(t, y, beta, sigma, gamma):
	s, e, i, r = y
	return np.array([-beta * i * s,
			-sigma * e + beta * i * s, 
			-gamma * i + sigma * e, 
			gamma * i])

			
def build_model():

	sol = solve_ivp(seir_f, [0, 60], [s, e, i, r], 
			rtol=1e-6, args=(beta, sigma, gamma))

	fig = plt.figure(); ax = fig.gca()
	curves = ax.plot(sol.t, sol.y.T)
	ax.legend(curves, ['S', 'E', 'I', 'R']);
	st.pyplot(fig,width=400, height=400)
if st.button('Press Simulation'):
	st.markdown('The SEIR Model.')
	build_model()


st.write("""(ref: http://web.pdx.edu/~gjay/teaching/mth271_2020/html/09_SEIR_model.html )""")