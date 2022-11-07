Package for Analysis of CD and HPLC data

Note: 
The algorithm has been designed for .txt data produced by the Äkta pure system (cytiva) and
CD spectrum data (molar ellipticity - wavelength spectrum and heat-denaturation spectrum) from
Jasco circular dichroism spectroscopy machinery line.

Make sure that the folder with the downloaded files contains an "input_txt" folder, an "output_graph" 
folder and an "output_table" folder.
These subdirectories are the default directories for data in- and output.

Program files:
Control_center.py
IteratorCD.py
HeatCD.py
SpectrumCD.py
HPLC.py

Program excutables (run Control_center.py):
Single file analysis (.txt format required)
    1. HPLC: format table (ft_hplc), plot chromatogram (pg_hplc), help (hplc_help)
    2. CD spectrum: format table (ft_spec), plot spectrum (pg_spec), help (spec_help)
    3: CD heat protein denaturation: format table (ft_heat), plot graph (pg_heat), help (heat_help)
    
    Multiple file analysis 
    1. Table supported data analysis (compare added txt file for more info, format: .csv) (tb_iter)
    2. Folder based data analysis (please drop the files in the included "input_txt" folder) (fb_iter)
    --> help (iter_help)
    
    End program (quit)



