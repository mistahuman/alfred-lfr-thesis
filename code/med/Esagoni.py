#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.2.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'.')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

#Parametri modificabili

numero_cerchi=9
lato_esagoni=9.872689603 #cm
altezza_totale=350.0 #cm
altezze_piani=[15.0, 90.0, 145.0, 155.0, 163.0, 171.0, 179.0, 187.0, 
              195.0, 205.0, 217.0, 222.0, 242.0, 282.00, 338.00]
#Costruzione esagono sorgente

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
sk = geompy.Sketcher2D()
sk.addPoint(lato_esagoni, 0.000000)
sk.addSegmentAbsolute(0.000000, 0.000000)
sk.addSegmentAngleLength(-60, lato_esagoni)
sk.addSegmentAngleLength(-60, lato_esagoni)
sk.addSegmentAngleLength(-60, lato_esagoni)
sk.addSegmentAngleLength(-60, lato_esagoni)
sk.addSegmentAngleLength(-60, lato_esagoni)
Sketch_1 = sk.wire(geomObj_1)
Face_1 = geompy.MakeFaceWires([Sketch_1], 1)

vettori=[] #6 vettori direzione, indice da 0 a 5

Face_1_vertex_13 = geompy.GetSubShape(Face_1, [13])
Face_1_vertex_9 = geompy.GetSubShape(Face_1, [9])
vettori.append(geompy.MakeVector(Face_1_vertex_13, Face_1_vertex_9))
Face_1_vertex_11 = geompy.GetSubShape(Face_1, [11])
Face_1_vertex_7 = geompy.GetSubShape(Face_1, [7])
vettori.append(geompy.MakeVector(Face_1_vertex_11, Face_1_vertex_7))
Face_1_vertex_5 = geompy.GetSubShape(Face_1, [5])
vettori.append(geompy.MakeVector(Face_1_vertex_9, Face_1_vertex_5))
Face_1_vertex_4 = geompy.GetSubShape(Face_1, [4])
vettori.append(geompy.MakeVector(Face_1_vertex_7, Face_1_vertex_4))
vettori.append(geompy.MakeVector(Face_1_vertex_5, Face_1_vertex_13))
vettori.append(geompy.MakeVector(Face_1_vertex_4, Face_1_vertex_11))
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sketch_1, 'Sketch_1' )
Face_1_vertex_7 = geompy.GetSubShape(Face_1, [7])
Face_1_vertex_13 = geompy.GetSubShape(Face_1, [13])
Line_1 = geompy.MakeLineTwoPnt(Face_1_vertex_7, Face_1_vertex_13)
Partition_1 = geompy.MakePartition([Face_1], [Line_1], [], [], geompy.ShapeType["FACE"], 0, [], 0)
#geompy.addToStudy(Partition_1, 'Face_1')






traslazioni=[] #Lista contenente tutti gli esagoni
apotema=math.sqrt((lato_esagoni*lato_esagoni)-((lato_esagoni/2)*(lato_esagoni/2)))
traslazioni.append(Partition_1)

n=1

for i in range(0,numero_cerchi): #loop su ogni "circonferenza"
    traslazioni.append(geompy.MakeTranslation(Partition_1, 2*(i+1)*apotema*math.cos(math.pi/6),2*(i+1)*apotema*math.sin(math.pi/6), 0))
    #if n==1:
        #geompy.addToStudy(traslazioni[n], 'Face_%d' %(n+1))
    #else:  
    if n!=1:    
        #geompy.addToStudy(traslazioni[n], 'Face_%d' %(n+2)) #Non va riaggiunta, le tre successive (in caso di necesita') si
        n=n+1    
    if i==0:
        for l in range(0,5): #loop sui 5 vettori direzione
            for k in range(0,i+1):
                traslazioni.append(geompy.MakeTranslationVector(traslazioni[n], vettori[l]))
                n=n+1
                #geompy.addToStudy(traslazioni[n], 'Face_%d' %(n+1)) 
    else:
        for j in range(0,6): #loop sui 6 vettori direzione
            if j!=5:
                for k in range(0,i+1):
                    traslazioni.append(geompy.MakeTranslationVector(traslazioni[n], vettori[j]))
                    n=n+1
                    #geompy.addToStudy(traslazioni[n], 'Face_%d' %(n+1)) 
            else:
                for k in range(0,i):
                    traslazioni.append(geompy.MakeTranslationVector(traslazioni[n], vettori[j]))
                    n=n+1
                    #geompy.addToStudy(traslazioni[n], 'Face_%d' %(n+2)) 

#for t in range(0,n+1,1): #Controllo esagoni
    #geompy.addToStudy(traslazioni[t], 'Face_%d' %(t) ) 

