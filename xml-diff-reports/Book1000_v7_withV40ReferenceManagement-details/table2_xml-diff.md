# Changes in Book1000_v7_withV40ReferenceManagement/xl/tables/table2.xml

```diff
diff --git a/Book1000_v7_withV40ReferenceManagement/xl/tables/table2.xml b/Book1000_v7_withV40ReferenceManagement/xl/tables/table2.xml
new file mode 100644
index 0000000..1eabc79
--- /dev/null
+++ b/Book1000_v7_withV40ReferenceManagement/xl/tables/table2.xml
@@ -0,0 +1,46 @@
+<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
+<table
+  xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
+  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
+  mc:Ignorable="xr xr3"
+  xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
+  xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
+  id="2"
+  xr:uid="{BB3DCF18-2BE8-48FE-A57B-2A65F9B11CD5}"
+  name="Table2"
+  displayName="Table2"
+  ref="A1:D1001"
+  totalsRowShown="0"
+  headerRowDxfId="6"
+  dataDxfId="4"
+  headerRowBorderDxfId="5"
+  ><autoFilter
+  ref="A1:D1001"
+  xr:uid="{BB3DCF18-2BE8-48FE-A57B-2A65F9B11CD5}"
+><tableColumns count="4"><tableColumn
+  id="1"
+  xr3:uid="{850E40B1-FD5B-4F56-B475-C71D367C7C5B}"
+  name="ID"
+  dataDxfId="3"
+  ><tableColumn
+  id="2"
+  xr3:uid="{7601C884-6319-4BCC-8EB6-F7163D882513}"
+  name="Selector"
+  dataDxfId="2"
+><calculatedColumnFormula>IF(Table2[[#This Row],[Part1]]="","",Table2[[#This Row],[Part1]][&]"_"[&]Table2[[#This Row],[Part2]])</calculatedColumnFormula></tableColumn><tableColumn
+  id="3"
+  xr3:uid="{4385B30F-6B80-4C65-B665-97859B097541}"
+  name="Part1"
+  dataDxfId="1"
+  ><tableColumn
+  id="4"
+  xr3:uid="{E3D2BD82-7536-4613-9426-34935924DE12}"
+  name="Part2"
+  dataDxfId="0"
+  ></tableColumns><tableStyleInfo
+  name="TableStyleLight9"
+  showFirstColumn="0"
+  showLastColumn="0"
+  showRowStripes="1"
+  showColumnStripes="0"
+  ></table>
\ No newline at end of file
```
