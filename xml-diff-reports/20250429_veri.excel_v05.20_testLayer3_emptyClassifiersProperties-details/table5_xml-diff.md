# Changes in 20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table5.xml

```diff
diff --git a/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table5.xml b/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table5.xml
index 1c7bf25..606c0d2 100644
--- a/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table5.xml
+++ b/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table5.xml
@@ -1,2 +1,55 @@
-<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="16" xr:uid="{B2345C52-F340-8841-B683-0AC52444DBD0}" name="meta_Snippets" displayName="meta_Snippets" ref="A1:H918" totalsRowShown="0"><autoFilter ref="A1:H918" xr:uid="{B2345C52-F340-8841-B683-0AC52444DBD0}"/><tableColumns count="8"><tableColumn id="1" xr3:uid="{69B9AC31-F0E8-BC47-AA18-356C43A82883}" name="ID"/><tableColumn id="8" xr3:uid="{1B246ACA-DE2B-42E4-BF9F-5B1B9F54087C}" name="Kind:srcLastSaved"/><tableColumn id="2" xr3:uid="{E5F6CEA0-213A-E54B-AAF3-5285468EA4C4}" name="Kind:src"><calculatedColumnFormula>IF(meta_Snippets[[#This Row],[Kind:srcLastSaved]]="",IF(meta_Snippets[[#This Row],[Kind]]="","",INDEX(meta_Classifiers[ID],MATCH(meta_Snippets[[#This Row],[Kind]],meta_Classifiers[Display Qualified],0))),meta_Snippets[[#This Row],[Kind:srcLastSaved]])</calculatedColumnFormula></tableColumn><tableColumn id="3" xr3:uid="{8A99F847-149C-3848-A20C-500C88A05B72}" name="Kind"/><tableColumn id="4" xr3:uid="{44ADD645-CB9E-AD4D-B115-2866AC7A50AE}" name="Package"/><tableColumn id="5" xr3:uid="{EC8094DA-1CFB-1441-BDE7-0BBC204E53AC}" name="Sub Package"/><tableColumn id="6" xr3:uid="{135BE991-7445-F24A-AA4B-450FE6A03875}" name="Line"/><tableColumn id="7" xr3:uid="{F98198AA-6E62-5F42-B9AC-401F7E30DA84}" name="Snippet"/></tableColumns><tableStyleInfo name="TableStyleMedium2" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
+<table
+  xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
+  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
+  mc:Ignorable="xr xr3"
+  xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
+  xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
+  id="16"
+  xr:uid="{B2345C52-F340-8841-B683-0AC52444DBD0}"
+  name="meta_Snippets"
+  displayName="meta_Snippets"
+  ref="A1:H918"
+  totalsRowShown="0"
+  ><autoFilter
+  ref="A1:H918"
+  xr:uid="{B2345C52-F340-8841-B683-0AC52444DBD0}"
+><tableColumns count="8"><tableColumn
+  id="1"
+  xr3:uid="{69B9AC31-F0E8-BC47-AA18-356C43A82883}"
+  name="ID"
+  ><tableColumn
+  id="8"
+  xr3:uid="{1B246ACA-DE2B-42E4-BF9F-5B1B9F54087C}"
+  name="Kind:srcLastSaved"
+  ><tableColumn
+  id="2"
+  xr3:uid="{E5F6CEA0-213A-E54B-AAF3-5285468EA4C4}"
+  name="Kind:src"
+><calculatedColumnFormula>IF(meta_Snippets[[#This Row],[Kind:srcLastSaved]]="",IF(meta_Snippets[[#This Row],[Kind]]="","",INDEX(meta_Classifiers[ID],MATCH(meta_Snippets[[#This Row],[Kind]],meta_Classifiers[Display Qualified],0))),meta_Snippets[[#This Row],[Kind:srcLastSaved]])</calculatedColumnFormula></tableColumn><tableColumn
+  id="3"
+  xr3:uid="{8A99F847-149C-3848-A20C-500C88A05B72}"
+  name="Kind"
+  ><tableColumn
+  id="4"
+  xr3:uid="{44ADD645-CB9E-AD4D-B115-2866AC7A50AE}"
+  name="Package"
+  ><tableColumn
+  id="5"
+  xr3:uid="{EC8094DA-1CFB-1441-BDE7-0BBC204E53AC}"
+  name="Sub Package"
+  ><tableColumn
+  id="6"
+  xr3:uid="{135BE991-7445-F24A-AA4B-450FE6A03875}"
+  name="Line"
+  ><tableColumn
+  id="7"
+  xr3:uid="{F98198AA-6E62-5F42-B9AC-401F7E30DA84}"
+  name="Snippet"
+  ></tableColumns><tableStyleInfo
+  name="TableStyleMedium2"
+  showFirstColumn="0"
+  showLastColumn="0"
+  showRowStripes="1"
+  showColumnStripes="0"
+  ></table>
\ No newline at end of file
```
