# Your Name
# si649w22 Altair transforms 2

# imports we will use

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data

st.set_page_config(
    page_title="xuchaozj SI649 Individual Project"

)

df_public=pd.read_csv('NCES_public_clean.csv')
df_private=pd.read_csv('NCES_private_clean.csv')

df_private= df_private.loc[:,['State Abbr [Private School] Latest available year','Black or African American Students [Private School] 2015-16','Full-Time Equivalent (FTE) Teachers [Private School] 2015-16','Total Students (Ungraded & K-12) [Private School] 2015-16','White Students [Private School] 2015-16']]
df_public=df_public.loc[:,['State Abbr [Public School] Latest available year','Black or African American Students [Public School] 2015-16','Full-Time Equivalent (FTE) Teachers [Public School] 2015-16','Total Students All Grades (Includes AE) [Public School] 2015-16','White Students [Public School] 2015-16']]


df_private = df_private.drop(df_private[df_private['Total Students (Ungraded & K-12) [Private School] 2015-16'].astype(str)=='–'].index)
df_private = df_private.drop(df_private[df_private['Full-Time Equivalent (FTE) Teachers [Private School] 2015-16'].astype(str)=='–'].index)
df_private = df_private.drop(df_private[df_private['Black or African American Students [Private School] 2015-16'].astype(str)=='–'].index)
df_private = df_private.drop(df_private[df_private['White Students [Private School] 2015-16'].astype(str)=='–'].index)
df_public = df_public.drop(df_public[df_public['Black or African American Students [Public School] 2015-16'].astype(str)=='–'].index)
df_public = df_public.drop(df_public[df_public['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16'].astype(str)=='–'].index)
df_public = df_public.drop(df_public[df_public['Total Students All Grades (Includes AE) [Public School] 2015-16'].astype(str)=='–'].index)
df_public = df_public.drop(df_public[df_public['White Students [Public School] 2015-16'].astype(str)=='–'].index)


df_private = df_private.drop(df_private[df_private['Total Students (Ungraded & K-12) [Private School] 2015-16'].astype(str)=='†'].index)
df_private = df_private.drop(df_private[df_private['Full-Time Equivalent (FTE) Teachers [Private School] 2015-16'].astype(str)=='†'].index)
df_private = df_private.drop(df_private[df_private['Black or African American Students [Private School] 2015-16'].astype(str)=='†'].index)
df_private = df_private.drop(df_private[df_private['White Students [Private School] 2015-16'].astype(str)=='†'].index)
df_public = df_public.drop(df_public[df_public['Black or African American Students [Public School] 2015-16'].astype(str)=='†'].index)
df_public = df_public.drop(df_public[df_public['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16'].astype(str)=='†'].index)
df_public = df_public.drop(df_public[df_public['Total Students All Grades (Includes AE) [Public School] 2015-16'].astype(str)=='†'].index)
df_public = df_public.drop(df_public[df_public['White Students [Public School] 2015-16'].astype(str)=='†'].index)


df_public = df_public.drop(df_public[df_public['Black or African American Students [Public School] 2015-16'].astype(str)=='‡'].index)
df_public = df_public.drop(df_public[df_public['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16'].astype(str)=='‡'].index)
df_public = df_public.drop(df_public[df_public['Total Students All Grades (Includes AE) [Public School] 2015-16'].astype(str)=='‡'].index)
df_public = df_public.drop(df_public[df_public['White Students [Public School] 2015-16'].astype(str)=='‡'].index)


df_private['Total Students (Ungraded & K-12) [Private School] 2015-16']=df_private['Total Students (Ungraded & K-12) [Private School] 2015-16'].astype(float)
df_private['Full-Time Equivalent (FTE) Teachers [Private School] 2015-16']=df_private['Full-Time Equivalent (FTE) Teachers [Private School] 2015-16'].astype(float)
df_private['Black or African American Students [Private School] 2015-16']=df_private['Black or African American Students [Private School] 2015-16'].astype(float)
df_private['White Students [Private School] 2015-16']=df_private['White Students [Private School] 2015-16'].astype(float)


