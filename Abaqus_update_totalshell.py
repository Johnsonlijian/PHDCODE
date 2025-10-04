# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_14-01.49.31 163176
# Run by 87028 on Tue Mar 22 00:36:18 2022
#
# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=92.9427032470703,height=126.414352416992)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)

A = 300  # H
B = 20  # B
C = 15  # t1
D = 5  # t2
L = 3000  # l`
E = 2  # 拼接数量
F = 1  # 横向螺栓数量（竖直方向）
BoltD = 20     # 螺栓直径
BoltB = 0.0     # 螺栓中心据y=0的横向距
sfricn = 0.0  # 切向接触摩擦系数
pbol = 90.0      # 螺栓预紧
yfss = 355.61  # 屈服应力
yfsn = 0.023   # 屈服应变平台尾部
yuss = 444  #ￄ应
yusn = 0.1576   #ￄ应
meshsz = 20    # 网格划分尺寸
meshszb = 4    # 螺栓网格划分尺寸
cf1f = 1.0
cf2f = 1.0
cf3f = 0.0
u1u = 1.0
u2u = 1.0
u3u = 0.0
trueu3 = 10.0
nodedeform = 6.0




printname='A'+str(A)+'B'+str(B)+'C'+str(C)+'D'+str(D)+'L'+str(L)+'E'+str(E)+'F'+str(F)+'BoltD'+str(BoltD)+'BoltB'\
          +str(BoltB)+'sfricn'+str(sfricn)+'pbol'+str(pbol)+'yfss'+str(yfss)+'yuss'+str(yuss)+'yusn'+str(yusn)\
          +'meshsz'+str(meshsz)+'cf1f'+str(cf1f)+'cf2f'+str(cf2f)+'cf3f'+str(cf3f)+'nodedeform'+str(nodedeform)


import os
os.chdir(r"C:\Users\HPC\Desktop\Isight_Catia_Abaqus\Abaqus_dataTE")

session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(0.0, 0), point2=(B/2, 0))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(0.0, 0), point2=(-B/2, 0))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.ParallelConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.Line(point1=(0.0, 0), point2=(0.0, A))
s.VerticalConstraint(entity=g[4], addUndoState=False)
s.PerpendicularConstraint(entity1=g[2], entity2=g[4], addUndoState=False)
s.Line(point1=(0.0, A), point2=(B/2, A))
s.HorizontalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.Line(point1=(0.0, A), point2=(-B/2, A))
s.HorizontalConstraint(entity=g[6], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[6], addUndoState=False)

p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseShellExtrude(sketch=s, depth=L)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']

# 截面形式调整
if E != 1:
    p = mdb.models['Model-1'].parts['Part-1']
    s1 = p.features['Shell extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2,
        upToFeature=p.features['Shell extrude-1'], filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=32.0238,
        farPlane=946.037, width=4902.41, height=2124.32, cameraPosition=(60.4493,
        532.114, 499.03), cameraTarget=(60.4493, 532.114, 0))
    s2.linearPattern(geomList=(g[4],g[5], g[6]), vertexList=(),
        number1=1, spacing1=20.0, angle1=0.0, number2=E, spacing2=A,
        angle2=90.0)
    s2.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    p.features['Shell extrude-1'].setValues(sketch=s2)
    del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['Part-1']
p.regenerate()


#材料截面
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((205000.0, 0.3),
    ))
mdb.models['Model-1'].materials['Material-1'].Density(table=((7.85e-09, ), ))
# 截面创建
mdb.models['Model-1'].HomogeneousShellSection(name='websection',
    preIntegrate=OFF, material='Material-1', thicknessType=UNIFORM,
    thickness=C, thicknessField='', nodalThicknessField='',
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT,
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF,
    integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].HomogeneousShellSection(name='flangesection',
    preIntegrate=OFF, material='Material-1', thicknessType=UNIFORM,
    thickness=D*2, thicknessField='', nodalThicknessField='',
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT,
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF,
    integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].HomogeneousShellSection(name='edgeflangesection',
    preIntegrate=OFF, material='Material-1', thicknessType=UNIFORM,
    thickness=D, thicknessField='', nodalThicknessField='',
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT,
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF,
    integrationRule=SIMPSON, numIntPts=5)
# 截面指派
# 腹板
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
if E==1:
    faces = f.findAt(((0.0, A/2*1, L/2), ))
if E==2:
    faces = f.findAt(((0.0, A/2*1, L/2), ), ((0.0, A*2-A/2, L/2), ))
if E==3:
    faces = f.findAt(((0.0, A/2*1, L/2), ), ((0.0, A*2-A/2, L/2), ), ((0.0, A*3-A/2, L/2),  ))
if E==4:
    faces = f.findAt(((0.0, A/2*1, L/2), ), ((0.0, A*2-A/2, L/2), ), ((0.0, A*3-A/2, L/2), ), ((0.0, A*4-A/2, L/2), ))
if E==5:
    faces = f.findAt(((0.0, A/2*1, L/2), ), ((0.0, A*2-A/2, L/2), ), ((0.0, A*3-A/2, L/2), ), ((0.0, A*4-A/2, L/2),),((0.0, A*5-A/2, L/2), ))
