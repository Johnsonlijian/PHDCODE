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

A = 1000  # H
B = 300  # B
C = 19.0  # t1
D = 36.0  # t2
L = 3000  # l`
E = 6  # 鎷兼帴鏁伴噺
F = 1  # 妯悜铻烘爴鏁伴噺锛堢珫鐩存柟鍚戯級
BoltD = 20     # 铻烘爴鐩村緞
BoltB = 56     # 铻烘爴涓績鎹畒=0鐨勬í鍚戣窛
sfricn = 0.35  # 鍒囧悜鎺ヨЕ鎽╂摝绯绘暟
pbol = 125000.0      # 铻烘爴棰勭揣
yfss = 355.61  # 灞堟湇搴斿姏
yfsn = 0.023   # 灞堟湇搴斿彉骞冲彴灏鹃儴
yuss = 444.0  #锟勫簲
yusn = 0.1576   #锟勫簲
meshsz = 40    # 缃戞牸鍒掑垎灏哄
meshszb = 4    # 铻烘爴缃戞牸鍒掑垎灏哄
cf1f = 1.0
cf2f = 1.0
cf3f = 0.0
u1u = 1.0
u2u = 1.0
u3u = 0.0
Imperfectfactor = 0.01
trueu3 = 60.0
nodedeform = 6.0



printname='A'+str(A)+'B'+str(B)+'C'+str(C)+'D'+str(D)+'L'+str(L)+'E'+str(E)+'F'+str(F)+'BoltD'+str(BoltD)+'BoltB'\
          +str(BoltB)+'sfricn'+str(sfricn)+'pbol'+str(pbol)+'yfss'+str(yfss)+'yuss'+str(yuss)+'yusn'+str(yusn)\
          +'meshsz'+str(meshsz)+'cf1f'+str(cf1f)+'cf2f'+str(cf2f)+'cf3f'+str(cf3f)+'Imperfectfactor'+str(Imperfectfactor)

path = 'C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/'
# 瀹氫箟鏂囦欢澶瑰悕绉��������������������������������
namee = str(printname)

isExists = os.path.exists(path + namee)
if not isExists:
    os.makedirs(path + namee)
import os
os.chdir(r"C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/"+str(printname))

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
p = mdb.models['Model-1'].parts['Part-1']
p.regenerate()

# #澶嶅埗part
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='Part-1-Copy',
    objectToCopy=mdb.models['Model-1'].parts['Part-1'])
session.viewports['Viewport: 1'].setValues(displayedObject=p)


# 鎵撳瓟璧峰part
p = mdb.models['Model-1'].parts['Part-1']
f, e = p.faces, p.edges
t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[3],
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(B/4, A-D/2, L/2))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=1091.12, gridSpacing=27.27, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.CircleByCenterPerimeter(center=(B/4-BoltB, 0), point1=(B/4-BoltB, BoltD/2))
s.CircleByCenterPerimeter(center=(B/4+BoltB, 0), point1=(B/4+BoltB, BoltD/2))
s.move(vector=(0.0, -L/2), objectList=(g[11], g[12]))

# 闃靛垪铻烘爴瀛��������������������������������
s.linearPattern(geomList=(g[11], g[12]), vertexList=(), number1=1,
    spacing1=109.112, angle1=0.0, number2=F+1, spacing2=L/(F+1), angle2=90.0)
s.delete(objectList=(g[11], g[12]))
p = mdb.models['Model-1'].parts['Part-1']
f1, e1 = p.faces, p.edges
p.CutExtrude(sketchPlane=f1[0], sketchUpEdge=e1[3], sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT, sketch=s, depth=D, flipExtrudeDirection=OFF)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

# 鎵撳瓟涓棿part
p = mdb.models['Model-1'].parts['Part-1-Copy']
f, e = p.faces, p.edges
t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[3],
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(B/4, A-D/2, L/2))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=1091.12, gridSpacing=27.27, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1-Copy']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.CircleByCenterPerimeter(center=(B/4-BoltB, 0), point1=(B/4-BoltB, BoltD/2))
s.CircleByCenterPerimeter(center=(B/4+BoltB, 0), point1=(B/4+BoltB, BoltD/2))
s.move(vector=(0.0, -L/2), objectList=(g[11], g[12]))

# 闃靛垪铻烘爴瀛��������������������������������
s.linearPattern(geomList=(g[11], g[12]), vertexList=(), number1=1,
    spacing1=109.112, angle1=0.0, number2=F+1, spacing2=L/(F+1), angle2=90.0)
s.delete(objectList=(g[11], g[12]))
p = mdb.models['Model-1'].parts['Part-1-Copy']
f1, e1 = p.faces, p.edges
p.CutExtrude(sketchPlane=f1[0], sketchUpEdge=e1[3], sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT, sketch=s, depth=A, flipExtrudeDirection=OFF)
s.unsetPrimaryObject()
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
# 鎴潰鍒涘缓涓よ竟
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

# 鎴潰鍒涘缓涓棿
p = mdb.models['Model-1'].parts['Part-1-Copy']
f = p.faces
faces = f.findAt(((0.0, A/2, L/2), ))
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-1-Copy']
p.SectionAssignment(region=region, sectionName='websection', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Part-1-Copy']
f = p.faces
faces = f.findAt(((-B/2, D/2, 1), ), ((-B/2, A-D/2, 1), ), ((B/2, A-D/2, 1), ), ((B/2, D/2, 1), ))
region = regionToolset.Region(faces=faces)
p = mdb.models['Model-1'].parts['Part-1-Copy']
p.SectionAssignment(region=region, sectionName='flangesection', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

# 瑁呴厤
if E == 1:
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a2 = mdb.models['Model-1'].rootAssembly
    a2.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1-Copy']
    a2.Instance(name='Part-1-Copy-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.fitView()
    mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-Copy-1',
                                                          toName='Part-1')

if E == 2:
    a1 = mdb.models['Model-1'].rootAssembly
    a1.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a1.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.fitView()
    mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-1',
                                                          toName='Part-1')

    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Part-1']
    a1.Instance(name='Part-1-1-lin-1-2', part=p, dependent=ON)
    p = a1.instances['Part-1-1-lin-1-2']
    p.translate(vector=(0, A, 0.0))
    session.viewports['Viewport: 1'].view.fitView()

    a1 = mdb.models['Model-1'].rootAssembly
    a1.rotate(instanceList=('Part-1-1-lin-1-2', ), axisPoint=(0, A+A/2, 0.0),
        axisDirection=(0.0, 0.0, 1.0), angle=180.0)
    mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-1-lin-1-2',
                                                          toName='Part-2')
