import pandas as pd
import numpy as np

def generate_customer_data(num_customers):
    data = {
        'CustomerID': np.arange(1, num_customers + 1),
        'FirstName': None,
        'LastName': np.random.choice(['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Rodriguez','Martinez','Hernandez','Lopez','Gonzalez','Wilson','Anderson','Thomas','Taylor','Moore','Jackson','Martin'], num_customers),
        'Gender': np.random.choice(['Male', 'Female'], num_customers),
        'Age': np.random.randint(18, 65, num_customers),
        'DateOfBirth': pd.date_range('1960-01-01', '2005-12-31', periods=num_customers).strftime('%Y-%m-%d'),
        'Email': ['example{}@domain.com'.format(i) for i in range(1, num_customers + 1)],
        'Phone': np.random.choice(['123-456-7890', '987-654-3210', '555-123-4567'], num_customers),
        'AddressLine1': ['Street {}'.format(i) for i in range(1, num_customers + 1)],
        'AddressLine2': ['Apt {}'.format(i) if i % 2 == 0 else '' for i in range(1, num_customers + 1)],
        'City': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'], num_customers),
        'State': np.random.choice(['NY', 'CA', 'IL', 'TX', 'PA'], num_customers),
        'ZipCode': np.random.randint(10000, 99999, num_customers),
        'Country': np.random.choice(['USA', 'Canada', 'UK', 'Australia', 'Germany'], num_customers),
        'Nationality': np.random.choice(['American', 'Canadian', 'British', 'Australian', 'German'], num_customers),
        'EducationLevel': np.random.choice(['High School', 'College', 'Bachelor', 'Master', 'PhD'], num_customers),
        'Occupation': np.random.choice(['Student', 'Professional', 'Manager', 'Entrepreneur', 'Retired'], num_customers),
        'Income': np.random.randint(20000, 150000, num_customers),
        'MaritalStatus': np.random.choice(['Single', 'Married', 'Divorced', 'Widowed'], num_customers),
        'NumberOfChildren': np.random.randint(0, 4, num_customers),
        'LanguagePreference': np.random.choice(['English', 'Spanish', 'French', 'German', 'Chinese'], num_customers),
        'PreferredContactMethod': np.random.choice(['Email', 'Phone', 'SMS', 'Mail'], num_customers),
        'LastPurchaseDate': pd.date_range('2020-01-01', '2022-12-31', periods=num_customers).strftime('%Y-%m-%d'),
        'TotalPurchaseAmount': np.random.uniform(0, 5000, num_customers),
        'LastLoginDate': pd.date_range('2022-01-01', '2022-12-31', periods=num_customers).strftime('%Y-%m-%d'),
        'AccountCreateDate': pd.date_range('2015-01-01', '2022-12-31', periods=num_customers).strftime('%Y-%m-%d'),
        'AccountType': np.random.choice(['Basic', 'Premium', 'VIP'], num_customers),
        'SubscriptionStatus': np.random.choice(['Active', 'Inactive'], num_customers),
        'PreferredPaymentMethod': np.random.choice(['Credit Card', 'PayPal', 'Bank Transfer'], num_customers),
        'CreditScore': np.random.randint(300, 850, num_customers),
        'CreditLimit': np.random.randint(1000, 10000, num_customers),
        'MembershipTier': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], num_customers),
        'LoyaltyPoints': np.random.randint(0, 10000, num_customers),
        'ReferralSource': np.random.choice(['Website', 'Friend', 'Advertisement', 'Social Media'], num_customers),
        'PurchaseFrequency': np.random.choice(['Low', 'Medium', 'High'], num_customers),
        'FavoriteProductCategory': np.random.choice(['Electronics', 'Clothing', 'Home Decor', 'Sports', 'Books'], num_customers),
        'PreferredStoreLocation': np.random.choice(['City Center', 'Shopping Mall', 'Suburb', 'Online'], num_customers),
        'TravelFrequency': np.random.choice(['None', 'Occasional', 'Frequent'], num_customers),
        'VehicleType': np.random.choice(['Car', 'Motorcycle', 'Bicycle'], num_customers),
        'InsuranceProvider': np.random.choice(['Company A', 'Company B', 'Company C'], num_customers),
        'HealthCondition': np.random.choice(['Good', 'Fair', 'Poor'], num_customers),
        'SocialMediaUsage': np.random.choice(['Low', 'Medium', 'High'], num_customers),
        'Interests': np.random.choice(['Sports', 'Music', 'Reading', 'Travel', 'Cooking'], num_customers),
        'SportsPreference': np.random.choice(['Football', 'Basketball', 'Tennis', 'Soccer', 'Golf'], num_customers),
        'MusicPreference': np.random.choice(['Pop', 'Rock', 'Hip Hop', 'Classical', 'Country'], num_customers)
    }

    data['FirstName'] = choose_first_name(data['Gender'], num_customers)

    return pd.DataFrame(data)

def choose_first_name(gender, num_customers):
    female_list = ['Emma','Olivia','Ava','Isabella','Sophia','Mia','Charlotte','Amelia','Harper','Evelyn','Abigail','Emily','Elizabeth','Mila','Ella','Avery','Sofia','Camila','Luna','Scarlett']
    male_list = ['Liam','Noah','William','James','Oliver','Benjamin','Elijah','Lucas','Henry','Alexander','Mason','Michael','Ethan','Daniel','Jacob','Logan','Jackson','Levi','Sebastian','Matthew']
    is_female = (gender == 'Female')
    name = np.where(is_female, np.random.choice(female_list, num_customers), np.random.choice(male_list, num_customers))
    return name

if __name__ == "__main__":
    num_customers = 1000
    df = generate_customer_data(num_customers)
    file_path = '.\\dataframe_generator\\data_file\\customer_demographics.csv'
    df.to_csv(file_path, index=False)
    print('Customer demographics file generated successfully.')
