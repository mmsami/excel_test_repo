# Changes in 20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table2.xml

```diff
diff --git a/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table2.xml b/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table2.xml
index 53f639f..ab513de 100644
--- a/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table2.xml
+++ b/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table2.xml
@@ -1,2 +1,149 @@
-<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="5" xr:uid="{AD87CC92-9C6D-4FC9-9A68-CAA6E43063D2}" name="catalog_GlossaryProperties" displayName="catalog_GlossaryProperties" ref="A1:Y4568" totalsRowShown="0" headerRowDxfId="88" headerRowBorderDxfId="87"><autoFilter ref="A1:Y4568" xr:uid="{AD87CC92-9C6D-4FC9-9A68-CAA6E43063D2}"/><sortState ref="A2:Y4568" xmlns:xlrd2="http://schemas.microsoft.com/office/spreadsheetml/2017/richdata2"><sortCondition ref="L1:L4568"/></sortState><tableColumns count="25"><tableColumn id="1" xr3:uid="{DBDB718E-0C57-409F-8C40-AA392671A544}" name="ID" dataDxfId="86"/><tableColumn id="12" xr3:uid="{CDAC742C-526B-42D9-9EC1-E85A52131BCA}" name="Package" dataDxfId="85"/><tableColumn id="3" xr3:uid="{5A18541E-D7CA-409D-B505-7603AB7A3F08}" name="Display" dataDxfId="0"><calculatedColumnFormula>SUBSTITUTE(catalog_GlossaryProperties[[#This Row],[Owning Class]]," ","")[&]"."[&]catalog_GlossaryProperties[[#This Row],[Lower Camel Name]][&]"TESTGIT123456"</calculatedColumnFormula></tableColumn><tableColumn id="4" xr3:uid="{8CBDBAE8-CEB3-43B5-8027-CE4CDAA779D0}" name="Kind" dataDxfId="84"/><tableColumn id="9" xr3:uid="{599607E8-3B39-463F-B148-F21774C2666B}" name="Owning Class:src" dataDxfId="83"/><tableColumn id="23" xr3:uid="{A6FAC649-744A-4D38-9714-31CBD97C6E81}" name="Owning Class  IsoName" dataDxfId="82"><calculatedColumnFormula>INDEX(catalog_GlossaryClassifiers[Original Iso20022 Name],MATCH(catalog_GlossaryProperties[[#This Row],[Owning Class:src]],catalog_GlossaryClassifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="8" xr3:uid="{84044855-0254-49A6-8629-DFE17025A285}" name="Owning Class" dataDxfId="81"><calculatedColumnFormula>INDEX(catalog_GlossaryClassifiers[Name],MATCH(catalog_GlossaryProperties[[#This Row],[Owning Class:src]],catalog_GlossaryClassifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="24" xr3:uid="{5EE34E91-7F60-4B17-9243-E5451BAF90C9}" name="Iso20022BizOrder" dataDxfId="80"><calculatedColumnFormula>catalog_GlossaryProperties[[#This Row],[Owning Class  IsoName]][&]"_"[&]catalog_GlossaryProperties[[#This Row],[Iso20022Order]]</calculatedColumnFormula></tableColumn><tableColumn id="22" xr3:uid="{6E8B75F4-9C5B-4501-86F5-D22CF1733F71}" name="Iso20022Order" dataDxfId="79"><calculatedColumnFormula>INDEX(BusinessModelTable_fromISO20022[Original Order],MATCH(catalog_GlossaryProperties[[#This Row],[Iso20022BizID]],BusinessModelTable_fromISO20022[Biz ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="21" xr3:uid="{438AA7AA-F4BB-4D4C-9B63-FCA5BEC3E86C}" name="Iso20022BizID" dataDxfId="78"><calculatedColumnFormula>catalog_GlossaryProperties[[#This Row],[Owning Class  IsoName]][&]"."[&]catalog_GlossaryProperties[[#This Row],[Original Iso20022 Name]]</calculatedColumnFormula></tableColumn><tableColumn id="20" xr3:uid="{6B1D7A78-1E3F-4D5B-876F-F723B4BA7F50}" name="Original Iso20022 Name" dataDxfId="77"/><tableColumn id="28" xr3:uid="{137FA068-C469-487D-A8C7-61DF6D5F4BF5}" name="Iso20022 Sort Order" dataDxfId="76"/><tableColumn id="11" xr3:uid="{30D9CF1A-2D02-48AD-8B2A-C85860473B3B}" name="Lower Camel Name" dataDxfId="75"/><tableColumn id="10" xr3:uid="{688760D6-1A1D-4D55-B3BD-A8C9C32FD440}" name="Name or Type" dataDxfId="74"><calculatedColumnFormula>IF(catalog_GlossaryProperties[[#This Row],[Name]]="",catalog_GlossaryProperties[[#This Row],[Type]],catalog_GlossaryProperties[[#This Row],[Name]])</calculatedColumnFormula></tableColumn><tableColumn id="2" xr3:uid="{E4830EBC-AEFF-466E-BAFF-0BBB05BCECAE}" name="Name"/><tableColumn id="14" xr3:uid="{342FE83B-7274-4D05-86EF-9D3C906C7E70}" name="Description"/><tableColumn id="6" xr3:uid="{E3DBB0A9-FE68-4B15-95D0-47DE534A796E}" name="Type:src" dataDxfId="73"/><tableColumn id="32" xr3:uid="{5E2C8AD5-2C8E-4560-975F-C3FF9C08525D}" name="typeFromOriginalIsoExel" dataDxfId="72"><calculatedColumnFormula>INDEX(BusinessModelTable_fromISO20022[Business Element Type Name],MATCH(catalog_GlossaryProperties[[#This Row],[Iso20022BizID]],BusinessModelTable_fromISO20022[Biz ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="5" xr3:uid="{273DBA54-CD77-4016-AB7A-78C75C21B568}" name="Type"><calculatedColumnFormula>IF(catalog_GlossaryProperties[[#This Row],[Type:src]]="","",INDEX(catalog_GlossaryClassifiers[Name],MATCH(catalog_GlossaryProperties[[#This Row],[Type:src]],catalog_GlossaryClassifiers[ID],0)))</calculatedColumnFormula></tableColumn><tableColumn id="13" xr3:uid="{2981FC26-DC7B-774F-B426-C50AA28F7A90}" name="min" dataDxfId="71"/><tableColumn id="16" xr3:uid="{9D6D8C33-060F-8B42-BC70-AEEDF24F7B72}" name="max" dataDxfId="70"/><tableColumn id="7" xr3:uid="{FAE6C648-41D1-41BC-9985-340BA90D1ADF}" name="Arity"/><tableColumn id="17" xr3:uid="{AFE3A896-F758-4FB5-9732-722F4B010A4D}" name="Type Description" dataDxfId="69"><calculatedColumnFormula>INDEX(catalog_GlossaryClassifiers[Description],MATCH(catalog_GlossaryProperties[[#This Row],[Type:src]],catalog_GlossaryClassifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="18" xr3:uid="{2C8B9AD8-6B4A-4038-A92C-FC38ECAB5CC7}" name="Opposite:src" dataDxfId="68"/><tableColumn id="25" xr3:uid="{149EF191-6883-4DB2-AEEA-B3129815817D}" name="Opposite" dataDxfId="67"><calculatedColumnFormula>IF(catalog_GlossaryProperties[[#This Row],[Opposite:src]]="","",INDEX(catalog_GlossaryProperties[Name],MATCH(catalog_GlossaryProperties[[#This Row],[Opposite:src]],catalog_GlossaryProperties[ID],0)))</calculatedColumnFormula></tableColumn></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
+<table
+  xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
+  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
+  mc:Ignorable="xr xr3"
+  xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
+  xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
+  id="5"
+  xr:uid="{AD87CC92-9C6D-4FC9-9A68-CAA6E43063D2}"
+  name="catalog_GlossaryProperties"
+  displayName="catalog_GlossaryProperties"
+  ref="A1:Y4568"
+  totalsRowShown="0"
+  headerRowDxfId="88"
+  headerRowBorderDxfId="87"
+  ><autoFilter
+  ref="A1:Y4568"
+  xr:uid="{AD87CC92-9C6D-4FC9-9A68-CAA6E43063D2}"
+  ><sortState
+  ref="A2:Y4568"
+  xmlns:xlrd2="http://schemas.microsoft.com/office/spreadsheetml/2017/richdata2"
+><sortCondition ref="L1:L4568"/></sortState><tableColumns count="25"><tableColumn
+  id="1"
+  xr3:uid="{DBDB718E-0C57-409F-8C40-AA392671A544}"
+  name="ID"
+  dataDxfId="86"
+  ><tableColumn
+  id="12"
+  xr3:uid="{CDAC742C-526B-42D9-9EC1-E85A52131BCA}"
+  name="Package"
+  dataDxfId="85"
+  ><tableColumn
+  id="3"
+  xr3:uid="{5A18541E-D7CA-409D-B505-7603AB7A3F08}"
+  name="Display"
+  dataDxfId="0"
+  ><calculatedColumnFormula>SUBSTITUTE(catalog_GlossaryProperties[[#This Row],[Owning Class]]," ","")[&]"."[&]catalog_GlossaryProperties[[#This Row],[Lower Camel Name]][&]"TESTGIT123456"</calculatedColumnFormula></tableColumn><tableColumn
+  id="4"
+  xr3:uid="{8CBDBAE8-CEB3-43B5-8027-CE4CDAA779D0}"
+  name="Kind"
+  dataDxfId="84"
+  ><tableColumn
+  id="9"
+  xr3:uid="{599607E8-3B39-463F-B148-F21774C2666B}"
+  name="Owning Class:src"
+  dataDxfId="83"
+  ><tableColumn
+  id="23"
+  xr3:uid="{A6FAC649-744A-4D38-9714-31CBD97C6E81}"
+  name="Owning Class  IsoName"
+  dataDxfId="82"
+  ><calculatedColumnFormula>INDEX(catalog_GlossaryClassifiers[Original Iso20022 Name],MATCH(catalog_GlossaryProperties[[#This Row],[Owning Class:src]],catalog_GlossaryClassifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn
+  id="8"
+  xr3:uid="{84044855-0254-49A6-8629-DFE17025A285}"
+  name="Owning Class"
+  dataDxfId="81"
+  ><calculatedColumnFormula>INDEX(catalog_GlossaryClassifiers[Name],MATCH(catalog_GlossaryProperties[[#This Row],[Owning Class:src]],catalog_GlossaryClassifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn
+  id="24"
+  xr3:uid="{5EE34E91-7F60-4B17-9243-E5451BAF90C9}"
+  name="Iso20022BizOrder"
+  dataDxfId="80"
+  ><calculatedColumnFormula>catalog_GlossaryProperties[[#This Row],[Owning Class  IsoName]][&]"_"[&]catalog_GlossaryProperties[[#This Row],[Iso20022Order]]</calculatedColumnFormula></tableColumn><tableColumn
+  id="22"
+  xr3:uid="{6E8B75F4-9C5B-4501-86F5-D22CF1733F71}"
+  name="Iso20022Order"
+  dataDxfId="79"
+  ><calculatedColumnFormula>INDEX(BusinessModelTable_fromISO20022[Original Order],MATCH(catalog_GlossaryProperties[[#This Row],[Iso20022BizID]],BusinessModelTable_fromISO20022[Biz ID],0))</calculatedColumnFormula></tableColumn><tableColumn
+  id="21"
+  xr3:uid="{438AA7AA-F4BB-4D4C-9B63-FCA5BEC3E86C}"
+  name="Iso20022BizID"
+  dataDxfId="78"
+  ><calculatedColumnFormula>catalog_GlossaryProperties[[#This Row],[Owning Class  IsoName]][&]"."[&]catalog_GlossaryProperties[[#This Row],[Original Iso20022 Name]]</calculatedColumnFormula></tableColumn><tableColumn
+  id="20"
+  xr3:uid="{6B1D7A78-1E3F-4D5B-876F-F723B4BA7F50}"
+  name="Original Iso20022 Name"
+  dataDxfId="77"
+  ><tableColumn
+  id="28"
+  xr3:uid="{137FA068-C469-487D-A8C7-61DF6D5F4BF5}"
+  name="Iso20022 Sort Order"
+  dataDxfId="76"
+  ><tableColumn
+  id="11"
+  xr3:uid="{30D9CF1A-2D02-48AD-8B2A-C85860473B3B}"
+  name="Lower Camel Name"
+  dataDxfId="75"
+  ><tableColumn
+  id="10"
+  xr3:uid="{688760D6-1A1D-4D55-B3BD-A8C9C32FD440}"
+  name="Name or Type"
+  dataDxfId="74"
+><calculatedColumnFormula>IF(catalog_GlossaryProperties[[#This Row],[Name]]="",catalog_GlossaryProperties[[#This Row],[Type]],catalog_GlossaryProperties[[#This Row],[Name]])</calculatedColumnFormula></tableColumn><tableColumn
+  id="2"
+  xr3:uid="{E4830EBC-AEFF-466E-BAFF-0BBB05BCECAE}"
+  name="Name"
+  ><tableColumn
+  id="14"
+  xr3:uid="{342FE83B-7274-4D05-86EF-9D3C906C7E70}"
+  name="Description"
+  ><tableColumn
+  id="6"
+  xr3:uid="{E3DBB0A9-FE68-4B15-95D0-47DE534A796E}"
+  name="Type:src"
+  dataDxfId="73"
+  ><tableColumn
+  id="32"
+  xr3:uid="{5E2C8AD5-2C8E-4560-975F-C3FF9C08525D}"
+  name="typeFromOriginalIsoExel"
+  dataDxfId="72"
+  ><calculatedColumnFormula>INDEX(BusinessModelTable_fromISO20022[Business Element Type Name],MATCH(catalog_GlossaryProperties[[#This Row],[Iso20022BizID]],BusinessModelTable_fromISO20022[Biz ID],0))</calculatedColumnFormula></tableColumn><tableColumn
+  id="5"
+  xr3:uid="{273DBA54-CD77-4016-AB7A-78C75C21B568}"
+  name="Type"
+><calculatedColumnFormula>IF(catalog_GlossaryProperties[[#This Row],[Type:src]]="","",INDEX(catalog_GlossaryClassifiers[Name],MATCH(catalog_GlossaryProperties[[#This Row],[Type:src]],catalog_GlossaryClassifiers[ID],0)))</calculatedColumnFormula></tableColumn><tableColumn
+  id="13"
+  xr3:uid="{2981FC26-DC7B-774F-B426-C50AA28F7A90}"
+  name="min"
+  dataDxfId="71"
+  ><tableColumn
+  id="16"
+  xr3:uid="{9D6D8C33-060F-8B42-BC70-AEEDF24F7B72}"
+  name="max"
+  dataDxfId="70"
+  ><tableColumn
+  id="7"
+  xr3:uid="{FAE6C648-41D1-41BC-9985-340BA90D1ADF}"
+  name="Arity"
+  ><tableColumn
+  id="17"
+  xr3:uid="{AFE3A896-F758-4FB5-9732-722F4B010A4D}"
+  name="Type Description"
+  dataDxfId="69"
+  ><calculatedColumnFormula>INDEX(catalog_GlossaryClassifiers[Description],MATCH(catalog_GlossaryProperties[[#This Row],[Type:src]],catalog_GlossaryClassifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn
+  id="18"
+  xr3:uid="{2C8B9AD8-6B4A-4038-A92C-FC38ECAB5CC7}"
+  name="Opposite:src"
+  dataDxfId="68"
+  ><tableColumn
+  id="25"
+  xr3:uid="{149EF191-6883-4DB2-AEEA-B3129815817D}"
+  name="Opposite"
+  dataDxfId="67"
+><calculatedColumnFormula>IF(catalog_GlossaryProperties[[#This Row],[Opposite:src]]="","",INDEX(catalog_GlossaryProperties[Name],MATCH(catalog_GlossaryProperties[[#This Row],[Opposite:src]],catalog_GlossaryProperties[ID],0)))</calculatedColumnFormula></tableColumn></tableColumns><tableStyleInfo
+  name="TableStyleLight9"
+  showFirstColumn="0"
+  showLastColumn="0"
+  showRowStripes="1"
+  showColumnStripes="0"
+  ></table>
\ No newline at end of file
```