if E == 3:
    a1 = mdb.models['Model-1'].rootAssembly
    a1.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a1.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.fitView()
    mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-1',
                                                          toName='Part-1')

    a2 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Part-1']
    a2.Instance(name='Part-1-1-lin-1-2', part=p, dependent=ON)
    p = a2.instances['Part-1-1-lin-1-2']

    a2 = mdb.models['Model-1'].rootAssembly
    a2.rotate(instanceList=('Part-1-1-lin-1-2',), axisPoint=(0.0, 0.0, 0.0),
              axisDirection=(1, 0, 0.0), angle=180.0)

    a2 = mdb.models['Model-1'].rootAssembly
    a2.translate(instanceList=('Part-1-1-lin-1-2',), vector=(0.0, 3 * A, L))
    mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-1-lin-1-2',
                                                          toName='Part-3')

    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Part-1-Copy']
    a1.Instance(name='Part-1-Copy-1', part=p, dependent=ON)
    p1 = a1.instances['Part-1-Copy-1']
    p1.translate(vector=(0, A, 0.0))
    session.viewports['Viewport: 1'].view.fitView()
    mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-Copy-1',
                                                          toName='Part-2')
if E >= 4:
    a1 = mdb.models['Model-1'].rootAssembly
    a1.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a1.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.fitView()

    a2 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Part-1']
    a2.Instance(name='Part-1-2', part=p, dependent=ON)
    p = a2.instances['Part-1-2']
    # p.translate(vector=(220.0, 0.0, 0.0))
    # session.viewports['Viewport: 1'].view.fitView()
    a2 = mdb.models['Model-1'].rootAssembly
    a2.rotate(instanceList=('Part-1-2',), axisPoint=(0.0, 0.0, 0.0),
              axisDirection=(1, 0, 0.0), angle=180.0)

    a2 = mdb.models['Model-1'].rootAssembly
    a2.translate(instanceList=('Part-1-2',), vector=(0.0, E* A, L))

    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['Part-1-Copy']
    a1.Instance(name='Part-1-Copy-1', part=p, dependent=ON)
    p1 = a1.instances['Part-1-Copy-1']
    p1.translate(vector=(0, A, 0.0))
    session.viewports['Viewport: 1'].view.fitView()

    # 闃靛垪
    a2 = mdb.models['Model-1'].rootAssembly
    a2.LinearInstancePattern(instanceList=('Part-1-Copy-1', ), direction1=(1.0,
        0.0, 0.0), direction2=(0.0, 1.0, 0.0), number1=1, number2=E-2, spacing1=0, spacing2=A)
    # 鏀瑰悕
    mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-1',
                                                          toName='Part-1')
    # 鏀瑰悕
    mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-Copy-1',
                                                          toName='Part-2')
    # # 鏀瑰悕
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-2', toName='Part-'+str(E))
    for i in range(E-3):
        mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Part-1-Copy-1-lin-1-'+str(i+2), toName='Part-'+str(i+3))

# 闆嗗悎

# 鍒涘缓闈㈤泦(闇勶拷閰嶅悎鏉′欢鍒ゆ柇锛��������������������������������
if E == 1:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    a.Set(edges=edges1, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    a.Set(edges=edges1, name='Bsurface')

elif E == 2:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    a.Set(edges=edges1 + edges2, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    a.Set(edges=edges1 + edges2, name='Bsurface')

elif E == 3:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3, name='Bsurface')

elif E == 4:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4, name='Bsurface')

elif E == 5:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5, name='Bsurface')

elif E == 6:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6, name='Bsurface')

