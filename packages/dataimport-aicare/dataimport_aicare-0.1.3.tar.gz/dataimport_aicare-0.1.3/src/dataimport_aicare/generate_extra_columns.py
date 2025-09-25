import pandas as pd
from .data_loading import import_aicare
from .data_preprocessing import calculate_survival_time_multiregistry
import argparse

def getTumors(datapath:str, entity:str) -> pd.DataFrame:
    data = import_aicare(datapath, entity, registry="all")
    inputData = data["patient"].merge(data["tumor"].drop(columns=["Register_ID_FK", "Patient_ID_FK"]),
                                on="Patient_ID_unique")
    inputData["survival_time"] = calculate_survival_time_multiregistry(inputData, registry_col="Register_ID_FK", diag_col="Diagnosedatum", vit_col="Datum_Vitalstatus",
                                                                       deceased_col="Verstorben", days_diag_to_death_col="Anzahl_Tage_Diagnose_Tod", 
                                                                       months_diag_to_censorship_col="Anzahl_Monate_Diagnose_Zensierung")
    
    return inputData

def get_cols(datapath):
    
    allTumors = []
    for entity in "non_hodgkin_lymphoma", "lung", "thyroid", "breast" :
        tumor = getTumors(datapath, entity)
        allTumors.append(tumor)


    completeFrame = pd.concat([df for df in allTumors if not df.empty],axis=0)

    relevant_cols = completeFrame.loc[:,["Register_ID_FK", "Patient_ID", "Tumor_ID", "Primaertumor_ICD", "survival_time", "histo_group", "TNM_Version", "TNM_T", "TNM_N", "TNM_M", "UICC", "Ann_Arbor"]]
    
    return relevant_cols

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, default="none", help="Path of AI-CARE dataset")
    
    args = parser.parse_args()

    relevant_cols = get_cols(args.dir)
    relevant_cols.to_csv(f"{args.dir}tumor_extra_columns.csv",index=False)
    tumors = pd.read_csv(f"{args.dir}tumor.csv")
    strange_tumors = tumors[~tumors["Tumor_ID"].isin(relevant_cols["Tumor_ID"])]
    strange_tumors.to_csv(f"{args.dir}strange_tumors_2.csv", index=False)



if __name__ == "__main__":
    main()
    
    