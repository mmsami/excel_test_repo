# Changes in veri.excel/xl/tables/table12.xml

```diff
diff --git a/veri.excel/xl/tables/table12.xml b/veri.excel/xl/tables/table12.xml
new file mode 100644
index 0000000..b710d8c
--- /dev/null
+++ b/veri.excel/xl/tables/table12.xml
@@ -0,0 +1,12 @@
+<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
+<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="5" xr:uid="{00000000-000C-0000-FFFF-FFFF08000000}" name="meta_Literals" displayName="meta_Literals" ref="A1:J31" totalsRowShown="0" headerRowDxfId="209" dataDxfId="207" headerRowBorderDxfId="208" tableBorderDxfId="206"><autoFilter ref="A1:J31" xr:uid="{00000000-0009-0000-0100-000005000000}"/><tableColumns count="10"><tableColumn id="8" xr3:uid="{00000000-0010-0000-0800-000008000000}" name="ID" dataDxfId="205"/><tableColumn id="5" xr3:uid="{00000000-0010-0000-0800-000005000000}" name="Kind:src" dataDxfId="7"/><tableColumn id="2" xr3:uid="{00000000-0010-0000-0800-000002000000}" name="Kind" dataDxfId="204"><calculatedColumnFormula>IF(meta_Literals[[#This Row],[Kind:src]]="","",INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Literals[[#This Row],[Kind:src]],meta_Classifiers[ID],0)))</calculatedColumnFormula></tableColumn><tableColumn id="6" xr3:uid="{00000000-0010-0000-0800-000006000000}" name="Package"/><tableColumn id="1" xr3:uid="{00000000-0010-0000-0800-000001000000}" name="Sub Package" dataDxfId="203"/><tableColumn id="10" xr3:uid="{00000000-0010-0000-0800-00000A000000}" name="Display:q" dataDxfId="202"><calculatedColumnFormula>IF(TRIM(meta_Literals[[#This Row],[Package]])="","",TRIM(LOWER(meta_Literals[[#This Row],[Package]]))&"::")&meta_Literals[[#This Row],[Display]]</calculatedColumnFormula></tableColumn><tableColumn id="9" xr3:uid="{00000000-0010-0000-0800-000009000000}" name="Display" dataDxfId="201"><calculatedColumnFormula>TRIM(SUBSTITUTE(meta_Literals[[#This Row],[Name]]," ",""))</calculatedColumnFormula></tableColumn><tableColumn id="3" xr3:uid="{00000000-0010-0000-0800-000003000000}" name="Name" dataDxfId="200"/><tableColumn id="7" xr3:uid="{00000000-0010-0000-0800-000007000000}" name="Parent:src"/><tableColumn id="4" xr3:uid="{00000000-0010-0000-0800-000004000000}" name="Parent" dataDxfId="199"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Literals[[#This Row],[Parent:src]] ) = "",
+"",
+IF( LEFT(meta_Literals[[#This Row],[Parent:src]],1)="_",
+RIGHT(meta_Literals[[#This Row],[Parent:src]],LEN(meta_Literals[[#This Row],[Parent:src]])-1),
+IF( TRIM( meta_Literals[[#This Row],[Package]] )
+    <> TRIM( INDEX( meta_Literals[Package], MATCH( meta_Literals[[#This Row],[Parent:src]], meta_Literals[ID],0 ) ) ),
+TRIM( INDEX( meta_Literals[Package], MATCH( meta_Literals[[#This Row],[Parent:src]], meta_Literals[ID], 0 ) ) )
+& "::"
+& INDEX( meta_Literals[Display], MATCH( meta_Literals[[#This Row],[Parent:src]], meta_Literals[ID], 0 ) ),
+INDEX( meta_Literals[Display], MATCH( meta_Literals[[#This Row],[Parent:src]], meta_Literals[ID], 0 ) )
+))), "")</calculatedColumnFormula></tableColumn></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
```