df_public['Black or African American Students [Public School] 2015-16']=df_public['Black or African American Students [Public School] 2015-16'].astype(float)
df_public['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16']=df_public['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16'].astype(float)
df_public['Total Students All Grades (Includes AE) [Public School] 2015-16']=df_public['Total Students All Grades (Includes AE) [Public School] 2015-16'].astype(float)
df_public['White Students [Public School] 2015-16']=df_public['White Students [Public School] 2015-16'].astype(float)

df_private=df_private.dropna()
df_public=df_public.dropna()
df_private['whitepercent']=df_private['White Students [Private School] 2015-16']/df_private['Total Students (Ungraded & K-12) [Private School] 2015-16']
df_public['whitepercent']=df_public['White Students [Public School] 2015-16']/df_public['Total Students All Grades (Includes AE) [Public School] 2015-16']


df_public=df_public.rename(columns={'State Abbr [Public School] Latest available year':'state','Black or African American Students [Public School] 2015-16':'black','Full-Time Equivalent (FTE) Teachers [Public School] 2015-16':'teachers','Total Students All Grades (Includes AE) [Public School] 2015-16':'students','White Students [Public School] 2015-16':'white'})
df_private=df_private.rename(columns={'State Abbr [Private School] Latest available year':'state','Black or African American Students [Private School] 2015-16':'black','Full-Time Equivalent (FTE) Teachers [Private School] 2015-16':'teachers','Total Students (Ungraded & K-12) [Private School] 2015-16':'students','White Students [Private School] 2015-16':'white'})

df_school=pd.concat([df_public,df_private])
df_school['issegregated']=df_school.apply(lambda x:1 if (x['whitepercent']>=0.9)|(x['whitepercent']<=0.1) else 0,axis=1)
df_school['schoolnum']=1
df_school.sample()

counties = alt.topo_feature(data.us_10m.url, 'states')
source = data.unemployment.url

df_state=df_school.groupby('state').agg({'issegregated':'sum','schoolnum':'count'})
df_state=df_state.reset_index()
#df_state

state_dict={'AL':1,'AK':2,'AZ':4,'AR':5,'CA':6,'CO':8,'CT':9,'DE':10,'DC':11,'FL':12,'GA':13,'HI':15,'ID':16,'IL':17,'IN':18,
           'IA':19,'KS':20,'KY':21,'LA':22,'ME':23,'MD':24,'MA':25,'MI':26,'MN':27,'MS':28,'MO':29,'MT':30,'NE':31,'NV':32,
           'NH':33,'NJ':34,'NM':35,'NY':36,'NC':37,'ND':38,'OH':39,'OK':40,'OR':41,'PA':42,'RI':44,'SC':45,'SD':46,'TN':47,
           'TX':48,'UT':49,'VT':50,'VA':51,'WA':53,'WV':54,'WI':55,'WY':56}
df_state['id']=df_state.apply(lambda x:state_dict[x['state'][0:2]],axis=1)
df_state.sample()

vis1=alt.Chart(counties).mark_geoshape().transform_lookup(
    lookup='id',
    from_=alt.LookupData(df_state, 'id',['schoolnum','issegregated','state'])
).transform_calculate(
    segregate_ratio=alt.datum.issegregated/alt.datum.schoolnum
).encode(
    color=alt.Color('segregate_ratio:Q',scale=alt.Scale(scheme='reds')),
    tooltip=[alt.Tooltip('state:N'),
             alt.Tooltip('schoolnum:Q',title='The number of schools in the state'),
             alt.Tooltip('issegregated:Q',title='The number of intensely segregated school(white students consists of more than 90% or less than 10%)'),
             alt.Tooltip('segregate_ratio:Q',title='ratio of segregated schools in the state'),
             ],
    
).project(
    type='albersUsa'
).project(
    type='albersUsa'
).properties(title='segregate ratio of each state')




###code for the second visualization

import re
pattern = re.compile(r'[(].+[)]')  