if E==6:
    faces = f.findAt(((0.0, A/2*1, L/2), ), ((0.0, A*2-A/2, L/2), ), ((0.0, A*3-A/2, L/2), ), ((0.0, A*4-A/2, L/2),),((0.0, A*5-A/2, L/2),),
                    ((0.0, A*6-A/2, L/2), ))
if E==7:
    faces = f.findAt(((0.0, A/2*1, L/2), ), ((0.0, A*2-A/2, L/2), ), ((0.0, A*3-A/2, L/2), ), ((0.0, A*4-A/2, L/2),),((0.0, A*5-A/2, L/2),),
                    ((0.0, A*6-A/2, L/2),), ((0.0, A*7-A/2, L/2), ))
if E==8:
    faces = f.findAt(((0.0, A/2*1, L/2), ), ((0.0, A*2-A/2, L/2), ), ((0.0, A*3-A/2, L/2), ), ((0.0, A*4-A/2, L/2),),((0.0, A*5-A/2, L/2),),
                    ((0.0, A*6-A/2, L/2),), ((0.0, A*7-A/2, L/2), ), ((0.0, A*8-A/2, L/2), ))
if E==9:
    faces = f.findAt(((0.0, A/2*1, L/2), ), ((0.0, A*2-A/2, L/2), ), ((0.0, A*3-A/2, L/2), ), ((0.0, A*4-A/2, L/2),),((0.0, A*5-A/2, L/2),),
                    ((0.0, A*6-A/2, L/2),), ((0.0, A*7-A/2, L/2), ), ((0.0, A*8-A/2, L/2),), ((0.0, A*9-A/2, L/2), ))
if E==10:
    faces = f.findAt(((0.0, A/2*1, L/2), ), ((0.0, A*2-A/2, L/2), ), ((0.0, A*3-A/2, L/2), ), ((0.0, A*4-A/2, L/2),),((0.0, A*5-A/2, L/2),),
                    ((0.0, A*6-A/2, L/2),), ((0.0, A*7-A/2, L/2), ), ((0.0, A*8-A/2, L/2),), ((0.0, A*9-A/2, L/2), ), ((0.0, A*10-A/2, L/2), ))

region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='websection', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
# 翼缘（x正向）仅考虑中部翼缘
if E != 1:
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces

    if E == 2:
        faces = f.findAt( ( (B/4, A , L / 2), ))
    if E == 3:
        faces = f.findAt(( (B/4, A , L / 2), ), ( (B/4, A * 2 , L / 2),))
    if E == 4:
        faces = f.findAt(( (B/4, A , L / 2), ), ( (B/4, A * 2 , L / 2), ),((B/4, A * 3 , L / 2), ))
    if E == 5:
        faces = f.findAt(( (B/4, A , L / 2), ), ( (B/4, A * 2 , L / 2), ),((B/4, A * 3 , L / 2),),((B/4, A * 4 , L / 2),))
    if E == 6:
        faces = f.findAt( ( (B/4, A , L / 2), ), ( (B/4, A * 2 , L / 2), ),
                         ((B/4, A * 3 , L / 2), ), ( (B/4, A * 4 , L / 2), ), ( (B/4, A * 5 , L / 2),))
    if E == 7:
        faces = f.findAt(( (B/4, A , L / 2), ), ( (B/4, A * 2 , L / 2), ),
                         ((B/4, A * 3 , L / 2), ), ( (B/4, A * 4 , L / 2), ), ( (B/4, A * 5 , L / 2),), (
                          (B/4, A * 6 , L / 2), ))
    if E == 8:
        faces = f.findAt(( (B/4, A , L / 2), ), ( (B/4, A * 2 , L / 2), ),
                         ((B/4, A * 3 , L / 2), ), ( (B/4, A * 4 , L / 2), ), ( (B/4, A * 5 , L / 2),), (
                          (B/4, A * 6 , L / 2), ), ( (B/4, A * 7 , L / 2),))
    if E == 9:
        faces = f.findAt( ( (B/4, A , L / 2), ), ( (B/4, A * 2 , L / 2), ),
                         ((B/4, A * 3, L / 2), ), ( (B/4, A * 4 , L / 2), ), ( (B/4, A * 5 , L / 2),), (
                         (B/4, A * 6, L / 2), ), ( (B/4, A * 7 , L / 2), ), (  (B/4, A * 8 , L / 2),  ))
    if E == 10:
        faces = f.findAt( ( (B/4, A , L / 2), ), ( (B/4, A * 2 , L / 2), ),((B/4, A * 3 , L / 2), ),
                          ( (B/4, A * 4 , L / 2), ), ( (B/4, A * 5 , L / 2),), (
                          (B/4, A * 6 , L / 2), ), ( (B/4, A * 7 , L / 2), ), (  (B/4, A * 8 , L / 2), ),
                                                     ( (B/4, A * 9 , L / 2),))
    region = regionToolset.Region(faces=faces)
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='flangesection', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].view.fitView()



