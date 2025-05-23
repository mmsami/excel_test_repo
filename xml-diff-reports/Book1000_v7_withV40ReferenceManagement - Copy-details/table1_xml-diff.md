# Changes in Book1000_v7_withV40ReferenceManagement - Copy/xl/tables/table1.xml

```diff
diff --git a/Book1000_v7_withV40ReferenceManagement - Copy/xl/tables/table1.xml b/Book1000_v7_withV40ReferenceManagement - Copy/xl/tables/table1.xml
index e270db2..b9c3394 100644
--- a/Book1000_v7_withV40ReferenceManagement - Copy/xl/tables/table1.xml	
+++ b/Book1000_v7_withV40ReferenceManagement - Copy/xl/tables/table1.xml	
@@ -31,12 +31,12 @@
   id="4"
   xr3:uid="{923FD8ED-28C5-4CB3-8C87-9917F7DBCEF4}"
   name="Ref:selectFromSourceLastSaved"
-  dataDxfId="9"
-><calculatedColumnFormula>IF(Table1[[#This Row],[Ref:srcLastSaved]]="","",INDEX(Table2[Selector],MATCH(Table1[[#This Row],[Ref:srcLastSaved]],Table2[ID],0)))[&]"Goofy"</calculatedColumnFormula></tableColumn><tableColumn
+  dataDxfId="0"
+><calculatedColumnFormula>IF(Table1[[#This Row],[Ref:srcLastSaved]]="","",INDEX(Table2[Selector],MATCH(Table1[[#This Row],[Ref:srcLastSaved]],Table2[ID],0)))[&]"Sami"</calculatedColumnFormula></tableColumn><tableColumn
   id="5"
   xr3:uid="{08C9A757-0B42-4205-9629-A9536EDBA5B0}"
   name="Ref:srcFromActual"
-  dataDxfId="0"
+  dataDxfId="9"
 ><calculatedColumnFormula>IF(Table1[[#This Row],[Ref]]="","",INDEX(Table2[ID],MATCH(Table1[[#This Row],[Ref]], Table2[Selector],0)))[&]"Fritz"</calculatedColumnFormula></tableColumn><tableColumn
   id="3"
   xr3:uid="{6DC90CBB-8D95-4FE2-902C-199AC5BD0806}"
```
