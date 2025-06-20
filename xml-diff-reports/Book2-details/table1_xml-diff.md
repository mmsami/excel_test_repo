# Changes in Book2/xl/tables/table1.xml

```diff
diff --git a/Book2/xl/tables/table1.xml b/Book2/xl/tables/table1.xml
index c01ea2f..d855c6d 100644
--- a/Book2/xl/tables/table1.xml
+++ b/Book2/xl/tables/table1.xml
@@ -1,27 +1,5 @@
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table>
-    xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
-    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
-    mc:Ignorable="xr
-    xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
-    xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
-    id="1"
-    xr:uid="{562DDDFA-75DE-4D06-B40C-108F06E36225}"
-    name="Table1"
-    displayName="Table1"
-    ref="A1:B3"
-    totalsRowShown="0"<autoFilter
-    ref="A1:B3"
-    xr:uid="{562DDDFA-75DE-4D06-B40C-108F06E36225}"/<tableColumns
-    count="2"<tableColumn
-    id="1"
-    xr3:uid="{CF9405A0-E035-4B21-9E75-176614C8A895}"
-    name="ID"/<tableColumn
-    id="2"
-    xr3:uid="{CE56EC3B-7AA6-4F23-9937-BD2CE3F47E75}"
-    name="Ref"/</tableColumns<tableStyleInfo
-    name="TableStyleLight9"
-    showFirstColumn="0"
-    showLastColumn="0"
-    showRowStripes="1"
-    showColumnStripes="0"/</table
\ No newline at end of file
+<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="1" xr:uid="{562DDDFA-75DE-4D06-B40C-108F06E36225}" name="Table1" displayName="Table1" ref="A1:B3" totalsRowShown="0"><autoFilter ref="A1:B3" xr:uid="{562DDDFA-75DE-4D06-B40C-108F06E36225}"/>
+<tableColumns count="2">
+    <tableColumn id="1" xr3:uid="{CF9405A0-E035-4B21-9E75-176614C8A895}" name="ID"/>
+    <tableColumn id="2" xr3:uid="{CE56EC3B-7AA6-4F23-9937-BD2CE3F47E75}" name="Ref"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
```
