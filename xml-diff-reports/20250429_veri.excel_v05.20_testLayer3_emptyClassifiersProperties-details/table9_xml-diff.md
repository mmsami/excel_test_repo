# Changes in 20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table9.xml

```diff
diff --git a/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table9.xml b/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table9.xml
index 61f64b4..8a7fccf 100644
--- a/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table9.xml
+++ b/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/20250429_veri.excel_v05.20_testLayer3_emptyClassifiersProperties/xl/tables/table9.xml
@@ -1,14 +1,143 @@
-<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="2" xr:uid="{00000000-000C-0000-FFFF-FFFF01000000}" name="meta_Classifiers" displayName="meta_Classifiers" ref="A2:U3" totalsRowShown="0" headerRowDxfId="92" dataDxfId="90" headerRowBorderDxfId="91"><autoFilter ref="A2:U3" xr:uid="{00000000-0009-0000-0100-000002000000}"/><tableColumns count="21"><tableColumn id="1" xr3:uid="{00000000-0010-0000-0100-000001000000}" name="ID" dataDxfId="89"/><tableColumn id="12" xr3:uid="{00000000-0010-0000-0100-00000C000000}" name="Kind:srcLastSaved" dataDxfId="88"/><tableColumn id="18" xr3:uid="{2BE72F52-E16A-4A6E-B454-1FDF1FC0AC76}" name="Kind:src" dataDxfId="87"><calculatedColumnFormula>IF(meta_Classifiers[[#This Row],[Kind:srcLastSaved]][<][>]"", meta_Classifiers[[#This Row],[Kind:srcLastSaved]],
-   IF(meta_Classifiers[[#This Row],[Kind]]="","",
-      INDEX(meta_Classifiers[ID],
-         MATCH(meta_Classifiers[[#This Row],[Kind]],meta_Classifiers[Display Qualified],0))))</calculatedColumnFormula></tableColumn><tableColumn id="3" xr3:uid="{00000000-0010-0000-0100-000003000000}" name="Kind" dataDxfId="86"/><tableColumn id="17" xr3:uid="{C15F333B-6398-4ED0-8E83-CB851911C29C}" name="Order" dataDxfId="85"/><tableColumn id="6" xr3:uid="{00000000-0010-0000-0100-000006000000}" name="Package" dataDxfId="84"/><tableColumn id="11" xr3:uid="{00000000-0010-0000-0100-00000B000000}" name="Sub Package" dataDxfId="83"/><tableColumn id="8" xr3:uid="{00000000-0010-0000-0100-000008000000}" name="Display Qualified" dataDxfId="82"><calculatedColumnFormula>IF(LEFT(meta_Classifiers[[#This Row],[ID]],1)="_",RIGHT(meta_Classifiers[[#This Row],[ID]],LEN(meta_Classifiers[[#This Row],[ID]])-1),IF(TRIM(meta_Classifiers[[#This Row],[Package]])="","",TRIM(LOWER(meta_Classifiers[[#This Row],[Package]]))[&]"::")[&]meta_Classifiers[[#This Row],[Display]])</calculatedColumnFormula></tableColumn><tableColumn id="7" xr3:uid="{00000000-0010-0000-0100-000007000000}" name="Display" dataDxfId="81"><calculatedColumnFormula>camelCaseUpper(meta_Classifiers[[#This Row],[Name]])</calculatedColumnFormula></tableColumn><tableColumn id="2" xr3:uid="{00000000-0010-0000-0100-000002000000}" name="Name" dataDxfId="80"/><tableColumn id="10" xr3:uid="{00000000-0010-0000-0100-00000A000000}" name="Class - Abstract" dataDxfId="79"/><tableColumn id="4" xr3:uid="{00000000-0010-0000-0100-000004000000}" name="Class - Generalization:srcLastSaved" dataDxfId="78"/><tableColumn id="19" xr3:uid="{ED60A2E8-F17C-4073-BE76-82B6FA2B86D4}" name="Class - Generalization:src" dataDxfId="77"><calculatedColumnFormula>IF(meta_Classifiers[[#This Row],[Class - Generalization:srcLastSaved]][<][>]"", meta_Classifiers[[#This Row],[Class - Generalization:srcLastSaved]],
-   IF(meta_Classifiers[[#This Row],[Class - Generalization]]="","",
-      INDEX(meta_Classifiers[ID],
-         MATCH(meta_Classifiers[[#This Row],[Class - Generalization]],meta_Classifiers[Display Qualified],0))))</calculatedColumnFormula></tableColumn><tableColumn id="9" xr3:uid="{00000000-0010-0000-0100-000009000000}" name="Class - Generalization" dataDxfId="76"/><tableColumn id="5" xr3:uid="{00000000-0010-0000-0100-000005000000}" name="Definition" dataDxfId="75"/><tableColumn id="20" xr3:uid="{E074B6E9-B94D-4E36-AB65-A0E5E5549465}" name="Class - Display Property:srcLastSaved" dataDxfId="74"/><tableColumn id="15" xr3:uid="{67827286-A0CE-49AE-BFD2-FA4C08880A6B}" name="Class - Display Property:src" dataDxfId="73"><calculatedColumnFormula>IF(meta_Classifiers[[#This Row],[Class - Display Property:srcLastSaved]][<][>]"", meta_Classifiers[[#This Row],[Class - Display Property:srcLastSaved]],
-   IF(meta_Classifiers[[#This Row],[Class - Display Property]]="","",
-      INDEX(meta_TypedModelElements[ID],
-         MATCH(meta_Classifiers[[#This Row],[Class - Display Property]],meta_TypedModelElements[Display Qualified],0))))</calculatedColumnFormula></tableColumn><tableColumn id="13" xr3:uid="{FBD4F397-3D8C-4243-AF74-B11E28814CC7}" name="Class - Display Property" dataDxfId="72"/><tableColumn id="21" xr3:uid="{B8BA11DB-EFB5-466E-8AB6-18EFBE69CC8A}" name="Class - Business ID Property:srcLastSaved" dataDxfId="71"/><tableColumn id="16" xr3:uid="{6EB0D161-6AFB-4810-AC28-A47D7D3FC7C6}" name="Class - Business ID Property:src" dataDxfId="70"><calculatedColumnFormula>IF(meta_Classifiers[[#This Row],[Class - Business ID Property:srcLastSaved]][<][>]"", meta_Classifiers[[#This Row],[Class - Business ID Property:srcLastSaved]],
-   IF(meta_Classifiers[[#This Row],[Class - Business ID Property]]="","",
-      INDEX(meta_TypedModelElements[ID],
-         MATCH(meta_Classifiers[[#This Row],[Class - Business ID Property]],meta_TypedModelElements[Display Qualified],0))))</calculatedColumnFormula></tableColumn><tableColumn id="14" xr3:uid="{5DEE7546-0461-4D10-BEC9-28B98283AB48}" name="Class - Business ID Property" dataDxfId="69"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
+<table
+  xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
+  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
+  mc:Ignorable="xr xr3"
+  xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
+  xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
+  id="2"
+  xr:uid="{00000000-000C-0000-FFFF-FFFF01000000}"
+  name="meta_Classifiers"
+  displayName="meta_Classifiers"
+  ref="A2:U3"
+  totalsRowShown="0"
+  headerRowDxfId="92"
+  dataDxfId="90"
+  headerRowBorderDxfId="91"
+  ><autoFilter
+  ref="A2:U3"
+  xr:uid="{00000000-0009-0000-0100-000002000000}"
+><tableColumns count="21"><tableColumn
+  id="1"
+  xr3:uid="{00000000-0010-0000-0100-000001000000}"
+  name="ID"
+  dataDxfId="89"
+  ><tableColumn
+  id="12"
+  xr3:uid="{00000000-0010-0000-0100-00000C000000}"
+  name="Kind:srcLastSaved"
+  dataDxfId="88"
+  ><tableColumn
+  id="18"
+  xr3:uid="{2BE72F52-E16A-4A6E-B454-1FDF1FC0AC76}"
+  name="Kind:src"
+  dataDxfId="87"
+  ><calculatedColumnFormula>IF(meta_Classifiers[[#This Row],[Kind:srcLastSaved]][<][>]"", meta_Classifiers[[#This Row],[Kind:srcLastSaved]],
+   IF(meta_Classifiers[[#This Row],[Kind]]="","",
+  INDEX(meta_Classifiers[ID],
+  MATCH(meta_Classifiers[[#This Row],[Kind]],meta_Classifiers[Display Qualified],0))))</calculatedColumnFormula></tableColumn><tableColumn
+  id="3"
+  xr3:uid="{00000000-0010-0000-0100-000003000000}"
+  name="Kind"
+  dataDxfId="86"
+  ><tableColumn
+  id="17"
+  xr3:uid="{C15F333B-6398-4ED0-8E83-CB851911C29C}"
+  name="Order"
+  dataDxfId="85"
+  ><tableColumn
+  id="6"
+  xr3:uid="{00000000-0010-0000-0100-000006000000}"
+  name="Package"
+  dataDxfId="84"
+  ><tableColumn
+  id="11"
+  xr3:uid="{00000000-0010-0000-0100-00000B000000}"
+  name="Sub Package"
+  dataDxfId="83"
+  ><tableColumn
+  id="8"
+  xr3:uid="{00000000-0010-0000-0100-000008000000}"
+  name="Display Qualified"
+  dataDxfId="82"
+><calculatedColumnFormula>IF(LEFT(meta_Classifiers[[#This Row],[ID]],1)="_",RIGHT(meta_Classifiers[[#This Row],[ID]],LEN(meta_Classifiers[[#This Row],[ID]])-1),IF(TRIM(meta_Classifiers[[#This Row],[Package]])="","",TRIM(LOWER(meta_Classifiers[[#This Row],[Package]]))[&]"::")[&]meta_Classifiers[[#This Row],[Display]])</calculatedColumnFormula></tableColumn><tableColumn
+  id="7"
+  xr3:uid="{00000000-0010-0000-0100-000007000000}"
+  name="Display"
+  dataDxfId="81"
+  ><calculatedColumnFormula>camelCaseUpper(meta_Classifiers[[#This Row],[Name]])</calculatedColumnFormula></tableColumn><tableColumn
+  id="2"
+  xr3:uid="{00000000-0010-0000-0100-000002000000}"
+  name="Name"
+  dataDxfId="80"
+  ><tableColumn
+  id="10"
+  xr3:uid="{00000000-0010-0000-0100-00000A000000}"
+  name="Class - Abstract"
+  dataDxfId="79"
+  ><tableColumn
+  id="4"
+  xr3:uid="{00000000-0010-0000-0100-000004000000}"
+  name="Class - Generalization:srcLastSaved"
+  dataDxfId="78"
+  ><tableColumn
+  id="19"
+  xr3:uid="{ED60A2E8-F17C-4073-BE76-82B6FA2B86D4}"
+  name="Class - Generalization:src"
+  dataDxfId="77"
+  ><calculatedColumnFormula>IF(meta_Classifiers[[#This Row],[Class - Generalization:srcLastSaved]][<][>]"", meta_Classifiers[[#This Row],[Class - Generalization:srcLastSaved]],
+   IF(meta_Classifiers[[#This Row],[Class - Generalization]]="","",
+  INDEX(meta_Classifiers[ID],
+  MATCH(meta_Classifiers[[#This Row],[Class - Generalization]],meta_Classifiers[Display Qualified],0))))</calculatedColumnFormula></tableColumn><tableColumn
+  id="9"
+  xr3:uid="{00000000-0010-0000-0100-000009000000}"
+  name="Class - Generalization"
+  dataDxfId="76"
+  ><tableColumn
+  id="5"
+  xr3:uid="{00000000-0010-0000-0100-000005000000}"
+  name="Definition"
+  dataDxfId="75"
+  ><tableColumn
+  id="20"
+  xr3:uid="{E074B6E9-B94D-4E36-AB65-A0E5E5549465}"
+  name="Class - Display Property:srcLastSaved"
+  dataDxfId="74"
+  ><tableColumn
+  id="15"
+  xr3:uid="{67827286-A0CE-49AE-BFD2-FA4C08880A6B}"
+  name="Class - Display Property:src"
+  dataDxfId="73"
+  ><calculatedColumnFormula>IF(meta_Classifiers[[#This Row],[Class - Display Property:srcLastSaved]][<][>]"", meta_Classifiers[[#This Row],[Class - Display Property:srcLastSaved]],
+   IF(meta_Classifiers[[#This Row],[Class - Display Property]]="","",
+  INDEX(meta_TypedModelElements[ID],
+  MATCH(meta_Classifiers[[#This Row],[Class - Display Property]],meta_TypedModelElements[Display Qualified],0))))</calculatedColumnFormula></tableColumn><tableColumn
+  id="13"
+  xr3:uid="{FBD4F397-3D8C-4243-AF74-B11E28814CC7}"
+  name="Class - Display Property"
+  dataDxfId="72"
+  ><tableColumn
+  id="21"
+  xr3:uid="{B8BA11DB-EFB5-466E-8AB6-18EFBE69CC8A}"
+  name="Class - Business ID Property:srcLastSaved"
+  dataDxfId="71"
+  ><tableColumn
+  id="16"
+  xr3:uid="{6EB0D161-6AFB-4810-AC28-A47D7D3FC7C6}"
+  name="Class - Business ID Property:src"
+  dataDxfId="70"
+  ><calculatedColumnFormula>IF(meta_Classifiers[[#This Row],[Class - Business ID Property:srcLastSaved]][<][>]"", meta_Classifiers[[#This Row],[Class - Business ID Property:srcLastSaved]],
+   IF(meta_Classifiers[[#This Row],[Class - Business ID Property]]="","",
+  INDEX(meta_TypedModelElements[ID],
+  MATCH(meta_Classifiers[[#This Row],[Class - Business ID Property]],meta_TypedModelElements[Display Qualified],0))))</calculatedColumnFormula></tableColumn><tableColumn
+  id="14"
+  xr3:uid="{5DEE7546-0461-4D10-BEC9-28B98283AB48}"
+  name="Class - Business ID Property"
+  dataDxfId="69"
+  ></tableColumns><tableStyleInfo
+  name="TableStyleLight9"
+  showFirstColumn="0"
+  showLastColumn="0"
+  showRowStripes="1"
+  showColumnStripes="0"
+  ></table>
\ No newline at end of file
```
