# Generation 1 of the heat and spectrum algorithm for Circular dichroism data


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib


class HeatPlot:

    # set base path independant of device:
    path = str(pathlib.Path().absolute()) # /home/user/Analyzer_Hagn_Data_package

    @staticmethod
    def help():
        print("""
          Functions of the script: 
          
          normalize_heat(df = fwf one column dataframe with \\t separation)
            --> returns normalized CD values in correlation to the temperature (DataFrame)
            
          plot_heat --> dataframe from the prior normalize_heat method
         
          """)

    def __init__(self, df):
        self.df = df

    def normalize_heat(self):
        sum_array = []
        i = 15
        while self.df.iloc[i, 0] != "##### Extended Information":
            intermediate = str(self.df.iloc[i, 0]).split("\t")
            sum_array.append(intermediate)
            i = i + 1
        df_heat_clean = pd.DataFrame(sum_array, dtype=np.float64, columns=["temperature", "CD_value", "voltage"])
        df_heat_clean = df_heat_clean.drop(columns=["voltage"])

        df_heatmax = np.array(df_heat_clean.idxmax()) # start of Normalization --> search min and max value
        df_heatmin = np.array(df_heat_clean.idxmin())

        min_heat = df_heat_clean.iloc[df_heatmin[1], 1]
        max_heat = df_heat_clean.iloc[df_heatmax[1], 1]

        # generate normalized column
        base_cell = []
        i = 0
        while i != len(df_heat_clean.index):
            inter_value_norm = (((df_heat_clean.iloc[i, 1]) - max_heat) / (max_heat - min_heat))
            base_cell.append(inter_value_norm)
            i = i + 1
        df_norm_heat = pd.DataFrame(base_cell, columns=["norm_heat"])
        df_norm_heat = df_norm_heat.abs()  # abs because we want absolute values

        # replace old CD_value with normalized heat values of CD as Nativity of protein (norm_heat)
        df_combine_heat = df_heat_clean.join(df_norm_heat)
        df_combine_heat = df_combine_heat.drop(columns=["CD_value"])
        return df_combine_heat


    def plot_heat(self, set_show=1, set_name="CD_heat", set_directory= str(path) + "/output_graphs/", set_color="r"):

        # generating temp50; searches the temperature where 50% of the protein is denaturated
        df_50 = self.loc[(self["norm_heat"] >= 0.45) & (self["norm_heat"] <= 0.55)]
        df_50_mean = df_50.mean()
        df_50_result_temp = (df_50_mean.iloc[1] * df_50_mean.iloc[0]) / 0.5
        temp50 = round(df_50_result_temp, 2)

        # plotting of the graph (singular, not multiple graphs in one figure)
        max_temp = 110
        plt.figure(figsize=(10, 10))
        ax1 = plt.subplot(1, 1, 1)
        ax1.scatter(data=self, x="temperature", y="norm_heat", color=str(set_color))
        ax1.set_xlabel("temperature [°C]", fontsize=15)
        ax1.set_ylabel("relative protein nativity", fontsize=15)
        x1, y1 = (temp50, temp50), (0.5, 0)  # first bracket is for the x values, second for the y brackets
        x2, y2 = (20, temp50), (0.5, 0.5)
        plt.plot(x1, y1, color="black", linestyle="--")
        plt.plot(x2, y2, color="black", linestyle="--")
        plt.scatter(temp50, 0.5, color="black")
        ax1.text(temp50 - 25, 0, "$T_{1/2}$ = " + str(temp50) + " °C", fontsize=15)
        ax1.set_title("Heat denaturation of " + str(set_name), fontsize=25)
        plt.xticks(np.arange(20, max_temp + 1, 10))
        plt.yticks(np.arange(0, 1 + 0.1, 0.1))

        if set_show != 0:
            plt.show()
        else:
            plt.savefig(str(set_directory)+str(set_name)+"_heat.png", dpi=400, bbox_inches="tight")