df_position=pd.read_csv('School_Locations.csv')
#df_position['longti']=df_position.apply(lambda x:pattern.search(x['Location 1']).group(0),axis=1)

#df_position['longti']=df_position.apply(lambda x:(x['Location 1']))
#['Location 1'].str.extract(r'[(]',expand=True)

df_position['longstr']=df_position['Location 1'].str.extract(r'(,.+[)])',expand=True)
df_position['longstr']=df_position['longstr'].str.slice(1,-1)
df_position['longtitude']=df_position.apply(lambda x:float(x['longstr']),axis=1)

df_position['latstr']=df_position['Location 1'].str.extract(r'([(].+,)',expand=True)
df_position['latstr']=df_position['latstr'].str.slice(1,-1)
df_position['latitude']=df_position.apply(lambda x:float(x['latstr']),axis=1)
df_position=df_position[['ATS SYSTEM CODE','longtitude','latitude']]

#df_position['encode']=df_position['ATS SYSTEM CODE'].apply(lambda x: int(encodeDBN(str(x))))
#df_position['encode']=df_position['ATS SYSTEM CODE'].apply(lambda x: x[6])
df_position['ATS SYSTEM CODE']=df_position['ATS SYSTEM CODE'].str.slice(0,6)
df_position.head()

df_math=pd.read_csv('ny-math-results-2013-2019-public-all.csv')
df_ela=pd.read_csv('ny-ela-results-2013-2019-public-all.csv')

df_math=df_math.drop(df_math[df_math['Mean Scale Score']=='s'].index)

df_math['totalscore']=df_math.apply(lambda x:float(x['Number Tested'])*float(x['Mean Scale Score']),axis=1)
df_math=df_math.groupby(['DBN','School Name']).agg({'Number Tested':'sum','totalscore':'sum'}).reset_index()
#df_math['encode']=df_math['DBN'].apply(lambda x: float(encodeDBN(str(x))))

#df[df.score < 50].index
#df_grad.sample()
df_ela=df_ela.drop(df_ela[df_ela['Mean Scale Score']=='s'].index)
df_ela['totalscore']=df_ela.apply(lambda x:float(x['Number Tested'])*float(x['Mean Scale Score']),axis=1)
df_ela=df_ela.groupby(['DBN','School Name']).agg({'Number Tested':'sum','totalscore':'sum'}).reset_index()
#df_ela['encode']=df_ela['DBN'].apply(lambda x: float(encodeDBN(str(x))))

df_public=pd.read_csv('NCES_public_clean.csv')
df_private=pd.read_csv('NCES_private_clean.csv')
df_public['latitude']=df_public['Latitude [Public School] 2015-16'].apply(lambda x:float(x) if x!='†' else 0)
df_public['longtitude']=df_public['Longitude [Public School] 2015-16'].apply(lambda x:float(x) if x!='†' else 0)


df_score=pd.merge(left=df_ela,right=df_math,left_on='DBN',right_on='DBN')
df_score=pd.merge(left=df_score,right=df_position,left_on='DBN',right_on='ATS SYSTEM CODE')
#df_score=pd.merge(left=df_score,right=df_public,left_on=['longtitude',''],right_on='ATS SYSTEM CODE')

df_score['ela_mean']=df_score['totalscore_x']/df_score['Number Tested_x']
df_score['math_mean']=df_score['totalscore_y']/df_score['Number Tested_y']
df_score['schoolname']=df_score['School Name_x'].apply(lambda x : 'other' if x!='P.S. 307 DANIEL HALE WILLIAMS' else x)



states = alt.topo_feature(data.us_10m.url, feature='states')


brush1 = alt.selection(type='interval')
vis22=alt.Chart(df_score).mark_point().encode(
    x=alt.X('longtitude:Q',scale = alt.Scale(domain=(-74.3,-73.6)),title='longitude',axis=None),
    y=alt.Y('latitude:Q',scale = alt.Scale(domain=(40.4,41)),axis=None),
    size=alt.value(5),
    color=alt.Color('ela_mean:Q',scale=alt.Scale(scheme='reds')),
    tooltip=['DBN','ela_mean',alt.Tooltip('School Name_x',title='school')]
).properties(
    width=400,
    height=400,
    title='The ela score of schools in NYC'
).add_selection(
    brush1
)

