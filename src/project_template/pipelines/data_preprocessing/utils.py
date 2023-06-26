import pandas as pd
from sklearn.preprocessing import StandardScaler



# Change column names to lowercase and no special characters
# Define a function to remove spaces and parentheses from column names and convert them to lowercase
def grp_clean_column_name(column_name):
    cleaned_name = column_name.replace(' ', '_').replace('(', '').replace(')', '').lower()
    return cleaned_name





def grp_standardize(df, method):
    num = ['age', 'balance_euros', 'last_contact_day', 'last_contact_month', 'last_contact_duration', 'campaign', 'pdays', 'previous' ]
    categ = ['job','marital_status','education', 'contact', 'poutcome', 'credit', 'housing_loan', 'personal_loan']

    data = df.copy()
    data = data[num]
    scaler = method.fit(data)
    out = scaler.transform(data)
    out = pd.DataFrame(out, columns = data.columns).set_index(data.index)
    return out



def grp_feature_engineering(df):
    num = ['age', 'balance_euros', 'last_contact_day', 'last_contact_month', 'last_contact_duration', 'campaign', 'pdays', 'previous' ]
    categ = ['job','marital_status','education', 'contact', 'poutcome', 'credit', 'housing_loan', 'personal_loan']

    data = df.copy()

    data["credit"] = data["credit"].map({"no": 0, "yes":1})
    data["housing_loan"] = data["housing_loan"].map({"no": 0, "yes":1}) 
    data["personal_loan"] = data["personal_loan"].map({"no": 0, "yes":1}) 
    data["subscription"] = data["subscription"].map({1:1, 2:0})
    data["last_contact_month"] = data["last_contact_month"].map({'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12 })
    

 
    data.drop( 'poutcome', axis=1, inplace = True)
    df_temp = grp_standardize(data, method = StandardScaler())
    data[num] = df_temp
    
    data = pd.get_dummies(data, drop_first=True)
    
    return data


