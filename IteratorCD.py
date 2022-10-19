"""
Iterator Module is designed to automate the generation of Graphs for both spektrum and heat CD Data based on an excel sheet
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import os
import glob
import SpectrumCD as spec
import HeatCD as heat
import HPLC as hplc

class IteratorCD:

    #set base path independant of device:
    path = str(pathlib.Path().absolute()) #/home/user/Analyzer_Hagn_Data_package

    @staticmethod
    def help():
        print("""
        Functions:
        
        CD_data_iterator() --> takes in a table which is then processed by the algorithm (see example in the package)
                               
        CD-iterator_advanced() --> requires "input" folder, pints out graphs in designated output folder
                                   requires: path to output folder (will be created in directory automatically)
        """)

    def __init__(self, df_new):
        self.df_new = df_new


    def CD_data_iterator(self):
        i = 0
        while i != int(len(self.index-1)):
            if self.iloc[i, 1].lower() == "h":
                df = pd.read_fwf(str(self.iloc[i, 0]) + ".txt")
                df_inter1 = heat.HeatPlot(df)
                df_inter2 = df_inter1.normalize_heat()
                heat.HeatPlot.plot_heat(df_inter2, set_show=0, set_name=str(self.iloc[i, 3]), set_directory=str(self.iloc[i, 4]), set_color=str(self.iloc[i, 5]))

            elif self.iloc[i, 1].lower() == "s":
                df = pd.read_fwf(str(self.iloc[i, 0]) + ".txt")
                df_inter1 = spec.SpectrumPlot(df)
                df_inter2 = df_inter1.clean_spectrum()
                spec.SpectrumPlot.spectrum_plot(df_inter2, set_show=0, set_name=str(self.iloc[i, 3]), set_directory=str(self.iloc[i, 4]), set_color=str(self.iloc[i, 5]))
            else:
                print("Index " + str(i) + " in the table could not be printed")
            i = i+1
    @staticmethod
    def CD_iterator_advanced(set_target_directory = str(path) + "/output_graphs/"):

        #chack and create new target directory if input given
        if os.path.exists(set_target_directory):
            print("Path already exists, skip folder creation...")
        else:
            path = os.mkdir(set_target_directory)
            print("Path " + str(set_target_directory) + " is created...")
            # read files from target folder "input"

        txt_files = glob.glob(str(path) + "/input/*.txt")
        # decipher txt data and create dataframe with parameters based on the name tags
        k = 0
        array_txt = []
        while k <= int(len(txt_files)-1):
            df_txt = str(txt_files[k]).split(";")
            array_txt.append(df_txt)
            k = k+1
        # print(array_txt)

        # determine graph color, since two graphs belong to each other and appear next to each other, duplicate color in table
        color_array = ["red", "blue", "green", "yellow", "orange", "red", "blue", "green", "yellow", "orange"]
        color_setter = []
        h = 0
        while h <= ((len(array_txt) - 1) / 2):
            inter = color_array[h]
            color_setter.append(inter)
            color_setter.append(inter)
            h = h+1
        # print(color_setter)

        # process data (needs modification) and color swapper in while loop
        i = 0
        while i <= int(len(array_txt)-1):
            #get inner items, array in array) (extract data from array_txt file)
            intermediate_info_array = array_txt[i]
            # i_date = intermediate_info_array[0]
            i_type = intermediate_info_array[1]
            i_name = intermediate_info_array[2]

            if i_type.lower() == "h":
                df = pd.read_fwf(str(txt_files[i]))
                df_inter1 = heat.HeatPlot(df)
                df_inter2 = df_inter1.normalize_heat()
                heat.HeatPlot.plot_heat(df_inter2, set_show=0, set_name=str(i_name), set_directory=str(set_target_directory), set_color=str(color_setter[i]))
                print("Printing " + str(txt_files[i]) + ".")

            elif i_type.lower() == "s":
                df = pd.read_fwf(txt_files[i])
                df_inter1 = spec.SpectrumPlot(df)
                df_inter2 = df_inter1.clean_spectrum()
                spec.SpectrumPlot.spectrum_plot(df_inter2, set_show=0, set_name=str(i_name), set_directory=str(set_target_directory), set_color=str(color_setter[i]))
                print("Printing " + str(txt_files[i]) + ".")

            elif i_type.lower() == "s200a":
                df = pd.read_fwf(txt_files[i])
                df_inter1 = hplc.HPLC(df)
                df_inter2 = df_inter1.clean_graph()
                df_interfrac = df_inter1.clean_frac()
                if df_interfrac.empty == True:
                    set_frac=0
                else:
                    set_frac= df_interfrac

                hplc.HPLC.hplc_plot(df_inter2, df_frac= set_frac,set_show=0, set_name=str(i_name),set_directory=str(set_target_directory), set_color=str(color_setter[i]))
                print("Printing " + str(txt_files[i]) + ".")
            else:
                print("Index " + str(i) + " in the table could not be printed")
            i = i+1



# IteratorCD.CD_iterator_advanced(set_target_directory="/home/Freiherr/outputs/")

# data = pd.read_csv(r"/home/Freiherr/graphs/OEP24 A ATP.csv")
# IteratorCD.CD_data_iterator(data)
