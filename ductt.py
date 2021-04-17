import arcpy
arcpy.env.overwriteOutput = True
for x in ["Bochoi_mua dong", "Bochoi_muahe", "Bochoi_muathu", "Bochoi_muaxuan", "Bochoi_nam",
          "Bucxa_III-V", "Bucxa_IX-XI", "Bucxa_nam", "Bucxa_VI-VIII", "Bucxa_XII-II",
          "Chisoam_mua dong", "Chisoam_mua he", "Chisoam_mua thu", "Chisoam_mua xuan", "Chisoam_nam",
          "Cstongthuong_hanhan", "Cstongthuong_mualon", "Cstongthuong_rethai", "Cstonthuong_nangnong",
          "Doam_mua dong", "Doam_mua he", "Doam_mua thu", "Doam_mua xuan", "Doam_nam",
          "Hanhanbd_20", "Hanhanbd_50", "Hanhanbd_80", "Hanhankt_20", "Hanhankt_50", "Hanhankt_80",
          "Khanangruiro_hanhan", "Khanangruiro_mualon", "Khanangruiro_nangnong", "Khanangruiro_rethai",
          "Luongmua_mua 1", "Luongmua_mua 2", "Luongmua_mua 3", "Luongmua_mua 4", "Luongmua_mua 5", "Luongmua_mua 6",
          "Luongmua_mua 7", "Luongmua_mua 8", "Luongmua_mua 9", "Luongmua_mua 10", "Luongmua_mua 11", "Luongmua_mua 12",
          "Luongmua_nam",
          "Mualonbd_20", "Mualonbd_50", "Mualonbd_80", "Mualonkt_20", "Mualonkt_50", "Mualonkt_80",
          "Mucdokhackhiet_mualon", "Mucdokhackhiet_nangnong", "Mucdokhackhiet_rethai", "Mucdokhacnghiet_han",
          "Nangnongbd_20", "Nangnongbd_50", "Nangnongbd_80", "Nangnongkt_20", "Nangnongkt_50", "Nangnongkt_80",
          "Nhietdo_mua 1", "Nhietdo_mua 2", "Nhietdo_mua 3", "Nhietdo_mua 4", "Nhietdo_mua 5", "Nhietdo_mua 6",
          "Nhietdo_mua 7", "Nhietdo_mua 8", "Nhietdo_mua 9", "Nhietdo_mua 10", "Nhietdo_mua 11", "Nhietdo_mua 12",
          "Nhietdo_nam",
          "R_Maxtrongbao", "R_muadong", "R_muahe",
          "Rethaibd_20", "Rethaibd_50", "Rethaibd_80", "Rethaikt_20", "Rethaikt_50", "Rethaikt_80",
          "Sogionang_III - V", "Sogionang_IX - XI", "Sogionang_nam", "Sogionang_VI - VIII", "Sogionang_XII - II",
          "Songaymua_III-V", "Songaymua_IX-XI", "Songaymua_VI-VIII", "Songaymua_XII-II",
          "Songayrethai", "Sothang_han",
          "Thd_nam", "Thd_T1", "Thd_T7",
          "Tm_nam",
          "Tm_VI-VIII", "Tm_XII-II",
          "Toc do gio trong bao lon nhat", "Tocdogio_nam",
          "Tx_nam", "Tx_VI-VIII", "Tx_XII-II",
          "Tieuvungkhihau", "Aplucgio", "duong_pv_xd", "nl_gio_sohoa_catvung",
          "CCN_T1_VUNG", "CCN_T7", "Bao_Nam", "Tansuatbao_Nam", "TOCDOGIO",
          "Chisotichhopkhihaudulichnghingoi_THANNHIET",
          "Chisotichhopkhihaudulichnghingoi",
          "Chisonhietdosinhlylytuong",
          "Chisonhietdosinhlytuongduong",
          "pv_baoduongbetong_region",
          "RSI_T7", "RSI_Nam", "TCI_T1", "TCI_T7", "TCI_TBNam", "HanhanNN_kt_20", "HanhanNN_kt_50", "HanhanNN_kt_80", "Hanhanbd_NN_20", "Hanhanbd_NN_50", "Cstongthuong_hanhan", "Cstongthuong_han_NN", "HanhanNN_bd_80", "Mucdokhacnghiet_han_NN", "2mien_7vung", "2mien_7vung"] :
    print(x)
    filemxd = "K:/mxd_design/" + str(x) + ".mxd"
    filepdf = "K:/mxd_design/PDF/" + str(x) + ".pdf"
    mxd = arcpy.mapping.MapDocument(filemxd)
    arcpy.mapping.ExportToPDF(mxd, filepdf)
    del mxd
