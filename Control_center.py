"""
All the different executions you can perform are listed here
"""
import pandas as pd
import os
import IteratorCD as iter
import SpectrumCD as spec
import HPLC as hplc
import HeatCD as heat
import pathlib

# single method directory setter
def make_directory(set_target_directory):
    # check and create new target directory if input given
    if os.path.exists(set_target_directory):
        print("Path already exists, skip folder creation...")
    else:
        path = os.mkdir(set_target_directory)
        print("Path " + str(set_target_directory) + " is created...")
        # read files from target folder "input"

path_folder = str(pathlib.Path().absolute())

while True:
    # innitiation of programm
    print("""
    Data Analyzer for HPLC and CD data
    --> please input the given code string in brackets for the desired mode
    
    Single file analysis (.txt format required)
    1. HPLC: format table (ft_hplc), plot chromatogram (pg_hplc), help (hplc_help)
    2. CD spectrum: format table (ft_spec), plot spectrum (pg_spec), help (spec_help)
    3: CD heat protein denaturation: format table (ft_heat), plot graph (pg_heat), help (heat_help)
    
    Multiple file analysis 
    1. Table supported data analysis (compare added txt file for more info, format: .csv) (tb_iter)
    2. Folder based data analysis (please drop the files in the included "input_txt" folder) (fb_iter)
    --> help (iter_help)
    
    End program (quit)
    
    """)

    initial_input = input("please select the mode: ")

    if str(initial_input).lower() == "quit":
        print("Program is terminated")
        break

    # HPLC
    elif str(initial_input).lower() == "hplc_help":
        hplc.HPLC.help()

    elif str(initial_input).lower() == "ft_hplc":
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        input_wantmkdir = input("Do you want to export the file in a specific directory? (yes/no): ")
        if input_wantmkdir.lower() == "yes":
            input_mkdir = input("Write the absolute path of the target directory: ")
            make_directory(input_mkdir)
        else:
            input_mkdir = str(path_folder + "/output_tables")

        df1 = pd.read_fwf(str(input1))
        df2 = hplc.HPLC(df1)
        normalized_table = df2.clean_graph()
        normalized_table.to_csv(input_mkdir + "/" + input2 + ".csv")

        frac_ask = input("Do you want to create fraction file? (yes/no) ")
        if frac_ask.lower() == "yes":
            input3 = input("Set the name of the Fraction file: ")
            frac_norm = df2.clean_frac()
            frac_norm.to_csv(input3)

        print("Task finished!")

    elif str(initial_input).lower() == "pg_hplc":
        fraction = 0
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        input3 = input("Set the color (red, blue, green, yellow, etc.): ").lower()
        input_wantmkdir = input("Do you want to export the file in a specific directory? (yes/no): ")
        if input_wantmkdir.lower() == "yes":
            input_mkdir = input("Write the absolute path of the target directory: ")
            make_directory(input_mkdir)
        else:
            input_mkdir = str(path_folder + "/output_graphs")

        df1 = pd.read_fwf(str(input1))
        df2 = hplc.HPLC(df1)
        normalized_table = df2.clean_graph()

        frac_ask = input("Do you want to add Fractions? (yes/no) ")
        if frac_ask.lower() == "yes":
            fraction = 1

        hplc.HPLC.hplc_plot(normalized_table, df_frac=fraction, set_show=1, set_name=input2, set_color=input3, set_directory=input_mkdir)
        print("Task finished!")

    # CD_spec
    elif str(initial_input).lower() == "spec_help":
        spec.SpectrumPlot.help()

    elif str(initial_input).lower() == "ft_spec":
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        input_wantmkdir = input("Do you want to export the file in a specific directory? (yes/no): ")
        if input_wantmkdir.lower() == "yes":
            input_mkdir = input("Write the absolute path of the target directory: ")
            make_directory(input_mkdir)
        else:
            input_mkdir = str(path_folder + "/output_tables")

        df1 = pd.read_fwf(str(input1))
        df2 = spec.SpectrumPlot(df1)
        normalized_table = df2.clean_spectrum()
        normalized_table.to_csv(input_mkdir + "/" + input2 + ".csv")
        print("Task finished!")

    elif str(initial_input).lower() == "pg_spec":
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        input3 = input("Set the color (red, blue, green, yellow, etc.): ").lower()
        input_wantmkdir = input("Do you want to export the file in a specific directory? (yes/no): ")
        if input_wantmkdir.lower() == "yes":
            input_mkdir = input("Write the absolute path of the target directory: ")
            make_directory(input_mkdir)
        else:
            input_mkdir = str(path_folder + "/output_graphs")

        df1 = pd.read_fwf(str(input1))
        df2 = spec.SpectrumPlot(df1)
        df3 = df2.clean_spectrum()
        spec.SpectrumPlot.spectrum_plot(df3, set_show=0, set_name=str(input2), set_color=input3, set_directory=input_mkdir)
        print("Task finished!")

    # CD_heat
    elif str(initial_input).lower() == "heat_help":
        heat.HeatPlot.help()

    elif str(initial_input).lower() == "ft_heat":
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        input_wantmkdir = input("Do you want to export the file in a specific directory? (yes/no): ")
        if input_wantmkdir.lower() == "yes":
            input_mkdir = input("Write the absolute path of the target directory: ")
            make_directory(input_mkdir)
        else:
            input_mkdir = str(path_folder + "/output_tables")

        df1 = pd.read_fwf(str(input1))
        df2 = heat.HeatPlot(df1)
        normalized_table = df2.normalize_heat()
        normalized_table.to_csv(input_mkdir + "/" + input2 + ".csv")
        print("Task finished!")

    elif str(initial_input).lower() == "pg_heat":
        input1 = input("Path of Text file: ")
        input2 = input("Set the name: ")
        input3 = input("Set the color (red, blue, green, yellow, etc.): ").lower()
        input_wantmkdir = input("Do you want to export the file in a specific directory? (yes/no): ")
        if input_wantmkdir.lower() == "yes":
            input_mkdir = input("Write the absolute path of the target directory: ")
            make_directory(input_mkdir)
        else:
            input_mkdir = str(path_folder + "/output_graphs")

        df1 = pd.read_fwf(str(input1))
        df2 = heat.HeatPlot(df1)
        df3 = df2.normalize_heat()
        heat.HeatPlot.plot_heat(df3, set_show=0, set_name=str(input2), set_color=input3, set_directory=input_mkdir)
        print("Task finished!")

    # Iterator
    elif str(initial_input).lower() == "tb_iter":
        input_csv = input("Please type in the path of your .csv table: ")
        data = pd.read_csv(str(input_csv))
        iter.IteratorCD.CD_data_iterator(data)
        print("Task finished!")

    elif str(initial_input).lower() == "fb_iter":
        input_wantmkdir = input("Do you want to export the file in a specific directory? (yes/no): ")
        if input_wantmkdir.lower() == "yes":
            input_mkdir = input("Write the absolute path of the target directory: ")
            make_directory(input_mkdir)
        else:
            input_mkdir = str(path_folder + "/output_graphs/")
        iter.IteratorCD.CD_iterator_advanced(set_target_directory=str(input_mkdir))
        print("Task finished!")

    elif str(initial_input).lower() == "iter_help":
        iter.IteratorCD.help()

    else:
        print("Invalid command, please try again...")
