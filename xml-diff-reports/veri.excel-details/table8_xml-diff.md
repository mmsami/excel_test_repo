# Changes in veri.excel/xl/tables/table8.xml

```diff
diff --git a/veri.excel/xl/tables/table8.xml b/veri.excel/xl/tables/table8.xml
index 061ab6b..eabb03e 100644
--- a/veri.excel/xl/tables/table8.xml
+++ b/veri.excel/xl/tables/table8.xml
@@ -206,12 +206,14 @@
                         meta_Columns[[#This Row],[Owning Table]]&"."&meta_Columns[[#This Row],[Excel Column - Label]]
                     </calculatedColumnFormula></tableColumn>
                     <tableColumn id="8" xr3:uid="{00000000-0010-0000-0400-000008000000}" name="Excel Column - Label Overwrite" dataDxfId="311"/>
-                    <tableColumn id="17" xr3:uid="{00000000-0010-0000-0400-000011000000}" name="Excel Column - Label" dataDxfId="310"><calculatedColumnFormula>
-                        IF(TRIM(meta_Columns[[#This Row],[Excel Column - Label Overwrite]])<>"",meta_Columns[[#This Row],[Excel Column - Label Overwrite]],meta_Columns[[#This Row],[Excel Column - Label from Property or Referenced Table]])
+                    <tableColumn id="17" xr3:uid="{00000000-0010-0000-0400-000011000000}" name="Excel Column - Label" dataDxfId="0"><calculatedColumnFormula>
+                        IF(TRIM(meta_Columns[[#This Row],[Excel Column - Label Overwrite]])<>"",
+                        meta_Columns[[#This Row],[Excel Column - Label Overwrite]],
+                        meta_Columns[[#This Row],[Excel Column - Label from Property or Referenced Table]])
                     </calculatedColumnFormula></tableColumn>
-                    <tableColumn id="38" xr3:uid="{00000000-0010-0000-0400-000026000000}" name="Excel Column - Explicit Excel Formula" dataDxfId="309"/>
-                    <tableColumn id="39" xr3:uid="{00000000-0010-0000-0400-000027000000}" name="Excel Column - Excel Formula" dataDxfId="308"><calculatedColumnFormula>
+                    <tableColumn id="38" xr3:uid="{00000000-0010-0000-0400-000026000000}" name="Excel Column - Explicit Excel Formula" dataDxfId="310"/>
+                    <tableColumn id="39" xr3:uid="{00000000-0010-0000-0400-000027000000}" name="Excel Column - Excel Formula" dataDxfId="309"><calculatedColumnFormula>
                         IF(meta_Columns[[#This Row],[Excel Column - Explicit Excel Formula]]="","",meta_Columns[[#This Row],[Excel Column - Explicit Excel Formula]])
                     </calculatedColumnFormula></tableColumn>
-                    <tableColumn id="57" xr3:uid="{C2776EE3-610F-C044-84D9-D4ECD4E36C59}" name="Excel Column - Validation Formula" dataDxfId="307"/>
-                    <tableColumn id="2" xr3:uid="{C6EC425D-35C3-094D-B676-8DF67F65D351}" name="Excel Column - String Type" dataDxfId="306"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+                    <tableColumn id="57" xr3:uid="{C2776EE3-610F-C044-84D9-D4ECD4E36C59}" name="Excel Column - Validation Formula" dataDxfId="308"/>
+                    <tableColumn id="2" xr3:uid="{C6EC425D-35C3-094D-B676-8DF67F65D351}" name="Excel Column - String Type" dataDxfId="307"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
```
