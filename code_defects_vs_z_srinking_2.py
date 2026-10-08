#!/usr/bin/env python3
"""

"""
import pandas as pd
import numpy as np

import glob
import os
import os.path
import re
import sys
import warnings


def layer_category_fix_n(zmin,zmax,n):
    layers_list = []
    beginning = zmin
    h_step = (zmax-zmin)/n
    n_layer = 0
    while (beginning < zmax):
        layers_list.append([beginning, beginning+h_step, h_step, n_layer])
        beginning = beginning + h_step 
        n_layer += 1
    return sorted(layers_list)

def main():
    
    # ignore warnings
    warnings.filterwarnings("ignore")
    
    layer_height = int(sys.argv[-1])
            
    #Creatte directory to put avg results
    directory_frames = 'cascades_form_spectra_for_movie_npt'
    directory = f'{directory_frames}/results_defects_vs_z_h{layer_height}_shrinking'
    try:
        os.makedirs(directory)
    except FileExistsError:
        # directory already exists
        pass
    
    # list of files
    list_files = glob.glob(f'{directory_frames}/final_pyro_cascades_*.xyz')
    
    count_files = 1
    for filename in list_files:
        n = 36 #37
        print(count_files, "/", len(list_files), "file name:", filename[n:])
        
        border_factor = 0
        if border_factor == 0:
            file_output = f'{directory}/def_vs_z_h{layer_height}_shrinking_{filename[n:]}'
        else:
            file_output = f'{directory}/def_vs_z_h{layer_height}_b{border_factor}_shrinking_{filename[n:]}'
        
        if os.path.exists(file_output) == False:
        #if os.path.exists(file_output) == True:
            # load data from file
            input_data = open(filename).read()
            df_atoms = pd.read_table(filename, skiprows=9,
                                       names=['element', 'x', 'y', 'z', 'id', 'coord_num', 'pot_eng'],
                                       sep='\\s+')
            df_atoms = df_atoms.drop(['element'],axis=1)
            
            
            drop_list = df_atoms[(df_atoms['x'] < df_atoms['x'].min()+border_factor) | (df_atoms['x'] > df_atoms['x'].max()-border_factor) | \
                                 (df_atoms['y'] < df_atoms['y'].min()+border_factor) | (df_atoms['y'] > df_atoms['y'].max()-border_factor)   \
                                ].index
            
            df_atoms = df_atoms.drop(drop_list, axis=0).reset_index(drop=True)
            
            # assign z_layer_fix_n
            init_intf = 6
            init_z_min = -169.64307163528616
            init_z_max = 150.98293179686004
            n = (init_z_max - init_z_min) //layer_height
            
            layers = layer_category_fix_n(df_atoms['z'].min(),df_atoms['z'].max(), n)
                
            # assign z_layer group 
            def hight_category(hight):
                for i in layers:
                    cond=(i[0]< hight and hight <= i[1]);
                    if cond: 
                        return i[3]
                    else:
                        pass
            #    raise ValueError
                print("Error: Incorrect coordinate fix_n")
                print(f"{i[0]}, {i[1]}, {i[2]}, {df_atoms['z'].max()}")
            
            df_atoms['z_layers'] = df_atoms['z'].apply(hight_category)
             
            #count atoms in each layer
            df_atoms_grouped = df_atoms.groupby('z_layers')['id'].count()
            df_atoms_grouped = df_atoms_grouped.reset_index()
            df_atoms_grouped = df_atoms_grouped.rename(columns={"id": "atoms_total"})

            #count defect in each layer
            df_poteng = df_atoms[df_atoms['pot_eng'] > -7.0].groupby('z_layers')['pot_eng'].count()
            df_poteng = df_poteng.reset_index()
            df_poteng = df_poteng.rename(columns={"pot_eng": "def_pot_eng"})
            
            df_coordnum = df_atoms[df_atoms['coord_num'] != 3].groupby('z_layers')['coord_num'].count()
            df_coordnum = df_coordnum.reset_index()
            df_coordnum = df_coordnum.rename(columns={"coord_num": "def_coord_num"})
            
            df_coordnum_1 = df_atoms[df_atoms['coord_num'] == 1].groupby('z_layers')['coord_num'].count()
            df_coordnum_1 = df_coordnum_1.reset_index()
            df_coordnum_1 = df_coordnum_1.rename(columns={"coord_num": "coord_num_1"})
            
            df_coordnum_2 = df_atoms[df_atoms['coord_num'] == 2].groupby('z_layers')['coord_num'].count()
            df_coordnum_2 = df_coordnum_2.reset_index()
            df_coordnum_2 = df_coordnum_2.rename(columns={"coord_num": "coord_num_2"})
            
            df_coordnum_3 = df_atoms[df_atoms['coord_num'] == 3].groupby('z_layers')['coord_num'].count()
            df_coordnum_3 = df_coordnum_3.reset_index()
            df_coordnum_3 = df_coordnum_3.rename(columns={"coord_num": "coord_num_3"})
            
            df_coordnum_4 = df_atoms[df_atoms['coord_num'] == 4].groupby('z_layers')['coord_num'].count()
            df_coordnum_4 = df_coordnum_4.reset_index()
            df_coordnum_4 = df_coordnum_4.rename(columns={"coord_num": "coord_num_4"})
            
            df_coordnum_5 = df_atoms[df_atoms['coord_num'] == 5].groupby('z_layers')['coord_num'].count()
            df_coordnum_5 = df_coordnum_5.reset_index()
            df_coordnum_5 = df_coordnum_5.rename(columns={"coord_num": "coord_num_5"})
            
            df_coordnum_6 = df_atoms[df_atoms['coord_num'] == 6].groupby('z_layers')['coord_num'].count()
            df_coordnum_6 = df_coordnum_6.reset_index()
            df_coordnum_6 = df_coordnum_6.rename(columns={"coord_num": "coord_num_6"})
            
            # merge result in one dataframe
            array=np.array(layers)        
            df_def = pd.DataFrame(array,columns=['beginning','ending','height','z_layers'])
            df_def = df_def.merge(df_atoms_grouped, how='outer')
            df_def = df_def.merge(df_coordnum, how='outer')
            df_def = df_def.merge(df_poteng,how='outer')
            df_def = df_def.merge(df_coordnum_1, how='outer')
            df_def = df_def.merge(df_coordnum_2, how='outer')
            df_def = df_def.merge(df_coordnum_3, how='outer')
            df_def = df_def.merge(df_coordnum_4, how='outer')
            df_def = df_def.merge(df_coordnum_5, how='outer')
            df_def = df_def.merge(df_coordnum_6, how='outer')
            df_def = df_def.fillna(0)
            
            # write results into file
            df_def.to_csv(file_output)
        
        count_files += 1

if __name__ == "__main__":
    sys.exit(main())