elif E == 7:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    e7 = a.instances['Part-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, L),), ((B / 4, 6*A + D / 2, L),), ((0, 6*A  + A / 2, L),),
                       ((-B / 4, 7 * A - D / 2, L),), ((B / 4, 7 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    e7 = a.instances['Part-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, 0.0),), ((B / 4, 6*A + D / 2, 0.0),), ((0, 6*A  + A / 2, 0.0),),
                       ((-B / 4, 7 * A - D / 2, 0.0),), ((B / 4, 7 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7, name='Bsurface')

elif E == 8:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    e7 = a.instances['Part-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, L),), ((B / 4, 6*A + D / 2, L),), ((0, 6*A  + A / 2, L),),
                       ((-B / 4, 7 * A - D / 2, L),), ((B / 4, 7 * A - D / 2, L),))
    e8 = a.instances['Part-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, L),), ((B / 4, 7*A + D / 2, L),), ((0, 7*A  + A / 2, L),),
                       ((-B / 4, 8 * A - D / 2, L),), ((B / 4, 8 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    e7 = a.instances['Part-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, 0.0),), ((B / 4, 6*A + D / 2, 0.0),), ((0, 6*A  + A / 2, 0.0),),
                       ((-B / 4, 7 * A - D / 2, 0.0),), ((B / 4, 7 * A - D / 2, 0.0),))
    e8 = a.instances['Part-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, 0.0),), ((B / 4, 7*A + D / 2, 0.0),), ((0, 7*A  + A / 2, 0.0),),
                       ((-B / 4, 8 * A - D / 2, 0.0),), ((B / 4, 8 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8, name='Bsurface')

elif E == 9:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    e7 = a.instances['Part-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, L),), ((B / 4, 6*A + D / 2, L),), ((0, 6*A  + A / 2, L),),
                       ((-B / 4, 7 * A - D / 2, L),), ((B / 4, 7 * A - D / 2, L),))
    e8 = a.instances['Part-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, L),), ((B / 4, 7*A + D / 2, L),), ((0, 7*A  + A / 2, L),),
                       ((-B / 4, 8 * A - D / 2, L),), ((B / 4, 8 * A - D / 2, L),))
    e9 = a.instances['Part-9'].edges
    edges9 = e9.findAt(((-B / 4, 8*A + D / 2, L),), ((B / 4, 8*A + D / 2, L),), ((0, 8*A  + A / 2, L),),
                       ((-B / 4, 9 * A - D / 2, L),), ((B / 4, 9 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8+ edges9, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    e7 = a.instances['Part-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, 0.0),), ((B / 4, 6*A + D / 2, 0.0),), ((0, 6*A  + A / 2, 0.0),),
                       ((-B / 4, 7 * A - D / 2, 0.0),), ((B / 4, 7 * A - D / 2, 0.0),))
    e8 = a.instances['Part-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, 0.0),), ((B / 4, 7*A + D / 2, 0.0),), ((0, 7*A  + A / 2, 0.0),),
                       ((-B / 4, 8 * A - D / 2, 0.0),), ((B / 4, 8 * A - D / 2, 0.0),))
    e9 = a.instances['Part-9'].edges
    edges9 = e9.findAt(((-B / 4, 8*A + D / 2, 0.0),), ((B / 4, 8*A + D / 2, 0.0),), ((0, 8*A  + A / 2, 0.0),),
                       ((-B / 4, 9 * A - D / 2, 0.0),), ((B / 4, 9 * A - D / 2, 0.0),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8+ edges9, name='Bsurface')

else:
# 椤堕儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, L),), ((B/4, D/2, L),),  ((0, A/2,L),),
                   ((-B/4, A-D/2, L),),  ((B/4, A-D/2, L),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, L),), ((B/4, A+D/2, L),), ((0, A+A/2,L),),
                   ((-B/4, 2*A-D/2, L),), ((B/4, 2*A-D/2, L),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, L),), ((B / 4, 2*A + D / 2, L),), ((0, 2*A + A / 2, L),),
                       ((-B / 4, 3 * A - D / 2, L),), ((B / 4, 3 * A - D / 2, L),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, L),), ((B / 4, 3*A + D / 2, L),), ((0, 3*A  + A / 2, L),),
                       ((-B / 4, 4 * A - D / 2, L),), ((B / 4, 4 * A - D / 2, L),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, L),), ((B / 4, 4*A + D / 2, L),), ((0, 4*A  + A / 2, L),),
                       ((-B / 4, 5 * A - D / 2, L),), ((B / 4, 5 * A - D / 2, L),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, L),), ((B / 4, 5*A + D / 2, L),), ((0, 5*A  + A / 2, L),),
                       ((-B / 4, 6 * A - D / 2, L),), ((B / 4, 6 * A - D / 2, L),))
    e7 = a.instances['Part-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, L),), ((B / 4, 6*A + D / 2, L),), ((0, 6*A  + A / 2, L),),
                       ((-B / 4, 7 * A - D / 2, L),), ((B / 4, 7 * A - D / 2, L),))
    e8 = a.instances['Part-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, L),), ((B / 4, 7*A + D / 2, L),), ((0, 7*A  + A / 2, L),),
                       ((-B / 4, 8 * A - D / 2, L),), ((B / 4, 8 * A - D / 2, L),))
    e9 = a.instances['Part-9'].edges
    edges9 = e9.findAt(((-B / 4, 8*A + D / 2, L),), ((B / 4, 8*A + D / 2, L),), ((0, 8*A  + A / 2, L),),
                       ((-B / 4, 9 * A - D / 2, L),), ((B / 4, 9 * A - D / 2, L),))
    e10 = a.instances['Part-10'].edges
    edges10 = e10.findAt(((-B / 4, 9*A + D / 2, L),), ((B / 4, 9*A + D / 2, L),), ((0, 9*A  + A / 2, L),),
                       ((-B / 4, 10 * A - D / 2, L),), ((B / 4, 10 * A - D / 2, L),))
    a.Set(edges=edges1 + edges2+ edges3+ edges4+ edges5+ edges6+ edges7+ edges8+ edges9+ edges10, name='Tsurface')
# 搴曢儴
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1'].edges
    edges1 = e1.findAt(((-B/4, D/2, 0.0),), ((B/4, D/2, 0.0),), ((0, A/2,0.0),),
                   ((-B/4, A-D/2, 0.0),), ((B/4, A-D/2, 0.0),))
    e2 = a.instances['Part-2'].edges
    edges2 = e2.findAt(((-B/4, A+D/2, 0.0),), ((B/4, A+D/2, 0.0),), ((0, A+A/2,0.0),),
                   ((-B/4, 2*A-D/2, 0.0),), ((B/4, 2*A-D/2, 0.0),))
    e3 = a.instances['Part-3'].edges
    edges3 = e3.findAt(((-B / 4, 2*A + D / 2, 0.0),), ((B / 4, 2*A + D / 2, 0.0),), ((0, 2*A + A / 2, 0.0),),
                       ((-B / 4, 3 * A - D / 2, 0.0),), ((B / 4, 3 * A - D / 2, 0.0),))
    e4 = a.instances['Part-4'].edges
    edges4 = e4.findAt(((-B / 4, 3*A + D / 2, 0.0),), ((B / 4, 3*A + D / 2, 0.0),), ((0, 3*A  + A / 2, 0.0),),
                       ((-B / 4, 4 * A - D / 2, 0.0),), ((B / 4, 4 * A - D / 2, 0.0),))
    e5 = a.instances['Part-5'].edges
    edges5 = e5.findAt(((-B / 4, 4*A + D / 2, 0.0),), ((B / 4, 4*A + D / 2, 0.0),), ((0, 4*A  + A / 2, 0.0),),
                       ((-B / 4, 5 * A - D / 2, 0.0),), ((B / 4, 5 * A - D / 2, 0.0),))
    e6 = a.instances['Part-6'].edges
    edges6 = e6.findAt(((-B / 4, 5*A + D / 2, 0.0),), ((B / 4, 5*A + D / 2, 0.0),), ((0, 5*A  + A / 2, 0.0),),
                       ((-B / 4, 6 * A - D / 2, 0.0),), ((B / 4, 6 * A - D / 2, 0.0),))
    e7 = a.instances['Part-7'].edges
    edges7 = e7.findAt(((-B / 4, 6*A + D / 2, 0.0),), ((B / 4, 6*A + D / 2, 0.0),), ((0, 6*A  + A / 2, 0.0),),
                       ((-B / 4, 7 * A - D / 2, 0.0),), ((B / 4, 7 * A - D / 2, 0.0),))
    e8 = a.instances['Part-8'].edges
    edges8 = e8.findAt(((-B / 4, 7*A + D / 2, 0.0),), ((B / 4, 7*A + D / 2, 0.0),), ((0, 7*A  + A / 2, 0.0),),
                       ((-B / 4, 8 * A - D / 2, 0.0),), ((B / 4, 8 * A - D / 2, 0.0),))
    e9 = a.instances['Part-9'].edges
    edges9 = e9.findAt(((-B / 4, 8*A + D / 2, 0.0),), ((B / 4, 8*A + D / 2, 0.0),), ((0, 8*A  + A / 2, 0.0),),
                       ((-B / 4, 9 * A - D / 2, 0.0),), ((B / 4, 9 * A - D / 2, 0.0),))
    e10 = a.instances['Part-10'].edges
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



#  ----------甯冪疆绉嶅瓙鍜孧ESH锛圥ART-1-copy锛��������������������������������
#浣跨敤鑽夊浘鍒嗗尯
# 杩戞
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
p = mdb.models['Model-1'].parts['Part-1-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
f, e2, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(1, D/2,
    0), normal=(0.0, -1.0, 0.0)), sketchUpEdge=e2.findAt(coordinates=(
    B/2, D/2, L/4)), sketchPlaneSide=SIDE1, origin=(0, D/2, 0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=2084.8, gridSpacing=52.12, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1-Copy']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
# 鍋氳灪鏍撳附鐨勯潰
# 杩欓噷BoltD/1.2浠ｈ〃铻哄附瀵硅竟璺濈s鏄灪鏍撶殑BoltD/0.6鍊嶏紝鐒跺悗鍙樺崐寰��������������������������������
for i in range(F):
    s.CircleByCenterPerimeter(center=(BoltB, (i+1)*L/(F+1)), point1=(BoltB, (i+1)*L/(F+1)-BoltD/1.2))
# 绔栧悜鍒嗗尯
s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
    number1=2, spacing1=BoltB-BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
    number1=2, spacing1=BoltB+BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
    number1=2, spacing1=BoltB, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
# 姘村钩鍒嗗尯
s.linearPattern(geomList=(g.findAt((1, 0)), ), vertexList=(),
    number1=1, spacing1=20.0, angle1=0.0, number2=F+1, spacing2=L/(F+1),
    angle2=90.0)
for i in range(F):
    p = mdb.models['Model-1'].parts['Part-1-Copy']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)+BoltD/1.2), objectList=(g.findAt((1, 0)), ))
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)-BoltD/1.2), objectList=(g.findAt((1, 0)), ))
p = mdb.models['Model-1'].parts['Part-1-Copy']
f = p.faces
pickedFaces = f.findAt(((1, D/2, L/2), ))
e3, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e3.findAt(coordinates=(B/2, D/2, L/2)),
    faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
# # 杩戣礋
p = mdb.models['Model-1'].parts['Part-1-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
f, e2, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(-1, D/2,
    0), normal=(0.0, -1.0, 0.0)), sketchUpEdge=e2.findAt(coordinates=(
    B/2, D/2, L/4)), sketchPlaneSide=SIDE1, origin=(0, D/2, 0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=2084.8, gridSpacing=52.12, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1-Copy']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
# 鍋氳灪鏍撳附鐨勯潰
# 杩欓噷BoltD/1.2浠ｈ〃铻哄附瀵硅竟璺濈s鏄灪鏍撶殑BoltD/0.6鍊嶏紝鐒跺悗鍙樺崐寰��������������������������������
for i in range(F):
    s.CircleByCenterPerimeter(center=(-BoltB, (i+1)*L/(F+1)), point1=(-BoltB, (i+1)*L/(F+1)-BoltD/1.2))
# 绔栧悜鍒嗗尯
s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
    number1=2, spacing1=B/2-BoltB-BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
    number1=2, spacing1=B/2-BoltB, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
    number1=2, spacing1=B/2-BoltB+BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
# 姘村钩鍒嗗尯
s.linearPattern(geomList=(g.findAt((-1, 0)), ), vertexList=(),
    number1=1, spacing1=20.0, angle1=0.0, number2=F+1, spacing2=L/(F+1),
    angle2=90.0)
for i in range (F):
    p = mdb.models['Model-1'].parts['Part-1-Copy']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)+BoltD/1.2), objectList=(g.findAt((-1, 0)), ))
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)-BoltD/1.2), objectList=(g.findAt((-1, 0)), ))
p = mdb.models['Model-1'].parts['Part-1-Copy']
f = p.faces
pickedFaces = f.findAt(((-1, D/2, L/2), ))
e3, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e3.findAt(coordinates=(B/2,  D/2, L/2)),
    faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
