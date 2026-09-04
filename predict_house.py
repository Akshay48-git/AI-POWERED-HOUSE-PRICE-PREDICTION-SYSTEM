import pandas as pd
import joblib

# Load trained model
gb = joblib.load("house_model.pkl")
print(type(gb))



#Load_training columns
train_columns = joblib.load("train_columns.pkl")
#user input
city = input("Enter City( Hyderabad,Bangalore,Mumbai,Delhi): ")
locality = input("Enter Locality: ")
property_type = input("Enter Property Type (Apartment/Villa): ")
bhk = int(input("Enter BHK: "))
bathrooms = int(input("Enter Bathrooms: "))
built_up_area = float(input("Enter Built-up Area (sq.ft): "))
carpet_area = float(input("Enter Carpet Area (sq.ft): "))
furnishing_status = input("Enter Furnishing Status (Fully Furnished/Semi Furnished/Unfurnished): ")
property_age = int(input("Enter Property Age (Years): "))
parking_spaces = int(input("Enter Parking Spaces: "))
distance_to_metro_km = float(input("Distance to Metro (km): "))
distance_to_city_center_km = float(input("Distance to City Center (km): "))
nearby_schools = int(input("Nearby Schools: "))
nearby_hospitals = int(input("Nearby Hospitals: "))
# house prediction
new_house = pd.DataFrame({
    "city": [city],
    "locality": [locality],
    "property_type": [property_type],
    "bhk": [bhk],
    "bathrooms": [bathrooms],
    "built_up_area": [built_up_area],
    "carpet_area": [carpet_area],
    "furnishing_status": [furnishing_status],
    "property_age": [property_age],
    "parking_spaces": [parking_spaces],
    "distance_to_metro_km": [distance_to_metro_km],
    "distance_to_city_center_km": [distance_to_city_center_km],
    "nearby_schools": [nearby_schools],
    "nearby_hospitals": [nearby_hospitals]
})
new_house = pd.get_dummies(new_house)

new_house = new_house.reindex(columns=train_columns, fill_value=0)

predicted_price = gb.predict(new_house)


print(f"\nEstimated House Price: ₹ {predicted_price[0]:,.2f} Lakhs")