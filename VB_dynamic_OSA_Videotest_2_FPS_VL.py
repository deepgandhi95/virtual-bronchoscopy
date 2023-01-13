# trace generated using paraview version 5.6.2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import numpy as np
from numpy import genfromtxt
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'STL Reader'
out_00 = STLReader(FileNames=['F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000000.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000050.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000100.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000150.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000200.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000250.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000300.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000350.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000400.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000450.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000500.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000550.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000600.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000650.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000700.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000750.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000800.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000850.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000900.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_000950.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001000.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001050.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001100.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001150.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001200.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001250.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001300.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001350.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001400.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001450.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001500.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001550.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001600.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001650.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001700.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001750.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001800.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001850.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001900.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_001950.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002000.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002050.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002100.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002150.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002200.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002250.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002300.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002350.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002400.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002450.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002500.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002550.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002600.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002650.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002700.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002750.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002800.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002850.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002900.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_002950.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003000.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003050.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003100.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003150.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003200.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003250.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003300.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003350.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003400.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003450.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003500.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003550.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003600.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003650.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003700.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003750.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003800.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003850.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003900.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_003950.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004000.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004050.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004100.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004150.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004200.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004250.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004300.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004350.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004400.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004450.stl', 'F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/STLs_50/out_004500.stl'])

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [1024, 500]

# get layout
layout1 = GetLayout()

# show data in view
out_00Display = Show(out_00, renderView1)

# get color transfer function/color map for 'STLSolidLabeling'
sTLSolidLabelingLUT = GetColorTransferFunction('STLSolidLabeling')

# trace defaults for the display properties.
out_00Display.Representation = 'Surface'
out_00Display.ColorArrayName = ['CELLS', 'STLSolidLabeling']
out_00Display.LookupTable = sTLSolidLabelingLUT
out_00Display.OSPRayScaleFunction = 'PiecewiseFunction'
out_00Display.SelectOrientationVectors = 'None'
out_00Display.ScaleFactor = 22.249900054931643
out_00Display.SelectScaleArray = 'STLSolidLabeling'
out_00Display.GlyphType = 'Arrow'
out_00Display.GlyphTableIndexArray = 'STLSolidLabeling'
out_00Display.GaussianRadius = 1.112495002746582
out_00Display.SetScaleArray = [None, '']
out_00Display.ScaleTransferFunction = 'PiecewiseFunction'
out_00Display.OpacityArray = [None, '']
out_00Display.OpacityTransferFunction = 'PiecewiseFunction'
out_00Display.DataAxesGrid = 'GridAxesRepresentation'
out_00Display.SelectionCellLabelFontFile = ''
out_00Display.SelectionPointLabelFontFile = ''
out_00Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
out_00Display.DataAxesGrid.XTitleFontFile = ''
out_00Display.DataAxesGrid.YTitleFontFile = ''
out_00Display.DataAxesGrid.ZTitleFontFile = ''
out_00Display.DataAxesGrid.XLabelFontFile = ''
out_00Display.DataAxesGrid.YLabelFontFile = ''
out_00Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
out_00Display.PolarAxes.PolarAxisTitleFontFile = ''
out_00Display.PolarAxes.PolarAxisLabelFontFile = ''
out_00Display.PolarAxes.LastRadialAxisTextFontFile = ''
out_00Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
out_00Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'STLSolidLabeling'
sTLSolidLabelingPWF = GetOpacityTransferFunction('STLSolidLabeling')

# create a new 'Loop Subdivision'
loopSubdivision1 = LoopSubdivision(Input=out_00)

# Properties modified on loopSubdivision1
loopSubdivision1.NumberofSubdivisions = 4

# show data in view
loopSubdivision1Display = Show(loopSubdivision1, renderView1)

