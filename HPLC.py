import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib
# data needs to be ugf8 --> is ugf16 by default, not readable


class HPLC:

    # set base path independant of device:
    path = str(pathlib.Path().absolute()) # /home/user/Analyzer_Hagn_Data_package

    @staticmethod
    def help():
        print("""
        Functions of the script:
        
        clean_graph(df = fwf one column dataframe with \\t separation)
           --> outputs primary table for protein UV signal to volume (buffer flow through column)
           
        clean_frac(df = same as before)
           --> outputs secondary table with all the fractions taken at each increment during chromatography
        
        hplc_plot(df = both prior dataframes are taken automatically (Iterator is advisable to use))
           --> outputs chromatogram in set_directory folder
        """)

    def __init__(self, df3):
        self.df3 = df3

    def clean_graph(self):
        # primary table for UV signal volume graph
        sum_array_hplc = []
        i = 2
        while i != int(len(self.df3.index)):
            intermediate0_hplc = str(self.df3.iloc[i, 0]).split("\t")[0]
            intermediate1_hplc = str(self.df3.iloc[i, 0]).split("\t")[1]
            sum_array_hplc.append([intermediate0_hplc, intermediate1_hplc])
            i = i + 1
        df_hplc_clean = pd.DataFrame(sum_array_hplc, dtype=np.float64, columns=["Volume", "UV/Vis signal"])

        if df_hplc_clean.Volume[df_hplc_clean.Volume > 30.0].any() == True:
            new_cutoff = df_hplc_clean.Volume[df_hplc_clean.Volume > 30.0].min()
            inter = df_hplc_clean["Volume"].where(df_hplc_clean["Volume"] == new_cutoff).dropna(axis="rows").index[0]
            df_inter_hplc_clean = df_hplc_clean.truncate(0, inter, axis="rows")
            df_hplc_clean = df_inter_hplc_clean
            return df_hplc_clean
        else:
            return df_hplc_clean

    def clean_frac(self, txt_name = "unnamed"):
        # generate secondary table for fractions
        if len(self.df3.iloc[0,0].split("\t")) >= 12:
            j = 2
            sum_fractions_hplc = []
            while self.df3.iloc[j, 0].split("\t")[11] != '"Waste"':
                intermediate0_frac = str(self.df3.iloc[j, 0]).split("\t")[10]
                intermediate1_frac = str(self.df3.iloc[j, 0]).split("\t")[11]
                sum_fractions_hplc.append([intermediate0_frac, intermediate1_frac])
                j = j+1
            df_frac_clean = pd.DataFrame(sum_fractions_hplc, columns=["Volume", "Fraction number"])
            return df_frac_clean
        else:
            df_frac_clean = pd.DataFrame(["nothing"])
            print("For graph " + str(txt_name) + ", fractions could not be printed!")
            return df_frac_clean



    def hplc_plot(self, df_frac = 0, set_show=1, set_name="protein", set_directory= str(path) + "/output_graphs/", set_color="r"):
        plt.figure(figsize=(25, 10))
        ax2 = plt.subplot(1, 1, 1)
        ax2.scatter(data=self, x="Volume", y="UV/Vis signal", color=str(set_color))
        ax2.set_ylabel("UV/Vis signal [mAU]", fontsize=15)
        ax2.set_xlabel("Volume [ml]", fontsize=15)
        ax2.set_title("Chromatogram of " + str(set_name), fontsize=25)
        plt.scatter(x=0, y = -20, color="white")
        # generation of fraction markings if given --> != 0
        if df_frac.iloc[0,0] != "nothing":
            plt.text(0.0, -20.0, "Fractions:", fontsize=15)
            p=0
            while p <= (len(df_frac.index)-1):
                plt.text(float(df_frac.iloc[p,0]), -20.0, df_frac.iloc[p,1])
                p = p+1

        if set_show != 0:
            plt.show()
        else:
            plt.savefig(str(set_directory) + str(set_name) + "_hplc.png", dpi=400,bbox_inches="tight")