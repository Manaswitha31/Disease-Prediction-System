from tkinter import *
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

#List of the symptoms is listed here in list l1.
list1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']
#List of Diseases is listed in list disease.
disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']
list2=[]
for l in range(0,len(list1)):
    list2.append(0)

dfrm=pd.read_csv("Prototype.csv")

#Replace the values in the imported file by pandas by the inbuilt function replace in pandas.

dfrm.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

#check the df 
#print(df.head())

x= dfrm[list1]

#print(X)

y = dfrm[["prognosis"]]
np.ravel(y)

#print(y)

#Read a csv named Testing.csv

tr_data=pd.read_csv("Prototype-1.csv")

#Use replace method in pandas.

tr_data.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

xtst= tr_data[list1]
ytst = tr_data[["prognosis"]]

np.ravel(ytst)

def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    cf = RandomForestClassifier()
    cf = cf.fit(x,np.ravel(y))
    # calculating accuracy 
    from sklearn.metrics import accuracy_score
    y_pred=cf.predict(xtst)
    print(accuracy_score(ytst, y_pred))
    print(accuracy_score(ytst, y_pred,normalize=False))
    
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for i in range(0,len(list1)):
        for j in psymptoms:
            if(j==list1[i]):
                list2[i]=1
    itst = [list2]
    prd = cf.predict(itst)
    prdd=prd[0]
    h='no'
    for a in range(0,len(disease)):
        if(prdd == a):
            h='yes'
            break
    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")
        
# GUI stuff..............................................................................
        
root = Tk()
root.configure(background='#e5cbf5')

Symptom1 = StringVar()
Symptom1.set("Select Here")

Symptom2 = StringVar()
Symptom2.set("Select Here")

Symptom3 = StringVar()
Symptom3.set("Select Here")

Symptom4 = StringVar()
Symptom4.set("Select Here")

Symptom5 = StringVar()
Symptom5.set("Select Here")

Name = StringVar()

w2 = Label(root, justify=LEFT, text="Disease Predictor System", fg="black", bg="white")
w2.config(font=("Times",36,"bold italic"))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb = Label(root, text="Name of the Patient", fg="White", bg="black")
NameLb.config(font=("Times",15,"bold italic"))
NameLb.grid(row=6, column=0, pady=15, sticky=W)

S1 = Label(root, text="Symptom 1", fg="white", bg="purple")
S1.config(font=("Times",15,"bold italic"))
S1.grid(row=7, column=0, pady=10, sticky=W)

S2 = Label(root, text="Symptom 2", fg="White", bg="Purple")
S2.config(font=("Times",15,"bold italic"))
S2.grid(row=8, column=0, pady=10, sticky=W)

S3 = Label(root, text="Symptom 3", fg="White",bg="purple")
S3.config(font=("Times",15,"bold italic"))
S3.grid(row=9, column=0, pady=10, sticky=W)

S4 = Label(root, text="Symptom 4", fg="white", bg="purple")
S4.config(font=("Times",15,"bold italic"))
S4.grid(row=10, column=0, pady=10, sticky=W)

S5 = Label(root, text="Symptom 5", fg="white", bg="purple")
S5.config(font=("Times",15,"bold italic"))
S5.grid(row=11, column=0, pady=10, sticky=W)

ranf = Label(root, text="Predicted Disease", fg="white", bg="black")
ranf.config(font=("Times",15,"bold italic"))
ranf.grid(row=19, column=0, pady=10, sticky=W)

OPTIONS = sorted(list1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

S1o = OptionMenu(root, Symptom1,*OPTIONS)
S1o.grid(row=7, column=1)

S2o = OptionMenu(root, Symptom2,*OPTIONS)
S2o.grid(row=8, column=1)

S3o = OptionMenu(root, Symptom3,*OPTIONS)
S3o.grid(row=9, column=1)

S4o = OptionMenu(root, Symptom4,*OPTIONS)
S4o.grid(row=10, column=1)

S5o = OptionMenu(root, Symptom5,*OPTIONS)
S5o.grid(row=11, column=1)

lr = Button(root, text="Predict disease risk", command=randomforest,bg="#2b2b2b",fg="white")
lr.config(font=("Times",15,"bold italic"))
lr.grid(row=10, column=3,padx=10)

t1 = Text(root, height=1, width=40,bg="black",fg="white")
t1.config(font=("Times",15,"bold italic"))
t1.grid(row=19, column=1 , padx=10)

root.mainloop()