# trace defaults for the display properties.
loopSubdivision1Display.Representation = 'Surface'
loopSubdivision1Display.ColorArrayName = ['CELLS', 'STLSolidLabeling']
loopSubdivision1Display.LookupTable = sTLSolidLabelingLUT
loopSubdivision1Display.OSPRayScaleFunction = 'PiecewiseFunction'
loopSubdivision1Display.SelectOrientationVectors = 'None'
loopSubdivision1Display.ScaleFactor = 22.245645904541018
loopSubdivision1Display.SelectScaleArray = 'STLSolidLabeling'
loopSubdivision1Display.GlyphType = 'Arrow'
loopSubdivision1Display.GlyphTableIndexArray = 'STLSolidLabeling'
loopSubdivision1Display.GaussianRadius = 1.1122822952270508
loopSubdivision1Display.SetScaleArray = [None, '']
loopSubdivision1Display.ScaleTransferFunction = 'PiecewiseFunction'
loopSubdivision1Display.OpacityArray = [None, '']
loopSubdivision1Display.OpacityTransferFunction = 'PiecewiseFunction'
loopSubdivision1Display.DataAxesGrid = 'GridAxesRepresentation'
loopSubdivision1Display.SelectionCellLabelFontFile = ''
loopSubdivision1Display.SelectionPointLabelFontFile = ''
loopSubdivision1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
loopSubdivision1Display.DataAxesGrid.XTitleFontFile = ''
loopSubdivision1Display.DataAxesGrid.YTitleFontFile = ''
loopSubdivision1Display.DataAxesGrid.ZTitleFontFile = ''
loopSubdivision1Display.DataAxesGrid.XLabelFontFile = ''
loopSubdivision1Display.DataAxesGrid.YLabelFontFile = ''
loopSubdivision1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
loopSubdivision1Display.PolarAxes.PolarAxisTitleFontFile = ''
loopSubdivision1Display.PolarAxes.PolarAxisLabelFontFile = ''
loopSubdivision1Display.PolarAxes.LastRadialAxisTextFontFile = ''
loopSubdivision1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(out_00, renderView1)

# show color bar/color legend
loopSubdivision1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# turn off scalar coloring
ColorBy(loopSubdivision1Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(sTLSolidLabelingLUT, renderView1)

# change solid color
loopSubdivision1Display.DiffuseColor = [1.0, 0.6666666666666666, 0.4980392156862745]

# Create a new 'Light'
light1 = AddLight(view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=light1)

# remove light added to the view
RemoveLight(light=light1)

# Create a new 'Light'
light2 = AddLight(view=renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=light2)

# Properties modified on light2
light2.Enable = 0

# Properties modified on light2
light2.Enable = 1

# Properties modified on light2
light2.Enable = 0

# Properties modified on light2
light2.Enable = 1

# Properties modified on light2
light2.Coords = 'Ambient'

# Properties modified on light2
light2.Coords = 'Headlight'

# Properties modified on light2
light2.Coords = 'Camera'
light2.Position = [0.0, 0.0, 1.0]
light2.FocalPoint = [0.0, 0.0, 0.0]

# Properties modified on light2
light2.Intensity = 0.5

# number_frames = 96.0
STL_counter = 1.0
animationScene1.AnimationTime = 0.0
timeKeeper1.Time = 0.0

x1 = genfromtxt('F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/Trachbronchi1_x_SG.txt', delimiter=',')
y1 = genfromtxt('F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/Trachbronchi1_y_SG.txt', delimiter=',')
z1 = genfromtxt('F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/Trachbronchi1_z_SG.txt', delimiter=',')

focalpoint_distance = 10

#### saving camera placements for all active views
#renderView1.CameraViewUp = [0, 1, 0]
# current camera placement for renderView1
for i in range(len(x1)):
    animationScene1.AnimationTime += STL_counter
    timeKeeper1.Time += STL_counter
    if animationScene1.AnimationTime > 91: #Total number of STLs
       animationScene1.AnimationTime = 1.0
       timeKeeper1.Time = 1.0
    A = [x1[i+1],y1[i+1],z1[i+1]]
    B = [x1[i],y1[i],z1[i]]
    C = np.array(B) - np.array(A)
    D = [0, -C[2],C[1]]
    renderView1.CameraViewUp = D #np.cross(B,C)
    # B - A and tangent at B
	# Frenet normal or binormal?
    renderView1.CameraPosition = [x1[i],y1[i],z1[i]]
    renderView1.CameraFocalPoint = [x1[i+focalpoint_distance], y1[i+focalpoint_distance], z1[i+focalpoint_distance]]
    renderView1.CameraParallelScale = 124.4329125000106

    WriteImage("F:/CPIR/Alister/OSA_measurements/ForQiwei/DYMOSA803/DISE_2021/DISE_Images5/Test_{}.png".format(i))
