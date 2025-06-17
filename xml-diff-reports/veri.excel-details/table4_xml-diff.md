# Changes in veri.excel/xl/tables/table4.xml

```diff
diff --git a/veri.excel/xl/tables/table4.xml b/veri.excel/xl/tables/table4.xml
index b12dcaa..220c4ef 100644
--- a/veri.excel/xl/tables/table4.xml
+++ b/veri.excel/xl/tables/table4.xml
@@ -1,2 +1,63 @@
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="15" xr:uid="{00000000-000C-0000-FFFF-FFFF00000000}" name="meta_DocumentVersions" displayName="meta_DocumentVersions" ref="A2:J10" totalsRowShown="0" headerRowDxfId="411" dataDxfId="410"><autoFilter ref="A2:J10" xr:uid="{00000000-0009-0000-0100-00000F000000}"/><tableColumns count="10"><tableColumn id="1" xr3:uid="{00000000-0010-0000-0000-000001000000}" name="ID" dataDxfId="409"/><tableColumn id="2" xr3:uid="{00000000-0010-0000-0000-000002000000}" name="Name" dataDxfId="408"/><tableColumn id="3" xr3:uid="{00000000-0010-0000-0000-000003000000}" name="Version" dataDxfId="407"/><tableColumn id="4" xr3:uid="{00000000-0010-0000-0000-000004000000}" name="Date Tag" dataDxfId="406"/><tableColumn id="5" xr3:uid="{00000000-0010-0000-0000-000005000000}" name="File Name" dataDxfId="405"><calculatedColumnFormula>meta_DocumentVersions[[#This Row],[Date Tag]]&"_"&meta_DocumentVersions[[#This Row],[Name]]&"_"&meta_DocumentVersions[[#This Row],[Version]]&".xlsm"</calculatedColumnFormula></tableColumn><tableColumn id="6" xr3:uid="{00000000-0010-0000-0000-000006000000}" name="Change Log" dataDxfId="404"/><tableColumn id="9" xr3:uid="{00000000-0010-0000-0000-000009000000}" name="Branch of Document" dataDxfId="403"/><tableColumn id="7" xr3:uid="{00000000-0010-0000-0000-000007000000}" name="Create Branch" dataDxfId="402"/><tableColumn id="8" xr3:uid="{00000000-0010-0000-0000-000008000000}" name="Merge Branch" dataDxfId="401"/><tableColumn id="10" xr3:uid="{00000000-0010-0000-0000-00000A000000}" name="Freeze Version" dataDxfId="400"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+<table>
+    xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
+    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
+    mc:Ignorable="xr
+    xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
+    xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
+    id="15"
+    xr:uid="{00000000-000C-0000-FFFF-FFFF00000000}"
+    name="meta_DocumentVersions"
+    displayName="meta_DocumentVersions"
+    ref="A2:J10"
+    totalsRowShown="0"
+    headerRowDxfId="420"
+    dataDxfId="419"<autoFilter
+    ref="A2:J10"
+    xr:uid="{00000000-0009-0000-0100-00000F000000}"/<tableColumns
+    count="10"<tableColumn
+    id="1"
+    xr3:uid="{00000000-0010-0000-0000-000001000000}"
+    name="ID"
+    dataDxfId="418"/<tableColumn
+    id="2"
+    xr3:uid="{00000000-0010-0000-0000-000002000000}"
+    name="Name"
+    dataDxfId="417"/<tableColumn
+    id="3"
+    xr3:uid="{00000000-0010-0000-0000-000003000000}"
+    name="Version"
+    dataDxfId="416"/<tableColumn
+    id="4"
+    xr3:uid="{00000000-0010-0000-0000-000004000000}"
+    name="Date
+    dataDxfId="415"/<tableColumn
+    id="5"
+    xr3:uid="{00000000-0010-0000-0000-000005000000}"
+    name="File
+    dataDxfId="414"<calculatedColumnFormulameta_DocumentVersions[[#This
+    id="6"
+    xr3:uid="{00000000-0010-0000-0000-000006000000}"
+    name="Change
+    dataDxfId="413"/<tableColumn
+    id="9"
+    xr3:uid="{00000000-0010-0000-0000-000009000000}"
+    name="Branch
+    dataDxfId="412"/<tableColumn
+    id="7"
+    xr3:uid="{00000000-0010-0000-0000-000007000000}"
+    name="Create
+    dataDxfId="411"/<tableColumn
+    id="8"
+    xr3:uid="{00000000-0010-0000-0000-000008000000}"
+    name="Merge
+    dataDxfId="410"/<tableColumn
+    id="10"
+    xr3:uid="{00000000-0010-0000-0000-00000A000000}"
+    name="Freeze
+    dataDxfId="409"/</tableColumns<tableStyleInfo
+    name="TableStyleLight9"
+    showFirstColumn="0"
+    showLastColumn="0"
+    showRowStripes="1"
+    showColumnStripes="0"/</table
\ No newline at end of file
```