# 翼缘（x负向）仅考虑中部翼缘
if E != 1:
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    if E == 2:
        faces = f.findAt( ( (-B/4, A , L / 2), ))
    if E == 3:
        faces = f.findAt(( (-B/4, A , L / 2), ), ( (-B/4, A * 2 , L / 2), ))
    if E == 4:
        faces = f.findAt(( (-B/4, A , L / 2), ), ( (-B/4, A * 2 , L / 2), ),((-B/4, A * 3 , L / 2),))
    if E == 5:
        faces = f.findAt(( (-B/4, A , L / 2), ), ( (-B/4, A * 2 , L / 2), ),((-B/4, A * 3 , L / 2),),((-B/4, A * 4 , L / 2),))
    if E == 6:
        faces = f.findAt( ( (-B/4, A , L / 2), ), ( (-B/4, A * 2 , L / 2), ),
                         ((-B/4, A * 3 , L / 2), ), ( (-B/4, A * 4 , L / 2), ), ( (-B/4, A * 5 , L / 2),))
    if E == 7:
        faces = f.findAt(( (-B/4, A , L / 2), ), ( (-B/4, A * 2 , L / 2), ),
                         ((-B/4, A * 3 , L / 2), ), ( (-B/4, A * 4 , L / 2), ), ( (-B/4, A * 5 , L / 2),), (
                          (-B/4, A * 6 , L / 2), ))
    if E == 8:
        faces = f.findAt(( (-B/4, A , L / 2), ), ( (-B/4, A * 2 , L / 2), ),
                         ((-B/4, A * 3 , L / 2), ), ( (-B/4, A * 4 , L / 2), ), ( (-B/4, A * 5 , L / 2),), (
                          (-B/4, A * 6 , L / 2), ), ( (-B/4, A * 7 , L / 2),))
    if E == 9:
        faces = f.findAt( ( (-B/4, A , L / 2), ), ( (-B/4, A * 2 , L / 2), ),
                         ((-B/4, A * 3, L / 2), ), ( (-B/4, A * 4 , L / 2), ), ( (-B/4, A * 5 , L / 2),), (
                         (-B/4, A * 6, L / 2), ), ( (-B/4, A * 7 , L / 2), ), (  (-B/4, A * 8 , L / 2),  ))
    if E == 10:
        faces = f.findAt( ( (-B/4, A , L / 2), ), ( (-B/4, A * 2 , L / 2), ),((-B/4, A * 3 , L / 2), ),
                          ( (-B/4, A * 4 , L / 2), ), ( (-B/4, A * 5 , L / 2),), (
                          (-B/4, A * 6 , L / 2), ), ( (-B/4, A * 7 , L / 2), ), (  (-B/4, A * 8 , L / 2), ),
                                                     ( (-B/4, A * 9 , L / 2),))
    region = regionToolset.Region(faces=faces)
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='flangesection', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].view.fitView()

# 翼缘（x正向）仅考虑两边翼缘
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
if E == 1:
    faces = f.findAt(((B/4, 0, L / 2), ), ( (B/4, E*A, L / 2), ))
if E == 2:
    faces = f.findAt(((B / 4, 0, L / 2),), ((B / 4, E * A, L / 2),))
if E == 3:
    faces = f.findAt(((B/4, 0, L / 2), ), ( (B/4, E*A, L / 2), ))
if E == 4:
    faces = f.findAt(((B/4, 0, L / 2), ), ( (B/4, E*A, L / 2), ))
if E == 5:
    faces = f.findAt(((B/4, 0, L / 2), ), ( (B/4, E*A, L / 2), ))
if E == 6:
    faces = f.findAt(((B/4, 0, L / 2), ), ( (B/4, E*A, L / 2), ))
if E == 7:
    faces = f.findAt(((B/4, 0, L / 2), ), ( (B/4, E*A, L / 2), ))
if E == 8:
    faces = f.findAt(((B/4, 0, L / 2), ), ( (B/4, E*A, L / 2), ))
if E == 9:
    faces = f.findAt(((B/4, 0, L / 2), ), ( (B/4, E*A, L / 2), ))
if E == 10:
    faces = f.findAt(((B/4, 0, L / 2), ), ( (B/4, E*A, L / 2), ))
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='edgeflangesection', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.fitView()


# 翼缘（x负向）仅考虑两边翼缘
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
if E == 1:
    faces = f.findAt(((-B/4, 0, L / 2), ), ( (-B/4, E*A, L / 2), ))
if E == 2:
    faces = f.findAt(((-B / 4, 0, L / 2),), ((-B / 4, E * A, L / 2),))
if E == 3:
    faces = f.findAt(((-B/4, 0, L / 2), ), ( (-B/4, E*A, L / 2), ))
if E == 4:
    faces = f.findAt(((-B/4, 0, L / 2), ), ( (-B/4, E*A, L / 2), ))
if E == 5:
    faces = f.findAt(((-B/4, 0, L / 2), ), ( (-B/4, E*A, L / 2), ))
if E == 6:
    faces = f.findAt(((-B/4, 0, L / 2), ), ( (-B/4, E*A, L / 2), ))
if E == 7:
    faces = f.findAt(((-B/4, 0, L / 2), ), ( (-B/4, E*A, L / 2), ))
if E == 8:
    faces = f.findAt(((-B/4, 0, L / 2), ), ( (-B/4, E*A, L / 2), ))
if E == 9:
    faces = f.findAt(((-B/4, 0, L / 2), ), ( (-B/4, E*A, L / 2), ))
if E == 10:
    faces = f.findAt(((-B/4, 0, L / 2), ), ( (-B/4, E*A, L / 2), ))
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='edgeflangesection', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.fitView()
# # # #进入装配--------------------------------------------
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)

# # 分析歄�
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].BuckleStep(name='Step-1', previous='Initial',
    numEigen=10, eigensolver=LANCZOS, minEigen=None, blockSize=DEFAULT,
    maxBlocks=DEFAULT)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')

