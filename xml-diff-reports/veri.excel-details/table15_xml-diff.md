# Changes in veri.excel/xl/tables/table15.xml

```diff
diff --git a/veri.excel/xl/tables/table15.xml b/veri.excel/xl/tables/table15.xml
index 44ff140..0e994c5 100644
--- a/veri.excel/xl/tables/table15.xml
+++ b/veri.excel/xl/tables/table15.xml
@@ -11,57 +11,57 @@
     displayName="meta_CodeTemplates"
     ref="A2:X5"
     totalsRowShown="0"
-    headerRowDxfId="57"
-    dataDxfId="55"
-    headerRowBorderDxfId="56"<autoFilter
+    headerRowDxfId="58"
+    dataDxfId="56"
+    headerRowBorderDxfId="57"<autoFilter
     ref="A2:X5"
     xr:uid="{00000000-0009-0000-0100-000012000000}"/<tableColumns
     count="24"<tableColumn
     id="1"
     xr3:uid="{00000000-0010-0000-0700-000001000000}"
     name="ID"
-    dataDxfId="54"/<tableColumn
+    dataDxfId="55"/<tableColumn
     id="12"
     xr3:uid="{00000000-0010-0000-0700-00000C000000}"
     name="Kind:src"
-    dataDxfId="53"/<tableColumn
+    dataDxfId="54"/<tableColumn
     id="3"
     xr3:uid="{00000000-0010-0000-0700-000003000000}"
     name="Kind"
-    dataDxfId="52"/<tableColumn
+    dataDxfId="53"/<tableColumn
     id="6"
     xr3:uid="{00000000-0010-0000-0700-000006000000}"
     name="Package"
-    dataDxfId="51"/<tableColumn
+    dataDxfId="52"/<tableColumn
     id="11"
     xr3:uid="{00000000-0010-0000-0700-00000B000000}"
     name="Sub
-    dataDxfId="50"/<tableColumn
+    dataDxfId="51"/<tableColumn
     id="8"
     xr3:uid="{00000000-0010-0000-0700-000008000000}"
     name="Display:q"
-    dataDxfId="49"<calculatedColumnFormulaIF(TRIM(meta_CodeTemplates[[#This
+    dataDxfId="50"<calculatedColumnFormulaIF(TRIM(meta_CodeTemplates[[#This
     Row],[Package]])="","",TRIM(LOWER(meta_CodeTemplates[[#This
     id="7"
     xr3:uid="{00000000-0010-0000-0700-000007000000}"
     name="Display"
-    dataDxfId="48"<calculatedColumnFormulaTRIM(SUBSTITUTE(meta_CodeTemplates[[#This
+    dataDxfId="49"<calculatedColumnFormulaTRIM(SUBSTITUTE(meta_CodeTemplates[[#This
     id="10"
     xr3:uid="{00000000-0010-0000-0700-00000A000000}"
     name="Where
-    dataDxfId="47"/<tableColumn
+    dataDxfId="48"/<tableColumn
     id="2"
     xr3:uid="{00000000-0010-0000-0700-000002000000}"
     name="Template
-    dataDxfId="46"/<tableColumn
+    dataDxfId="47"/<tableColumn
     id="4"
     xr3:uid="{00000000-0010-0000-0700-000004000000}"
     name="Matched
-    dataDxfId="45"/<tableColumn
+    dataDxfId="46"/<tableColumn
     id="9"
     xr3:uid="{00000000-0010-0000-0700-000009000000}"
     name="Matched
-    dataDxfId="44"<calculatedColumnFormula
+    dataDxfId="45"<calculatedColumnFormula
     xml:space="preserve"
     =
     "",
@@ -73,4 +73,4 @@
         & "::"
         & INDEX( meta_CodeTemplates[Display], MATCH( meta_CodeTemplates[[#This Row],[Matched Patern 1:src]], meta_CodeTemplates[ID], 0 ) ),
         INDEX( meta_CodeTemplates[Display], MATCH( meta_CodeTemplates[[#This Row],[Matched Patern 1:src]], meta_CodeTemplates[ID], 0 ) )
-        ))), "")</calculatedColumnFormula></tableColumn><tableColumn id="19" xr3:uid="{00000000-0010-0000-0700-000013000000}" name="Matched Pattern 1 Filter Value 1" dataDxfId="43"/><tableColumn id="20" xr3:uid="{00000000-0010-0000-0700-000014000000}" name="Matched Pattern 1 Filter Value 2" dataDxfId="42"/><tableColumn id="28" xr3:uid="{00000000-0010-0000-0700-00001C000000}" name="Matched Pattern 1 Template Column" dataDxfId="41"/><tableColumn id="18" xr3:uid="{00000000-0010-0000-0700-000012000000}" name="Template Middle" dataDxfId="40"/><tableColumn id="29" xr3:uid="{00000000-0010-0000-0700-00001D000000}" name="Matched Pattern 2:src" dataDxfId="39"/><tableColumn id="27" xr3:uid="{00000000-0010-0000-0700-00001B000000}" name="Matched Pattern2" dataDxfId="38"/><tableColumn id="21" xr3:uid="{00000000-0010-0000-0700-000015000000}" name="Matched Pattern 2 Filter Value 1" dataDxfId="37"/><tableColumn id="22" xr3:uid="{00000000-0010-0000-0700-000016000000}" name="Matched Pattern 2 Filter Value 2" dataDxfId="36"/><tableColumn id="17" xr3:uid="{00000000-0010-0000-0700-000011000000}" name="Matched Pattern 2 Template Column" dataDxfId="35"/><tableColumn id="16" xr3:uid="{00000000-0010-0000-0700-000010000000}" name="Template End" dataDxfId="34"/><tableColumn id="14" xr3:uid="{00000000-0010-0000-0700-00000E000000}" name="Excel Formula - Target Property" dataDxfId="33"/><tableColumn id="13" xr3:uid="{00000000-0010-0000-0700-00000D000000}" name="VBA Code - Target Module" dataDxfId="32"/><tableColumn id="5" xr3:uid="{00000000-0010-0000-0700-000005000000}" name="Definition" dataDxfId="31"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+        ))), "")</calculatedColumnFormula></tableColumn><tableColumn id="19" xr3:uid="{00000000-0010-0000-0700-000013000000}" name="Matched Pattern 1 Filter Value 1" dataDxfId="44"/><tableColumn id="20" xr3:uid="{00000000-0010-0000-0700-000014000000}" name="Matched Pattern 1 Filter Value 2" dataDxfId="43"/><tableColumn id="28" xr3:uid="{00000000-0010-0000-0700-00001C000000}" name="Matched Pattern 1 Template Column" dataDxfId="42"/><tableColumn id="18" xr3:uid="{00000000-0010-0000-0700-000012000000}" name="Template Middle" dataDxfId="41"/><tableColumn id="29" xr3:uid="{00000000-0010-0000-0700-00001D000000}" name="Matched Pattern 2:src" dataDxfId="40"/><tableColumn id="27" xr3:uid="{00000000-0010-0000-0700-00001B000000}" name="Matched Pattern2" dataDxfId="39"/><tableColumn id="21" xr3:uid="{00000000-0010-0000-0700-000015000000}" name="Matched Pattern 2 Filter Value 1" dataDxfId="38"/><tableColumn id="22" xr3:uid="{00000000-0010-0000-0700-000016000000}" name="Matched Pattern 2 Filter Value 2" dataDxfId="37"/><tableColumn id="17" xr3:uid="{00000000-0010-0000-0700-000011000000}" name="Matched Pattern 2 Template Column" dataDxfId="36"/><tableColumn id="16" xr3:uid="{00000000-0010-0000-0700-000010000000}" name="Template End" dataDxfId="35"/><tableColumn id="14" xr3:uid="{00000000-0010-0000-0700-00000E000000}" name="Excel Formula - Target Property" dataDxfId="34"/><tableColumn id="13" xr3:uid="{00000000-0010-0000-0700-00000D000000}" name="VBA Code - Target Module" dataDxfId="33"/><tableColumn id="5" xr3:uid="{00000000-0010-0000-0700-000005000000}" name="Definition" dataDxfId="32"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
```
