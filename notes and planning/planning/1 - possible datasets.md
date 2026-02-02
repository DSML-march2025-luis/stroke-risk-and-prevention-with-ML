

# Possible datasets



## Option 1 - Kaggle

- 5k datapoints
- Most features are very user friendly (ie. most people have the knowledge to answer to those questions). Some of them are actionable (eg. BMI, smoking status).

Link:
- Kaggle: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/


Limitations: 
- Origin of the data is not really clear (https://chatgpt.com/share/6851916d-f2dc-8003-874c-9b0494dcb164)



## Option 2a - NHANES:

- https://chatgpt.com/share/68519534-4c38-8003-b229-4c06970ff91b
- Which cycle to use:
    - The latest cycle may not be fully ready (some data components are still undergoing processing and quality assessment), and it may not be reliable to merge with other cycles because of design changes.
    - **"NHANES 2017-March 2020 Pre-pandemic"** may be the best option, specially if at any point I want to merge it with previous cycles to get more datapoints.

Links:
- All NHANES Cycles and datasets: https://wwwn.cdc.gov/nchs/nhanes/default.aspx
- NHANES 2017-March 2020 Pre-pandemic: https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2017-2020


Interesting things:
- It is very well documented (inc. how data was obtained)
- Includes a lot of datapoints (~8k entries for each cycle)
- Includes if the person suffered a stroke and also at which age it happened
- Features: age, gender, weight, smoking habits, drinking habits, etc...
- Labels: If the person had a stroke at any point in the past + at what age they had a stroke


Limitations:
- **Reverse causation bias**. How to predict the factors that led to a stroke (rather than the factors post-stroke)
    - ie. after a stroke, a person may have changed their drinking and smoking habits.



## Option 2b - NHANES + mortality data

Option 1: use older NHANES datasets + mortality data
- https://chatgpt.com/share/68543666-a3ac-8003-a38d-4d4039260887

Limitations: 
- Does not include info about non-fatal strokes.



## Option 2c - NHEFS (NHANES I Epidemiologic Follow-up Study)

- it's a longitudinal dataset based on participants from the NHANES I survey (1971–1975).
- 14k participants, all aged 25–74 at baseline.
- 13k were eligible for follow-up.
- 12k were successfully traced and interviewed in at least one follow-up wave (1982, 1986, 1987, or 1992).

- Ninety-six percent of the study population has been successfully traced at some point through the 1992 follow-up. 
- Contains data on:
    - Lifestyle (smoking, drinking, diet)
    - Health conditions
    - Hospitalizations and mortality
    - Stroke and other cardiovascular outcomes


Limitations:
- Documentation is not great (specially compared with the recent nhanes cycles, which are very well documented)
- Would need to mix data from quite a few different files and sources
- Also, data is in txt, to parse, see here: https://chatgpt.com/c/6856ad6e-ba94-8003-a410-b8c6d3d1c1d6
- It is a bit old (Data from 1971–1987). Lifestyles, medical care, and stroke risk factors may differ from today; risk patterns (e.g. smoking prevalence, obesity rates) have changed.
- It is not as comprehensive as the most recent cycles of nhanes (for example, in nhanes I there's only a field for serum cholesterol, not a breakdown in LDL and HDL)
- Main follow-up from 1982–1984 (7–13 years after baseline).
    - This can actually be good if i want to predict risk in the coming 10 years.

Things to consider:
- From the 14k participants, it seems there's stroke studies only on 9k ("~9,800–9,900 people used in stroke studies are the subset with complete and relevant data, free of stroke at baseline, and trackable over time to observe incident strokes."). ie. it seems that there's no follow up on people that already had a stroke by the time of the first interview.
    - Check that in detail, as it make add bias / **model may not be suitable to predict risk in people that already had a stroke**.


Links:
- NHANES I (1971-1974): https://wwwn.cdc.gov/nchs/nhanes/nhanes1/default.aspx
- NHEFS (NHANES I Epidemiologic Follow-up Study): https://wwwn.cdc.gov/nchs/nhanes/nhefs/default.aspx



## Option 3 - Framingham Heart Study (Teaching Dataset) 

- publicly available (requires to apply but the process usually takes a couple of days)
- includes data on approximately 4,240–4,434 participants, with 16 variables (including age, gender, smoking, blood pressure, BMI, glucose, prevalent stroke, and follow-up outcomes) 
- includes three clinical examination and 20 year follow-up data based on a subset of the original Framingham cohort participants.

Limitations:
- It is a teaching dataset, not intended for clinical applications ("Users are cautioned that teaching datasets are completely unsuitable for publication purposes since specific statistical measures were used to create anonymous versions")
    - Note: 
        - Application for the full dataset doesn't seem to be complex. 
        - Can also apply to get the full dataset once MVP is ready.


Links:
- Application: https://biolincc.nhlbi.nih.gov/teaching/
- Documentation: https://biolincc.nhlbi.nih.gov/media/teachingstudies/FHS_Teaching_Longitudinal_Data_Documentation_2021a.pdf?link_time=2025-06-21_05:23:00.117024




## NHANES vs. NHEFS vs. Framingham

https://chatgpt.com/share/68566ff7-9f0c-8003-85d0-8e82af32c5b4