# # 杩滄
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
p = mdb.models['Model-1'].parts['Part-1-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
f, e2, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(1, A-D/2,
    0), normal=(0.0, -1.0, 0.0)), sketchUpEdge=e2.findAt(coordinates=(
    B/2, A-D/2, L/4)), sketchPlaneSide=SIDE1, origin=(0, A-D/2, 0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=2084.8, gridSpacing=52.12, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1-Copy']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
# 鍋氳灪鏍撳附鐨勯潰
# 杩欓噷BoltD/1.2浠ｈ〃铻哄附瀵硅竟璺濈s鏄灪鏍撶殑BoltD/0.6鍊嶏紝鐒跺悗鍙樺崐寰��������������������������������
for i in range(F):
    s.CircleByCenterPerimeter(center=(BoltB, (i+1)*L/(F+1)), point1=(BoltB, (i+1)*L/(F+1)-BoltD/1.2))
# 绔栧悜鍒嗗尯
s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
    number1=2, spacing1=BoltB-BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
    number1=2, spacing1=BoltB+BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
    number1=2, spacing1=BoltB, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
# 姘村钩鍒嗗尯
s.linearPattern(geomList=(g.findAt((1, 0)), ), vertexList=(),
    number1=1, spacing1=20.0, angle1=0.0, number2=F+1, spacing2=L/(F+1),
    angle2=90.0)
for i in range(F):
    p = mdb.models['Model-1'].parts['Part-1-Copy']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)+BoltD/1.2), objectList=(g.findAt((1, 0)), ))
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)-BoltD/1.2), objectList=(g.findAt((1, 0)), ))
p = mdb.models['Model-1'].parts['Part-1-Copy']
f = p.faces
pickedFaces = f.findAt(((1, A-D/2, L/2), ))
e3, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e3.findAt(coordinates=(B/2, A-D/2, L/2)),
    faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
# # 杩滆礋
p = mdb.models['Model-1'].parts['Part-1-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
f, e2, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(-1, A-D/2,
    0), normal=(0.0, -1.0, 0.0)), sketchUpEdge=e2.findAt(coordinates=(
    B/2, A-D/2, L/4)), sketchPlaneSide=SIDE1, origin=(0, A-D/2, 0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=2084.8, gridSpacing=52.12, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1-Copy']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
# 鍋氳灪鏍撳附鐨勯潰
# 杩欓噷BoltD/1.2浠ｈ〃铻哄附瀵硅竟璺濈s鏄灪鏍撶殑BoltD/0.6鍊嶏紝鐒跺悗鍙樺崐寰��������������������������������
for i in range(F):
    s.CircleByCenterPerimeter(center=(-BoltB, (i+1)*L/(F+1)), point1=(-BoltB, (i+1)*L/(F+1)-BoltD/1.2))
# 绔栧悜鍒嗗尯
s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
    number1=2, spacing1=B/2-BoltB-BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
    number1=2, spacing1=B/2-BoltB, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
    number1=2, spacing1=B/2-BoltB+BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
# 姘村钩鍒嗗尯
s.linearPattern(geomList=(g.findAt((-1, 0)), ), vertexList=(),
    number1=1, spacing1=20.0, angle1=0.0, number2=F+1, spacing2=L/(F+1),
    angle2=90.0)
for i in range (F):
    p = mdb.models['Model-1'].parts['Part-1-Copy']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)+BoltD/1.2), objectList=(g.findAt((-1, 0)), ))
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)-BoltD/1.2), objectList=(g.findAt((-1, 0)), ))
p = mdb.models['Model-1'].parts['Part-1-Copy']
f = p.faces
pickedFaces = f.findAt(((-1, A-D/2, L/2), ))
e3, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e3.findAt(coordinates=(B/2,  A-D/2, L/2)),
    faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']


#  ----------鍒掑垎锛圥ART-1锛��������������������������������
#浣跨敤鑽夊浘鍒嗗尯
# 杩戞(杩欓儴鍒嗕笉闇��������������������������������斤級
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
f, e2, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(1, D/2,
    0), normal=(0.0, -1.0, 0.0)), sketchUpEdge=e2.findAt(coordinates=(
    B/2, D/2, L/4)), sketchPlaneSide=SIDE1, origin=(0, D/2, 0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=2084.8, gridSpacing=52.12, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
# 鍋氳灪鏍撳附鐨勯潰
# 杩欓噷BoltD/1.2浠ｈ〃铻哄附瀵硅竟璺濈s鏄灪鏍撶殑BoltD/0.6鍊嶏紝鐒跺悗鍙樺崐寰��������������������������������
# for i in range(F):
#     s.CircleByCenterPerimeter(center=(BoltB, (i+1)*L/(F+1)), point1=(BoltB, (i+1)*L/(F+1)-BoltD/1.2))
# 绔栧悜鍒嗗尯
# s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
#     number1=2, spacing1=BoltB-BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
#     angle2=0)
# s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
#     number1=2, spacing1=BoltB+BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
#     angle2=0)
# s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
#     number1=2, spacing1=BoltB, angle1=0, number2=1, spacing2=208.48,
#     angle2=0)
# 姘村钩鍒嗗尯
s.linearPattern(geomList=(g.findAt((1, 0)), ), vertexList=(),
    number1=1, spacing1=20.0, angle1=0.0, number2=F+1, spacing2=L/(F+1),
    angle2=90.0)
for i in range(F):
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)+BoltD/1.2), objectList=(g.findAt((1, 0)), ))
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)-BoltD/1.2), objectList=(g.findAt((1, 0)), ))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces = f.findAt(((1, D/2, L/2), ))
e3, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e3.findAt(coordinates=(B/2, D/2, L/2)),
    faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
