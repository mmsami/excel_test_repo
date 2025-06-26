# Changes in veri.excel/xl/tables/table13.xml

```diff
diff --git a/veri.excel/xl/tables/table13.xml b/veri.excel/xl/tables/table13.xml
index 9a41537..331108d 100644
--- a/veri.excel/xl/tables/table13.xml
+++ b/veri.excel/xl/tables/table13.xml
@@ -1,83 +1,83 @@
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="1" xr:uid="{00000000-000C-0000-FFFF-FFFF05000000}" name="meta_Rules" displayName="meta_Rules" ref="A1:DD5" totalsRowShown="0" headerRowDxfId="192" dataDxfId="190" headerRowBorderDxfId="191"><autoFilter ref="A1:DD5" xr:uid="{00000000-0009-0000-0100-000001000000}"/>
+<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="1" xr:uid="{00000000-000C-0000-FFFF-FFFF05000000}" name="meta_Rules" displayName="meta_Rules" ref="A1:DD5" totalsRowShown="0" headerRowDxfId="193" dataDxfId="191" headerRowBorderDxfId="192"><autoFilter ref="A1:DD5" xr:uid="{00000000-0009-0000-0100-000001000000}"/>
 <tableColumns count="108">
-    <tableColumn id="1" xr3:uid="{00000000-0010-0000-0500-000001000000}" name="ID" dataDxfId="189"/>
-    <tableColumn id="32" xr3:uid="{00000000-0010-0000-0500-000020000000}" name="Kind:src" dataDxfId="188"/>
-    <tableColumn id="3" xr3:uid="{00000000-0010-0000-0500-000003000000}" name="Kind" dataDxfId="187"><calculatedColumnFormula>
+    <tableColumn id="1" xr3:uid="{00000000-0010-0000-0500-000001000000}" name="ID" dataDxfId="190"/>
+    <tableColumn id="32" xr3:uid="{00000000-0010-0000-0500-000020000000}" name="Kind:src" dataDxfId="189"/>
+    <tableColumn id="3" xr3:uid="{00000000-0010-0000-0500-000003000000}" name="Kind" dataDxfId="188"><calculatedColumnFormula>
         IF(meta_Rules[[#This Row],[Kind:src]]="","",INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Kind:src]],meta_Classifiers[ID],0)))
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="23" xr3:uid="{00000000-0010-0000-0500-000017000000}" name="Package" dataDxfId="186"><calculatedColumnFormula>
+    <tableColumn id="23" xr3:uid="{00000000-0010-0000-0500-000017000000}" name="Package" dataDxfId="187"><calculatedColumnFormula>
         _xlfn.IFNA(IF(meta_Rules[[#This Row],[Class:src]]="","util",INDEX(meta_Classifiers[Package],MATCH(meta_Rules[[#This Row],[Class:src]],meta_Classifiers[ID],0))),"")
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="104" xr3:uid="{00000000-0010-0000-0500-000068000000}" name="Sub Package" dataDxfId="185"/>
-    <tableColumn id="46" xr3:uid="{00000000-0010-0000-0500-00002E000000}" name="Super Class 6:display:q." dataDxfId="184"><calculatedColumnFormula>
+    <tableColumn id="104" xr3:uid="{00000000-0010-0000-0500-000068000000}" name="Sub Package" dataDxfId="186"/>
+    <tableColumn id="46" xr3:uid="{00000000-0010-0000-0500-00002E000000}" name="Super Class 6:display:q." dataDxfId="185"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Super Class 6]],meta_Classifiers[ID],0))&".","")
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="38" xr3:uid="{00000000-0010-0000-0500-000026000000}" name="Super Class 6" dataDxfId="183"><calculatedColumnFormula>
+    <tableColumn id="38" xr3:uid="{00000000-0010-0000-0500-000026000000}" name="Super Class 6" dataDxfId="184"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Rules[[#This Row],[Super Class 5]],meta_Classifiers[ID],0)),0)
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="45" xr3:uid="{00000000-0010-0000-0500-00002D000000}" name="Super Class 5:display:q." dataDxfId="182"><calculatedColumnFormula>
+    <tableColumn id="45" xr3:uid="{00000000-0010-0000-0500-00002D000000}" name="Super Class 5:display:q." dataDxfId="183"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Super Class 5]],meta_Classifiers[ID],0))&".","")
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="37" xr3:uid="{00000000-0010-0000-0500-000025000000}" name="Super Class 5" dataDxfId="181"><calculatedColumnFormula>
+    <tableColumn id="37" xr3:uid="{00000000-0010-0000-0500-000025000000}" name="Super Class 5" dataDxfId="182"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Rules[[#This Row],[Super Class 4]],meta_Classifiers[ID],0)),0)
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="44" xr3:uid="{00000000-0010-0000-0500-00002C000000}" name="Super Class 4:display:q." dataDxfId="180"><calculatedColumnFormula>
+    <tableColumn id="44" xr3:uid="{00000000-0010-0000-0500-00002C000000}" name="Super Class 4:display:q." dataDxfId="181"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Super Class 4]],meta_Classifiers[ID],0))&".","")
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="36" xr3:uid="{00000000-0010-0000-0500-000024000000}" name="Super Class 4" dataDxfId="179"><calculatedColumnFormula>
+    <tableColumn id="36" xr3:uid="{00000000-0010-0000-0500-000024000000}" name="Super Class 4" dataDxfId="180"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Rules[[#This Row],[Super Class 3]],meta_Classifiers[ID],0)),0)
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="43" xr3:uid="{00000000-0010-0000-0500-00002B000000}" name="Super Class 3:display:q." dataDxfId="178"><calculatedColumnFormula>
+    <tableColumn id="43" xr3:uid="{00000000-0010-0000-0500-00002B000000}" name="Super Class 3:display:q." dataDxfId="179"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Super Class 3]],meta_Classifiers[ID],0))&".","")
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="35" xr3:uid="{00000000-0010-0000-0500-000023000000}" name="Super Class 3" dataDxfId="177"><calculatedColumnFormula>
+    <tableColumn id="35" xr3:uid="{00000000-0010-0000-0500-000023000000}" name="Super Class 3" dataDxfId="178"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Rules[[#This Row],[Super Class 2]],meta_Classifiers[ID],0)),0)
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="42" xr3:uid="{00000000-0010-0000-0500-00002A000000}" name="Super Class 2:display:q." dataDxfId="176"><calculatedColumnFormula>
+    <tableColumn id="42" xr3:uid="{00000000-0010-0000-0500-00002A000000}" name="Super Class 2:display:q." dataDxfId="177"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Super Class 2]],meta_Classifiers[ID],0))&".","")
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="34" xr3:uid="{00000000-0010-0000-0500-000022000000}" name="Super Class 2" dataDxfId="175"><calculatedColumnFormula>
+    <tableColumn id="34" xr3:uid="{00000000-0010-0000-0500-000022000000}" name="Super Class 2" dataDxfId="176"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Rules[[#This Row],[Super Class 1]],meta_Classifiers[ID],0)),0)
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="40" xr3:uid="{00000000-0010-0000-0500-000028000000}" name="Super Class 1:display:q." dataDxfId="174"><calculatedColumnFormula>
+    <tableColumn id="40" xr3:uid="{00000000-0010-0000-0500-000028000000}" name="Super Class 1:display:q." dataDxfId="175"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Super Class 1]],meta_Classifiers[ID],0))&".","")
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="33" xr3:uid="{00000000-0010-0000-0500-000021000000}" name="Super Class 1" dataDxfId="173"><calculatedColumnFormula>
+    <tableColumn id="33" xr3:uid="{00000000-0010-0000-0500-000021000000}" name="Super Class 1" dataDxfId="174"><calculatedColumnFormula>
         _xlfn.IFNA(INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Rules[[#This Row],[Class:src]],meta_Classifiers[ID],0)),0)
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="41" xr3:uid="{00000000-0010-0000-0500-000029000000}" name="Class:display:q." dataDxfId="172"><calculatedColumnFormula>
+    <tableColumn id="41" xr3:uid="{00000000-0010-0000-0500-000029000000}" name="Class:display:q." dataDxfId="173"><calculatedColumnFormula>
         INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Class:src]],meta_Classifiers[ID],0))&"."
     </calculatedColumnFormula></tableColumn>
-    <tableColumn id="4" xr3:uid="{00000000-0010-0000-0500-000004000000}" name="Class:src" dataDxfId="171"/>
-    <tableColumn id="30" xr3:uid="{00000000-0010-0000-0500-00001E000000}" name="Class" dataDxfId="170"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Rules[[#This Row],[Class:src]] ) = "", "",
+    <tableColumn id="4" xr3:uid="{00000000-0010-0000-0500-000004000000}" name="Class:src" dataDxfId="172"/>
+    <tableColumn id="30" xr3:uid="{00000000-0010-0000-0500-00001E000000}" name="Class" dataDxfId="171"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Rules[[#This Row],[Class:src]] ) = "", "",
         INDEX( meta_Classifiers[Display Qualified], MATCH( meta_Rules[[#This Row],[Class:src]], meta_Classifiers[ID], 0 ) ) )</calculatedColumnFormula></tableColumn>
-        <tableColumn id="48" xr3:uid="{00000000-0010-0000-0500-000030000000}" name="Feature Type" dataDxfId="169"><calculatedColumnFormula>
+        <tableColumn id="48" xr3:uid="{00000000-0010-0000-0500-000030000000}" name="Feature Type" dataDxfId="170"><calculatedColumnFormula>
             IF(TRIM(meta_Rules[[#This Row],[Feature]])="","",INDEX(meta_TypedModelElements[Type Derived],MATCH(meta_Rules[[#This Row],[Feature:src]],meta_TypedModelElements[ID],0)))
         </calculatedColumnFormula></tableColumn>
-        <tableColumn id="99" xr3:uid="{00000000-0010-0000-0500-000063000000}" name="Feature Base Type Kind" dataDxfId="168"><calculatedColumnFormula>
+        <tableColumn id="99" xr3:uid="{00000000-0010-0000-0500-000063000000}" name="Feature Base Type Kind" dataDxfId="169"><calculatedColumnFormula>
             IF(meta_Rules[[#This Row],[Class:src]]="","_Datatype","_Class")
         </calculatedColumnFormula></tableColumn>
-        <tableColumn id="39" xr3:uid="{00000000-0010-0000-0500-000027000000}" name="Feature:src" dataDxfId="167"/>
-        <tableColumn id="5" xr3:uid="{00000000-0010-0000-0500-000005000000}" name="Feature" dataDxfId="166"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Feature:src]] ) = "",
+        <tableColumn id="39" xr3:uid="{00000000-0010-0000-0500-000027000000}" name="Feature:src" dataDxfId="168"/>
+        <tableColumn id="5" xr3:uid="{00000000-0010-0000-0500-000005000000}" name="Feature" dataDxfId="167"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Feature:src]] ) = "",
             "",
             INDEX( meta_TypedModelElements[Display without Class], MATCH( meta_Rules[[#This Row],[Feature:src]], meta_TypedModelElements[ID], 0 ) )
  ), "")</calculatedColumnFormula></tableColumn>
-            <tableColumn id="114" xr3:uid="{6FFBDF1C-B3B4-1243-9B10-6C1BCF68BF28}" name="VBA Function Step 1" dataDxfId="165"/>
-            <tableColumn id="113" xr3:uid="{48E2B363-37B5-F842-903F-FA77081BCE10}" name="VBA Function Step 2" dataDxfId="164"/>
-            <tableColumn id="112" xr3:uid="{28CD41D5-218C-4942-89C9-F94630A9FC92}" name="VBA Function Step 3" dataDxfId="163"/>
-            <tableColumn id="111" xr3:uid="{D81BFF57-55DF-E948-A4C2-C4202E263512}" name="Do Action Rule Details" dataDxfId="162"/>
-            <tableColumn id="19" xr3:uid="{00000000-0010-0000-0500-000013000000}" name="Line" dataDxfId="161"/>
-            <tableColumn id="21" xr3:uid="{00000000-0010-0000-0500-000015000000}" name="Part:src" dataDxfId="160"/>
-            <tableColumn id="22" xr3:uid="{00000000-0010-0000-0500-000016000000}" name="Part:displayedChoice" dataDxfId="159"/>
-            <tableColumn id="24" xr3:uid="{00000000-0010-0000-0500-000018000000}" name="Part:q" dataDxfId="158"><calculatedColumnFormula>
+            <tableColumn id="114" xr3:uid="{6FFBDF1C-B3B4-1243-9B10-6C1BCF68BF28}" name="VBA Function Step 1" dataDxfId="166"/>
+            <tableColumn id="113" xr3:uid="{48E2B363-37B5-F842-903F-FA77081BCE10}" name="VBA Function Step 2" dataDxfId="165"/>
+            <tableColumn id="112" xr3:uid="{28CD41D5-218C-4942-89C9-F94630A9FC92}" name="VBA Function Step 3" dataDxfId="164"/>
+            <tableColumn id="111" xr3:uid="{D81BFF57-55DF-E948-A4C2-C4202E263512}" name="Do Action Rule Details" dataDxfId="163"/>
+            <tableColumn id="19" xr3:uid="{00000000-0010-0000-0500-000013000000}" name="Line" dataDxfId="162"/>
+            <tableColumn id="21" xr3:uid="{00000000-0010-0000-0500-000015000000}" name="Part:src" dataDxfId="161"/>
+            <tableColumn id="22" xr3:uid="{00000000-0010-0000-0500-000016000000}" name="Part:displayedChoice" dataDxfId="160"/>
+            <tableColumn id="24" xr3:uid="{00000000-0010-0000-0500-000018000000}" name="Part:q" dataDxfId="159"><calculatedColumnFormula>
                 IF(TRIM(meta_Rules[[#This Row],[Part]])="","",IF(
                 TRIM(meta_Rules[[#This Row],[Package]])="",
                 "",
                 meta_Rules[[#This Row],[Package]]&"::")
                 &meta_Rules[[#This Row],[Part]])
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="97" xr3:uid="{00000000-0010-0000-0500-000061000000}" name="Line As Text" dataDxfId="157"><calculatedColumnFormula>
+            <tableColumn id="97" xr3:uid="{00000000-0010-0000-0500-000061000000}" name="Line As Text" dataDxfId="158"><calculatedColumnFormula>
                 meta_Rules[[#This Row],[Class]]&IF(meta_Rules[[#This Row],[Feature]]=""," ","."&meta_Rules[[#This Row],[Feature]]&" ")&
                 IF(LEN(meta_Rules[[#This Row],[Class]])+LEN(meta_Rules[[#This Row],[Feature]])>65,REPT(" ",78+IF(meta_Rules[[#This Row],[Feature]]="",1,0)-(LEN(meta_Rules[[#This Row],[Class]])+LEN(meta_Rules[[#This Row],[Feature]]))),
                 IF(LEN(meta_Rules[[#This Row],[Class]])+LEN(meta_Rules[[#This Row],[Feature]])>55,REPT(" ",68+IF(meta_Rules[[#This Row],[Feature]]="",1,0)-(LEN(meta_Rules[[#This Row],[Class]])+LEN(meta_Rules[[#This Row],[Feature]]))),
@@ -91,69 +91,69 @@
                 meta_Rules[[#This Row],[Kind]]&
                 IF(meta_Rules[[#This Row],[Line]]="","",REPT(" ",10-LEN(meta_Rules[[#This Row],[Kind]]))&TEXT(meta_Rules[[#This Row],[Line]],"00"))
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="16" xr3:uid="{00000000-0010-0000-0500-000010000000}" name="Part" dataDxfId="156"/>
-            <tableColumn id="9" xr3:uid="{00000000-0010-0000-0500-000009000000}" name="Rule Code" dataDxfId="155"/>
-            <tableColumn id="29" xr3:uid="{00000000-0010-0000-0500-00001D000000}" name="Rule Biz ID Without Line" dataDxfId="154"><calculatedColumnFormula>
+            <tableColumn id="16" xr3:uid="{00000000-0010-0000-0500-000010000000}" name="Part" dataDxfId="157"/>
+            <tableColumn id="9" xr3:uid="{00000000-0010-0000-0500-000009000000}" name="Rule Code" dataDxfId="156"/>
+            <tableColumn id="29" xr3:uid="{00000000-0010-0000-0500-00001D000000}" name="Rule Biz ID Without Line" dataDxfId="155"><calculatedColumnFormula>
                 meta_Rules[[#This Row],[Class:src]]&"_"&meta_Rules[[#This Row],[Feature]]&"_"&meta_Rules[[#This Row],[Kind]]
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="27" xr3:uid="{00000000-0010-0000-0500-00001B000000}" name="Rule Biz ID" dataDxfId="153"><calculatedColumnFormula>
+            <tableColumn id="27" xr3:uid="{00000000-0010-0000-0500-00001B000000}" name="Rule Biz ID" dataDxfId="154"><calculatedColumnFormula>
                 meta_Rules[[#This Row],[Rule Biz ID Without Line]]&"_"&meta_Rules[[#This Row],[Line]]
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="31" xr3:uid="{00000000-0010-0000-0500-00001F000000}" name="Part:src At Line - 1" dataDxfId="152"><calculatedColumnFormula>
+            <tableColumn id="31" xr3:uid="{00000000-0010-0000-0500-00001F000000}" name="Part:src At Line - 1" dataDxfId="153"><calculatedColumnFormula>
                 IF(meta_Rules[[#This Row],[Line-1]]="","",INDEX(meta_Rules[Part:src],MATCH(meta_Rules[[#This Row],[Rule Biz ID Without Line]]&"_"&meta_Rules[[#This Row],[Line-1]],meta_Rules[Rule Biz ID],0)))
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="28" xr3:uid="{00000000-0010-0000-0500-00001C000000}" name="Line-1" dataDxfId="151"><calculatedColumnFormula>
+            <tableColumn id="28" xr3:uid="{00000000-0010-0000-0500-00001C000000}" name="Line-1" dataDxfId="152"><calculatedColumnFormula>
                 IF(TRIM(meta_Rules[[#This Row],[Line]])="","",IF(meta_Rules[[#This Row],[Line]]=1,"",meta_Rules[[#This Row],[Line]]-1))
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="26" xr3:uid="{00000000-0010-0000-0500-00001A000000}" name="Indent" dataDxfId="150"><calculatedColumnFormula>
+            <tableColumn id="26" xr3:uid="{00000000-0010-0000-0500-00001A000000}" name="Indent" dataDxfId="151"><calculatedColumnFormula>
                 IF(TRIM(meta_Rules[[#This Row],[Line]])="",0,IF(meta_Rules[[#This Row],[Line]]=1,0,
                 999))
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="25" xr3:uid="{00000000-0010-0000-0500-000019000000}" name="Generation" dataDxfId="149"/>
-            <tableColumn id="17" xr3:uid="{00000000-0010-0000-0500-000011000000}" name="Operator" dataDxfId="148"/>
-            <tableColumn id="62" xr3:uid="{00000000-0010-0000-0500-00003E000000}" name="Base Super Class 6:display:q." dataDxfId="147"><calculatedColumnFormula>
+            <tableColumn id="25" xr3:uid="{00000000-0010-0000-0500-000019000000}" name="Generation" dataDxfId="150"/>
+            <tableColumn id="17" xr3:uid="{00000000-0010-0000-0500-000011000000}" name="Operator" dataDxfId="149"/>
+            <tableColumn id="62" xr3:uid="{00000000-0010-0000-0500-00003E000000}" name="Base Super Class 6:display:q." dataDxfId="148"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Base Super Class 6]],meta_Classifiers[ID],0))&".","")
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="61" xr3:uid="{00000000-0010-0000-0500-00003D000000}" name="Base Super Class 6" dataDxfId="146"><calculatedColumnFormula>
+            <tableColumn id="61" xr3:uid="{00000000-0010-0000-0500-00003D000000}" name="Base Super Class 6" dataDxfId="147"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Base Super Class 5]],meta_Classifiers[ID],0)),0)
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="60" xr3:uid="{00000000-0010-0000-0500-00003C000000}" name="Base Super Class 5:display:q." dataDxfId="145"><calculatedColumnFormula>
+            <tableColumn id="60" xr3:uid="{00000000-0010-0000-0500-00003C000000}" name="Base Super Class 5:display:q." dataDxfId="146"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Base Super Class 5]],meta_Classifiers[ID],0))&".","")
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="59" xr3:uid="{00000000-0010-0000-0500-00003B000000}" name="Base Super Class 5" dataDxfId="144"><calculatedColumnFormula>
+            <tableColumn id="59" xr3:uid="{00000000-0010-0000-0500-00003B000000}" name="Base Super Class 5" dataDxfId="145"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Base Super Class 4]],meta_Classifiers[ID],0)),0)
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="58" xr3:uid="{00000000-0010-0000-0500-00003A000000}" name="Base Super Class 4:display:q." dataDxfId="143"><calculatedColumnFormula>
+            <tableColumn id="58" xr3:uid="{00000000-0010-0000-0500-00003A000000}" name="Base Super Class 4:display:q." dataDxfId="144"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Base Super Class 4]],meta_Classifiers[ID],0))&".","")
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="57" xr3:uid="{00000000-0010-0000-0500-000039000000}" name="Base Super Class 4" dataDxfId="142"><calculatedColumnFormula>
+            <tableColumn id="57" xr3:uid="{00000000-0010-0000-0500-000039000000}" name="Base Super Class 4" dataDxfId="143"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Base Super Class 3]],meta_Classifiers[ID],0)),0)
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="56" xr3:uid="{00000000-0010-0000-0500-000038000000}" name="Base Super Class 3:display:q." dataDxfId="141"><calculatedColumnFormula>
+            <tableColumn id="56" xr3:uid="{00000000-0010-0000-0500-000038000000}" name="Base Super Class 3:display:q." dataDxfId="142"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Base Super Class 3]],meta_Classifiers[ID],0))&".","")
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="55" xr3:uid="{00000000-0010-0000-0500-000037000000}" name="Base Super Class 3" dataDxfId="140"><calculatedColumnFormula>
+            <tableColumn id="55" xr3:uid="{00000000-0010-0000-0500-000037000000}" name="Base Super Class 3" dataDxfId="141"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Base Super Class 2]],meta_Classifiers[ID],0)),0)
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="54" xr3:uid="{00000000-0010-0000-0500-000036000000}" name="Base Super Class 2:display:q." dataDxfId="139"><calculatedColumnFormula>
+            <tableColumn id="54" xr3:uid="{00000000-0010-0000-0500-000036000000}" name="Base Super Class 2:display:q." dataDxfId="140"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Base Super Class 2]],meta_Classifiers[ID],0))&".","")
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="53" xr3:uid="{00000000-0010-0000-0500-000035000000}" name="Base Super Class 2" dataDxfId="138"><calculatedColumnFormula>
+            <tableColumn id="53" xr3:uid="{00000000-0010-0000-0500-000035000000}" name="Base Super Class 2" dataDxfId="139"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Base Super Class 1]],meta_Classifiers[ID],0)),0)
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="52" xr3:uid="{00000000-0010-0000-0500-000034000000}" name="Base Super Class 1:display:q." dataDxfId="137"><calculatedColumnFormula>
+            <tableColumn id="52" xr3:uid="{00000000-0010-0000-0500-000034000000}" name="Base Super Class 1:display:q." dataDxfId="138"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Base Super Class 1]],meta_Classifiers[ID],0))&".","")
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="51" xr3:uid="{00000000-0010-0000-0500-000033000000}" name="Base Super Class 1" dataDxfId="136"><calculatedColumnFormula>
+            <tableColumn id="51" xr3:uid="{00000000-0010-0000-0500-000033000000}" name="Base Super Class 1" dataDxfId="137"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Base Type]],meta_Classifiers[ID],0)),0)
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="50" xr3:uid="{00000000-0010-0000-0500-000032000000}" name="Base Class:display:q." dataDxfId="135"><calculatedColumnFormula>
+            <tableColumn id="50" xr3:uid="{00000000-0010-0000-0500-000032000000}" name="Base Class:display:q." dataDxfId="136"><calculatedColumnFormula>
                 INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Base Type]],meta_Classifiers[ID],0))&"."
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="98" xr3:uid="{00000000-0010-0000-0500-000062000000}" name="Base Type Kind" dataDxfId="134"><calculatedColumnFormula>
+            <tableColumn id="98" xr3:uid="{00000000-0010-0000-0500-000062000000}" name="Base Type Kind" dataDxfId="135"><calculatedColumnFormula>
                 INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Base Type]],meta_Classifiers[ID],0))
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="49" xr3:uid="{00000000-0010-0000-0500-000031000000}" name="Base Type" dataDxfId="133"><calculatedColumnFormula>
+            <tableColumn id="49" xr3:uid="{00000000-0010-0000-0500-000031000000}" name="Base Type" dataDxfId="134"><calculatedColumnFormula>
                 IF(meta_Rules[[#This Row],[Base]]="self",meta_Rules[[#This Row],[Class:src]],
                 IF(meta_Rules[[#This Row],[Base]]="super", "TODO type of overwritten version of this property or function. Needs resolution from feature to overwritten/specialized feature",
                 IF(meta_Rules[[#This Row],[Base]]="trg", meta_Rules[[#This Row],[Feature Type]],
@@ -163,67 +163,67 @@
                 IF(meta_Rules[[#This Row],[Base as Parameter]]<>"",INDEX(meta_TypedModelElements[Type Derived],MATCH(meta_Rules[[#This Row],[Base as Parameter]],meta_TypedModelElements[ID],0)),
                 "_String")))))))
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="81" xr3:uid="{00000000-0010-0000-0500-000051000000}" name="Base as Parameter" dataDxfId="132"><calculatedColumnFormula>
+            <tableColumn id="81" xr3:uid="{00000000-0010-0000-0500-000051000000}" name="Base as Parameter" dataDxfId="133"><calculatedColumnFormula>
                 _xlfn.IFNA(INDEX(meta_TypedModelElements[ID],MATCH(meta_Rules[[#This Row],[Feature:src]]&"."&meta_Rules[[#This Row],[Base]],meta_TypedModelElements[ID],0)),"")
             </calculatedColumnFormula></tableColumn>
-            <tableColumn id="15" xr3:uid="{00000000-0010-0000-0500-00000F000000}" name="Base" dataDxfId="131"/>
-            <tableColumn id="63" xr3:uid="{00000000-0010-0000-0500-00003F000000}" name="Property 1:src" dataDxfId="130"/>
-            <tableColumn id="14" xr3:uid="{00000000-0010-0000-0500-00000E000000}" name="Property 1" dataDxfId="129"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Property 1:src]] ) = "",
+            <tableColumn id="15" xr3:uid="{00000000-0010-0000-0500-00000F000000}" name="Base" dataDxfId="132"/>
+            <tableColumn id="63" xr3:uid="{00000000-0010-0000-0500-00003F000000}" name="Property 1:src" dataDxfId="131"/>
+            <tableColumn id="14" xr3:uid="{00000000-0010-0000-0500-00000E000000}" name="Property 1" dataDxfId="130"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Property 1:src]] ) = "",
                 "",
                 INDEX( meta_TypedModelElements[Display without Class], MATCH( meta_Rules[[#This Row],[Property 1:src]], meta_TypedModelElements[ID], 0 ) )
  ), "")</calculatedColumnFormula></tableColumn>
-                <tableColumn id="80" xr3:uid="{00000000-0010-0000-0500-000050000000}" name="Property 1 Super Class 6:display:q." dataDxfId="128"><calculatedColumnFormula>
+                <tableColumn id="80" xr3:uid="{00000000-0010-0000-0500-000050000000}" name="Property 1 Super Class 6:display:q." dataDxfId="129"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 1 Super Class 6]],meta_Classifiers[ID],0))&".","")
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="79" xr3:uid="{00000000-0010-0000-0500-00004F000000}" name="Property 1 Super Class 6" dataDxfId="127"><calculatedColumnFormula>
+                <tableColumn id="79" xr3:uid="{00000000-0010-0000-0500-00004F000000}" name="Property 1 Super Class 6" dataDxfId="128"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 1 Super Class 5]],meta_Classifiers[ID],0)),0)
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="78" xr3:uid="{00000000-0010-0000-0500-00004E000000}" name="Property 1 Super Class 5:display:q." dataDxfId="126"><calculatedColumnFormula>
+                <tableColumn id="78" xr3:uid="{00000000-0010-0000-0500-00004E000000}" name="Property 1 Super Class 5:display:q." dataDxfId="127"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 1 Super Class 5]],meta_Classifiers[ID],0))&".","")
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="77" xr3:uid="{00000000-0010-0000-0500-00004D000000}" name="Property 1 Super Class 5" dataDxfId="125"><calculatedColumnFormula>
+                <tableColumn id="77" xr3:uid="{00000000-0010-0000-0500-00004D000000}" name="Property 1 Super Class 5" dataDxfId="126"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 1 Super Class 4]],meta_Classifiers[ID],0)),0)
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="76" xr3:uid="{00000000-0010-0000-0500-00004C000000}" name="Property 1 Super Class 4:display:q." dataDxfId="124"><calculatedColumnFormula>
+                <tableColumn id="76" xr3:uid="{00000000-0010-0000-0500-00004C000000}" name="Property 1 Super Class 4:display:q." dataDxfId="125"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 1 Super Class 4]],meta_Classifiers[ID],0))&".","")
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="75" xr3:uid="{00000000-0010-0000-0500-00004B000000}" name="Property 1 Super Class 4" dataDxfId="123"><calculatedColumnFormula>
+                <tableColumn id="75" xr3:uid="{00000000-0010-0000-0500-00004B000000}" name="Property 1 Super Class 4" dataDxfId="124"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 1 Super Class 3]],meta_Classifiers[ID],0)),0)
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="74" xr3:uid="{00000000-0010-0000-0500-00004A000000}" name="Property 1 Super Class 3:display:q." dataDxfId="122"><calculatedColumnFormula>
+                <tableColumn id="74" xr3:uid="{00000000-0010-0000-0500-00004A000000}" name="Property 1 Super Class 3:display:q." dataDxfId="123"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 1 Super Class 3]],meta_Classifiers[ID],0))&".","")
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="73" xr3:uid="{00000000-0010-0000-0500-000049000000}" name="Property 1 Super Class 3" dataDxfId="121"><calculatedColumnFormula>
+                <tableColumn id="73" xr3:uid="{00000000-0010-0000-0500-000049000000}" name="Property 1 Super Class 3" dataDxfId="122"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 1 Super Class 2]],meta_Classifiers[ID],0)),0)
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="72" xr3:uid="{00000000-0010-0000-0500-000048000000}" name="Property 1 Super Class 2:display:q." dataDxfId="120"><calculatedColumnFormula>
+                <tableColumn id="72" xr3:uid="{00000000-0010-0000-0500-000048000000}" name="Property 1 Super Class 2:display:q." dataDxfId="121"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 1 Super Class 2]],meta_Classifiers[ID],0))&".","")
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="71" xr3:uid="{00000000-0010-0000-0500-000047000000}" name="Property 1 Super Class 2" dataDxfId="119"><calculatedColumnFormula>
+                <tableColumn id="71" xr3:uid="{00000000-0010-0000-0500-000047000000}" name="Property 1 Super Class 2" dataDxfId="120"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 1 Super Class 1]],meta_Classifiers[ID],0)),0)
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="70" xr3:uid="{00000000-0010-0000-0500-000046000000}" name="Property 1 Super Class 1:display:q." dataDxfId="118"><calculatedColumnFormula>
+                <tableColumn id="70" xr3:uid="{00000000-0010-0000-0500-000046000000}" name="Property 1 Super Class 1:display:q." dataDxfId="119"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 1 Super Class 1]],meta_Classifiers[ID],0))&".","")
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="69" xr3:uid="{00000000-0010-0000-0500-000045000000}" name="Property 1 Super Class 1" dataDxfId="117"><calculatedColumnFormula>
+                <tableColumn id="69" xr3:uid="{00000000-0010-0000-0500-000045000000}" name="Property 1 Super Class 1" dataDxfId="118"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 1 Type]],meta_Classifiers[ID],0)),0)
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="68" xr3:uid="{00000000-0010-0000-0500-000044000000}" name="Property 1 Class:display:q." dataDxfId="116"><calculatedColumnFormula>
+                <tableColumn id="68" xr3:uid="{00000000-0010-0000-0500-000044000000}" name="Property 1 Class:display:q." dataDxfId="117"><calculatedColumnFormula>
                     _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 1 Type]],meta_Classifiers[ID],0))&".",0)
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="100" xr3:uid="{00000000-0010-0000-0500-000064000000}" name="Property 1 Type Kind" dataDxfId="115"><calculatedColumnFormula>
+                <tableColumn id="100" xr3:uid="{00000000-0010-0000-0500-000064000000}" name="Property 1 Type Kind" dataDxfId="116"><calculatedColumnFormula>
                     IF(meta_Rules[[#This Row],[Property 1 Type]]="","",INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 1 Type]],meta_Classifiers[ID],0)))
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="67" xr3:uid="{00000000-0010-0000-0500-000043000000}" name="Property 1 Type" dataDxfId="114"><calculatedColumnFormula>
+                <tableColumn id="67" xr3:uid="{00000000-0010-0000-0500-000043000000}" name="Property 1 Type" dataDxfId="115"><calculatedColumnFormula>
                     IF(meta_Rules[[#This Row],[Property 1:src]]="","",INDEX(meta_TypedModelElements[Type:src],MATCH(meta_Rules[[#This Row],[Property 1:src]],meta_TypedModelElements[ID],0)))
                 </calculatedColumnFormula></tableColumn>
-                <tableColumn id="66" xr3:uid="{00000000-0010-0000-0500-000042000000}" name="Property 2:src" dataDxfId="113"/>
-                <tableColumn id="13" xr3:uid="{00000000-0010-0000-0500-00000D000000}" name="Property 2" dataDxfId="112"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Property 2:src]] ) = "",
+                <tableColumn id="66" xr3:uid="{00000000-0010-0000-0500-000042000000}" name="Property 2:src" dataDxfId="114"/>
+                <tableColumn id="13" xr3:uid="{00000000-0010-0000-0500-00000D000000}" name="Property 2" dataDxfId="113"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Property 2:src]] ) = "",
                     "",
                     INDEX( meta_TypedModelElements[Display without Class], MATCH( meta_Rules[[#This Row],[Property 2:src]], meta_TypedModelElements[ID], 0 ) )
  ), "")</calculatedColumnFormula></tableColumn>
-                    <tableColumn id="65" xr3:uid="{00000000-0010-0000-0500-000041000000}" name="Cast:src" dataDxfId="111"/>
-                    <tableColumn id="12" xr3:uid="{00000000-0010-0000-0500-00000C000000}" name="Cast" dataDxfId="110"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Cast:src]] ) = "",
+                    <tableColumn id="65" xr3:uid="{00000000-0010-0000-0500-000041000000}" name="Cast:src" dataDxfId="112"/>
+                    <tableColumn id="12" xr3:uid="{00000000-0010-0000-0500-00000C000000}" name="Cast" dataDxfId="111"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Cast:src]] ) = "",
                         "",
                         IF( LEFT(meta_Rules[[#This Row],[Cast:src]],1)="_",
                         RIGHT(meta_Rules[[#This Row],[Cast:src]],LEN(meta_Rules[[#This Row],[Cast:src]])-1),
@@ -234,68 +234,68 @@
                             & INDEX( meta_Classifiers[Display], MATCH( meta_Rules[[#This Row],[Cast:src]], meta_Classifiers[ID], 0 ) ),
                             INDEX( meta_Classifiers[Display], MATCH( meta_Rules[[#This Row],[Cast:src]], meta_Classifiers[ID], 0 ) )
     ))), "")</calculatedColumnFormula></tableColumn>
-                            <tableColumn id="96" xr3:uid="{00000000-0010-0000-0500-000060000000}" name="Property 2 Super Class 6:display:q." dataDxfId="109"><calculatedColumnFormula>
+                            <tableColumn id="96" xr3:uid="{00000000-0010-0000-0500-000060000000}" name="Property 2 Super Class 6:display:q." dataDxfId="110"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 2 Super Class 6]],meta_Classifiers[ID],0))&".","")
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="95" xr3:uid="{00000000-0010-0000-0500-00005F000000}" name="Property 2 Super Class 6" dataDxfId="108"><calculatedColumnFormula>
+                            <tableColumn id="95" xr3:uid="{00000000-0010-0000-0500-00005F000000}" name="Property 2 Super Class 6" dataDxfId="109"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 2 Super Class 5]],meta_Classifiers[ID],0)),0)
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="94" xr3:uid="{00000000-0010-0000-0500-00005E000000}" name="Property 2 Super Class 5:display:q." dataDxfId="107"><calculatedColumnFormula>
+                            <tableColumn id="94" xr3:uid="{00000000-0010-0000-0500-00005E000000}" name="Property 2 Super Class 5:display:q." dataDxfId="108"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 2 Super Class 5]],meta_Classifiers[ID],0))&".","")
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="93" xr3:uid="{00000000-0010-0000-0500-00005D000000}" name="Property 2 Super Class 5" dataDxfId="106"><calculatedColumnFormula>
+                            <tableColumn id="93" xr3:uid="{00000000-0010-0000-0500-00005D000000}" name="Property 2 Super Class 5" dataDxfId="107"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 2 Super Class 4]],meta_Classifiers[ID],0)),0)
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="92" xr3:uid="{00000000-0010-0000-0500-00005C000000}" name="Property 2 Super Class 4:display:q." dataDxfId="105"><calculatedColumnFormula>
+                            <tableColumn id="92" xr3:uid="{00000000-0010-0000-0500-00005C000000}" name="Property 2 Super Class 4:display:q." dataDxfId="106"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 2 Super Class 4]],meta_Classifiers[ID],0))&".","")
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="91" xr3:uid="{00000000-0010-0000-0500-00005B000000}" name="Property 2 Super Class 4" dataDxfId="104"><calculatedColumnFormula>
+                            <tableColumn id="91" xr3:uid="{00000000-0010-0000-0500-00005B000000}" name="Property 2 Super Class 4" dataDxfId="105"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 2 Super Class 3]],meta_Classifiers[ID],0)),0)
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="90" xr3:uid="{00000000-0010-0000-0500-00005A000000}" name="Property 2 Super Class 3:display:q." dataDxfId="103"><calculatedColumnFormula>
+                            <tableColumn id="90" xr3:uid="{00000000-0010-0000-0500-00005A000000}" name="Property 2 Super Class 3:display:q." dataDxfId="104"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 2 Super Class 3]],meta_Classifiers[ID],0))&".","")
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="89" xr3:uid="{00000000-0010-0000-0500-000059000000}" name="Property 2 Super Class 3" dataDxfId="102"><calculatedColumnFormula>
+                            <tableColumn id="89" xr3:uid="{00000000-0010-0000-0500-000059000000}" name="Property 2 Super Class 3" dataDxfId="103"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 2 Super Class 2]],meta_Classifiers[ID],0)),0)
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="88" xr3:uid="{00000000-0010-0000-0500-000058000000}" name="Property 2 Super Class 2:display:q." dataDxfId="101"><calculatedColumnFormula>
+                            <tableColumn id="88" xr3:uid="{00000000-0010-0000-0500-000058000000}" name="Property 2 Super Class 2:display:q." dataDxfId="102"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 2 Super Class 2]],meta_Classifiers[ID],0))&".","")
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="87" xr3:uid="{00000000-0010-0000-0500-000057000000}" name="Property 2 Super Class 2" dataDxfId="100"><calculatedColumnFormula>
+                            <tableColumn id="87" xr3:uid="{00000000-0010-0000-0500-000057000000}" name="Property 2 Super Class 2" dataDxfId="101"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 2 Super Class 1]],meta_Classifiers[ID],0)),0)
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="86" xr3:uid="{00000000-0010-0000-0500-000056000000}" name="Property 2 Super Class 1:display:q." dataDxfId="99"><calculatedColumnFormula>
+                            <tableColumn id="86" xr3:uid="{00000000-0010-0000-0500-000056000000}" name="Property 2 Super Class 1:display:q." dataDxfId="100"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 2 Super Class 1]],meta_Classifiers[ID],0))&".","")
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="85" xr3:uid="{00000000-0010-0000-0500-000055000000}" name="Property 2 Super Class 1" dataDxfId="98"><calculatedColumnFormula>
+                            <tableColumn id="85" xr3:uid="{00000000-0010-0000-0500-000055000000}" name="Property 2 Super Class 1" dataDxfId="99"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 2 or Cast Type]],meta_Classifiers[ID],0)),0)
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="84" xr3:uid="{00000000-0010-0000-0500-000054000000}" name="Property 2 Class:display:q." dataDxfId="97"><calculatedColumnFormula>
+                            <tableColumn id="84" xr3:uid="{00000000-0010-0000-0500-000054000000}" name="Property 2 Class:display:q." dataDxfId="98"><calculatedColumnFormula>
                                 _xlfn.IFNA(INDEX(meta_Classifiers[Display Qualified],MATCH(meta_Rules[[#This Row],[Property 2 or Cast Type]],meta_Classifiers[ID],0))&".",0)
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="101" xr3:uid="{00000000-0010-0000-0500-000065000000}" name="Property 2 or Cast Type Kind" dataDxfId="96"><calculatedColumnFormula>
+                            <tableColumn id="101" xr3:uid="{00000000-0010-0000-0500-000065000000}" name="Property 2 or Cast Type Kind" dataDxfId="97"><calculatedColumnFormula>
                                 IF(meta_Rules[[#This Row],[Property 2 or Cast Type]]="","",INDEX(#REF!,MATCH(meta_Rules[[#This Row],[Property 2 or Cast Type]],meta_Classifiers[ID],0)))
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="83" xr3:uid="{00000000-0010-0000-0500-000053000000}" name="Property 2 or Cast Type" dataDxfId="95"><calculatedColumnFormula>
+                            <tableColumn id="83" xr3:uid="{00000000-0010-0000-0500-000053000000}" name="Property 2 or Cast Type" dataDxfId="96"><calculatedColumnFormula>
                                 IF(meta_Rules[[#This Row],[Cast:src]]<>"",meta_Rules[[#This Row],[Cast:src]],IF(meta_Rules[[#This Row],[Property 2:src]]="","",INDEX(meta_TypedModelElements[Type:src],MATCH(meta_Rules[[#This Row],[Property 2:src]],meta_TypedModelElements[ID],0))))
                             </calculatedColumnFormula></tableColumn>
-                            <tableColumn id="82" xr3:uid="{00000000-0010-0000-0500-000052000000}" name="Property 3:src" dataDxfId="94"/>
-                            <tableColumn id="11" xr3:uid="{00000000-0010-0000-0500-00000B000000}" name="Property 3" dataDxfId="93"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Property 3:src]] ) = "",
+                            <tableColumn id="82" xr3:uid="{00000000-0010-0000-0500-000052000000}" name="Property 3:src" dataDxfId="95"/>
+                            <tableColumn id="11" xr3:uid="{00000000-0010-0000-0500-00000B000000}" name="Property 3" dataDxfId="94"><calculatedColumnFormula xml:space="preserve"> _xlfn.IFNA( IF( TRIM( meta_Rules[[#This Row],[Property 3:src]] ) = "",
                                 "",
                                 INDEX( meta_TypedModelElements[Display without Class], MATCH( meta_Rules[[#This Row],[Property 3:src]], meta_TypedModelElements[ID], 0 ) )
  ), "")</calculatedColumnFormula></tableColumn>
-                                <tableColumn id="10" xr3:uid="{00000000-0010-0000-0500-00000A000000}" name="Processor" dataDxfId="92"/>
-                                <tableColumn id="47" xr3:uid="{00000000-0010-0000-0500-00002F000000}" name="Rule" dataDxfId="91"><calculatedColumnFormula>
+                                <tableColumn id="10" xr3:uid="{00000000-0010-0000-0500-00000A000000}" name="Processor" dataDxfId="93"/>
+                                <tableColumn id="47" xr3:uid="{00000000-0010-0000-0500-00002F000000}" name="Rule" dataDxfId="92"><calculatedColumnFormula>
                                     +"1"
                                 </calculatedColumnFormula></tableColumn>
-                                <tableColumn id="6" xr3:uid="{00000000-0010-0000-0500-000006000000}" name="Manual VBA Code" dataDxfId="90"/>
-                                <tableColumn id="102" xr3:uid="{00000000-0010-0000-0500-000066000000}" name="VBA Code" dataDxfId="89"><calculatedColumnFormula>
+                                <tableColumn id="6" xr3:uid="{00000000-0010-0000-0500-000006000000}" name="Manual VBA Code" dataDxfId="91"/>
+                                <tableColumn id="102" xr3:uid="{00000000-0010-0000-0500-000066000000}" name="VBA Code" dataDxfId="90"><calculatedColumnFormula>
                                     IF(meta_Rules[[#This Row],[Manual VBA Code]]<>"",meta_Rules[[#This Row],[Manual VBA Code]],"TODO")
                                 </calculatedColumnFormula></tableColumn>
-                                <tableColumn id="7" xr3:uid="{00000000-0010-0000-0500-000007000000}" name="Manual Excel Formula" dataDxfId="88"/>
-                                <tableColumn id="103" xr3:uid="{00000000-0010-0000-0500-000067000000}" name="Excel Formula" dataDxfId="87"/>
-                                <tableColumn id="20" xr3:uid="{00000000-0010-0000-0500-000014000000}" name="Constraint Is Invariant" dataDxfId="86"/>
-                                <tableColumn id="18" xr3:uid="{00000000-0010-0000-0500-000012000000}" name="Update - Name" dataDxfId="85"/>
-                                <tableColumn id="64" xr3:uid="{00000000-0010-0000-0500-000040000000}" name="Update LHS - Feature:src" dataDxfId="84"/>
-                                <tableColumn id="2" xr3:uid="{00000000-0010-0000-0500-000002000000}" name="Update LHS - Feature" dataDxfId="83"/>
-                                <tableColumn id="8" xr3:uid="{00000000-0010-0000-0500-000008000000}" name="Update LHS - Mode" dataDxfId="82"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+                                <tableColumn id="7" xr3:uid="{00000000-0010-0000-0500-000007000000}" name="Manual Excel Formula" dataDxfId="89"/>
+                                <tableColumn id="103" xr3:uid="{00000000-0010-0000-0500-000067000000}" name="Excel Formula" dataDxfId="88"/>
+                                <tableColumn id="20" xr3:uid="{00000000-0010-0000-0500-000014000000}" name="Constraint Is Invariant" dataDxfId="87"/>
+                                <tableColumn id="18" xr3:uid="{00000000-0010-0000-0500-000012000000}" name="Update - Name" dataDxfId="86"/>
+                                <tableColumn id="64" xr3:uid="{00000000-0010-0000-0500-000040000000}" name="Update LHS - Feature:src" dataDxfId="85"/>
+                                <tableColumn id="2" xr3:uid="{00000000-0010-0000-0500-000002000000}" name="Update LHS - Feature" dataDxfId="84"/>
+                                <tableColumn id="8" xr3:uid="{00000000-0010-0000-0500-000008000000}" name="Update LHS - Mode" dataDxfId="83"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
```
