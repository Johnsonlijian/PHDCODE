# -*- coding: mbcs -*-

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

A = 400  # H
B = 400  # B
C = 13.0  # t1
D = 21.0  # t2
L = 3000  # l`
E = 1  # 鎷兼帴鏁伴噺
F = 4  # 妯悜铻烘爴鏁伴噺锛堢珫鐩存柟鍚戯級
BoltD = 20     # 铻烘爴鐩村緞
BoltB = 0.0     # 铻烘爴涓績鎹畒=0鐨勬í鍚戣窛
sfricn = 0.35  # 鍒囧悜鎺ヨЕ鎽╂摝绯绘暟
pbol = 90.0      # 铻烘爴棰勭揣
yfss = 355.61  # 灞堟湇搴斿姏
yfsn = 0.023   # 灞堟湇搴斿彉骞冲彴灏鹃儴
yuss = 444.0  #锟勫簲
yusn = 0.1576   #锟勫簲
meshsz = 20    # 缃戞牸鍒掑垎灏哄
meshszb = 4    # 铻烘爴缃戞牸鍒掑垎灏哄
cf1f = 0.0
cf2f = 1.0
cf3f = 381462.847
u1u = 0.0
u2u = 1.0
u3u = 381462.847
trueu3 = 60.0
nodedeform = 6.0

printname='A'+str(A)+'B'+str(B)+'C'+str(C)+'D'+str(D)+'L'+str(L)+'E'+str(E)+'F'+str(F)+'BoltD'+str(BoltD)+'BoltB'\
          +str(BoltB)+'sfricn'+str(sfricn)+'pbol'+str(pbol)+'yfss'+str(yfss)+'yuss'+str(yuss)+'yusn'+str(yusn)\
          +'meshsz'+str(meshsz)+'cf1f'+str(cf1f)+'cf2f'+str(cf2f)+'cf3f'+str(cf3f)+'nodedeform'+str(nodedeform)
path = 'C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\picandcsv/'
namee = str(printname)
isExists = os.path.exists(path + namee)
if not isExists:
    os.makedirs(path + namee)
import os
os.chdir(r"C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\picandcsv/"+str(printname))

session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(0.0, D/2), point2=(B/2, D/2))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(0.0, D/2), point2=(-B/2, D/2))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.ParallelConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.Line(point1=(0.0, D/2), point2=(0.0, A-D/2))
s.PerpendicularConstraint(entity1=g[2], entity2=g[4], addUndoState=False)
s.Line(point1=(0.0, A-D/2), point2=(B/2, A-D/2))
s.HorizontalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.Line(point1=(0.0, A-D/2), point2=(-B/2, A-D/2))
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



#鏉愭枡鎴潰
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((205000.0, 0.3),
    ))
mdb.models['Model-1'].materials['Material-1'].Density(table=((7.85e-09, ), ))
# 鎴潰鍒涘缓
mdb.models['Model-1'].HomogeneousShellSection(name='websection',
    preIntegrate=OFF, material='Material-1', thicknessType=UNIFORM,
    thickness=C, thicknessField='', nodalThicknessField='',
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT,
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF,
    integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].HomogeneousShellSection(name='flangesection',
    preIntegrate=OFF, material='Material-1', thicknessType=UNIFORM,
    thickness=D, thicknessField='', nodalThicknessField='',
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT,
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF,
    integrationRule=SIMPSON, numIntPts=5)
# 鎴潰鎸囨淳
#鏉愭枡鎴潰
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((205000.0, 0.3),
    ))
mdb.models['Model-1'].materials['Material-1'].Density(table=((7.85e-09, ), ))
# 鎴潰鍒涘缓
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.findAt(((0.0, A/2, L/2), ))
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='websection', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.findAt(((-B/2, D/2, L/2), ), ((-B/2, A-D/2, L/2), ), ((B/2, A-D/2, L/2), ), ((B/2, D/2, L/2), ))
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='flangesection', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

# 瑁呴厤
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
a.Instance(name='Part-1-1', part=p, dependent=ON)
# 闃靛垪
a = mdb.models['Model-1'].rootAssembly
a.LinearInstancePattern(instanceList=('Part-1-1', ), direction1=(1.0, 0.0,
    0.0), direction2=(0.0, 1.0, 0.0), number1=1, number2=E, spacing1=100,
    spacing2=A)