# 集点
# 顶部
a1 = mdb.models['Model-1'].rootAssembly
a1.AttachmentPoints(name='RPR1', points=((0, A*E/2, L), ))
# 集点
a1 = mdb.models['Model-1'].rootAssembly
v1 = a1.vertices
verts1 = v1.findAt(((0, A*E/2, L), ))
a1.Set(vertices=verts1, name='TTpoint')

# 底部
# a1 = mdb.models['Model-1'].rootAssembly
a1.AttachmentPoints(name='RPR2', points=((0, A*E/2, 0), ))
# 集点
a1 = mdb.models['Model-1'].rootAssembly
v1 = a1.vertices
verts1 = v1.findAt(((0, A*E/2, 0), ))
a1.Set(vertices=verts1, name='BBpoint')
# 边集（每个构件有四个翼缘集一个腹板边集）
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
if E==1:
    edges1 = e1.findAt(((+B/4, A*0+0, L), ), ((0.0, A/2, L), ),((-B/4, A*0+0, L),),
                                                                ((+B/4, A*1+0, L), ),((-B/4, A*1+0, L),  ))

if E==2:
    edges1 = e1.findAt(((+B/4, A*0+0, L), ), ((0.0, A/2, L), ),((-B/4, A*0+0, L), ))
    edges2 = e1.findAt(((+B/4, A*1+0, L),),((0.0, 2*A-A/2, L), ),((-B/4, A*1+0, L),),
                                                                ((+B/4, A*2+0, L), ),((-B/4, A*2+0, L),  ))

if E==3:
    edges1 = e1.findAt(((+B/4, A*0+0, L), ), ((0.0, A/2, L), ),((-B/4, A*0+0, L), ))
    edges2 = e1.findAt(((+B/4, A*1+0, L),  ),((0.0, 2*A-A/2, L), ),((-B/4, A*1+0, L),))
    edges3 = e1.findAt(((+B/4, A*2+0, L), ), ((0.0, 3*A-A/2, L), ),((-B/4, A*2+0, L),),
                                                                ((+B/4, A*3+0, L), ),((-B/4, A*3+0, L),  ))

if E==4:
    edges1 = e1.findAt(((+B/4, A*0+0, L), ), ((0.0, A/2, L), ),((-B/4, A*0+0, L), ))
    edges2 = e1.findAt(((+B/4, A*1+0, L),  ),((0.0, 2*A-A/2, L), ),((-B/4, A*1+0, L),))
    edges3 = e1.findAt(((+B/4, A*2+0, L), ), ((0.0, 3*A-A/2, L), ),((-B/4, A*2+0, L),))
    edges4 = e1.findAt(((+B/4, A*3+0, L), ), ((0.0, 4*A-A/2, L), ),((-B/4, A*3+0, L),),
                                                                ((+B/4, A*4+0, L), ),((-B/4, A*4+0, L),  ))

if E==5:
    edges1 = e1.findAt(((+B/4, A*0+0, L), ), ((0.0, A/2, L), ),((-B/4, A*0+0, L), ))
    edges2 = e1.findAt(((+B/4, A*1+0, L),  ),((0.0, 2*A-A/2, L), ),((-B/4, A*1+0, L),))
    edges3 = e1.findAt(((+B/4, A*2+0, L), ), ((0.0, 3*A-A/2, L), ),((-B/4, A*2+0, L),))
    edges4 = e1.findAt(((+B/4, A*3+0, L), ), ((0.0, 4*A-A/2, L), ),((-B/4, A*3+0, L), ))
    edges5 = e1.findAt(((+B/4, A*4+0, L),  ),((0.0,5*A-A/2, L), ),((-B/4, A*4+0, L),),
                                                                ((+B/4, A*5+0, L), ),((-B/4, A*5+0, L),  ))

if E==6:
    edges1 = e1.findAt(((+B/4, A*0+0, L), ), ((0.0, A/2, L), ),((-B/4, A*0+0, L), ))
    edges2 = e1.findAt(((+B/4, A*1+0, L),  ),((0.0, 2*A-A/2, L), ),((-B/4, A*1+0, L),))
    edges3 = e1.findAt(((+B/4, A*2+0, L), ), ((0.0, 3*A-A/2, L), ),((-B/4, A*2+0, L),))
    edges4 = e1.findAt(((+B/4, A*3+0, L), ), ((0.0, 4*A-A/2, L), ),((-B/4, A*3+0, L), ))
    edges5 = e1.findAt(((+B/4, A*4+0, L),  ),((0.0,5*A-A/2, L), ),((-B/4, A*4+0, L), ))
    edges6 = e1.findAt(((+B/4, A*5+0, L),  ),((0.0,6*A- A/2, L), ), ((-B/4, A*5+0, L),),
                                                                ((+B/4, A*6+0, L), ),((-B/4, A*6+0, L),  ))

