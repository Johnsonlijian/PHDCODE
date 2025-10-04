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
nodedeform = 30.0




printname='A'+str(A)+'B'+str(B)+'C'+str(C)+'D'+str(D)+'L'+str(L)+'E'+str(E)+'F'+str(F)+'BoltD'+str(BoltD)+'BoltB'\
          +str(BoltB)+'sfricn'+str(sfricn)+'pbol'+str(pbol)+'yfss'+str(yfss)+'yuss'+str(yuss)+'yusn'+str(yusn)\
          +'meshsz'+str(meshsz)+'cf1f'+str(cf1f)+'cf2f'+str(cf2f)+'cf3f'+str(cf3f)+'Imperfectfactor'+str(Imperfectfactor)





import os
os.chdir(r"C:\Users\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\picandcsv/"+str(printname))
openMdb(
    pathName='C:/Users/82173/Desktop/Isight_Catia_Abaqus/Abaqus_dataTEboltH/picandcsv/'+str(printname)+'/Elastic.cae')
#: 妯″瀷鏁版嵁搴刄sers\82173\Desktop\Isight_Catia_Abaqus\Abaqus_dataTEboltH\Elastic.cae" 宸叉墦寮��������������������������������
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
# # 澶嶅埗妯″瀷
mdb.Model(name='Model-1-Copy', objectToCopy=mdb.models['Model-1'])

# #寤虹珛鏂版潗鏂欏強鎴潰鏉愭枡锛圚鍨嬮挗锛��������������������������������
mdb.models['Model-1-Copy'].Material(name='Material-2')
mdb.models['Model-1-Copy'].materials['Material-2'].Elastic(table=((205000.0,
    0.3), ))
mdb.models['Model-1-Copy'].materials['Material-2'].Plastic(table=((yfss,
    0.0), (yfss, yfsn), (yuss, yusn)))
mdb.models['Model-1-Copy'].HomogeneousShellSection(name='websection',
    preIntegrate=OFF, material='Material-2', thicknessType=UNIFORM,
    thickness=C, thicknessField='', nodalThicknessField='',
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT,
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF,
    integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1-Copy'].HomogeneousShellSection(name='flangesection',
    preIntegrate=OFF, material='Material-2', thicknessType=UNIFORM,
    thickness=D*2, thicknessField='', nodalThicknessField='',
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT,
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF,
    integrationRule=SIMPSON, numIntPts=5)
# 鍒嗘瀽姝��������������������������������
if u1u != 0:
    dofd = 1
else:
    dofd = 2
del mdb.models['Model-1-Copy'].steps['Step-1']
del mdb.models['Model-1-Copy'].steps['Step-2']
regionDef=mdb.models['Model-1-Copy'].rootAssembly.sets['TTpoint']
mdb.models['Model-1-Copy'].StaticRiksStep(name='Step-1', previous='Initial',
    nodeOn=ON, maximumDisplacement=trueu3, region=regionDef, dof=dofd,
    maxNumInc=1000, initialArcInc=0.0001, maxArcInc=1, nlgeom=ON)
mdb.models['Model-1-Copy'].steps['Step-1'].setValues(minArcInc=1e-06)
# # 杞借嵎
mdb.models['Model-1-Copy'].boundaryConditions['BC-1'].setValuesInStep(
    stepName='Step-1', u1=u1u, u2=u2u)
# fieldhistpoutput
mdb.models['Model-1-Copy'].historyOutputRequests['H-Output-1'].setValues(
    variables=('ALLAE', ))
