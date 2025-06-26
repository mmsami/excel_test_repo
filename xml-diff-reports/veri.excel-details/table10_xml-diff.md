# Changes in veri.excel/xl/tables/table10.xml

```diff
diff --git a/veri.excel/xl/tables/table10.xml b/veri.excel/xl/tables/table10.xml
index 70931b5..5d80bb7 100644
--- a/veri.excel/xl/tables/table10.xml
+++ b/veri.excel/xl/tables/table10.xml
@@ -1,32 +1,32 @@
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="2" xr:uid="{00000000-000C-0000-FFFF-FFFF01000000}" name="meta_Classifiers" displayName="meta_Classifiers" ref="A2:S65" totalsRowShown="0" headerRowDxfId="290" dataDxfId="288" headerRowBorderDxfId="289"><autoFilter ref="A2:S65" xr:uid="{00000000-0009-0000-0100-000002000000}"><filterColumn colId="10"><filters><filter val="Package"/><filter val="Package Documentation"/></filters></filterColumn></autoFilter>
+<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="2" xr:uid="{00000000-000C-0000-FFFF-FFFF01000000}" name="meta_Classifiers" displayName="meta_Classifiers" ref="A2:S65" totalsRowShown="0" headerRowDxfId="291" dataDxfId="289" headerRowBorderDxfId="290"><autoFilter ref="A2:S65" xr:uid="{00000000-0009-0000-0100-000002000000}"><filterColumn colId="10"><filters><filter val="Package"/><filter val="Package Documentation"/></filters></filterColumn></autoFilter>
     <tableColumns count="19">
-        <tableColumn id="1" xr3:uid="{00000000-0010-0000-0100-000001000000}" name="ID" dataDxfId="287"/>
-        <tableColumn id="18" xr3:uid="{2BE72F52-E16A-4A6E-B454-1FDF1FC0AC76}" name="Kind:src" dataDxfId="286"/>
-        <tableColumn id="3" xr3:uid="{00000000-0010-0000-0100-000003000000}" name="Kind" dataDxfId="285"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Classifiers[[#This Row],[Kind:src]] ) = "", "",
+        <tableColumn id="1" xr3:uid="{00000000-0010-0000-0100-000001000000}" name="ID" dataDxfId="288"/>
+        <tableColumn id="18" xr3:uid="{2BE72F52-E16A-4A6E-B454-1FDF1FC0AC76}" name="Kind:src" dataDxfId="287"/>
+        <tableColumn id="3" xr3:uid="{00000000-0010-0000-0100-000003000000}" name="Kind" dataDxfId="286"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Classifiers[[#This Row],[Kind:src]] ) = "", "",
         INDEX( meta_Classifiers[Display Qualified], MATCH( meta_Classifiers[[#This Row],[Kind:src]], meta_Classifiers[ID], 0 ) ) )</calculatedColumnFormula></tableColumn>
-            <tableColumn id="17" xr3:uid="{C15F333B-6398-4ED0-8E83-CB851911C29C}" name="Order" dataDxfId="284"/>
-            <tableColumn id="6" xr3:uid="{00000000-0010-0000-0100-000006000000}" name="Package" dataDxfId="283"/>
-            <tableColumn id="11" xr3:uid="{00000000-0010-0000-0100-00000B000000}" name="Sub Package" dataDxfId="282"/>
-            <tableColumn id="8" xr3:uid="{00000000-0010-0000-0100-000008000000}" name="Display Qualified" dataDxfId="281"><calculatedColumnFormula>
+            <tableColumn id="17" xr3:uid="{C15F333B-6398-4ED0-8E83-CB851911C29C}" name="Order" dataDxfId="285"/>
+            <tableColumn id="6" xr3:uid="{00000000-0010-0000-0100-000006000000}" name="Package" dataDxfId="284"/>
+            <tableColumn id="11" xr3:uid="{00000000-0010-0000-0100-00000B000000}" name="Sub Package" dataDxfId="283"/>
+            <tableColumn id="8" xr3:uid="{00000000-0010-0000-0100-000008000000}" name="Display Qualified" dataDxfId="282"><calculatedColumnFormula>
                 IF(LEFT(meta_Classifiers[[#This Row],[ID]],1)="_",RIGHT(meta_Classifiers[[#This Row],[ID]],LEN(meta_Classifiers[[#This Row],[ID]])-1),IF(TRIM(meta_Classifiers[[#This Row],[Package]])="","",TRIM(LOWER(meta_Classifiers[[#This Row],[Package]]))&"::")&meta_Classifiers[[#This Row],[Display]])
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="12" xr3:uid="{C4932769-4A2F-4CCD-846B-6F83E29A3C65}" name="Display Allways Qualified" dataDxfId="280"><calculatedColumnFormula>
+            <tableColumn id="12" xr3:uid="{C4932769-4A2F-4CCD-846B-6F83E29A3C65}" name="Display Allways Qualified" dataDxfId="281"><calculatedColumnFormula>
                 IF(TRIM(meta_Classifiers[[#This Row],[Package]])="","",TRIM(LOWER(meta_Classifiers[[#This Row],[Package]]))&"::")&meta_Classifiers[[#This Row],[Display]]
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="4" xr3:uid="{1F96AF77-F561-498C-83C6-97508193393F}" name="Class Display Qualified" dataDxfId="279"><calculatedColumnFormula>
+            <tableColumn id="4" xr3:uid="{1F96AF77-F561-498C-83C6-97508193393F}" name="Class Display Qualified" dataDxfId="280"><calculatedColumnFormula>
                 IF(meta_Classifiers[[#This Row],[Kind:src]]="_Class",meta_Classifiers[[#This Row],[Display Qualified]],"")
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="7" xr3:uid="{00000000-0010-0000-0100-000007000000}" name="Display" dataDxfId="278"><calculatedColumnFormula array="1">_xlfn.IFNA(INDEX(meta_Names[Camel Upper], MATCH(meta_Classifiers[[#This Row],[Name]],meta_Names[String],0)),camelCaseUpper(meta_Classifiers[[#This Row],[Name]]))</calculatedColumnFormula></tableColumn>
-                <tableColumn id="2" xr3:uid="{00000000-0010-0000-0100-000002000000}" name="Name" dataDxfId="277"/>
-                <tableColumn id="10" xr3:uid="{00000000-0010-0000-0100-00000A000000}" name="Class - Abstract" dataDxfId="276"/>
-                <tableColumn id="19" xr3:uid="{ED60A2E8-F17C-4073-BE76-82B6FA2B86D4}" name="Class - Generalization:src" dataDxfId="275"/>
-                <tableColumn id="9" xr3:uid="{00000000-0010-0000-0100-000009000000}" name="Class - Generalization" dataDxfId="274"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Classifiers[[#This Row],[Class - Generalization:src]] ) = "", "",
+            <tableColumn id="7" xr3:uid="{00000000-0010-0000-0100-000007000000}" name="Display" dataDxfId="279"><calculatedColumnFormula array="1">_xlfn.IFNA(INDEX(meta_Names[Camel Upper], MATCH(meta_Classifiers[[#This Row],[Name]],meta_Names[String],0)),camelCaseUpper(meta_Classifiers[[#This Row],[Name]]))</calculatedColumnFormula></tableColumn>
+                <tableColumn id="2" xr3:uid="{00000000-0010-0000-0100-000002000000}" name="Name" dataDxfId="278"/>
+                <tableColumn id="10" xr3:uid="{00000000-0010-0000-0100-00000A000000}" name="Class - Abstract" dataDxfId="277"/>
+                <tableColumn id="19" xr3:uid="{ED60A2E8-F17C-4073-BE76-82B6FA2B86D4}" name="Class - Generalization:src" dataDxfId="276"/>
+                <tableColumn id="9" xr3:uid="{00000000-0010-0000-0100-000009000000}" name="Class - Generalization" dataDxfId="275"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Classifiers[[#This Row],[Class - Generalization:src]] ) = "", "",
         INDEX( meta_Classifiers[Display Qualified], MATCH( meta_Classifiers[[#This Row],[Class - Generalization:src]], meta_Classifiers[ID], 0 ) ) )</calculatedColumnFormula></tableColumn>
-                    <tableColumn id="5" xr3:uid="{00000000-0010-0000-0100-000005000000}" name="Definition" dataDxfId="273"/>
-                    <tableColumn id="15" xr3:uid="{67827286-A0CE-49AE-BFD2-FA4C08880A6B}" name="Class - Display Property:src" dataDxfId="272"/>
-                    <tableColumn id="13" xr3:uid="{FBD4F397-3D8C-4243-AF74-B11E28814CC7}" name="Class - Display Property" dataDxfId="271"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Classifiers[[#This Row],[Class - Display Property:src]] ) = "", "",
+                    <tableColumn id="5" xr3:uid="{00000000-0010-0000-0100-000005000000}" name="Definition" dataDxfId="274"/>
+                    <tableColumn id="15" xr3:uid="{67827286-A0CE-49AE-BFD2-FA4C08880A6B}" name="Class - Display Property:src" dataDxfId="273"/>
+                    <tableColumn id="13" xr3:uid="{FBD4F397-3D8C-4243-AF74-B11E28814CC7}" name="Class - Display Property" dataDxfId="272"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Classifiers[[#This Row],[Class - Display Property:src]] ) = "", "",
         INDEX( meta_TypedModelElements[Display Qualified], MATCH( meta_Classifiers[[#This Row],[Class - Display Property:src]], meta_TypedModelElements[ID], 0 ) ) )</calculatedColumnFormula></tableColumn>
                         <tableColumn id="16" xr3:uid="{6EB0D161-6AFB-4810-AC28-A47D7D3FC7C6}" name="Class - Business ID Property:src"/>
-                        <tableColumn id="14" xr3:uid="{5DEE7546-0461-4D10-BEC9-28B98283AB48}" name="Class - Business ID Property" dataDxfId="270"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Classifiers[[#This Row],[Class - Business ID Property:src]] ) = "", "",
+                        <tableColumn id="14" xr3:uid="{5DEE7546-0461-4D10-BEC9-28B98283AB48}" name="Class - Business ID Property" dataDxfId="271"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Classifiers[[#This Row],[Class - Business ID Property:src]] ) = "", "",
         INDEX( meta_TypedModelElements[Display Qualified], MATCH( meta_Classifiers[[#This Row],[Class - Business ID Property:src]], meta_TypedModelElements[ID], 0 ) ) )</calculatedColumnFormula></tableColumn></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
```