Glue_1 = geompy.MakeGlueEdges(traslazioni, 1e-07)
geompy.addToStudy(Glue_1, 'Glue_1' ) 


#[A] = geompy.SubShapes(Glue_1, [380])
A = geompy.MakeVertex(0., 0., 0.)
B = geompy.MakeVertexWithRef(A, 0., 0., altezza_totale)
Line_2 = geompy.MakeLineTwoPnt(A, B)
geompy.addToStudy(A, 'A' ) 
geompy.addToStudy(B, 'B' ) 
geompy.addToStudy(Line_2, 'Line_2')
base = geompy.CreateGroup(Glue_1, geompy.ShapeType["FACE"])
facce = geompy.SubShapeAllIDs(Glue_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(base, facce)
geompy.addToStudyInFather( Glue_1, base, 'base' )




###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

altezze_piani_normalizzata= [x / altezza_totale for x in altezze_piani]
parametro_FixedPoints1D=[1]*(len(altezze_piani_normalizzata)+1) #lista di 1's per la funzione FixedPoints1D



smesh = smeshBuilder.New()
mesh_base = smesh.Mesh(Glue_1)
Regular_1D = mesh_base.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(1,None,[])
Quadrangle_2D = mesh_base.Quadrangle(algo=smeshBuilder.QUADRANGLE)
isDone = mesh_base.Compute()
base_1 = mesh_base.GroupOnGeom(base,'base',SMESH.FACE)
mesh_linea = smesh.Mesh(Line_2)
Regular_1D_1 = mesh_linea.Segment()
Fixed_Points_1 = Regular_1D_1.FixedPoints1D(altezze_piani_normalizzata,parametro_FixedPoints1D,[])
Fixed_Points_1.SetObjectEntry( "Line_2" )
isDone = mesh_linea.Compute()
([ base_extruded, base_top ], error) = mesh_base.ExtrusionAlongPathObjects( [ mesh_base ], [ mesh_base ], [ mesh_base ], mesh_linea, None, 1, 0, [  ], 0, 0, [ 0, 0, 0 ], 1 )
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_FreeFaces,SMESH.FT_Undefined,0,SMESH.FT_Undefined,SMESH.FT_LogicalAND)
aCriteria.append(aCriterion)
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_BelongToMeshGroup,SMESH.FT_Undefined,base_1,SMESH.FT_LogicalNOT)
aCriteria.append(aCriterion)
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_BelongToMeshGroup,SMESH.FT_Undefined,base_top,SMESH.FT_LogicalNOT)
aCriteria.append(aCriterion)
aFilter_1 = smesh.GetFilterFromCriteria(aCriteria)
aFilter_1.SetMesh(mesh_base.GetMesh())
lato = mesh_base.GroupOnFilter( SMESH.FACE, 'lato', aFilter_1 )
mesh_base.Compute
mesh_base.ConvertToQuadratic(0, mesh_base,True)

#Traslazione per avere il centro dell'esagono in (0,0,0)
# mesh_base.TranslateObject( mesh_base, [ -lato_esagoni/2., -apotema, 0 ], 0 )

## Set names of Mesh objects
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Fixed_Points_1, 'Fixed Points_1')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(base_1, 'base')
smesh.SetName(base_top, 'base_top')
smesh.SetName(lato, 'lato')
smesh.SetName(mesh_base.GetMesh(), 'mesh_base')
smesh.SetName(mesh_linea.GetMesh(), 'mesh_linea')
smesh.SetName(base_extruded, 'base_extruded')








##Estrusione
#Extrusion_1 = geompy.MakePrismVecH(Glue_1, OZ, altezza_totale)

##Creo i punti alle altezze_piani
#punti=[]
#for r in range(0, len(altezze_piani)):
    #punti.append(geompy.MakeVertex(  0.,   0., altezze_piani[r]))

#piani=[]
##creo i piani per tagliare il solido
#for y in range(0, len(punti)) :
    #piani.append(geompy.MakePlane(punti[y], OZ, 1000))

##Partizioni il solido alle varie altezze_piani
#solido_partizionato = geompy.MakePartition([Extrusion_1], piani, [], [], geompy.ShapeType["SOLID"], 0, [], 0)

#geompy.addToStudy(solido_partizionato, 'Solido Partizionato' ) 

###
### SMESH component
###

#import  SMESH, SALOMEDS
#from salome.smesh import smeshBuilder

#smesh = smeshBuilder.New()
#Mesh_1 = smesh.Mesh(Glue_1)
#Regular_1D = Mesh_1.Segment()
#Number_of_Segments_1 = Regular_1D.NumberOfSegments(1)
#Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
#isDone = Mesh_1.Compute()


### Set names of Mesh objects
#smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
#smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
#smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
#smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')



if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