mdb.models['Model-1-Copy'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF'))
# if ur2r != 0:
#     mdb.models['Model-1'].boundaryConditions['BC-2'].setValuesInStep(stepName='Step-1', ur2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
#     mdb.models['Model-1'].boundaryConditions['BC-1'].setValuesInStep(stepName='Step-1', ur2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
#: 妯″瀷 "Model-1-Copy" 宸插垱寤��������������������������������
mdb.models['Model-1-Copy'].keywordBlock.synchVersions(
    storeNodesAndElements=False)
mdb.models['Model-1-Copy'].keywordBlock.setValues(edited = 0)
mdb.models['Model-1-Copy'].keywordBlock.synchVersions(
    storeNodesAndElements=False)
if E == 1:
    mdb.models['Model-1-Copy'].keywordBlock.replace(54,
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")
if E == 2:
    mdb.models['Model-1-Copy'].keywordBlock.replace(94+(F-1)*30,
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")
if E == 3:
    mdb.models['Model-1-Copy'].keywordBlock.replace(145+37*(E-3)+(F-1)*(60+30*(E-3)),
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")

if E == 4:
    mdb.models['Model-1-Copy'].keywordBlock.replace(145+37*(E-3)+(F-1)*(60+30*(E-3)),
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")
if E == 5:
    mdb.models['Model-1-Copy'].keywordBlock.replace(145+37*(E-3)+(F-1)*(60+30*(E-3)),
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")
if E == 6:
    mdb.models['Model-1-Copy'].keywordBlock.replace(145+37*(E-3)+(F-1)*(60+30*(E-3)),
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")
if E == 7:
    mdb.models['Model-1-Copy'].keywordBlock.replace(145+37*(E-3)+(F-1)*(60+30*(E-3)),
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")
if E == 8:
    mdb.models['Model-1-Copy'].keywordBlock.replace(145+37*(E-3)+(F-1)*(60+30*(E-3)),
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")
if E == 9:
    mdb.models['Model-1-Copy'].keywordBlock.replace(145+37*(E-3)+(F-1)*(60+30*(E-3)),
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")
if E == 10:
    mdb.models['Model-1-Copy'].keywordBlock.replace(145+37*(E-3)+(F-1)*(60+30*(E-3)),
"""** ----------------------------------------------------------------
*IMPERFECTION,FILE=Job-1, STEP=2
1,30.0
**
** STEP: Step-1
**""")
# 鍒朵綔set闆嗘彁鍙栬灪鏍撴暟鎹紙鍚屾椂寤虹珛鍒朵綔鍦鸿緭鍑鸿姹傦級
rpn = 1
if E >= 2:
    for i in range(E-1):
        for j in range(F):
            a = mdb.models['Model-1-Copy'].rootAssembly
            e1 = a.edges
            edges1 = e1.findAt(((-BoltB, (i+1)*A, (j+1)*(L/(F+1))), ))
            a.Set(edges=edges1, name='LB-'+str(rpn))
            regionDef = mdb.models['Model-1-Copy'].rootAssembly.sets['LB-1']
            mdb.models['Model-1-Copy'].FieldOutputRequest(name='F-OutputLB-'+str(rpn),
                                                          createStepName='Step-1',
                                                          variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U',
                                                                     'RF', 'CF', 'SF', 'CSTRESS', 'CSTRESSETOS',
                                                                     'CLINELOAD', 'CPOINTLOAD',
                                                                     'CDISP', 'CFORCE', 'CSTATUS', 'CTF', 'CEF', 'CU',
                                                                     'CUE', 'CUP'),
                                                          region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
            a = mdb.models['Model-1-Copy'].rootAssembly
            e1 = a.edges
            edges1 = e1.findAt(((BoltB, (i+1)*A, (j+1)*(L/(F+1))), ))
            a.Set(edges=edges1, name='LB-'+str(rpn+1))
            mdb.models['Model-1-Copy'].FieldOutputRequest(name='F-OutputLB-'+str(+1),
                                                          createStepName='Step-1',
                                                          variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U',
                                                                     'RF', 'CF', 'SF', 'CSTRESS', 'CSTRESSETOS',
                                                                     'CLINELOAD', 'CPOINTLOAD',
                                                                     'CDISP', 'CFORCE', 'CSTATUS', 'CTF', 'CEF', 'CU',
                                                                     'CUE', 'CUP'),
                                                          region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)
            rpn = rpn + 2
# 鍒朵綔鍦鸿緭鍑鸿姹��������������������������������

# # 鍒涘缓Job2
mdb.Job(name='Job-2', model='Model-1-Copy', description='', type=ANALYSIS,
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
    scratch='', resultsFormat=ODB, multiprocessingMode=THREADS, numCpus=16,
    numDomains=16, numGPUs=0)
# # # # # 绛夊緟鍒嗘瀽瀹屾垚
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)

a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF, optimizationTasks=OFF,
    geometricRestrictions=OFF, stopConditions=OFF)
# # 绛夊緟鍒嗘瀽瀹屾垚
mdb.jobs['Job-2'].waitForCompletion()

o3 = session.openOdb(
    name='C:/Users/82173/Desktop/Isight_Catia_Abaqus/Abaqus_dataTEboltH/picandcsv/'+str(printname)+'/Job-2.odb')
#: 妯″瀷: C:/Users/82173/Desktop/Isight_Catia_Abaqus/Abaqus_dataTEboltH/Job-2.odb
# : 瑁呴厤浠朵釜鏁��������������������������������
# : 瑁呴厤浠跺疄渚嬩釜鏁��������������������������������
# : 閮ㄤ欢瀹炰緥鐨勪釜鏁��������������������������������
# : 缃戞牸鏁��������������������������������
# : 鍗曞厓闆嗗悎鏁��������������������������������
# : 缁撶偣闆嗗悎鏁��������������������������������
#: 鍒嗘瀽姝ョ殑涓暟:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
# 瀛樻暟鎹埌鏁版嵁搴勫甫鏈夋洸绾跨殑鍏ㄩ儴鏁版嵁锛��������������������������������
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
odb = session.odbs['C:/Users/82173/Desktop/Isight_Catia_Abaqus/Abaqus_dataTEboltH/picandcsv/'+str(printname)+'/Job-2.odb']
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('RF',
    NODAL), ('RM', NODAL), ('U', NODAL), ('UR', NODAL), ), nodeSets=("TTPOINT",
    ))
x0 = session.xyDataObjects['RF:Magnitude PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x1 = session.xyDataObjects['RF:RF1 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x2 = session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x3 = session.xyDataObjects['RF:RF3 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x4 = session.xyDataObjects['RM:Magnitude PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x5 = session.xyDataObjects['RM:RM1 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x6 = session.xyDataObjects['RM:RM2 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x7 = session.xyDataObjects['RM:RM3 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x8 = session.xyDataObjects['U:Magnitude PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x9 = session.xyDataObjects['U:U1 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x10 = session.xyDataObjects['U:U2 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x11 = session.xyDataObjects['U:U3 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x12 = session.xyDataObjects['UR:Magnitude PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x13 = session.xyDataObjects['UR:UR1 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x14 = session.xyDataObjects['UR:UR2 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x15 = session.xyDataObjects['UR:UR3 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
session.xyReportOptions.setValues(xyData=ON, totals=OFF, minMax=OFF)
session.writeXYReport(
    fileName='C:/Users/82173/Desktop/Isight_Catia_Abaqus/Abaqus_dataTEboltH/picandcsv/'+'Plastic'+printname+'.csv',
    appendMode=OFF, xyData=(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11,
    x12, x13, x14, x15))


# # 瀛樻暟鎹紙浠呬繚瀛樻渶澶��������������������������������界敤浣滄煴瀛愭洸绾匡紕17
x0 = session.xyDataObjects['RF:RF1 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x1 = session.xyDataObjects['RF:RF2 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
x2 = session.xyDataObjects['RF:RF3 PI: ASSEMBLY N: ' + str(2+(E-1)*4+4*(E-1)*(F-1))]
session.xyReportOptions.setValues(xyData=OFF,totals=OFF, minMax=ON)
session.writeXYReport(
    fileName='C:/Users/82173/Desktop/Isight_Catia_Abaqus/Abaqus_dataTEboltH/Result2.rpt',appendMode=OFF,
    xyData=(x0, x1, x2))

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
    fileName='C:/Users/82173/Desktop/Isight_Catia_Abaqus/Abaqus_dataTEboltH/picandcsv/'+'Plastic'+printname+'.tiff',
    format=TIFF, canvasObjects=(session.viewports['Viewport: 1'], ))
# # mdb.save()
