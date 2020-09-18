# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:43:48 2020

@author: lllan
"""

from pymatgen import Structure, MPRester
from mechelastic.core import ELATE, ElasticProperties, Structure
import numpy as np

"Get the unique apiKey on materials project website"
apiKey = "xxxxxxxxxxxxxxxx"
a = MPRester("apiKey")

"Trigonal LiNbO3"
#mat_info = a.query(criteria={"task_id": "mp-3731"}, properties=["structure","elasticity"])[0]
"Tetragonal SiO2"
#mat_info = a.query(criteria={"task_id": "mp-6945"}, properties=["structure","elasticity"])[0]
"Trigonal SiO2"
mat_info = a.query(criteria={"task_id": "mp-6930"}, properties=["structure","elasticity"])[0]

s1 = mat_info['structure']
lattice = s1.lattice.matrix
species = [specie.symbol for specie in s1.species]
frac_coords = s1.frac_coords
structure = Structure(atoms = species, fractional_coordinates = frac_coords, lattice = lattice)

elastic_tensor = np.array(mat_info['elasticity']['elastic_tensor'])

elastic_properties = ElasticProperties(elastic_tensor, structure,crystal_type = 'rhombohedral-2')
elastic_properties.print_properties()
gV = elastic_properties.G_v
stability = elastic_properties.elastic_stability
elastic_properties.print_properties()

elastic_tensor = np.array(mat_info['elasticity']['elastic_tensor'])
row = elastic_tensor.shape[0]
col = elastic_tensor.shape[1]
rowsList = []
for i in range(row):
    columnsList = []
    for j in range(col):
        columnsList.append(round(elastic_tensor[i, j],3))
    rowsList.append(columnsList)



elas_tensor = ELATE.ELATE(rowsList)
elas_tensor.plot_2D(elastic_calc="POISSON")

elastic_tensor.print_properties()
elas_tensor.plot_3D(elastic_calc="YOUNG")