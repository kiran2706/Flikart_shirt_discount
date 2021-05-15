from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import datetime
model = load_model('flpkrt_shirt_discnt_prediction')

st.markdown(
    """
<style>
.sidebar .sidebar-content 
{
    background-image: linear-gradient(lightblue,lightyellow);
    color: white;
}
</style>
""",unsafe_allow_html=True,
)

st.markdown('<style>body{background-color: lightyellow;}</style>',unsafe_allow_html=True)

st.markdown('<style>h1{color: green;}</style>', unsafe_allow_html=True)



def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    score = predictions_df['Score'][0]
    return [predictions,score]

def run():
    from PIL import Image
    image = Image.open('flpkrt_image-1.jpg')
    image_office = Image.open('flpkrt_image-2.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('Predict the discount for shirt in flipkart')
    st.sidebar.success('''
    
    Low - 0-50

    Medium - 50-65
    
    High - 65-90''')
    st.sidebar.image(image_office)
    st.title("Predicting discount for a shirt")
    if add_selectbox == 'Online':


        Brand = st.selectbox('Brand', sorted(['Try This', 'X-MEN', 'Surhi', 'FASHLOOK', 'Dennis Lingo', 'FUBAR',
       'U TURN', 'TRIPR', 'FLYING MACHINE', 'BESPOQE', 'BASE 41','Tap in', 'ASIAN & FITCH', 'BEING REAL', 'VERO LIE', 'COBIO MAN',
       'DEELMO', 'HIGHLANDER', 'Jai Textiles', 'U.S. POLO ASSN.', 'GESPO','Qlonz store', 'FabTag - Deeksha', 'Mialo fashion', 'KILLER',
       'METRONAUT', 'Blue dove', 'IndoPrimo', 'Rope', 'FINIVO FASHION','ZOMBOM', 'Raymond', 'PETER ENGLAND', 'FastColors', 'UNITED CLUB',
       'Louis Philippe Jeans', 'Drashti Villa', "LEVI'S", 'Billion','Gritstones', 'Eyebogler', 'Carbonn Cloth', 'Jolly Creation', 'VH Brother', 'MR.KAMEEJ', 'Jump Cuts', 'Funday Fashion','Dipzon villa', 'MAYRA', 'Eviqe', 'Majestic Man', 'Selvia',
       'Louis Philippe Sport', 'icome', 'Amadore', 'GHPC','LOUIS PHILIPPE', 'CNDCREATION', 'Allen Solly Tribe', 'VeBNoR','VTEXX', 'MANIAC', '3SIX5', 'VAN HEUSEN SPORT', 'Lee Cross',
       'allen solly', 'Maitree Creations', 'Blackberrys','Trendz Deeksha', 'RED TAPE', 'Brinley', 'ELEPANTS', 'HANUMNTRA','almora', 'LITTLE MAN', 'Desh bandhu khadi', 'DEEKSHA CLOTHING','Tokyo Talkies', 'Arrow Sport', 'HASINI Fashion', 'Yukon',
       'PARK AVENUE', 'UC UNITED CLUB', 'MR.PLAYER', 'CLUBINDIA','5TH ANFOLD', 'Evernote', 'indicare', 'CRAFT HEAVEN','Peter England University', 'Solbiza', 'WOMEN MARTS', 'SASSAFRAS','Purple State', 'Kevin Swift', 'tfurnish', 'Rmartin', 'Pepe Jeans',
       'dense star', 'ARROW', 'La Zoire', 'KINGDENIM', 'Unistreet', 'Feed Up', 'DARZI', 'Lomoniya', 'EIGHTEEN UP', 'Apuesto',
       'ShopyBucket', 'MATELCO', 'RAHUL CREATION', 'V2 Retail Limited','Whipcord', 'red craft', 'DOM', 'Being Fab', 'Urbano Fashion',
       'GLADIATOR PRODUCTS', 'PANKHIL', 'MONTREZ', 'Kryptar', 'Kay Dee','Wild West', 'Ojass', 'GEUM', 'clinch fashion', 'Blue Scroll',
       'Raa Jeans', 'BOSQUE', 'SAT CREATION', 'THE NEXT LEVEL','INDICLUB', 'INDIAN TERRAIN', 'PROTOCOL', 'XTL', 'PAUSE Sport',
       'Ragoho', 'US Polo Kids', 'Alle Moda', 'GRITSMAD', 'ROADSTER','PERRIGEE', 'CAMPUS SUTRA', 'Zartha', 'dhayani fashion', 'ARIHANT', 'The Indian Garage Co.', 'VAN HEUSEN', 'PARX', 'Zolario',
       'PEARL OCEAN', 'Wishing Rack', 'PROVOGUE', 'Carbonn Blue','Aaj Collection', 'JUHIL BAZAR', 'REHAN', 'UD FABIC', 'PSK','FASHNOY', 'Kidsor', 'Spykar']))

        Collar = st.selectbox('Collar Type',['Spread', 'Button Down', 'Slim', 'Mandarin', 'Cut Away',
       'Hood', 'Ribbed Collar', 'Club', 'Ruffle Collar', 'Pointed Collar',
       'Tie up', 'Wingtip', 'Built-up', 'Curved Collar'])


        Original_Price = st.number_input('Price 0f Shirt',max_value=4500,min_value=500, value=1200,step=100)
        Rating = st.number_input('Rating',max_value=5.0,min_value=0.0, value=3.,step=0.1)
        Rating_Count = st.number_input('Number of Peoples Rated',min_value=0, value=100,step=50)
        Reviews = st.number_input('Count of Reviewes',min_value=0, value=100,step=50)
        
        Fit = st.selectbox('Fit',['Slim', 'Regular', 'Tailored', 'Super Slim'])


        Fabric = st.selectbox('Fabric', sorted(['Cotton Blend', 'Pure Cotton', 'Rayon', 'Polycotton',
       'Linen Blend', 'Denim', 'Lycra Blend', 'Polyester',
       'Cotton Rayon Blend', 'Poly Georgette', 'Crepe', 'Polyester Blend',
       'Satin Blend', 'Cotton Lycra Blend', 'Cotton Linen Blend',
       'Rayon Blend', 'Cotton Silk', 'Cotton Jersey', 'Khadi Cotton',
       'Viscose', 'Poly Crepe', 'Cotton', 'Denim Blend',
       'Cotton Viscose Blend', 'Pure Linen', 'Cotton Satin Blend',
       'Nylon Blend']))

        Sleeve = st.selectbox('Sleeve', ['Full Sleeve', 'Short Sleeve', 'Half Sleeve', 'Roll-up Sleeve',
       '3/4th Sleeve', 'Sleeveless'])

        Pattern = st.selectbox('Pattern',sorted(['Color Block', 'Solid', 'Checkered', 'Printed', 'Striped',
       'Floral Print', 'Applique', 'Houndstooth', 'Checkered, Printed',
       'Self Design', 'Geometric Print', 'Solid, Color Block',
       'Polka Print', 'Washed', 'Dyed, Solid', 'Polka Print, Printed',
       'Printed, Checkered', 'Printed, Washed', 'Military Camouflage',
       'Color Block, Solid', 'Animal Print']))

        Color = st.selectbox('Color', sorted(['White, Black', 'White, Blue', 
        'Pink', 'Brown', 'Blue', 'Orange',
       'Maroon', 'Black', 'Green', 'Maroon, Blue', 'Multicolor',
       'Dark Blue, Light Blue, Beige', 'Dark Blue, White', 'Grey',
       'Green, Black', 'White', 'Light Blue', 'Red', 'Dark Blue',
       'Purple', 'Yellow', 'Dark Green', 'Dark Blue, Red, Blue',
       'Black, White', 'Black, Red', 'Brown, Black, White',
       'White, Maroon', 'Beige', 'Brown, Black', 'Black, Beige',
       'Light Blue, White', 'Blue, Maroon', 'Blue, Yellow', 'Khaki',
       'Red, White, Black', 'Green, Black, Grey', 'Light Green',
       'White, Pink', 'Dark Blue, Red', 'White, Green', 'Dark Blue, Blue',
       'Black, Yellow', 'Maroon, Black', 'Black, Grey',
       'Green, Dark Blue', 'Dark Blue, Light Blue, White',
       'Dark Blue, Light Green', 'Red, Black', 'Red, White',
       'Blue, Black', 'Pink, Dark Blue', 'Blue, Green', 'White, Yellow',
       'Blue, Grey', 'Light Blue, Pink, Grey', 'Pink, White',
       'Blue, Pink', 'Black, Green', 'Dark Blue, Maroon', 'Beige, Orange',
       'Blue, Purple', 'Dark Green, White, Blue', 'Red, Blue',
       'Dark Blue, Green', 'White, Black, Beige']))


        Fabric_Care = st.selectbox('Fabric Care', sorted(['Regular Machine Wash', 
       'Dry clean only', 'Gentle Machine Wash',
       'Machine wash as per tag', 'Hand wash',
       'Reverse and dry, Do not tumble dry, Do not bleach, Gentle Machine Wash',
       'Do not tumble dry, Do not dry clean, Do not bleach, Gentle Machine Wash',
       'Cold water wash only', 'Slight color may bleed in first wash',
       'Do not tumble dry, Do not dry clean, Do not bleach, Wash with like colors',
       'Do not bleach, Dry in shade, Gentle Machine Wash, Hand wash',
       'Slight color may bleed in first wash, Wash with like colors',
       'Do not bleach, Wash with like colors, Do not wring, Do not dry clean',
       'Wash with like colors, Slight color may bleed in first wash',
       'First wash dry clean thereafter handwash',
       'Hand wash, Gentle Machine Wash',
       'Do not Iron on print/embroidery/embellishment',
       'Do not bleach, Do not tumble dry, Dry in shade, Gentle Machine Wash',
       'Regular Machine Wash, Do not tumble dry, Do not dry clean, Do not bleach',
       'Slight color may bleed in all washes',
       'Reverse and dry, Do not tumble dry, Slight color may bleed in all washes, Gentle Machine Wash',
       'Regular Machine Wash, Reverse and dry, Dry in shade, Do not bleach, Hand wash, Reverse and dry, Dry in shade, Do not bleach, Hand wash, Reverse and dry, Do not bleach',
       'Machine wash as per tag, Do not bleach, Reverse and dry, Wash with like colors, Dry in shade',
       'Machine wash as per tag, Regular Machine Wash, Do not bleach, Do not wring',
       'Slight color may bleed in first wash, First wash dry clean thereafter handwash',
       'Do not dry clean',
       'Regular Machine Wash, Reverse and dry, Do not bleach, Dry in shade',
       'Slight shrinkage would be expected',
       'Do not bleach, Dry in shade, Hand wash, Gentle Machine Wash',
       'Wash with like colors', 'Regular Machine Wash, Hand wash',
       'Reverse and iron, Slight shrinkage would be expected, Hand wash',
       'Do not bleach, Dry in shade, Gentle Machine Wash',
       'Do not bleach, Wash with like colors, Gentle Machine Wash',
       'Dry clean only, Regular Machine Wash',
       'Dry in shade, Do not tumble dry, Do not bleach, Gentle Machine Wash',
       'Do not bleach, Wash with like colors, Do not tumble dry, Do not wring',
       'Wash similar colors together', 'Do not bleach',
       'Dry in shade, Do not bleach, Machine wash as per tag',
       'Gentle Machine Wash, Slight color may bleed in first wash, Machine wash as per tag',
       'Do not Iron on print/embroidery/embellishment, Wash with like colors',
       'Machine wash as per tag, Reverse and dry, Do not bleach, Dry in shade',
       'Do not iron, Do not bleach, Regular Machine Wash', 'Dry in shade',
       'Do not iron', 'Regular Machine Wash, Cold water wash only',
       'Machine wash as per tag, Do not bleach, Dry in shade, Do not dry clean',
       'Regular Machine Wash, Hand wash, Cold water wash only, Do not bleach',
       'Regular Machine Wash, Reverse and dry, Dry in shade',
       'Machine wash as per tag, Do not bleach, Do not tumble dry, Do not wring',
       'Regular Machine Wash, Do not bleach, Hand wash, Gentle Machine Wash',
       'Regular Machine Wash, Do not Iron on print/embroidery/embellishment, Do not bleach']))


        Suitable_For = st.selectbox('Suitable For',['Western Wear','Non-Western'])
        if Suitable_For == 'Western Wear':
          Suitable_For = 1
        else:
          Suitable_For = 0


        





        output=""
        result =""

        input_dict = {'Brand': Brand,'Collar': Collar,'Color': Color,
        'Fabric': Fabric,'Fabric Care': Fabric_Care,
        'Fit': Fit,'Original Price': Original_Price,'Pattern': Pattern,
        'Rating': Rating,'Rating Count': Rating_Count,'Reviews': Reviews,
        'Sleeve': Sleeve,'Suitable For': Suitable_For}

        input_df = pd.DataFrame([input_dict])
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            if output[0]==2:
              result = "High"
            if output[0]==1:
              result = 'Medium'

            if output[0]==0:
              result = "low"
            st.success('Discount rate is  {}'.format(result))
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
