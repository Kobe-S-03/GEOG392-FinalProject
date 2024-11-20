import arcpy

#Select Data
aprx = arcpy.mp.ArcGISProject("current")
map = aprx.listMaps()[0]
newLayer = map.listLayers('Cotton_10')[0]

#Desin Bar Chart
chart = arcpy.Chart('MyChart')
chart.type = 'bar'
chart.title = 'Counties vs cotton production'
chart.description = 'This chart displays the top 10 counties with most cotton production (2001-2021).'
chart.xAxis.field = 'County'
chart.yAxis.field = 'F__of_Bale'
chart.xAxis.title = 'Counties'
chart.yAxis.title = 'Cotton Production'
chart.addToLayer(newLayer)
