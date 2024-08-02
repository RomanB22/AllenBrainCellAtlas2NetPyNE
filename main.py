from utils import *
import os
import glob

regionName = "VISp"
subregionName = ["VISp1", "VISp2/3", "VISp4", "VISp5","VISp6a","VISp6b"]
structure_area_abbrev = 'VISp'
structure_layer_name = ["1", "2/3", "4", "5", "6a", "6b"]

ABC_ATLAS_BASE, cell_meta, gene_meta, cell_meta_ext = loadMERFISHDatabase()

modelNet_data = obtainCellCounts(ABC_ATLAS_BASE, numCells=300000, regionName=regionName,
                                 subregionName=subregionName, modelName="v1")

Model_specification = cellsModelSpecification(modelNet_data,
                                              regionList=subregionName,
                                              structure_area_abbrev=structure_area_abbrev,
                                              structure_layer_name=structure_layer_name)

downloadCellModels(Model_specification)

cwd = os.getcwd()
cellModel = 'Peri'
configfiles = glob.glob(cwd+'/CellModels%s/**/manifest.json' % cellModel, recursive=True)

for i in range(len(configfiles)):
    path = os.path.normpath(configfiles[i])
    splitPath = path.split(os.sep)
    region = splitPath[-3]
    cellType, cell_id = splitPath[-2].split('_')

    workingDir = 'CellModels%s/%s/%s_%s/' % (cellModel,region,cellType,cell_id)
    cell, cellRule = convert2NetPyNE(workingDir=workingDir, cellModel=cellModel, cellType=cellType, region=region,
                                     id=cell_id, SaveCell=True)