# # 杩戣礋
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
f, e2, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(-1, D/2,
    0), normal=(0.0, -1.0, 0.0)), sketchUpEdge=e2.findAt(coordinates=(
    B/2, D/2, L/4)), sketchPlaneSide=SIDE1, origin=(0, D/2, 0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=2084.8, gridSpacing=52.12, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
# 鍋氳灪鏍撳附鐨勯潰
# 杩欓噷BoltD/1.2浠ｈ〃铻哄附瀵硅竟璺濈s鏄灪鏍撶殑BoltD/0.6鍊嶏紝鐒跺悗鍙樺崐寰��������������������������������
# for i in range(F):
#     s.CircleByCenterPerimeter(center=(-BoltB, (i+1)*L/(F+1)), point1=(-BoltB, (i+1)*L/(F+1)-BoltD/1.2))
# 绔栧悜鍒嗗尯
# s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
#     number1=2, spacing1=B/2-BoltB-BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
#     angle2=0)
# s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
#     number1=2, spacing1=B/2-BoltB, angle1=0, number2=1, spacing2=208.48,
#     angle2=0)
# s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
#     number1=2, spacing1=B/2-BoltB+BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
#     angle2=0)
# 姘村钩鍒嗗尯
s.linearPattern(geomList=(g.findAt((-1, 0)), ), vertexList=(),
    number1=1, spacing1=20.0, angle1=0.0, number2=F+1, spacing2=L/(F+1),
    angle2=90.0)
for i in range (F):
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)+BoltD/1.2), objectList=(g.findAt((-1, 0)), ))
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)-BoltD/1.2), objectList=(g.findAt((-1, 0)), ))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces = f.findAt(((-1, D/2, L/2), ))
e3, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e3.findAt(coordinates=(B/2,  D/2, L/2)),
    faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
# # 杩滄
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
f, e2, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(1, A-D/2,
    0), normal=(0.0, -1.0, 0.0)), sketchUpEdge=e2.findAt(coordinates=(
    B/2, A-D/2, L/4)), sketchPlaneSide=SIDE1, origin=(0, A-D/2, 0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=2084.8, gridSpacing=52.12, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
# 鍋氳灪鏍撳附鐨勯潰
# 杩欓噷BoltD/1.2浠ｈ〃铻哄附瀵硅竟璺濈s鏄灪鏍撶殑BoltD/0.6鍊嶏紝鐒跺悗鍙樺崐寰��������������������������������
for i in range(F):
    s.CircleByCenterPerimeter(center=(BoltB, (i+1)*L/(F+1)), point1=(BoltB, (i+1)*L/(F+1)-BoltD/1.2))
# 绔栧悜鍒嗗尯
s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
    number1=2, spacing1=BoltB-BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
    number1=2, spacing1=BoltB+BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((0, 1)), ), vertexList=(),
    number1=2, spacing1=BoltB, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
# 姘村钩鍒嗗尯
s.linearPattern(geomList=(g.findAt((1, 0)), ), vertexList=(),
    number1=1, spacing1=20.0, angle1=0.0, number2=F+1, spacing2=L/(F+1),
    angle2=90.0)
for i in range(F):
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)+BoltD/1.2), objectList=(g.findAt((1, 0)), ))
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)-BoltD/1.2), objectList=(g.findAt((1, 0)), ))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces = f.findAt(((1, A-D/2, L/2), ))
e3, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e3.findAt(coordinates=(B/2, A-D/2, L/2)),
    faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
# # 杩滆礋
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
f, e2, d = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f.findAt(coordinates=(-1, A-D/2,
    0), normal=(0.0, -1.0, 0.0)), sketchUpEdge=e2.findAt(coordinates=(
    B/2, A-D/2, L/4)), sketchPlaneSide=SIDE1, origin=(0, A-D/2, 0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
    sheetSize=2084.8, gridSpacing=52.12, transform=t)
g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
# 鍋氳灪鏍撳附鐨勯潰
# 杩欓噷BoltD/1.2浠ｈ〃铻哄附瀵硅竟璺濈s鏄灪鏍撶殑BoltD/0.6鍊嶏紝鐒跺悗鍙樺崐寰��������������������������������
for i in range(F):
    s.CircleByCenterPerimeter(center=(-BoltB, (i+1)*L/(F+1)), point1=(-BoltB, (i+1)*L/(F+1)-BoltD/1.2))
# 绔栧悜鍒嗗尯
s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
    number1=2, spacing1=B/2-BoltB-BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
    number1=2, spacing1=B/2-BoltB, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
s.linearPattern(geomList=(g.findAt((-B/2, 1)), ), vertexList=(),
    number1=2, spacing1=B/2-BoltB+BoltD/1.2, angle1=0, number2=1, spacing2=208.48,
    angle2=0)
# 姘村钩鍒嗗尯
s.linearPattern(geomList=(g.findAt((-1, 0)), ), vertexList=(),
    number1=1, spacing1=20.0, angle1=0.0, number2=F+1, spacing2=L/(F+1),
    angle2=90.0)
for i in range (F):
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)+BoltD/1.2), objectList=(g.findAt((-1, 0)), ))
    s.copyMove(vector=(0.0, (i+1)*L/(F+1)-BoltD/1.2), objectList=(g.findAt((-1, 0)), ))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces = f.findAt(((-1, A-D/2, L/2), ))
e3, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e3.findAt(coordinates=(B/2,  A-D/2, L/2)),
    faces=pickedFaces, sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

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
# 鐩镐簰浣滅敤灞濱ntProp-1" 宸插垱寤��������������������������������
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].ContactStd(name='Int-1', createStepName='Initial')
mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    stepName='Initial', assignments=((GLOBAL, SELF, 'IntProp-1'), ))