if E==7:
    edges1 = e1.findAt(((+B/4, A*0+0, L),), ((0.0, A/2, L), ),((-B/4, A*0+0, L), ))
    edges2 = e1.findAt(((+B/4, A*1+0, L),),((0.0, 2*A-A/2, L), ),((-B/4, A*1+0, L),))
    edges3 = e1.findAt(((+B/4, A*2+0, L),), ((0.0, 3*A-A/2, L), ),((-B/4, A*2+0, L),))
    edges4 = e1.findAt(((+B/4, A*3+0, L),), ((0.0, 4*A-A/2, L), ),((-B/4, A*3+0, L), ))
    edges5 = e1.findAt(((+B/4, A*4+0, L),),((0.0,5*A-A/2, L), ),((-B/4, A*4+0, L), ))
    edges6 = e1.findAt(((+B/4, A*5+0, L),),((0.0,6*A- A/2, L), ), ((-B/4, A*5+0, L), ))
    edges7 = e1.findAt(((+B/4, A*6+0, L),),((0.0, 7*A-A/2, L), ), ((-B/4, A*6+0, L),),
                                                                ((+B/4, A*7+0, L), ),((-B/4, A*7+0, L),  ))


if E==8:
    edges1 = e1.findAt(((+B/4, A*0+0, L),), ((0.0, A/2, L), ),((-B/4, A*0+0, L), ))
    edges2 = e1.findAt(((+B/4, A*1+0, L),),((0.0, 2*A-A/2, L), ),((-B/4, A*1+0, L),))
    edges3 = e1.findAt(((+B/4, A*2+0, L),), ((0.0, 3*A-A/2, L), ),((-B/4, A*2+0, L),))
    edges4 = e1.findAt(((+B/4, A*3+0, L),), ((0.0, 4*A-A/2, L), ),((-B/4, A*3+0, L), ))
    edges5 = e1.findAt(((+B/4, A*4+0, L),),((0.0,5*A-A/2, L), ),((-B/4, A*4+0, L), ))
    edges6 = e1.findAt(((+B/4, A*5+0, L),),((0.0,6*A- A/2, L), ), ((-B/4, A*5+0, L), ))
    edges7 = e1.findAt(((+B/4, A*6+0, L),),((0.0, 7*A-A/2, L), ), ((-B/4, A*6+0, L), ))
    edges8 = e1.findAt(((+B/4, A*7+0, L),),((0.0, 8*A-A/2, L), ), ((-B/4, A*7+0, L),),
                                                                ((+B/4, A*8+0, L), ),((-B/4, A*8+0, L),  ))

if E==9:
    edges1 = e1.findAt(((+B/4, A*0+0, L),), ((0.0, A/2, L), ),((-B/4, A*0+0, L), ))
    edges2 = e1.findAt(((+B/4, A*1+0, L),),((0.0, 2*A-A/2, L), ),((-B/4, A*1+0, L),))
    edges3 = e1.findAt(((+B/4, A*2+0, L),), ((0.0, 3*A-A/2, L), ),((-B/4, A*2+0, L),))
    edges4 = e1.findAt(((+B/4, A*3+0, L),), ((0.0, 4*A-A/2, L), ),((-B/4, A*3+0, L), ))
    edges5 = e1.findAt(((+B/4, A*4+0, L),),((0.0,5*A-A/2, L), ),((-B/4, A*4+0, L), ))
    edges6 = e1.findAt(((+B/4, A*5+0, L),),((0.0,6*A- A/2, L), ), ((-B/4, A*5+0, L), ))
    edges7 = e1.findAt(((+B/4, A*6+0, L),),((0.0, 7*A-A/2, L), ), ((-B/4, A*6+0, L), ))
    edges8 = e1.findAt(((+B/4, A*7+0, L),),((0.0, 8*A-A/2, L), ), ((-B/4, A*7+0, L),  ))
    edges9 = e1.findAt(((+B/4, A*8+0, L),),((0.0, 9*A-A/2, L), ), ((-B/4, A*8+0, L),),
                                                                ((+B/4, A*9+0, L), ),((-B/4, A*9+0, L),  ))

if E ==10:
    edges1 = e1.findAt(((+B/4, A*0+0, L),), ((0.0, A/2, L), ),((-B/4, A*0+0, L), ))
    edges2 = e1.findAt(((+B/4, A*1+0, L),),((0.0, 2*A-A/2, L), ),((-B/4, A*1+0, L),))
    edges3 = e1.findAt(((+B/4, A*2+0, L),), ((0.0, 3*A-A/2, L), ),((-B/4, A*2+0, L),))
    edges4 = e1.findAt(((+B/4, A*3+0, L),), ((0.0, 4*A-A/2, L), ),((-B/4, A*3+0, L), ))
    edges5 = e1.findAt(((+B/4, A*4+0, L),),((0.0,5*A-A/2, L), ),((-B/4, A*4+0, L), ))
    edges6 = e1.findAt(((+B/4, A*5+0, L),),((0.0,6*A- A/2, L), ), ((-B/4, A*5+0, L), ))
    edges7 = e1.findAt(((+B/4, A*6+0, L),),((0.0, 7*A-A/2, L), ), ((-B/4, A*6+0, L), ))
    edges8 = e1.findAt(((+B/4, A*7+0, L),),((0.0, 8*A-A/2, L), ), ((-B/4, A*7+0, L), ))
    edges9 = e1.findAt(((+B/4, A*8+0, L),),((0.0, 9*A-A/2, L), ),((-B/4, A*8+0, L), ))
    edges10 = e1.findAt(((+B/4, A*9+0, L),),((0.0, 10*A-A/2, L), ),((-B/4, A*9, L),),
                                                                ((+B/4, A*10+0, L), ),((-B/4, A*10+0, L),  ))
if E == 1:
    a.Set(edges=edges1, name='Tsurface')