bar_red1 = alt.Chart(df_score, width=400,height=100).mark_bar(color = 'red',size=20).encode(
    x=alt.X('mean(ela_mean):Q',axis=alt.Axis(values=[0], ticks=True, grid=False, labels=False)),
    y=alt.Y('schoolname:N',title='School Name')
).transform_filter(
    alt.datum.schoolname== 'P.S. 307 DANIEL HALE WILLIAMS'
)

bars1 = alt.Chart(df_score,width=400,height=100).mark_bar(size=20).encode(
    x=alt.X('mean(ela_mean):Q',axis=alt.Axis(values=[0], ticks=True, grid=False),title='The mean score of language'),
    y=alt.Y('schoolname:N',title='School Name')
).transform_filter(
    brush1
).transform_filter(
    alt.datum.schoolname!= 'P.S. 307 DANIEL HALE WILLIAMS'
)

bar1_text = bars1.mark_text(
    align='left',
    baseline='middle',
    dx=5
).encode(
    text=alt.Text('mean(ela_mean):Q',format = '.0f')
    )
bar_red1_text = bar_red1.mark_text(
    align='left',
    baseline='middle',
    dx=5
).encode(
    text=alt.Text('mean(ela_mean):Q',format = '.0f')
    )
#vis22&(bars1+bar_red1+bar1_text+bar_red1_text)
brush2 = alt.selection(type='interval')
vis23=alt.Chart(df_score).mark_point().encode(
    x=alt.X('longtitude:Q',scale = alt.Scale(domain=(-74.3,-73.6)),title='longitude',axis=None),
    y=alt.Y('latitude:Q',scale = alt.Scale(domain=(40.4,41)),axis=None),
    size=alt.value(5),
    color=alt.Color('math_mean:Q',scale=alt.Scale(scheme='greens')),
    tooltip=['DBN','math_mean',alt.Tooltip('School Name_x',title='school')]
).project(
    type='albersUsa',
    scale=27000
).properties(
    width=400,
    height=400,
    title='The math score of schools in NYC'
).add_selection(
    brush2
)

bar_red2 = alt.Chart(df_score, width=400,height=100).mark_bar(color = 'red',size=20).encode(
    x=alt.X('mean(math_mean):Q',axis=alt.Axis(values=[0], ticks=True, grid=False, labels=False)),
    y=alt.Y('schoolname:N',title='School Name')
).transform_filter(
    alt.datum.schoolname== 'P.S. 307 DANIEL HALE WILLIAMS'
)

bars2 = alt.Chart(df_score,width=400,height=100).mark_bar(size=20).encode(
    x=alt.X('mean(math_mean):Q',axis=alt.Axis(values=[0], ticks=True, grid=False),title='The mean score of math'),
    y=alt.Y('schoolname:N',title='')
).transform_filter(
    brush2
).transform_filter(
    alt.datum.schoolname!= 'P.S. 307 DANIEL HALE WILLIAMS'
)

bar2_text = bars2.mark_text(
    align='left',
    baseline='middle',
    dx=5
).encode(
    text=alt.Text('mean(math_mean):Q',format = '.0f')
    )
bar_red2_text = bar_red2.mark_text(
    align='left',
    baseline='middle',
    dx=5
).encode(
    text=alt.Text('mean(math_mean):Q',format = '.0f')
    )
#vis23&(bars2+bar_red2+bar2_text+bar_red2_text)

vis2=(vis22&(bars1+bar_red1+bar1_text+bar_red1_text))
vis4=(vis23&(bars2+bar_red2+bar2_text+bar_red2_text))
#vis2=(vis23&(bars2+bar_red2+bar2_text+bar_red2_text))

###code for the third visualization


