from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import datetime
model = load_model('Scrap_cricket_model')

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)



def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    score = predictions_df['Score'][0]
    return [predictions,score]

def run():
    from PIL import Image
    image = Image.open('indian_team-2.jpg')
    image_office = Image.open('indian_team-1.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app was created to predict the chances of the Indian team to win')
    st.sidebar.success('http://www.howstat.com/cricket/Statistics/Matches/MatchListCountry_ODI.asp?A=IND')
    st.sidebar.image(image_office)
    st.title("Predicting Oneday odi match Result")
    if add_selectbox == 'Online':
        date = st.date_input('Match Date', datetime.date(2021,1,1))
        Versus = st.selectbox('Versus', ['England', 'New Zealand', 'Pakistan', 'West Indies',
        'Sri Lanka', 'Australia', 'Zimbabwe', 'Bangladesh', 'South Africa',
        'United Arab Emirates', 'Kenya', 'Singapore', 'Netherlands',
        'Namibia', 'Bermuda', 'Ireland', 'Scotland', 'Hong Kong',
        'Afghanistan'])
        First_Batting = st.selectbox('First Batting',[Versus,'India'])
        Ground = st.selectbox('Ground',['AMI Stadium','Adelaide Oval','Albion Sports Complex','Antigua Recreation Ground','Arbab Niaz Stadium',
 'Arnos Vale Ground','Arun Jaitley Stadium','Ayub National Stadium','Bangabandhu National Stadium','Barabati Stadium',
 'Barkatullah Khan Stadium','Barsapara Cricket Stadium','Basin Reserve','Bay Oval','Bellerive Oval','Boland Park',
 'Bourda','Brabourne Stadium','Brisbane Cricket Ground','Buffalo Park','Captain Roop Singh Stadium','Carisbrook',
 'City Oval','Civil Service Cricket Club','County Ground (Bristol)','County Ground (Chelmsford)','County Ground (Hove)',
 'Cricket, Skating & Curling Club','Darren Sammy National Cricket Stadium','Dr YS Rajasekhara Reddy Cricket Stadium','Dubai International Cricket Stadium',
 'Eden Gardens','Eden Park','Edgbaston','Gaddafi Stadium','Galle International Stadium','Gandhi Sports Complex Ground',
 'Gandhi Stadium','Grace Road','Green Park','Greenfield International Stadium','Gymkhana Club Ground','Harare Sports Club','Harrup Park',
 'Headingley','Himachal Pradesh Cricket Association Stadium','Holkar Cricket Stadium',
 'Ibn-e-Qasim Bagh Stadium','Indira Gandhi Stadium','Indira Priyadarshini Stadium','JSCA International Stadium Complex',
 'Jawaharlal Nehru Stadium (Delhi)','Jinnah Stadium (Gujwranwala)','Jinnah Stadium (Sialkot)','Kallang Ground',
 'Keenan Stadium','Kennington Oval','Kensington Oval','Khan Shaheb Osman Ali Stadium','Kingsmead',
 'Kinrara Academy Oval','Lal Bahadur Shastri Stadium',"Lord's",'M Chinnaswamy Stadium','MA Aziz Stadium','MA Chidambaram Stadium',
 'Madhavrao Scindia Cricket Ground','Maharashtra Cricket Association Stadium','Mahinda Rajapaksha International Cricket Stadium',
 'Mangaung Oval','Manuka Oval','McLean Park','Melbourne Cricket Ground',
 'Moti Bagh Stadium','Multan Cricket Stadium','Nahar Singh Stadium','Narendra Modi Stadium','National Stadium (Karachi)',
 'Nehru Stadium (Guwahati)','Nehru Stadium (Indore)','Nehru Stadium (Kochi)','Nehru Stadium (Margao)','Nehru Stadium (Pune)','Nevill Ground',
 'Newlands','Niaz Stadium','North Tasmania Cricket Association Ground',
 'Old Trafford','Owen Delany Park',
 'P Sara Oval','Padang Cricket Ground','Pallekele International Cricket Stadium','Providence Stadium','Punjab Cricket Association IS Bindra Stadium',
 "Queen's Park (Old)","Queen's Park Oval",'Queens Sports Club',
 'Queenstown Events Centre','R Premadasa Stadium','Rajiv Gandhi International Stadium',
 'Rangiri Dambulla International Stadium','Rawalpindi Cricket Stadium','Reliance Stadium','Riverside Ground',
 'Sabina Park',
 'Sardar Vallabhai Patel Stadium','Saurashtra Cricket Association Stadium','Sawai Mansingh Stadium','Sector 16 Stadium','Seddon Park','Sharjah Cricket Stadium','Sheikh Zayed Stadium','Sher-I-Kashmir Stadium','Shere Bangla National Stadium','Sinhalese Sports Club Ground','Sir Vivian Richards Stadium','Sophia Gardens',"St George's Park",'SuperSport Park', 'Sydney Cricket Ground','The Cooper Associates County Ground',
 'The Rose Bowl','Titwood','Trent Bridge','Tyronne Fernando Stadium','University Stadium','VRA Ground',
 'Vidarbha Cricket Association Ground','Vidarbha Cricket Association Stadium','WACA Ground','Wanderers Stadium','Wankhede Stadium','Warner Park','Westpac Stadium','Willowmoore Park','Zafar Ali (Sahiwal) Stadium'])
        Target_Runs = st.number_input('Target Runs',max_value=700, value=150)
        output=""
        result =""
        input_dict={'Date':date,'Versus':Versus,'First Batting':First_Batting,'Ground':Ground,'Target Runs':Target_Runs}
        input_df = pd.DataFrame([input_dict])
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            if output[0]=='1.0':
              result = "win"
            if output[0]=='0.0':
              result = "lose"
            st.success('India will {} the match'.format(result))
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
