# Changes in 20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table3.xml

```diff
diff --git a/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table3.xml b/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table3.xml
index de60d3e..636d169 100644
--- a/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table3.xml
+++ b/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table3.xml
@@ -1,2 +1,76 @@
-<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="8" xr:uid="{DF45D5B3-39DF-46DE-B349-4E3814CB0059}" name="catalog_Codes" displayName="catalog_Codes" ref="A1:J46565" totalsRowShown="0" headerRowDxfId="66" dataDxfId="64" headerRowBorderDxfId="65"><autoFilter ref="A1:J46565" xr:uid="{DF45D5B3-39DF-46DE-B349-4E3814CB0059}"/><tableColumns count="10"><tableColumn id="1" xr3:uid="{645F68AA-E559-4D28-BACA-192680A7C468}" name="ID" dataDxfId="63"/><tableColumn id="2" xr3:uid="{7EFD2FEF-6F58-48D8-B584-5656F8C295B6}" name="Package" dataDxfId="62"/><tableColumn id="3" xr3:uid="{DDF65B43-919C-4B6D-9E08-6B533E264DDC}" name="Derive" dataDxfId="61"/><tableColumn id="4" xr3:uid="{5DCCB904-A4E1-4C0B-9613-EBD6C5233497}" name="Kind:src" dataDxfId="60"/><tableColumn id="10" xr3:uid="{1B676D39-1C4A-41F3-9A75-A2678999CC8C}" name="Kind Iso" dataDxfId="59"/><tableColumn id="5" xr3:uid="{E4E0E824-3473-4979-81DE-4AD187557FB4}" name="Kind" dataDxfId="58"><calculatedColumnFormula>INDEX(catalog_GlossaryClassifiers[Name],MATCH(catalog_Codes[[#This Row],[Kind:src]],catalog_GlossaryClassifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="6" xr3:uid="{A9FA54CC-1C0A-418D-94F3-CE2545BD9222}" name="Name" dataDxfId="57"/><tableColumn id="9" xr3:uid="{675A8E41-5235-544F-988E-EA0746291C23}" name="Registration Status" dataDxfId="56"/><tableColumn id="7" xr3:uid="{8D0BFDE7-32A7-4F91-BBF4-66F3182F874F}" name="Code" dataDxfId="55"/><tableColumn id="8" xr3:uid="{87D6F492-1C0F-4107-81AB-AB3C74BCD3FA}" name="Description" dataDxfId="54"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
+<table
+  xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
+  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
+  mc:Ignorable="xr xr3"
+  xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
+  xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
+  id="8"
+  xr:uid="{DF45D5B3-39DF-46DE-B349-4E3814CB0059}"
+  name="catalog_Codes"
+  displayName="catalog_Codes"
+  ref="A1:J46565"
+  totalsRowShown="0"
+  headerRowDxfId="66"
+  dataDxfId="64"
+  headerRowBorderDxfId="65"
+  ><autoFilter
+  ref="A1:J46565"
+  xr:uid="{DF45D5B3-39DF-46DE-B349-4E3814CB0059}"
+><tableColumns count="10"><tableColumn
+  id="1"
+  xr3:uid="{645F68AA-E559-4D28-BACA-192680A7C468}"
+  name="ID"
+  dataDxfId="63"
+  ><tableColumn
+  id="2"
+  xr3:uid="{7EFD2FEF-6F58-48D8-B584-5656F8C295B6}"
+  name="Package"
+  dataDxfId="62"
+  ><tableColumn
+  id="3"
+  xr3:uid="{DDF65B43-919C-4B6D-9E08-6B533E264DDC}"
+  name="Derive"
+  dataDxfId="61"
+  ><tableColumn
+  id="4"
+  xr3:uid="{5DCCB904-A4E1-4C0B-9613-EBD6C5233497}"
+  name="Kind:src"
+  dataDxfId="60"
+  ><tableColumn
+  id="10"
+  xr3:uid="{1B676D39-1C4A-41F3-9A75-A2678999CC8C}"
+  name="Kind Iso"
+  dataDxfId="59"
+  ><tableColumn
+  id="5"
+  xr3:uid="{E4E0E824-3473-4979-81DE-4AD187557FB4}"
+  name="Kind"
+  dataDxfId="58"
+  ><calculatedColumnFormula>INDEX(catalog_GlossaryClassifiers[Name],MATCH(catalog_Codes[[#This Row],[Kind:src]],catalog_GlossaryClassifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn
+  id="6"
+  xr3:uid="{A9FA54CC-1C0A-418D-94F3-CE2545BD9222}"
+  name="Name"
+  dataDxfId="57"
+  ><tableColumn
+  id="9"
+  xr3:uid="{675A8E41-5235-544F-988E-EA0746291C23}"
+  name="Registration Status"
+  dataDxfId="56"
+  ><tableColumn
+  id="7"
+  xr3:uid="{8D0BFDE7-32A7-4F91-BBF4-66F3182F874F}"
+  name="Code"
+  dataDxfId="55"
+  ><tableColumn
+  id="8"
+  xr3:uid="{87D6F492-1C0F-4107-81AB-AB3C74BCD3FA}"
+  name="Description"
+  dataDxfId="54"
+  ></tableColumns><tableStyleInfo
+  name="TableStyleLight9"
+  showFirstColumn="0"
+  showLastColumn="0"
+  showRowStripes="1"
+  showColumnStripes="0"
+  ></table>
\ No newline at end of file
```
