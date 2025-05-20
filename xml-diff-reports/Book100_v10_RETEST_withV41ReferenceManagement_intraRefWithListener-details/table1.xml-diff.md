# Changes in Book100_v10_RETEST_withV41ReferenceManagement_intraRefWithListener/xl/tables/table1.xml

```diff
diff --git a/Book100_v10_RETEST_withV41ReferenceManagement_intraRefWithListener/xl/tables/table1.xml b/Book100_v10_RETEST_withV41ReferenceManagement_intraRefWithListener/xl/tables/table1.xml
new file mode 100644
index 0000000..c2841c6
--- /dev/null
+++ b/Book100_v10_RETEST_withV41ReferenceManagement_intraRefWithListener/xl/tables/table1.xml
@@ -0,0 +1,3 @@
+<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
+<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="1" xr:uid="{130F8B8F-D407-43B8-A880-7578C5A01AEF}" name="Table1" displayName="Table1" ref="A1:K101" totalsRowShown="0" headerRowDxfId="2" dataDxfId="1" headerRowBorderDxfId="22"><autoFilter ref="A1:K101" xr:uid="{130F8B8F-D407-43B8-A880-7578C5A01AEF}"/><tableColumns count="11"><tableColumn id="1" xr3:uid="{AE0AB6AE-A47C-46EF-8991-64C6463CD4F8}" name="ID" dataDxfId="12"/><tableColumn id="10" xr3:uid="{8BC4FC51-3BEA-4A08-AE36-2F1BC13CBCCD}" name="Selector" dataDxfId="11"><calculatedColumnFormula>"Dummy_"[&]Table1[[#This Row],[ID]]</calculatedColumnFormula></tableColumn><tableColumn id="2" xr3:uid="{85184C7D-DCB9-42BA-A488-C12ABDA8EFE9}" name="Ref:srcLastSaved" dataDxfId="10"/><tableColumn id="3" xr3:uid="{6DC90CBB-8D95-4FE2-902C-199AC5BD0806}" name="Ref" dataDxfId="9"/><tableColumn id="6" xr3:uid="{2DC4BB74-4145-4AD5-88DC-B2D40A96C076}" name="Ref2:srcLastSaved" dataDxfId="8"/><tableColumn id="7" xr3:uid="{360F9577-D113-4065-BB1C-1E67D583DE3F}" name="Ref2" dataDxfId="7"/><tableColumn id="8" xr3:uid="{513F75D8-2F10-4DB2-91C0-6213E3DDBE80}" name="Ref3:srcLAstSaved" dataDxfId="6"/><tableColumn id="9" xr3:uid="{C6463962-1A1E-4874-91BD-6A9B2219898A}" name="Ref3" dataDxfId="5"/><tableColumn id="4" xr3:uid="{034CF0D5-14AD-43A5-A523-15F860D0CC58}" name="IntraS1" dataDxfId="4"/><tableColumn id="5" xr3:uid="{5062B6FF-A7E9-4E20-B4DC-C04D04C4C16E}" name="IntraRef1:src" dataDxfId="3"/><tableColumn id="11" xr3:uid="{FAC54EAF-93FC-471F-A3F9-03B2F02A71DF}" name="IntraRef1" dataDxfId="0"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( Table1[[#This Row],[IntraRef1:src]] ) = "", "",
+        INDEX( Table1[IntraS1], MATCH( Table1[[#This Row],[IntraRef1:src]], Table1[ID], 0 ) ) )</calculatedColumnFormula></tableColumn></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
```
