"""
All the different executions you can perform are listed here
"""
import pandas as pd
import numpy as np
import IteratorCD as iter
import SpectrumCD as spec
import HPLC as hplc
import HeatCD as heat


while True:
    #innitiation of programm
    print("""
    Data Analyzer for HPLC and CD data
    --> please input the given code string in brackets for the desired mode
    
    Single file analysis (.txt format required)
    1. HPLC: format table (ft_hplc), plot chromatogram (pg_hplc), help (hplc_help)
    2. CD spectrum: format table (ft_spec), plot spectrum (pg_spec), help (spec_help)
    3: CD heat protein denaturation: format table (ft_heat), plot graph (pg_heat), help (heat_help)
    
    Multiple file analysis 
    1. Table supported data analysis (compare added txt file for more info, format: .csv) (tb_iter)
    2. Folder based data analysis (please drop the files in the included "input" folder) (fb_iter)
    
    End program (quit)
    
    """)

    initial_input = input("please select the mode: ")

    if str(initial_input).lower() == "quit":
        print("Program is terminated")
        break

    #HPLC
    elif str(initial_input).lower() == "hplc_help":
        hplc.HPLC.help()

    elif str(initial_input).lower() == "ft_hplc":
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        df1 = pd.read_fwf(str(input1))
        df2 = hplc.HPLC(df1)
        normalized_table = df2.clean_graph()
        normalize_table.to_csv(input2)

        frac_ask = output("Do you want to create fraction file? (yes/no) ")
        if frac_ask.lower() == yes:
            input3 = input("Set the name of the Fraction file: ")
            frac_norm = df2.clean_frac()
            frac_norm.to_csv(input3)

        print("Task finished!")

    elif str(initial_input).lower() == "pg_hplc":
        fraction = 0
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        df1 = pd.read_fwf(str(input1))
        df2 = hplc.HPLC(df1)
        normalized_table = df2.clean_graph()

        frac_ask = output("Do you want to add Fractions? (yes/no) ")
        if frac_ask.lower() == yes:
            fraction = 1

        hplc.HPLC.hplc_plot(self, df_frac = fraction, set_show=1, set_name=input2)
        print("Task finished!")

    #CD_spec
    elif str(initial_input).lower() == "spec_help":
        spec.SpectrumPlot.help()

    elif str(initial_input).lower() == "ft_spec":
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        df1 = pd.read_fwf(str(input1))
        df2 = spec.SpectrumPlot(df1)
        normalized_table = df2.clean_spectrum()
        normalize_table.to_csv(input2)
        print("Task finished!")

    elif str(initial_input).lower() == "pg_spec":
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        df1 = pd.read_fwf(str(input1))
        df2 = spec.SpectrumPlot(df1)
        df3 = df2.clean_spectrum()
        spec.SpectrumPlot.spectrum_plot(df3, set_show=0, set_name=str(input2))
        print("Task finished!")

    #CD_heat
    elif str(initial_input).lower() == "pg_heat":
        heat.HeatPlot.help()

    elif str(initial_input).lower() == "ft_heat":
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        df1 = pd.read_fwf(str(input1))
        df2 = heat.HeatPlot(df1)
        df3= df2.normalize_heat()
        heat.HeatPlot.plot_heat(df3, set_show=0, set_name=str(input2))
        print("Task finished!")

    elif str(initial_input).lower() == "ft_heat":
        input1 = input("Path of Text file: ")
        input2 = input("Set target directory with name: ")
        df1 = pd.read_fwf(str(input1))
        df2 = heat.HeatPlot(df1)
        normalized_table = df2.normalize_heat()
        normalize_table.to_csv(input2)
        print("Task finished!")

    #Iterator
    elif str(initial_input).lower() == "tb_iter":
        input_csv = input("Please type in the path of your .csv table: ")
        data = pd.read_csv(str(input_csv))
        iter.IteratorCD.CD_data_iterator(data)
        print("Task finished!")

    elif str(initial_input).lower() == "fb_iter":
        input_request = input("Name absolute target directory path: ")
        iter.IteratorCD.CD_iterator_advanced(set_target_directory=str(input_request))
        print("Task finished!")

    else:
        print("Invalid command, please try again...")
