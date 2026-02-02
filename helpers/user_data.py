import pandas as pd
import numpy as np


#
# Load scaler
#

import sys
sys.path.append("..")

from helpers.loaders import load_scaler
scaler = load_scaler()




def preprocess_user_data(gender, age, hypertension, heart_disease, weight_in_kg, height_in_m, smoking_status):
    """
    Receives data in raw format (as provided by the user),
    and returns the data ready for model predictions.

    smoking_status:
    - Possible values: "Unknown", "formerly smoked", "never smoked", "smokes"
    
    gender:
    - Possible values: 0 (male), 1 (female)

    """

    raw_data = {
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'weight_in_kg': weight_in_kg,
        'height_in_m': height_in_m,
        'smoking_status': smoking_status,
    }


    # Smoking encoding
    smoking_categories = ["formerly smoked", "never smoked", "smokes"]
    smoking_data = {f"smoking_{cat}": 0.0 for cat in smoking_categories}

    status = raw_data.get("smoking_status")
    if status != "Unknown" and status in smoking_categories:
        smoking_data[f"smoking_{status}"] = 1.0

    # Age encoding
    bins = [0, 17, 29, 44, 59, 74, np.inf]
    labels = ['0-17', '18-29', '30-44', '45-59', '60-74', '75+']

    age_group = pd.cut(
        [raw_data['age']],
        bins=bins,
        labels=labels
    )[0]

    age_data = {f"age_group_{label}": 0.0 for label in labels if label != '0-17'}
    if not pd.isna(age_group) and age_group != '0-17':
        age_data[f"age_group_{age_group}"] = 1.0


    # Calculate BMI (from weight and height)
    # bmi = weight_in_kg / (height_in_m * height_in_m)
    #
    w = raw_data.get("weight_in_kg")
    h = raw_data.get("height_in_m")
    bmi = w / (h * h)

    # Scale BMI
    bmi_scaled = scaler.transform([[bmi]])[0][0]

    # Merge all
    processed_data = {
        'gender': raw_data['gender'],
        'hypertension': raw_data['hypertension'],
        'heart_disease': raw_data['heart_disease'],
        'bmi': bmi_scaled,
        **smoking_data,
        **age_data
    }

    return processed_data
