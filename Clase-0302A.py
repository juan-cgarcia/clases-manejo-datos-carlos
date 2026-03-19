from numpy import dtype
import pandas as pd

def main() -> None:
    #air_quality_data= pd.read_csv("00-raw-data/Calidad-aire/contaminantes_2024.csv",
    #skiprows=9 # recorrer lineas en mi visualización de archivo 
    #)
    
    #air_quality_data["id_station"] = air_quality_data["id_station"].astype("category") #toma la columna de mis datos y lo cambia a category
    #air_quality_data["date"] = pd.to_datetime(air_quality_data["date"], format = "ISO8601") #cambie el tipo de dato al correcto 
    
    #SEGUNDA MANERA DE HACERLO 

    dtypes={
        "id_station": "category",
        "id_parameter":"category",
        "value": "float32", #32 porque mis mediciones tienen a lo más 2 numeros 
        "unit": "uint8"
    }

    air_quality_data = pd.read_csv(
        "00-raw-data/Calidad-aire/contaminantes_2024.csv",
        dtype=dtypes,
        parse_dates = ["date"],
        skiprows=9
    
    )

    print(air_quality_data.info()) #Que columnas tengo, cuantos valores y memoria 
    print(air_quality_data.head())


if __name__ == "__main__" :
    main()