if E == 2:
    a.Set(edges=edges1 + edges2,
          name='Tsurface')
if E == 3:
    a.Set(edges=edges1 + edges2 + edges3,
          name='Tsurface')
if E == 4:
    a.Set(edges=edges1 + edges2 + edges3 + edges4,
          name='Tsurface')
if E == 5:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5,
        name='Tsurface')
if E == 6:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6,
        name='Tsurface')
if E == 7:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6 + edges7,
        name='Tsurface')
if E == 8:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6 + edges7 + edges8,
        name='Tsurface')
if E == 9:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6 + edges7 + edges8+ edges9,
        name='Tsurface')
if E == 10:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6 + edges7 + edges8+ edges9+ edges10,
        name='Tsurface')
# 底部
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
if E==1:
    edges1 = e1.findAt(((+B/4, A*0+0, 0), ), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0),),
                       ((+B/4, A*1+0, 0), ),((-B/4, A*1+0, 0),))

if E==2:
    edges1 = e1.findAt(((+B/4, A*0+0, 0), ), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0), ))
    edges2 = e1.findAt(((+B/4, A*1+0, 0),  ),((0.0, 2*A-A/2, 0), ),((-B/4, A*1+0, 0),),
                       ((+B/4, A*2+0, 0), ),((-B/4, A*2+0, 0),))

if E==3:
    edges1 = e1.findAt(((+B/4, A*0+0, 0), ), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0), ))
    edges2 = e1.findAt(((+B/4, A*1+0, 0),  ),((0.0, 2*A-A/2, 0), ),((-B/4, A*1+0, 0),))
    edges3 = e1.findAt(((+B/4, A*2+0, 0), ), ((0.0, 3*A-A/2, 0), ),((-B/4, A*2+0, 0),),
                       ((+B/4, A*3+0, 0), ),((-B/4, A*3+0, 0),))

if E==4:
    edges1 = e1.findAt(((+B/4, A*0+0, 0), ), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0), ))
    edges2 = e1.findAt(((+B/4, A*1+0, 0),  ),((0.0, 2*A-A/2, 0), ),((-B/4, A*1+0, 0),))
    edges3 = e1.findAt(((+B/4, A*2+0, 0), ), ((0.0, 3*A-A/2, 0), ),((-B/4, A*2+0, 0),))
    edges4 = e1.findAt(((+B/4, A*3+0, 0), ), ((0.0, 4*A-A/2, 0), ),((-B/4, A*3+0, 0),),
                       ((+B/4, A*4+0, 0), ),((-B/4, A*4+0, 0),))

if E==5:
    edges1 = e1.findAt(((+B/4, A*0+0, 0), ), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0), ))
    edges2 = e1.findAt(((+B/4, A*1+0, 0),  ),((0.0, 2*A-A/2, 0), ),((-B/4, A*1+0, 0),))
    edges3 = e1.findAt(((+B/4, A*2+0, 0), ), ((0.0, 3*A-A/2, 0), ),((-B/4, A*2+0, 0),))
    edges4 = e1.findAt(((+B/4, A*3+0, 0), ), ((0.0, 4*A-A/2, 0), ),((-B/4, A*3+0, 0), ))
    edges5 = e1.findAt(((+B/4, A*4+0, 0),  ),((0.0,5*A-A/2, 0), ),((-B/4, A*4+0, 0),),
                       ((+B/4, A*5+0, 0), ),((-B/4, A*5+0, 0),))

if E==6:
    edges1 = e1.findAt(((+B/4, A*0+0, 0), ), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0), ))
    edges2 = e1.findAt(((+B/4, A*1+0, 0),  ),((0.0, 2*A-A/2, 0), ),((-B/4, A*1+0, 0),))
    edges3 = e1.findAt(((+B/4, A*2+0, 0), ), ((0.0, 3*A-A/2, 0), ),((-B/4, A*2+0, 0),))
    edges4 = e1.findAt(((+B/4, A*3+0, 0), ), ((0.0, 4*A-A/2, 0), ),((-B/4, A*3+0, 0), ))
    edges5 = e1.findAt(((+B/4, A*4+0, 0),  ),((0.0,5*A-A/2, 0), ),((-B/4, A*4+0, 0), ))
    edges6 = e1.findAt(((+B/4, A*5+0, 0),  ),((0.0,6*A- A/2, 0), ), ((-B/4, A*5+0, 0),),
                       ((+B/4, A*6+0, 0), ),((-B/4, A*6+0, 0),))

if E==7:
    edges1 = e1.findAt(((+B/4, A*0+0, 0), ), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0), ))
    edges2 = e1.findAt(((+B/4, A*1+0, 0),  ),((0.0, 2*A-A/2, 0), ),((-B/4, A*1+0, 0),))
    edges3 = e1.findAt(((+B/4, A*2+0, 0), ), ((0.0, 3*A-A/2, 0), ),((-B/4, A*2+0, 0),))
    edges4 = e1.findAt(((+B/4, A*3+0, 0), ), ((0.0, 4*A-A/2, 0), ),((-B/4, A*3+0, 0), ))
    edges5 = e1.findAt(((+B/4, A*4+0, 0),  ),((0.0,5*A-A/2, 0), ),((-B/4, A*4+0, 0), ))
    edges6 = e1.findAt(((+B/4, A*5+0, 0),  ),((0.0,6*A- A/2, 0), ), ((-B/4, A*5+0, 0), ))
    edges7 = e1.findAt(((+B/4, A*6+0, 0),  ),((0.0, 7*A-A/2, 0), ), ((-B/4, A*6+0, 0),),
                       ((+B/4, A*7+0, 0), ),((-B/4, A*7+0, 0),))