# #甯冪疆鍙傦拷1锟��������������������������������界偣閲囩敤杩炴帴鍣ㄦā鎷熻灪鏍��������������������������������
# 鎵归噺寤虹珛鍙傦拷1锟��������������������������������界偣
if E==1:
    for i in range(E-1):
    # 绗竴缁勬嫾鎺ョ晫闈��������������������������������
        for j in range(F):
            a1 = mdb.models['Model-1'].rootAssembly
            e1 = a1.instances['Part-1-1-lin-1-2'].edges
            a1.ReferencePoint(point=a1.instances['Part-1-1-lin-1-2'].InterestingPoint(
                edge=e1.findAt(coordinates=(-BoltB, (i+1)*A-D/2, (j+1)*L/j*F)), rule=CENTER))
            a1 = mdb.models['Model-1'].rootAssembly
            e1 = a1.instances['Part-1-1'].edges
            a1.ReferencePoint(point=a1.instances['Part-1-1'].InterestingPoint(
                edge=e1.findAt(coordinates=(-BoltB, (i+1)*A-D/2, (j+1)*L/j*F)), rule=CENTER))
            a1 = mdb.models['Model-1'].rootAssembly
            e1 = a1.instances['Part-1-1-lin-1-2'].edges
            a1.ReferencePoint(point=a1.instances['Part-1-1-lin-1-2'].InterestingPoint(
                edge=e1.findAt(coordinates=(BoltB, (i+1)*A-D/2, (j+1)*L/j*F)), rule=CENTER))
            a1 = mdb.models['Model-1'].rootAssembly
            e1 = a1.instances['Part-1-1'].edges
            a1.ReferencePoint(point=a1.instances['Part-1-1'].InterestingPoint(
                edge=e1.findAt(coordinates=(BoltB, (i+1)*A-D/2, (j+1)*L/j*F)), rule=CENTER))
if E >= 2:
    for i in range(1, E-1):
        for j in range(F):
            a1 = mdb.models['Model-1'].rootAssembly
            e1 = a1.instances['Part-'+str(i)].edges
            a1.ReferencePoint(point=a1.instances['Part-'+str(i)].InterestingPoint(
                edge=e1.findAt(coordinates=(-(BoltB+BoltD/2), (i)*A-D/2, (j+1)*(L/(F+1)))), rule=CENTER))
            a1 = mdb.models['Model-1'].rootAssembly
            e1 = a1.instances['Part-'+str(i+1)].edges
            a1.ReferencePoint(point=a1.instances['Part-'+str(i+1)].InterestingPoint(
                edge=e1.findAt(coordinates=(-BoltB-BoltD/2, (i)*A+D/2, (j+1)*(L/(F+1)))), rule=CENTER))
            a1 = mdb.models['Model-1'].rootAssembly
            e1 = a1.instances['Part-'+str(i)].edges
            a1.ReferencePoint(point=a1.instances['Part-'+str(i)].InterestingPoint(
                edge=e1.findAt(coordinates=((BoltB+BoltD/2), (i)*A-D/2, (j+1)*(L/(F+1)))), rule=CENTER))
            a1 = mdb.models['Model-1'].rootAssembly
            e1 = a1.instances['Part-'+str(i+1)].edges
            a1.ReferencePoint(point=a1.instances['Part-'+str(i+1)].InterestingPoint(
                edge=e1.findAt(coordinates=((BoltB+BoltD/2), (i)*A+D/2, (j+1)*(L/(F+1)))), rule=CENTER))
# 灏嗙瑳鍗″皵杩炴帴鍣ㄨ祴浜堝嚑浣��������������������������������
# if E >= 2:
#     for i in range(E-1):
#         for j in range(F):
#             a1 = mdb.models['Model-1'].rootAssembly
#             e1 = a1.edges
#             edges1 = e1.findAt(((BoltB, (i+1)*A, (j+1)*(L/(F+1))), ))
#             region1=regionToolset.Region(edges=edges1)
#             csa = a1.SectionAssignment(sectionName='ConnSect-1', region=region1)
#             edges2 = e1.findAt(((-BoltB, (i+1)*A, (j+1)*(L/(F+1))), ))
#             region2=regionToolset.Region(edges=edges1)
#             csa = a1.SectionAssignment(sectionName='ConnSect-1', region=region2)

# 灏唕p鐐硅祴浜坅ttachment
attachmentnum = 1
if E >= 2:
    for i in range(E-1):
        for j in range(F):
            a1 = mdb.models['Model-1'].rootAssembly
            a1.AttachmentPoints(name='Attachment Points-'+str(attachmentnum), points=((-BoltB, (i+1)*A-D/2, (j+1)*(L/(F+1))),))
            a1 = mdb.models['Model-1'].rootAssembly
            a1.AttachmentPoints(name='Attachment Points-'+str(attachmentnum+1), points=((-BoltB, (i+1)*A+D/2, (j+1)*(L/(F+1))),))
            a1 = mdb.models['Model-1'].rootAssembly
            a1.AttachmentPoints(name='Attachment Points-'+str(attachmentnum+2), points=((BoltB, (i+1)*A-D/2, (j+1)*(L/(F+1))),))
            a1 = mdb.models['Model-1'].rootAssembly
            a1.AttachmentPoints(name='Attachment Points-'+str(attachmentnum+3), points=((BoltB, (i+1)*A+D/2, (j+1)*(L/(F+1))),))
            attachmentnum += 4

