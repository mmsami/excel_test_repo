# Changes in veri.excel/xl/tables/table12.xml

```diff
diff --git a/veri.excel/xl/tables/table12.xml b/veri.excel/xl/tables/table12.xml
index cbafb35..7bb89cc 100644
--- a/veri.excel/xl/tables/table12.xml
+++ b/veri.excel/xl/tables/table12.xml
@@ -11,25 +11,25 @@
     displayName="meta_Literals"
     ref="A1:J31"
     totalsRowShown="0"
-    headerRowDxfId="204"
-    dataDxfId="202"
-    headerRowBorderDxfId="203"
-    tableBorderDxfId="201"<autoFilter
+    headerRowDxfId="205"
+    dataDxfId="203"
+    headerRowBorderDxfId="204"
+    tableBorderDxfId="202"<autoFilter
     ref="A1:J31"
     xr:uid="{00000000-0009-0000-0100-000005000000}"/<tableColumns
     count="10"<tableColumn
     id="8"
     xr3:uid="{00000000-0010-0000-0800-000008000000}"
     name="ID"
-    dataDxfId="200"/<tableColumn
+    dataDxfId="201"/<tableColumn
     id="5"
     xr3:uid="{00000000-0010-0000-0800-000005000000}"
     name="Kind:src"
-    dataDxfId="199"/<tableColumn
+    dataDxfId="200"/<tableColumn
     id="2"
     xr3:uid="{00000000-0010-0000-0800-000002000000}"
     name="Kind"
-    dataDxfId="198"<calculatedColumnFormulaIF(meta_Literals[[#This
+    dataDxfId="199"<calculatedColumnFormulaIF(meta_Literals[[#This
     Row],[Kind:src]]="","",INDEX(meta_Classifiers[Display
     id="6"
     xr3:uid="{00000000-0010-0000-0800-000006000000}"
@@ -37,27 +37,27 @@
     id="1"
     xr3:uid="{00000000-0010-0000-0800-000001000000}"
     name="Sub
-    dataDxfId="197"/<tableColumn
+    dataDxfId="198"/<tableColumn
     id="10"
     xr3:uid="{00000000-0010-0000-0800-00000A000000}"
     name="Display:q"
-    dataDxfId="196"<calculatedColumnFormulaIF(TRIM(meta_Literals[[#This
+    dataDxfId="197"<calculatedColumnFormulaIF(TRIM(meta_Literals[[#This
     Row],[Package]])="","",TRIM(LOWER(meta_Literals[[#This
     id="9"
     xr3:uid="{00000000-0010-0000-0800-000009000000}"
     name="Display"
-    dataDxfId="195"<calculatedColumnFormulaTRIM(SUBSTITUTE(meta_Literals[[#This
+    dataDxfId="196"<calculatedColumnFormulaTRIM(SUBSTITUTE(meta_Literals[[#This
     id="3"
     xr3:uid="{00000000-0010-0000-0800-000003000000}"
     name="Name"
-    dataDxfId="194"/<tableColumn
+    dataDxfId="195"/<tableColumn
     id="7"
     xr3:uid="{00000000-0010-0000-0800-000007000000}"
     name="Parent:src"/<tableColumn
     id="4"
     xr3:uid="{00000000-0010-0000-0800-000004000000}"
     name="Parent"
-    dataDxfId="193"<calculatedColumnFormula
+    dataDxfId="194"<calculatedColumnFormula
     xml:space="preserve"
     =
     "",
```