if E==8:
    edges1 = e1.findAt(((+B/4, A*0+0, 0), ), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0), ))
    edges2 = e1.findAt(((+B/4, A*1+0, 0),  ),((0.0, 2*A-A/2, 0), ),((-B/4, A*1+0, 0),))
    edges3 = e1.findAt(((+B/4, A*2+0, 0), ), ((0.0, 3*A-A/2, 0), ),((-B/4, A*2+0, 0),))
    edges4 = e1.findAt(((+B/4, A*3+0, 0), ), ((0.0, 4*A-A/2, 0), ),((-B/4, A*3+0, 0), ))
    edges5 = e1.findAt(((+B/4, A*4+0, 0),  ),((0.0,5*A-A/2, 0), ),((-B/4, A*4+0, 0), ))
    edges6 = e1.findAt(((+B/4, A*5+0, 0),  ),((0.0,6*A- A/2, 0), ), ((-B/4, A*5+0, 0), ))
    edges7 = e1.findAt(((+B/4, A*6+0, 0),  ),((0.0, 7*A-A/2, 0), ), ((-B/4, A*6+0, 0), ))
    edges8 = e1.findAt(((+B/4, A*7+0, 0),  ),((0.0, 8*A-A/2, 0), ), ((-B/4, A*7+0, 0),),
                       ((+B/4, A*8+0, 0), ),((-B/4, A*8+0, 0),))

if E==9:
    edges1 = e1.findAt(((+B/4, A*0+0, 0), ), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0), ))
    edges2 = e1.findAt(((+B/4, A*1+0, 0),  ),((0.0, 2*A-A/2, 0), ),((-B/4, A*1+0, 0),))
    edges3 = e1.findAt(((+B/4, A*2+0, 0), ), ((0.0, 3*A-A/2, 0), ),((-B/4, A*2+0, 0),))
    edges4 = e1.findAt(((+B/4, A*3+0, 0), ), ((0.0, 4*A-A/2, 0), ),((-B/4, A*3+0, 0), ))
    edges5 = e1.findAt(((+B/4, A*4+0, 0),  ),((0.0,5*A-A/2, 0), ),((-B/4, A*4+0, 0), ))
    edges6 = e1.findAt(((+B/4, A*5+0, 0),  ),((0.0,6*A- A/2, 0), ), ((-B/4, A*5+0, 0), ))
    edges7 = e1.findAt(((+B/4, A*6+0, 0),  ),((0.0, 7*A-A/2, 0), ), ((-B/4, A*6+0, 0), ))
    edges8 = e1.findAt(((+B/4, A*7+0, 0),  ),((0.0, 8*A-A/2, 0), ), ((-B/4, A*7+0, 0), ))
    edges9 = e1.findAt(((+B/4, A*8+0, 0),  ),((0.0, 9*A-A/2, 0), ),((-B/4, A*8+0, 0), ),
                       ((+B/4, A*9+0, 0), ),((-B/4, A*9+0, 0),))

if E==10:
    edges1 = e1.findAt(((+B/4, A*0+0, 0),), ((0.0, A/2, 0), ),((-B/4, A*0+0, 0), ))
    edges2 = e1.findAt(((+B/4, A*1+0, 0),),((0.0, 2*A-A/2, 0), ),((-B/4, A*1+0, 0),))
    edges3 = e1.findAt(((+B/4, A*2+0, 0),), ((0.0, 3*A-A/2, 0), ),((-B/4, A*2+0, 0),))
    edges4 = e1.findAt(((+B/4, A*3+0, 0),), ((0.0, 4*A-A/2, 0), ),((-B/4, A*3+0, 0), ))
    edges5 = e1.findAt(((+B/4, A*4+0, 0),),((0.0,5*A-A/2, 0), ),((-B/4, A*4+0, 0), ))
    edges6 = e1.findAt(((+B/4, A*5+0, 0),),((0.0,6*A- A/2, 0), ), ((-B/4, A*5+0, 0), ))
    edges7 = e1.findAt(((+B/4, A*6+0, 0),),((0.0, 7*A-A/2, 0), ), ((-B/4, A*6+0, 0), ))
    edges8 = e1.findAt(((+B/4, A*7+0, 0),),((0.0, 8*A-A/2, 0), ), ((-B/4, A*7+0, 0), ))
    edges9 = e1.findAt(((+B/4, A*8+0, 0),),((0.0, 9*A-A/2, 0), ),((-B/4, A*8+0, 0), ))
    edges10 = e1.findAt(((+B/4, A*9+0, 0),),((0.0, 10*A-A/2, 0), ),((-B/4, A*9, 0),),
                                                                ((+B/4, A*10+0, 0), ),((-B/4, A*10+0, 0),  ))
if E==1:
    a.Set(edges=edges1, name='Bsurface')
if E == 2:
    a.Set(edges=edges1 + edges2,
          name='Bsurface')
if E == 3:
    a.Set(edges=edges1 + edges2 + edges3,
          name='Bsurface')
if E == 4:
    a.Set(edges=edges1 + edges2 + edges3 + edges4,
          name='Bsurface')