# 闆嗗悎


# 鍒涘缓闈㈤泦(闇����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������介厤鍚堟潯浠跺垽鏂級
if E == 1:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    a.Set(edges=edges1, name='Tsurface')
    # 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    a.Set(edges=edges1, name='Bsurface')
elif E == 2:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    a.Set(edges=edges1 + edges2, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    a.Set(edges=edges1 + edges2, name='Bsurface')
elif E == 3:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),),( (B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3, name='Bsurface')
elif E == 4:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4, name='Bsurface')
elif E == 5:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5, name='Bsurface')
elif E == 6:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6, name='Bsurface')
elif E == 7:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    e7 = a.instances['Part-1-1-lin-1-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, L),), ((B / 4, 6*A + D / 2, L),), ((0, 6*A  + A / 2, L),),
                       ((-B / 4, 7 * A - D / 2, L),), ((B / 4, 7 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    e7 = a.instances['Part-1-1-lin-1-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, 0.0),), ((B / 4, 6*A + D / 2, 0.0),), ((0, 6*A  + A / 2, 0.0),),
                       ((-B / 4, 7 * A - D / 2, 0.0),), ((B / 4, 7 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7, name='Bsurface')
elif E == 8:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    e7 = a.instances['Part-1-1-lin-1-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, L),), ((B / 4, 6*A + D / 2, L),), ((0, 6*A  + A / 2, L),),
                       ((-B / 4, 7 * A - D / 2, L),), ((B / 4, 7 * A - D / 2, L),))
    e8 = a.instances['Part-1-1-lin-1-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, L),), ((B / 4, 7*A + D / 2, L),), ((0, 7*A  + A / 2, L),),
                       ((-B / 4, 8 * A - D / 2, L),), ((B / 4, 8 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    e7 = a.instances['Part-1-1-lin-1-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, 0.0),), ((B / 4, 6*A + D / 2, 0.0),), ((0, 6*A  + A / 2, 0.0),),
                       ((-B / 4, 7 * A - D / 2, 0.0),), ((B / 4, 7 * A - D / 2, 0.0),))
    e8 = a.instances['Part-1-1-lin-1-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, 0.0),), ((B / 4, 7*A + D / 2, 0.0),), ((0, 7*A  + A / 2, 0.0),),
                       ((-B / 4, 8 * A - D / 2, 0.0),), ((B / 4, 8 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8, name='Bsurface')
elif E == 9:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    e7 = a.instances['Part-1-1-lin-1-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, L),), ((B / 4, 6*A + D / 2, L),), ((0, 6*A  + A / 2, L),),
                       ((-B / 4, 7 * A - D / 2, L),), ((B / 4, 7 * A - D / 2, L),))
    e8 = a.instances['Part-1-1-lin-1-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, L),), ((B / 4, 7*A + D / 2, L),), ((0, 7*A  + A / 2, L),),
                       ((-B / 4, 8 * A - D / 2, L),), ((B / 4, 8 * A - D / 2, L),))
    e9 = a.instances['Part-1-1-lin-1-9'].edges
    edges9 = e9.findAt(((-B / 4, 8*A + D / 2, L),), ((B / 4, 8*A + D / 2, L),), ((0, 8*A  + A / 2, L),),
                       ((-B / 4, 9 * A - D / 2, L),), ((B / 4, 9 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8+ edges9, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    e7 = a.instances['Part-1-1-lin-1-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, 0.0),), ((B / 4, 6*A + D / 2, 0.0),), ((0, 6*A  + A / 2, 0.0),),
                       ((-B / 4, 7 * A - D / 2, 0.0),), ((B / 4, 7 * A - D / 2, 0.0),))
    e8 = a.instances['Part-1-1-lin-1-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, 0.0),), ((B / 4, 7*A + D / 2, 0.0),), ((0, 7*A  + A / 2, 0.0),),
                       ((-B / 4, 8 * A - D / 2, 0.0),), ((B / 4, 8 * A - D / 2, 0.0),))
    e9 = a.instances['Part-1-1-lin-1-9'].edges
    edges9 = e9.findAt(((-B / 4, 8*A + D / 2, 0.0),), ((B / 4, 8*A + D / 2, 0.0),), ((0, 8*A  + A / 2, 0.0),),
                       ((-B / 4, 9 * A - D / 2, 0.0),), ((B / 4, 9 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8+ edges9, name='Bsurface')
else:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    e7 = a.instances['Part-1-1-lin-1-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, L),), ((B / 4, 6*A + D / 2, L),), ((0, 6*A  + A / 2, L),),
                       ((-B / 4, 7 * A - D / 2, L),), ((B / 4, 7 * A - D / 2, L),))
    e8 = a.instances['Part-1-1-lin-1-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, L),), ((B / 4, 7*A + D / 2, L),), ((0, 7*A  + A / 2, L),),
                       ((-B / 4, 8 * A - D / 2, L),), ((B / 4, 8 * A - D / 2, L),))
    e9 = a.instances['Part-1-1-lin-1-9'].edges
    edges9 = e9.findAt(((-B / 4, 8*A + D / 2, L),), ((B / 4, 8*A + D / 2, L),), ((0, 8*A  + A / 2, L),),
                       ((-B / 4, 9 * A - D / 2, L),), ((B / 4, 9 * A - D / 2, L),))
    e10 = a.instances['Part-1-1-lin-1-10'].edges
    edges10 = e10.findAt(((-B / 4, 9*A + D / 2, L),), ((B / 4, 9*A + D / 2, L),), ((0, 9*A  + A / 2, L),),
                       ((-B / 4, 10 * A - D / 2, L),), ((B / 4, 10 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8+ edges9+ edges10, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-1-1-lin-1-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-1-1-lin-1-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-1-1-lin-1-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-1-1-lin-1-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-1-1-lin-1-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    e7 = a.instances['Part-1-1-lin-1-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, 0.0),), ((B / 4, 6*A + D / 2, 0.0),), ((0, 6*A  + A / 2, 0.0),),
                       ((-B / 4, 7 * A - D / 2, 0.0),), ((B / 4, 7 * A - D / 2, 0.0),))
    e8 = a.instances['Part-1-1-lin-1-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, 0.0),), ((B / 4, 7*A + D / 2, 0.0),), ((0, 7*A  + A / 2, 0.0),),
                       ((-B / 4, 8 * A - D / 2, 0.0),), ((B / 4, 8 * A - D / 2, 0.0),))
    e9 = a.instances['Part-1-1-lin-1-9'].edges
    edges9 = e9.findAt(((-B / 4, 8*A + D / 2, 0.0),), ((B / 4, 8*A + D / 2, 0.0),), ((0, 8*A  + A / 2, 0.0),),
                       ((-B / 4, 9 * A - D / 2, 0.0),), ((B / 4, 9 * A - D / 2, 0.0),))
    e10 = a.instances['Part-1-1-lin-1-10'].edges
    edges10 = e10.findAt(((-B / 4, 9*A + D / 2, 0.0),), ((B / 4, 9*A + D / 2, 0.0),), ((0, 9*A  + A / 2, 0.0),),
                       ((-B / 4, 10 * A - D / 2, 0.0),), ((B / 4, 10 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8+ edges9+ edges10, name='Bsurface')


# 闆嗙偣
# 椤堕儴
a1 = mdb.models['Model-1'].rootAssembly
a1.AttachmentPoints(name='RPR1', points=((0, A*E/2, L), ))
# 闆嗙偣
a1 = mdb.models['Model-1'].rootAssembly
v1 = a1.vertices
verts1 = v1.findAt(((0, A*E/2, L), ))
a1.Set(vertices=verts1, name='TTpoint')

# 搴曢儴
# a1 = mdb.models['Model-1'].rootAssembly
a1.AttachmentPoints(name='RPR2', points=((0, A*E/2, 0), ))
# 闆嗙偣
a1 = mdb.models['Model-1'].rootAssembly
v1 = a1.vertices
verts1 = v1.findAt(((0, A*E/2, 0), ))
a1.Set(vertices=verts1, name='BBpoint')

# # 鍒嗘瀽姝勶拷
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-2', previous='Initial',
    initialInc=0.00001, minInc=1e-08, maxInc=0.2)
mdb.models['Model-1'].BuckleStep(name='Step-1', previous='Step-2',
    numEigen=10, eigensolver=LANCZOS, minEigen=None, blockSize=DEFAULT,
    maxBlocks=DEFAULT)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')

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
# # 杈圭晫(鍔犲叆閰嶅悎鑽疯浇鐨勮鍙ュ垽鏂級
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['TTpoint']
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial',
    region=region, u1=SET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET,
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
# # 渚濇鍒ゆ柇淇敼杈圭晫鏉′欢
if cf1f != 0:
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', u1=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
if cf2f != 0:
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', u2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
# if cf3f != 0:
#     mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', u3=u3u)
# if ur2r != 0:
#     mdb.models['Model-1'].boundaryConditions['BC-2'].setValuesInStep(stepName='Step-1', ur2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
#     mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', ur2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
# 搴曢儴
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['BBpoint']
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial',
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET,
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)

# 鑽疯浇
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['TTpoint']
mdb.models['Model-1'].ConcentratedForce(name='Load-2', createStepName='Step-2',
    region=region, cf1=0, cf2=0, cf3=-cf3f, distributionType=UNIFORM,
    field='', localCsys=None)
mdb.models['Model-1'].ConcentratedForce(name='Load-1', createStepName='Step-1',
    region=region, cf1=cf1f, cf2=cf2f, cf3=0, distributionType=UNIFORM,
    field='', localCsys=None)

#
# # # # ----------甯冪疆绉嶅瓙鍜屽垝鍒嗙綉鏍����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������
#
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=meshsz, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()

# 鎺ヨЕ
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF,
    pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((
    sfricn, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION,
    fraction=0.005, elasticSlipStiffness=None)
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON,
    constraintEnforcementMethod=DEFAULT)
#: 鐩镐簰浣滅敤灞烇拷1锟������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������1" 宸插垱寤����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].ContactStd(name='Int-1', createStepName='Initial')
mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    stepName='Initial', assignments=((GLOBAL, SELF, 'IntProp-1'), ))

# # # # 鎻愬彇妯★拷
if E == 1:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(75, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 2:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(82, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 3:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(89, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 4:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(96, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 5:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(103, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 6:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(110, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 7:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(117, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 8:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(124, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 9:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(131, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 10:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(138  , """
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
# 绛夊緟鍒嗘瀽瀹屾垚
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1'].waitForCompletion()
# # # 鎻愬彇result
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF, optimizationTasks=OFF,
    geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(
    name='C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\picandcsv/'+str(printname)+'/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\picandcsv/'+str(printname)+'/Job-1.odb']
session.fieldReportOptions.setValues(printXYData=OFF, printTotal=OFF)
session.writeFieldReport(
    fileName='C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\Result1.rpt',
    append=OFF, sortItem='nodenumber', odb=odb, step=1, frame=1,
    outputPosition=NODAL, variable=(('U', NODAL),  ('UR', NODAL), ), stepFrame=SPECIFY)
# 瀛樻暟鎹埌鏁版嵁搴勶拷

session.writeFieldReport(
    fileName='C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\picandcsv/'+'Elasticdata'+printname+'.csv',
    append=OFF, sortItem='缁撶偣缂栧彿', odb=odb, step=1, frame=1,
    outputPosition=NODAL, variable=(('U', NODAL), ('UR', NODAL),  ), stepFrame=SPECIFY)
# 瀛樺浘
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\picandcsv/'+str(printname)+'/Job-1.odb'])
o3 = session.openOdb(
    name='C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\picandcsv/'+str(printname)+'/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()

# 鍥剧墖鏁堟灉璁剧疆
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
    stateFont='-*-瀹嬩綋-medium-r-normal-*-*-120-*-*-p-*-*-*')
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

# 瀛樺浘

session.printToFile(
    fileName='C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\picandcsv/'+'Elastic'+printname+'.tiff',
    format=TIFF, canvasObjects=(session.viewports['Viewport: 1'], ))
mdb.saveAs(
    pathName='C:\Users\HPCW\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEsepH\picandcsv/'+str(printname)+'/Elastic')
