import arcpy
arcpy.env.overwriteOutput = True
for x in ["Biendonhiet_MuaDONG",
          "Biendonhiet_Muahe",
          "Biendonhiet_T1",
          "Biendonhiet_T4",
          "Biendonhiet_T7",
          "Biendonhiet_T10",
          "Bochoi_Nam_8vungstnn", "Doam_Nam_8vungstnn", "Mua_Muadong", "Mua_Muahe",
          "Mua_Nam", "Mua_T01", "Mua_T02", "Mua_T03", "Mua_T04", "Mua_T05", "Mua_T06",
          "Mua_T07", "Mua_T08", "Mua_T09", "Mua_T10", "Mua_T11", "Mua_T12",
          "Sogionang_Nam_8vungstnn", "Sogionang_T01", "Sogionang_T04", "Sogionang_T07", "Sogionang_T10",
          "T_Muadong", "T_Muahe", "T_Nam", "T_Thang1", "T_Thang4", "T_Thang7", "T_Thang10"] :
    print(x)
    filemxd = "K:/mxd_design/" + str(x) + ".mxd"
    filepdf = "K:/mxd_design/PDF/" + str(x) + ".pdf"
    mxd = arcpy.mapping.MapDocument(filemxd)
    arcpy.mapping.ExportToPDF(mxd, filepdf)
    del mxd