if E == 5:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5,
        name='Bsurface')
if E == 6:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6,
        name='Bsurface')
if E == 7:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6 + edges7,
        name='Bsurface')
if E == 8:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6 + edges7 + edges8,
        name='Bsurface')
if E == 9:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6 + edges7 + edges8+ edges9,
        name='Bsurface')
if E == 10:
    a.Set(
        edges=edges1 + edges2 + edges3 + edges4 + edges5 + edges6 + edges7 + edges8+ edges9+ edges10,
        name='Bsurface')

# # -----------
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['TTpoint']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['Tsurface']
mdb.models['Model-1'].MultipointConstraint(name='Constraint-1',
    controlPoint=region1, surface=region2, mpcType=BEAM_MPC,
    userMode=DOF_MODE_MPC, userType=0, csys=None)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['BBpoint']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['Bsurface']
mdb.models['Model-1'].MultipointConstraint(name='Constraint-2',
    controlPoint=region1, surface=region2, mpcType=BEAM_MPC,
    userMode=DOF_MODE_MPC, userType=0, csys=None)
# # 边界(加入配合荷载的语句判断）
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['TTpoint']
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial',
    region=region, u1=SET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET,
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
# # 依次判断修改边界条件
if cf1f != 0:
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', u1=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
if cf2f != 0:
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', u2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
# if cf3f != 0:
#     mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', u3=u3u)
# if ur2r != 0:
#     mdb.models['Model-1'].boundaryConditions['BC-2'].setValuesInStep(stepName='Step-1', ur2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
#     mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', ur2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
# 底部
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['BBpoint']
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial',
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET,
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)

# 荷载
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['TTpoint']
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1',
    region=region, cf1=cf1f, cf2=cf2f, cf3=cf3f, distributionType=UNIFORM,
    field='', localCsys=None)

#
# # # # ----------布置种子和划分网栄1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7�1�7
#
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=meshsz, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()

# # # # 提取模�
if E!=1:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(67, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 1:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(59, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
# # # # # JOB
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,
    numGPUs=0)
# 等待分析完成
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1'].waitForCompletion()
# # # 提取result
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF, optimizationTasks=OFF,
    geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(
    name='C:/Users/HPC/Desktop/Isight_Catia_Abaqus/Abaqus_dataTE/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['C:/Users/HPC/Desktop/Isight_Catia_Abaqus/Abaqus_dataTE/Job-1.odb']
session.fieldReportOptions.setValues(printXYData=OFF, printTotal=OFF)
session.writeFieldReport(
    fileName='C:/Users/HPC/Desktop/Isight_Catia_Abaqus/Abaqus_dataTE/Result1.rpt',
    append=OFF, sortItem='nodenumber', odb=odb, step=0, frame=1,
    outputPosition=NODAL, variable=(('U', NODAL),  ('UR', NODAL), ), stepFrame=SPECIFY)
# 存数据到数据庄�

session.writeFieldReport(
    fileName='C:/Users/HPC/Desktop/Isight_Catia_Abaqus/Abaqus_dataTE/picandcsv/'+'Elasticdata'+printname+'.csv',
    append=OFF, sortItem='结点编号', odb=odb, step=0, frame=1,
    outputPosition=NODAL, variable=(('U', NODAL), ('UR', NODAL),  ), stepFrame=SPECIFY)
# 存图
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/HPC/Desktop/Isight_Catia_Abaqus/Abaqus_dataTE/Job-1.odb'])
o3 = session.openOdb(
    name='C:/Users/HPC/Desktop/Isight_Catia_Abaqus/Abaqus_dataTE/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()

# 图片效果设置
session.graphicsOptions.setValues(backgroundStyle=SOLID,
    backgroundColor='#FFFFFF')
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadPosition=(8, 9), legendBox=ON, legendPosition=(2, 98), title=ON,
    statePosition=(13, 12), annotations=ON, compass=ON,
    triadFont='-*-verdana-bold-r-normal-*-*-120-*-*-p-*',
    stateFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*',
    titleFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*',
    legendFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*')
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    stateFont='-*-宋体-medium-r-normal-*-*-120-*-*-p-*-*-*')
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    statePosition=(13, 25))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    statePosition=(10, 25))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendFont='-*-times new roman-medium-r-normal-*-*-120-*-*-p-*-*-*')
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendBox=OFF, legendPosition=(10, 80), title=OFF)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadFont='-*-times new roman-bold-r-normal-*-*-120-*-*-p-*-*-*')
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    statePosition=(60, 20))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    triadPosition=(11, 10))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1000,
    farPlane=1001, width=1000, height=1000, cameraPosition=(L+E*A,
    -E*A, L*1.5), cameraUpVector=(0, 0, 50),
    cameraTarget=(0, E*A/2, L/2), viewOffsetX=0,
    viewOffsetY=0)
session.viewports['Viewport: 1'].view.fitView()
# 存图
session.printToFile(
    fileName='C:/Users/HPC/Desktop/Isight_Catia_Abaqus/Abaqus_dataTE/picandcsv/'+'Elastic'+printname+'.tiff',
    format=TIFF, canvasObjects=(session.viewports['Viewport: 1'], ))
mdb.saveAs(
    pathName='C:/Users/HPC/Desktop/Isight_Catia_Abaqus/Abaqus_dataTE/Elastic')
