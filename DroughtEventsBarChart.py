import arcpy

aprx = arcpy.mp.ArcGISProject("current")
map = aprx.listMaps()[0]
newLayer = map.listLayers('Least_Drgt_events')[0]
chart = arcpy.Chart('MyChart')

chart.type = 'bar'
chart.title = 'Counties vs Drought Events'
chart.description = 'This chart displays the top 10 counties with least drought events (2001-2021).'
chart.xAxis.field = 'COUNTY'
chart.yAxis.field = 'DRGT_EVNTS'
chart.xAxis.title = 'Counties'
chart.yAxis.title = 'Number of Drought Events'
chart.addToLayer(newLayer)
