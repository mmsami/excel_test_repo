# Changes in 20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table1.xml

```diff
diff --git a/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table1.xml b/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table1.xml
index 01191e4..f65ab43 100644
--- a/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table1.xml
+++ b/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table1.xml
@@ -1,2 +1,54 @@
-<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="10" xr:uid="{25037879-D638-41CA-BC3C-A09C30E02942}" name="finance_Portfolios" displayName="finance_Portfolios" ref="A1:G2" totalsRowShown="0" headerRowDxfId="214" headerRowBorderDxfId="213" tableBorderDxfId="212"><autoFilter ref="A1:G2" xr:uid="{25037879-D638-41CA-BC3C-A09C30E02942}"/><tableColumns count="7"><tableColumn id="1" xr3:uid="{155820A8-4454-45CF-88E8-511231C6B171}" name="ID"/><tableColumn id="6" xr3:uid="{96F6DB92-4016-478B-9C2D-C8F62174ECC3}" name="Kind:srcLastSaved"/><tableColumn id="2" xr3:uid="{78BEFECE-D812-4DBC-8C34-4D40A1284A01}" name="Kind:src"><calculatedColumnFormula>IF(finance_Portfolios[[#This Row],[Kind:srcLastSaved]]="",IF(finance_Portfolios[[#This Row],[Kind]]="","",INDEX(meta_Classifiers[ID],MATCH(finance_Portfolios[[#This Row],[Kind]],meta_Classifiers[Display Qualified],0))),finance_Portfolios[[#This Row],[Kind:srcLastSaved]])</calculatedColumnFormula></tableColumn><tableColumn id="3" xr3:uid="{E322332C-9E54-4107-871F-955998B9900F}" name="Kind"/><tableColumn id="5" xr3:uid="{22547BBF-5FCA-4A1E-B937-85128D6A3147}" name="Package"/><tableColumn id="4" xr3:uid="{218A46C3-1A3E-4E23-9240-9D465E00E968}" name="Owner"/><tableColumn id="10" xr3:uid="{4CE77B86-BEC0-304C-9794-CF4BCDD29FB3}" name="Value"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
+<table
+  xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
+  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
+  mc:Ignorable="xr xr3"
+  xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
+  xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
+  id="10"
+  xr:uid="{25037879-D638-41CA-BC3C-A09C30E02942}"
+  name="finance_Portfolios"
+  displayName="finance_Portfolios"
+  ref="A1:G2"
+  totalsRowShown="0"
+  headerRowDxfId="214"
+  headerRowBorderDxfId="213"
+  tableBorderDxfId="212"
+  ><autoFilter
+  ref="A1:G2"
+  xr:uid="{25037879-D638-41CA-BC3C-A09C30E02942}"
+><tableColumns count="7"><tableColumn
+  id="1"
+  xr3:uid="{155820A8-4454-45CF-88E8-511231C6B171}"
+  name="ID"
+  ><tableColumn
+  id="6"
+  xr3:uid="{96F6DB92-4016-478B-9C2D-C8F62174ECC3}"
+  name="Kind:srcLastSaved"
+  ><tableColumn
+  id="2"
+  xr3:uid="{78BEFECE-D812-4DBC-8C34-4D40A1284A01}"
+  name="Kind:src"
+><calculatedColumnFormula>IF(finance_Portfolios[[#This Row],[Kind:srcLastSaved]]="",IF(finance_Portfolios[[#This Row],[Kind]]="","",INDEX(meta_Classifiers[ID],MATCH(finance_Portfolios[[#This Row],[Kind]],meta_Classifiers[Display Qualified],0))),finance_Portfolios[[#This Row],[Kind:srcLastSaved]])</calculatedColumnFormula></tableColumn><tableColumn
+  id="3"
+  xr3:uid="{E322332C-9E54-4107-871F-955998B9900F}"
+  name="Kind"
+  ><tableColumn
+  id="5"
+  xr3:uid="{22547BBF-5FCA-4A1E-B937-85128D6A3147}"
+  name="Package"
+  ><tableColumn
+  id="4"
+  xr3:uid="{218A46C3-1A3E-4E23-9240-9D465E00E968}"
+  name="Owner"
+  ><tableColumn
+  id="10"
+  xr3:uid="{4CE77B86-BEC0-304C-9794-CF4BCDD29FB3}"
+  name="Value"
+  ></tableColumns><tableStyleInfo
+  name="TableStyleLight9"
+  showFirstColumn="0"
+  showLastColumn="0"
+  showRowStripes="1"
+  showColumnStripes="0"
+  ></table>
\ No newline at end of file
```
