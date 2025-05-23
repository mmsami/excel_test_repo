# Changes in 20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table8.xml

```diff
diff --git a/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table8.xml b/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table8.xml
index 5d4d47f..7ec0408 100644
--- a/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table8.xml
+++ b/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/20250516_iso20022AndFiBO_v3.02/xl/tables/table8.xml
@@ -1,2 +1,78 @@
-<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="11" xr:uid="{D1410AD8-4705-CA48-8786-DB1356C6B445}" name="TypeModelElements_copy" displayName="TypeModelElements_copy" ref="A1:K4568" totalsRowShown="0" headerRowDxfId="18" headerRowBorderDxfId="17"><autoFilter ref="A1:K4568" xr:uid="{AD87CC92-9C6D-4FC9-9A68-CAA6E43063D2}"/><sortState ref="A2:J4568" xmlns:xlrd2="http://schemas.microsoft.com/office/spreadsheetml/2017/richdata2"><sortCondition ref="A1:A4568"/></sortState><tableColumns count="11"><tableColumn id="11" xr3:uid="{3CFF4112-F919-204C-B2A9-ABAAF64CD644}" name="Order" dataDxfId="16"/><tableColumn id="1" xr3:uid="{8FEF264A-04E8-8140-A156-66134F469E1E}" name="ID" dataDxfId="15"/><tableColumn id="4" xr3:uid="{E4DE1C9C-62CC-4847-9577-ED979CD8B05D}" name="Kind" dataDxfId="14"><calculatedColumnFormula>IF(TypeModelElements_copy[[#This Row],[Kind of Type]]="Class","Reference","Attribute")</calculatedColumnFormula></tableColumn><tableColumn id="9" xr3:uid="{342C024F-EEA3-884E-9502-633B0A1BA41F}" name="Owning Class:src" dataDxfId="13"/><tableColumn id="8" xr3:uid="{57DE8D6A-B5D5-BD48-BB83-FEE096F2B6F7}" name="Owning Class"/><tableColumn id="2" xr3:uid="{CAEE8184-4126-3243-9839-1E0535CFF523}" name="Name"/><tableColumn id="7" xr3:uid="{DF55407E-A7A0-0345-8060-A7E024704D94}" name="Description"/><tableColumn id="5" xr3:uid="{1290D9A1-FECB-FE48-BB83-D3AC269AA4AF}" name="Type"/><tableColumn id="3" xr3:uid="{D1522B75-313C-FA47-9B9B-42B9025E19DB}" name="Kind of Type" dataDxfId="12"><calculatedColumnFormula>INDEX(Classifiers_todo[Kind],MATCH(TypeModelElements_copy[[#This Row],[Type]],Classifiers_todo[Name],0))</calculatedColumnFormula></tableColumn><tableColumn id="10" xr3:uid="{628A9103-BAA8-AF47-B630-AE9BF6D0C804}" name="Opposite"/><tableColumn id="6" xr3:uid="{4C9C5AFB-8F6A-D340-A674-B65393F76215}" name="Description of Type" dataDxfId="11"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
+<table
+  xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
+  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
+  mc:Ignorable="xr xr3"
+  xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
+  xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
+  id="11"
+  xr:uid="{D1410AD8-4705-CA48-8786-DB1356C6B445}"
+  name="TypeModelElements_copy"
+  displayName="TypeModelElements_copy"
+  ref="A1:K4568"
+  totalsRowShown="0"
+  headerRowDxfId="18"
+  headerRowBorderDxfId="17"
+  ><autoFilter
+  ref="A1:K4568"
+  xr:uid="{AD87CC92-9C6D-4FC9-9A68-CAA6E43063D2}"
+  ><sortState
+  ref="A2:J4568"
+  xmlns:xlrd2="http://schemas.microsoft.com/office/spreadsheetml/2017/richdata2"
+><sortCondition ref="A1:A4568"/></sortState><tableColumns count="11"><tableColumn
+  id="11"
+  xr3:uid="{3CFF4112-F919-204C-B2A9-ABAAF64CD644}"
+  name="Order"
+  dataDxfId="16"
+  ><tableColumn
+  id="1"
+  xr3:uid="{8FEF264A-04E8-8140-A156-66134F469E1E}"
+  name="ID"
+  dataDxfId="15"
+  ><tableColumn
+  id="4"
+  xr3:uid="{E4DE1C9C-62CC-4847-9577-ED979CD8B05D}"
+  name="Kind"
+  dataDxfId="14"
+><calculatedColumnFormula>IF(TypeModelElements_copy[[#This Row],[Kind of Type]]="Class","Reference","Attribute")</calculatedColumnFormula></tableColumn><tableColumn
+  id="9"
+  xr3:uid="{342C024F-EEA3-884E-9502-633B0A1BA41F}"
+  name="Owning Class:src"
+  dataDxfId="13"
+  ><tableColumn
+  id="8"
+  xr3:uid="{57DE8D6A-B5D5-BD48-BB83-FEE096F2B6F7}"
+  name="Owning Class"
+  ><tableColumn
+  id="2"
+  xr3:uid="{CAEE8184-4126-3243-9839-1E0535CFF523}"
+  name="Name"
+  ><tableColumn
+  id="7"
+  xr3:uid="{DF55407E-A7A0-0345-8060-A7E024704D94}"
+  name="Description"
+  ><tableColumn
+  id="5"
+  xr3:uid="{1290D9A1-FECB-FE48-BB83-D3AC269AA4AF}"
+  name="Type"
+  ><tableColumn
+  id="3"
+  xr3:uid="{D1522B75-313C-FA47-9B9B-42B9025E19DB}"
+  name="Kind of Type"
+  dataDxfId="12"
+  ><calculatedColumnFormula>INDEX(Classifiers_todo[Kind],MATCH(TypeModelElements_copy[[#This Row],[Type]],Classifiers_todo[Name],0))</calculatedColumnFormula></tableColumn><tableColumn
+  id="10"
+  xr3:uid="{628A9103-BAA8-AF47-B630-AE9BF6D0C804}"
+  name="Opposite"
+  ><tableColumn
+  id="6"
+  xr3:uid="{4C9C5AFB-8F6A-D340-A674-B65393F76215}"
+  name="Description of Type"
+  dataDxfId="11"
+  ></tableColumns><tableStyleInfo
+  name="TableStyleLight9"
+  showFirstColumn="0"
+  showLastColumn="0"
+  showRowStripes="1"
+  showColumnStripes="0"
+  ></table>
\ No newline at end of file
```
