import pandas as pd
import hydra

from hydra import utils

@hydra.main(config_path="../config", config_name="variable")
def process(config) -> None:
    
    ### Read csv 
    
    try:
        df_entreprise = pd.read_csv(config.datasets.data)
        print(f"df_entreprise === {df_entreprise}")

    except Exception as e:
        print(e)
    
def main():
    process()


if __name__ == "__main__":
    main()