df_public2=pd.read_csv('NCES_public_clean.csv')
df_public2=df_public2.loc[:,['School Name','State Abbr [Public School] Latest available year','Black or African American Students [Public School] 2015-16','Full-Time Equivalent (FTE) Teachers [Public School] 2015-16','Total Students All Grades (Includes AE) [Public School] 2015-16','White Students [Public School] 2015-16','Longitude [Public School] 2015-16','Latitude [Public School] 2015-16','Location City [Public School] 2015-16']]

df_public2 = df_public2.drop(df_public2[df_public2['Black or African American Students [Public School] 2015-16'].astype(str)=='–'].index)
df_public2 = df_public2.drop(df_public2[df_public2['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16'].astype(str)=='–'].index)
df_public2 = df_public2.drop(df_public2[df_public2['Total Students All Grades (Includes AE) [Public School] 2015-16'].astype(str)=='–'].index)
df_public2 = df_public2.drop(df_public2[df_public2['White Students [Public School] 2015-16'].astype(str)=='–'].index)

df_public2 = df_public2.drop(df_public2[df_public2['Black or African American Students [Public School] 2015-16'].astype(str)=='†'].index)
df_public2 = df_public2.drop(df_public2[df_public2['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16'].astype(str)=='†'].index)
df_public2 = df_public2.drop(df_public2[df_public2['Total Students All Grades (Includes AE) [Public School] 2015-16'].astype(str)=='†'].index)
df_public2 = df_public2.drop(df_public2[df_public2['White Students [Public School] 2015-16'].astype(str)=='†'].index)

df_public2 = df_public2.drop(df_public2[df_public2['Black or African American Students [Public School] 2015-16'].astype(str)=='‡'].index)
df_public2 = df_public2.drop(df_public2[df_public2['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16'].astype(str)=='‡'].index)
df_public2 = df_public2.drop(df_public2[df_public2['Total Students All Grades (Includes AE) [Public School] 2015-16'].astype(str)=='‡'].index)
df_public2 = df_public2.drop(df_public2[df_public2['White Students [Public School] 2015-16'].astype(str)=='‡'].index)


df_public2 = df_public2.drop(df_public2[df_public2['Longitude [Public School] 2015-16'].astype(str)=='†'].index)
df_public2 = df_public2.drop(df_public2[df_public2['Latitude [Public School] 2015-16'].astype(str)=='†'].index)

df_public2['Black or African American Students [Public School] 2015-16']=df_public2['Black or African American Students [Public School] 2015-16'].astype(float)
df_public2['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16']=df_public2['Full-Time Equivalent (FTE) Teachers [Public School] 2015-16'].astype(float)
df_public2['Total Students All Grades (Includes AE) [Public School] 2015-16']=df_public2['Total Students All Grades (Includes AE) [Public School] 2015-16'].astype(float)
df_public2['White Students [Public School] 2015-16']=df_public2['White Students [Public School] 2015-16'].astype(float)

df_public2=df_public2.dropna()

df_public2['longitude']=df_public2['Longitude [Public School] 2015-16'].apply(lambda x:float(x))
df_public2['latitude']=df_public2['Latitude [Public School] 2015-16'].apply(lambda x:float(x))



df_public2['whitepercent']=df_public2['White Students [Public School] 2015-16']/df_public2['Total Students All Grades (Includes AE) [Public School] 2015-16']
df_public2['segregatepoint']=df_public2.apply(lambda x:abs(0.5-x['whitepercent']),axis=1)

df_public2=df_public2.rename(columns={'Location City [Public School] 2015-16':'city','State Abbr [Public School] Latest available year':'state','Black or African American Students [Public School] 2015-16':'black','Full-Time Equivalent (FTE) Teachers [Public School] 2015-16':'teachers','Total Students All Grades (Includes AE) [Public School] 2015-16':'students','White Students [Public School] 2015-16':'white'})
df_public2=df_public2[df_public2['state']=='NY ']
#df_public2=df_public2[(df_public2['city']=='OZONE PARK')|(df_public2['city']=='FLUSHING')|(df_public2['city']=='MIDDLE VILLAGE')|(df_public2['city']=='BRONX')|(df_public2['city']=='STATEN ISLAND')|(df_public2['city']=='NEW YORK')|(df_public2['city']=='BROOKLYN')|(df_public2['city']=='QUEENS VILLAGE')]
df_public2['issegregated']=df_public2.apply(lambda x:1 if (x['whitepercent']>=0.9)|(x['whitepercent']<=0.1) else 0,axis=1)