# 寤虹珛瀛旇竟鍙楀帇闈㈠拰attachment鐐逛箣闂寸殑鐩镐簰浣滅敤鑱旂郴
rpn = 1
if E >= 2:
    for i in range(E-1):
        for j in range(F):
            a1 = mdb.models['Model-1'].rootAssembly
            v1 = a1.vertices
            verts1 = v1.findAt(((-BoltB, (i+1)*A-D/2, (j+1)*(L/(F+1))), ))
            region1=regionToolset.Region(vertices=verts1)
            a1 = mdb.models['Model-1'].rootAssembly
            f1 = a1.instances['Part-'+str(i+1)].faces
            faces1 = f1.findAt(((-BoltB-(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A-D/2, (j+1)*(L/(F+1))+0.01),), ((-BoltB+(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A-D/2, (j+1)*(L/(F+1))+0.01),),
                               ((-BoltB-(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A-D/2, (j+1)*(L/(F+1))-0.01),), ((-BoltB+(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A-D/2, (j+1)*(L/(F+1))-0.01),))
            region2 = regionToolset.Region(faces=faces1)
            mdb.models['Model-1'].MultipointConstraint(name='Constraint-'+str(rpn), controlPoint=region1,
                                                       surface=region2, mpcType=BEAM_MPC, userMode=DOF_MODE_MPC, userType=0, csys=None)
            a1 = mdb.models['Model-1'].rootAssembly
            v1 = a1.vertices
            verts1 = v1.findAt(((-BoltB, (i+1)*A+D/2, (j+1)*(L/(F+1))), ))
            region1=regionToolset.Region(vertices=verts1)
            a1 = mdb.models['Model-1'].rootAssembly
            f1 = a1.instances['Part-'+str(i+2)].faces
            faces1 = f1.findAt(((-BoltB-(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A+D/2, (j+1)*(L/(F+1))+0.01),), ((-BoltB+(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A+D/2, (j+1)*(L/(F+1))+0.01),),
                               ((-BoltB-(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A+D/2, (j+1)*(L/(F+1))-0.01),), ((-BoltB+(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A+D/2, (j+1)*(L/(F+1))-0.01),))
            region2 = regionToolset.Region(faces=faces1)
            mdb.models['Model-1'].MultipointConstraint(name='Constraint-'+str(rpn+1), controlPoint=region1,
                                                       surface=region2, mpcType=BEAM_MPC, userMode=DOF_MODE_MPC, userType=0, csys=None)
            a1 = mdb.models['Model-1'].rootAssembly
            v1 = a1.vertices
            verts1 = v1.findAt(((+BoltB, (i+1)*A-D/2, (j+1)*(L/(F+1))), ))
            region1=regionToolset.Region(vertices=verts1)
            a1 = mdb.models['Model-1'].rootAssembly
            f1 = a1.instances['Part-'+str(i+1)].faces
            faces1 = f1.findAt(((+BoltB-(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A-D/2, (j+1)*(L/(F+1))+0.01),), ((+BoltB+(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A-D/2, (j+1)*(L/(F+1))+0.01),),
                               ((+BoltB-(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A-D/2, (j+1)*(L/(F+1))-0.01),), ((+BoltB+(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A-D/2, (j+1)*(L/(F+1))-0.01),))
            region2 = regionToolset.Region(faces=faces1)
            mdb.models['Model-1'].MultipointConstraint(name='Constraint-'+str(rpn+2), controlPoint=region1,
                                                       surface=region2, mpcType=BEAM_MPC, userMode=DOF_MODE_MPC, userType=0, csys=None)
            a1 = mdb.models['Model-1'].rootAssembly
            v1 = a1.vertices
            verts1 = v1.findAt(((+BoltB, (i+1)*A+D/2, (j+1)*(L/(F+1))), ))
            region1=regionToolset.Region(vertices=verts1)
            a1 = mdb.models['Model-1'].rootAssembly
            f1 = a1.instances['Part-'+str(i+2)].faces
            faces1 = f1.findAt(((+BoltB-(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A+D/2, (j+1)*(L/(F+1))+0.01),), ((+BoltB+(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A+D/2, (j+1)*(L/(F+1))+0.01),),
                               ((+BoltB-(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A+D/2, (j+1)*(L/(F+1))-0.01),), ((+BoltB+(BoltD/2+(BoltD/1.2-BoltD/2)/2), (i+1)*A+D/2, (j+1)*(L/(F+1))-0.01),))
            region2 = regionToolset.Region(faces=faces1)
            mdb.models['Model-1'].MultipointConstraint(name='Constraint-'+str(rpn+3), controlPoint=region1,
                                                       surface=region2, mpcType=BEAM_MPC, userMode=DOF_MODE_MPC, userType=0, csys=None)
            rpn = rpn + 4

# 鍒朵綔杩炴帴鍣ㄧ殑鎬ц川锛岀瑳鍗″皵杩炴帴鍣ㄥ睘鎬��������������������������������
mdb.models['Model-1'].ConnectorSection(name='ConnSect-1',
    translationalType=CARTESIAN)
# 鐣岄潰鍒锋柊
a4 = mdb.models['Model-1'].rootAssembly
a4.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON,
    constraints=ON, connectors=ON, engineeringFeatures=ON)
# elastic_0 = connectorBehavior.ConnectorElasticity(components=(2, ), table=((45465.0, ), ))
# mdb.models['Model-1'].sections['ConnSect-1'].setValues(behaviorOptions =(elastic_0, ), u2ReferenceLength=46.3)
# 鍒犻櫎RP鐐��������������������������������
for i in range(F*2*(E-1)*2):
    a4 = mdb.models['Model-1'].rootAssembly
    a4.deleteFeatures(('RP-'+str(i+1), ))

# 鍒朵綔杩炴帴鍣ㄧ殑鍑犱綍
if E >= 2:
    for i in range(E-1):
        for j in range(F):
            a5 = mdb.models['Model-1'].rootAssembly
            v11 = a5.vertices
            a5.WirePolyLine(points=((v11.findAt(coordinates=(BoltB, (i+1)*A-D/2, (j+1)*(L/(F+1)))),
                                   v11.findAt(coordinates=(BoltB, (i+1)*A+D/2, (j+1)*(L/(F+1))))),), mergeType=IMPRINT, meshable=OFF)
            a5.WirePolyLine(points=((v11.findAt(coordinates=(-BoltB, (i+1)*A-D/2, (j+1)*(L/(F+1)))),
                                   v11.findAt(coordinates=(-BoltB, (i+1)*A+D/2, (j+1)*(L/(F+1))))),), mergeType=IMPRINT, meshable=OFF)
#鍒涘缓杩炴帴鍣��������������������������������
if E >= 2:
    for i in range(E-1):
        for j in range(F):
            a = mdb.models['Model-1'].rootAssembly
            e1 = a.edges
            edges1 = e1.findAt(((-BoltB, (i+1)*A, (j+1)*(L/(F+1))), ))
            region=regionToolset.Region(edges=edges1)
            csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
            a = mdb.models['Model-1'].rootAssembly
            e1 = a.edges
            edges1 = e1.findAt(((BoltB, (i+1)*A, (j+1)*(L/(F+1))), ))
            region=regionToolset.Region(edges=edges1)
            csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
            # a = mdb.models['Model-1'].rootAssembly
            # e1 = a.edges
            # edges1 = e1.findAt(((-BoltB, (i+1)*A+D/2, (j+1)*(L/(F+1))), ))
            # region=regionToolset.Region(edges=edges1)
            # csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
            # a = mdb.models['Model-1'].rootAssembly
            # e1 = a.edges
            # edges1 = e1.findAt(((BoltB, (i+1)*A+D/2, (j+1)*(L/(F+1))), ))
            # region=regionToolset.Region(edges=edges1)
            # csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
# # 缃戞牸
p = mdb.models['Model-1'].parts['Part-1-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-1-Copy']
p.seedPart(size=meshsz, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1-Copy']
p.generateMesh()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=meshsz, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
# 椤堕儴鍜屽簳閮ㄩ泦
a3 = mdb.models['Model-1'].rootAssembly
region1=a3.sets['TTpoint']
a3 = mdb.models['Model-1'].rootAssembly
region2=a3.sets['Tsurface']
mdb.models['Model-1'].MultipointConstraint(name='BC-1',
    controlPoint=region1, surface=region2, mpcType=BEAM_MPC,
    userMode=DOF_MODE_MPC, userType=0, csys=None)
a3 = mdb.models['Model-1'].rootAssembly
region1=a3.sets['BBpoint']
a3 = mdb.models['Model-1'].rootAssembly
region2=a3.sets['Bsurface']
mdb.models['Model-1'].MultipointConstraint(name='BC-2',
    controlPoint=region1, surface=region2, mpcType=BEAM_MPC,
    userMode=DOF_MODE_MPC, userType=0, csys=None)
# 骞虫粦鍒嗘瀽姝��������������������������������
mdb.models['Model-1'].SmoothStepAmplitude(name='Amp-1', timeSpan=STEP, data=((
    0.0, 0.0), (1.0, 1.0)))

#  鍒嗘瀽姝��������������������������������
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial',
                                 initialInc=0.00001,minInc=1e-06, maxInc=1.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
# 杞借嵎铻烘爴棰勭揣鍔涳拷1锟��������������������������������借繃杞借嵎鏂藉姞锛屾澶勪笉闇��������������������������������
# rpn = 1
# if E >= 2:
#     for i in range(E-1):
#         for j in range(F):
#             # mdb.models['Model-1'].StaticStep(name='Step-'+str(rpn+1), previous='Step-'+str(rpn),
#             #                                  maxNumInc=50, initialInc=0.0001, nlgeom=ON)
#             a7 = mdb.models['Model-1'].rootAssembly
#             e1 = a7.edges
#             edges1 = e1.findAt(((-BoltB, (i+1)*A, (j+1)*(L/(F+1))), ))
#             region = regionToolset.Region(edges=edges1)
#             mdb.models['Model-1'].ConnectorForce(name='load-'+str(rpn), createStepName='Step-1',
#                                                  region=region, f2=-pbol, amplitude='Amp-1')
#             # mdb.models['Model-1'].StaticStep(name='Step-'+str(rpn+2), previous='Step-'+str(rpn+1),
#             #                                  maxNumInc=50, initialInc=0.0001, nlgeom=ON)
#             a7 = mdb.models['Model-1'].rootAssembly
#             e1 = a7.edges
#             edges1 = e1.findAt(((BoltB, (i+1)*A, (j+1)*(L/(F+1))), ))
#             region = regionToolset.Region(edges=edges1)
#             mdb.models['Model-1'].ConnectorForce(name='load-'+str(rpn+1), createStepName='Step-1',
#                                                  region=region, f2=-pbol, amplitude='Amp-1')
#             rpn += 2

# # 杈圭晫鏉′欢-----------
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['TTpoint']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['Tsurface']
mdb.models['Model-1'].MultipointConstraint(name='BC-1',
    controlPoint=region1, surface=region2, mpcType=BEAM_MPC,
    userMode=DOF_MODE_MPC, userType=0, csys=None)
a = mdb.models['Model-1'].rootAssembly
region1=a.sets['BBpoint']
a = mdb.models['Model-1'].rootAssembly
region2=a.sets['Bsurface']
mdb.models['Model-1'].MultipointConstraint(name='BC-2',
    controlPoint=region1, surface=region2, mpcType=BEAM_MPC,
    userMode=DOF_MODE_MPC, userType=0, csys=None)
# # 杈圭晫(鍔犲叆閰嶅悎鑽疯浇鐨勮鍙ュ垽鏂級
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['TTpoint']
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial',
    region=region, u1=SET, u2=SET, u3=UNSET, ur1=SET, ur2=SET, ur3=SET,
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
# 搴曢儴
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['BBpoint']
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial',
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET,
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)

# 灞堟洸鍒嗘瀽姝��������������������������������
mdb.models['Model-1'].BuckleStep(name='Step-2', previous='Step-1', numEigen=10,
                                 eigensolver=LANCZOS, minEigen=None, blockSize=DEFAULT, maxBlocks=DEFAULT)

# 鑽疯浇
mdb.models['Model-1'].StaticStep(name='Step-2', previous='Step-1')
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['TTpoint']
mdb.models['Model-1'].ConcentratedForce(name='Load-1000000', createStepName='Step-2',
    region=region, cf1=cf1f, cf2=cf2f, cf3=cf3f, distributionType=UNIFORM,
    field='', localCsys=None)

# # 渚濇鍒ゆ柇淇敼杈圭晫鏉′欢
if cf1f != 0:
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-2', u1=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
if cf2f != 0:
    mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-2', u2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
# if cf3f != 0:
#     mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', u3=u3u)
# if ur2r != 0:
#     mdb.models['Model-1'].boundaryConditions['BC-2'].setValuesInStep(stepName='Step-1', ur2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
#     mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', ur2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
# 纭绗簩鍒嗘瀽姝ヤ负灞堟洸鍒嗘瀽
mdb.models['Model-1'].BuckleStep(name='Step-2', previous='Step-1',
    maintainAttributes=True, numEigen=10, eigensolver=LANCZOS, minEigen=None,
    blockSize=DEFAULT, maxBlocks=DEFAULT)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-2')
# 棰勭揣浣滅敤
elastic_0 = connectorBehavior.ConnectorElasticity(components=(2, ), table=((
    205000*3.1416*BoltD*BoltD/4/(2*D), ), ))
mdb.models['Model-1'].sections['ConnSect-1'].setValues(behaviorOptions =(
    elastic_0, ), u2ReferenceLength=(D-pbol/(205000*3.1416*BoltD*BoltD/4/(2*D))) )
mdb.models['Model-1'].sections['ConnSect-1'].behaviorOptions[0].ConnectorOptions(
    )

#  鎻愬彇妯★拷1锟��������������������������������藉彉褰��������������������������������
if E == 1:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(75, """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 2:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(115+30*(F-1), """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 3:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(166+(E-3)*37+(60+30*(E-3))*(F-1), """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 4:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(166+(E-3)*37+(60+30*(E-3))*(F-1), """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 5:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(166+(E-3)*37+(60+30*(E-3))*(F-1), """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 6:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(166+(E-3)*37+(60+30*(E-3))*(F-1), """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 7:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(166+(E-3)*37+(60+30*(E-3))*(F-1), """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 8:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(166+(E-3)*37+(60+30*(E-3))*(F-1), """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 9:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(166+(E-3)*37+(60+30*(E-3))*(F-1), """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
if E == 10:
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(166+(E-3)*37+(60+30*(E-3))*(F-1), """
    *Output, field, variable=PRESELECT
    *NODE FILE,GLOBAL=YES
    U,""")
# # # # # # # JOB
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=96,
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, multiprocessingMode=THREADS, numCpus=16,
    numDomains=16, numGPUs=0)
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
    name='C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/'+str(printname)+'/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/'+str(printname)+'/Job-1.odb']
session.fieldReportOptions.setValues(printXYData=OFF, printTotal=OFF)
# 杩欎釜瑕佸瓨鍦ㄨ緭鍑虹洰褰��������������������������������
session.writeFieldReport(
    fileName='C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\Result1.rpt',
    append=OFF, sortItem='nodenumber', odb=odb, step=1, frame=1,
    outputPosition=NODAL, variable=(('U', NODAL),  ('UR', NODAL), ), stepFrame=SPECIFY)
# 瀛樻暟鎹埌鏁版嵁搴勶拷

session.writeFieldReport(
    fileName='C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/'+'Elasticdata'+printname+'.csv',
    append=OFF, sortItem='缁撶偣缂栧彿', odb=odb, step=1, frame=1,
    outputPosition=NODAL, variable=(('U', NODAL), ('UR', NODAL),  ), stepFrame=SPECIFY)
# 瀛樺浘
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/'+str(printname)+'/Job-1.odb'])
o3 = session.openOdb(
    name='C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/'+str(printname)+'/Job-1.odb')
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
    fileName='C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/'+'Elastic'+printname+'.tiff',
    format=TIFF, canvasObjects=(session.viewports['Viewport: 1'], ))
mdb.saveAs(
    pathName='C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/'+str(printname)+'/Elastic')
