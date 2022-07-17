import streamlit as st
import json
import pandas as pd
import os
import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb
import random
import statsmodels.api as sm

sb.set(rc={'figure.figsize':(18,12)})

st.title('Auto EDA')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	df = pd.read_csv(uploaded_file)
	df.dropna(axis=1, how='all',inplace=True)
	st.dataframe(df)

	st.write('Describing Dataframe')
	st.dataframe(df.describe())

	st.write('Total Null Values in Dataframe')
	st.table(df.isnull().sum())

	st.write('-'*1000)

	agree = st.checkbox("Correlation Plot")
	if agree:
		cor = sb.heatmap(df.corr(), cmap="YlGnBu", annot=True)
		fig = cor.get_figure()
		st.pyplot(fig)
	st.write('-'*1000)


	agree2 = st.checkbox("Distribution Plots")
	if agree2:
		options = st.selectbox(
	     	'select variable for Histogram Plots',df.columns.tolist())
		st.write('-'*1000)
		if len(options)>0:
			st.subheader('Histograms')
			binwidth = st.text_input('Type number of bins required')
			try:
				mp.figure()
				hist = sb.histplot(df[options],binwidth=int(binwidth))
				fig1 = hist.get_figure()
				st.pyplot(fig1)
			except:
				st.subheader('Below plot is the default plot and for specific binwidth please provide above the bin value')
				mp.figure()
				hist1 = sb.histplot(df[options])
				fig10 = hist1.get_figure()
				st.pyplot(fig10)

		st.write('-'*1000)
		st.subheader('Probability Distribution Function')
		options3 = st.selectbox(
	     	'select variable for Distribution Plots',df.columns.tolist())
		options2 = st.selectbox('Select target column for hue',df.columns.tolist())
		if len(options2)>0:
			try:
				mp.figure()
				kde = sb.kdeplot(data=df, x=options3, hue=options2)
				fig6 = kde.get_figure()
				st.pyplot(fig6)
				st.subheader('Cumulative Distribution function')
				mp.figure()
				kde2 = sb.kdeplot(data=df, x=options3, hue=options2,cumulative=True)
				fig7 = kde2.get_figure()
				st.pyplot(fig7)	
			except:
				st.subheader('please provide numerical column name for PDF and CDF')

	st.write('-'*1000)
	agree3 = st.checkbox("Scatter Plots")
	if agree3:
		multi = st.multiselect('select two variable for scatter plot',df.columns.tolist())
		if len(multi)==2:
			agree5 = st.checkbox("hue as target column")
			if agree5:
				options4 = st.selectbox('Select target column for hue',df.columns.tolist(),key='2')
				try:
					if len(options4)>0:
						mp.figure()
						scatter = sb.scatterplot(data = df,x=multi[0],y=multi[1],hue=options4)
						fig2 = scatter.get_figure()
						st.pyplot(fig2)
				except:
					st.write('Please Give proper target column name')


			else:
				mp.figure()
				scatter = sb.scatterplot(data = df,x=multi[0],y=multi[1])
				fig2 = scatter.get_figure()
				st.pyplot(fig2)

	st.write('-'*1000)
	agree4 = st.checkbox("Pair Plots")
	if agree4:
		options1 = st.selectbox(
	     	'select target column',df.columns.tolist())

		if len(options1)>0:
			try:
				mp.figure()
				st.pyplot(sb.pairplot(df,hue=options1, height=2.5))
			except Exception:
				st.subheader('Please provide proper target columns to plot a pair plot')

	st.write('-'*1000)

	agree5 = st.checkbox("Box Plots")
	if agree5:
		st.write('First selection will be assigned to X axis and Second selection will be assigned to Y axis')
		multi1 = st.multiselect('select two variable for box plot',df.columns.tolist())
		if len(multi1)==2:
			mp.figure()
			boxplot = sb.boxplot(data = df,x=multi1[0],y=multi1[1])
			fig3 = boxplot.get_figure()
			st.pyplot(fig3)


	st.write('-'*1000)
	agree6 = st.checkbox("Violin Plots")
	if agree6:
		st.write('First selection will be assigned to X axis and Second selection will be assigned to Y axis')
		multi2 = st.multiselect('select two variable for Violin plot',df.columns.tolist())
		if len(multi2)==2:
			mp.figure()
			vio = sb.violinplot(data = df,x=multi2[0],y=multi2[1])
			fig3 = vio.get_figure()
			st.pyplot(fig3)

	st.write('-'*1000)
	agree7 = st.checkbox("QQ plot")
	if agree7:
		options5 = st.selectbox('Select the column ',df.columns.tolist(),key='3')
		if len(options5)>0:
			try:
				mp.figure()
				qq = sm.qqplot(df[options5])
				fig9 = qq.get_figure()
				st.pyplot(fig9)
				st.write("QQ plot of {}".format(options5))	
			except:
				st.subheader('please provide proper column name')