public2=alt.Chart(df_public2).mark_point().transform_calculate(
    issegregate= 'datum.issegregated==0? "False":"True"'
).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    color='issegregate:N',
    size=alt.Size('segregatepoint:Q',scale=alt.Scale(domain=[0,5])),
    
    #size=alt.value(3),
    #shape=alt.Shape('issegregated:N'),
    #shape='issegregated:N',
    tooltip=['School Name','whitepercent:Q','city','issegregate:N',alt.Tooltip('segregatepoint:Q',title='The absolute value of difference between white percent and 0.5 ')]
).project(
    type='albersUsa',
    scale=22000,
    translate=[-6300,1800]
).properties(
    width=700,
    height=500
)
base2= alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project(
    type='albersUsa',
    scale=22000,
    translate=[-6300,1800]
).properties(
    width=700,
    height=500,
    title='segregate situation in NYC and neighbourhood '
)
vis3=base2+public2



### Display charts
### Hint: Create a sidebar 'selectbox' and use if, else statements for the correct outputs [Information is also in the handout]

# vis_options=['Vis1','Vis2','Vis3']
# vis_selectbox=st.sidebar.selectbox(
# label='select a visualization to display',
# options=vis_options
# )
#
# if(vis_selectbox=='Vis1'):
#     st.write(vis1)
# elif(vis_selectbox=='Vis2'):
#     st.write(vis2)
# elif(vis_selectbox=='Vis3'):
#     st.write(vis3)


st.title('School Segregation')
'This blog and accompanying visualizations are written and designed for the article "Choosing a School for My Daughter in a Segregated City" ' \
'published on The New York Time Magazine(https://www.nytimes.com/2016/06/12/magazine/choosing-a-school-for-my-daughter-in-a-segregated-city.html)' \
'For the viewers that have limited knowldge about the school segregation situation, this blog may help you walk through and gain the basic information' \
'about school segregation.'
'Before we really come to the visualization, some definition need to be clarified at the very beginning. In all visualizations, I regard the schools' \
'with the proportion of white students higher than 90% or lower than 10% as segregated schools. Of course you may have different perspective or thoughts' \
'on the threshold value, but the boundary of 10% does help to reveal some facts.'
st.header('The segregation on the state scale')
'The first visualization shows the proportion, number of segregated schools in each state. As you can see that the state with deeper color tend to ' \
'face a more severe school segregation as total. If you are interested at some state, for example, your living state, simply move your cursor on it,' \
'and you will see the detailed statistics as annotation.'
st.write(vis1)

st.header('Segregate Situation in NYC')
'As the author lived in NYC, I pick the neighbourhood area out and label each school in the area as a circle. The segregaed school is colored by orange ' \
'whilst unsegregated school by blue. Here I introduce one new parameter which I called segregate point, which is the absolute value of the difference ' \
'between 0.5 and white student percent. And the size of each circle is encoded with the segregate point. Like the former visualization, when you ' \
'hover on each point you could see the detailed information.'
st.write(vis3)

st.header('Academic Performance of School in NYC')
'In the article, the author finally send her daughter to PS 307, which is typical segregated school. Does the segregated school tend to behave' \
'differently in standard academic test? This visualization includes two parts, the first is for language test and the second is for math test.' \
'Not only do I add annotation to these schools, you could use the cursor to drag and choose the schools in the area you are interested. The mean' \
'value of the test score will be displayed in the following bar chart, which makes it possible for you to compare the academic performance between ' \
'schools.'
st.write(vis2)
st.write(vis4)

#st.write(np.__version__)
#st.write( pd.show_versions())