import arcpy
arcpy.env.overwriteOutput = True
for x in ["Mua_Muadong_9LVS",
          "Mua_Muahe_9LVS",
          "Mua_Nam_9LVS",
          "Mua_T01_9LVS",
          "Mua_T02_9LVS",
          "Mua_T03_9LVS",
          "Mua_T04_9LVS",
          "Mua_T05_9LVS",
          "Mua_T06_9LVS",
          "Mua_T07_9LVS",
          "Mua_T08_9LVS",
          "Mua_T09_9LVS",
          "Mua_T10_9LVS",
          "Mua_T11_9LVS",
          "Mua_T12_9LVS"] :
    print(x)
    filemxd = "K:/mxd_design/" + str(x) + ".mxd"
    filepdf = "K:/mxd_design/PDF/" + str(x) + ".pdf"
    mxd = arcpy.mapping.MapDocument(filemxd)
    arcpy.mapping.ExportToPDF(mxd, filepdf)
    del mxd
