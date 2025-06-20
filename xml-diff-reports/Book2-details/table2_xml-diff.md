# Changes in Book2/xl/tables/table2.xml

```diff
diff --git a/Book2/xl/tables/table2.xml b/Book2/xl/tables/table2.xml
index 77b6b5c..2a7c96f 100644
--- a/Book2/xl/tables/table2.xml
+++ b/Book2/xl/tables/table2.xml
@@ -1,24 +1,8 @@
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table>
-    xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
-    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
-    mc:Ignorable="xr
-    xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
-    xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
-    id="2"
-    xr:uid="{66B616BC-A4F3-4ADE-9100-38A6D218C8A8}"
-    name="Table2"
-    displayName="Table2"
-    ref="A1:B5"
-    totalsRowShown="0"<autoFilter
-    ref="A1:B5"
-    xr:uid="{66B616BC-A4F3-4ADE-9100-38A6D218C8A8}"/<tableColumns
-    count="2"<tableColumn
-    id="1"
-    xr3:uid="{76EC1407-7957-4F4C-8663-9ADB29B5BE58}"
-    name="ID"/<tableColumn
-    id="2"
-    xr3:uid="{FEB4BD9E-DAD3-4F9C-9A37-8DF0377C3852}"
-    name="Column1"
-    dataDxfId="0"<calculatedColumnFormulaTable2[[#This
-    /2</calculatedColumnFormula></tableColumn></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="2" xr:uid="{66B616BC-A4F3-4ADE-9100-38A6D218C8A8}" name="Table2" displayName="Table2" ref="A1:B5" totalsRowShown="0"><autoFilter ref="A1:B5" xr:uid="{66B616BC-A4F3-4ADE-9100-38A6D218C8A8}"/>
+<tableColumns count="2">
+    <tableColumn id="1" xr3:uid="{76EC1407-7957-4F4C-8663-9ADB29B5BE58}" name="ID"/>
+    <tableColumn id="2" xr3:uid="{FEB4BD9E-DAD3-4F9C-9A37-8DF0377C3852}" name="Column1" dataDxfId="0"><calculatedColumnFormula>
+        Table2[[#This Row],[ID]]+13
+        /2
+    </calculatedColumnFormula></tableColumn></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
```
