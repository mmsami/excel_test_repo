# Changes in veri.excel/xl/tables/table8.xml

```diff
diff --git a/veri.excel/xl/tables/table8.xml b/veri.excel/xl/tables/table8.xml
index 10d7256..061ab6b 100644
--- a/veri.excel/xl/tables/table8.xml
+++ b/veri.excel/xl/tables/table8.xml
@@ -1,121 +1,217 @@
 <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
-<table>
-    xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
-    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
-    mc:Ignorable="xr
-    xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision"
-    xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3"
-    id="14"
-    xr:uid="{00000000-000C-0000-FFFF-FFFF04000000}"
-    name="meta_Columns"
-    displayName="meta_Columns"
-    ref="A1:BE422"
-    totalsRowShown="0"
-    headerRowDxfId="367"
-    dataDxfId="365"
-    headerRowBorderDxfId="366"
-    tableBorderDxfId="364"
-    totalsRowBorderDxfId="363"<autoFilter
-    ref="A1:BE422"
-    xr:uid="{00000000-0009-0000-0100-00000E000000}"/<tableColumns
-    count="57"<tableColumn
-    id="1"
-    xr3:uid="{00000000-0010-0000-0400-000001000000}"
-    name="ID"
-    dataDxfId="362"/<tableColumn
-    id="49"
-    xr3:uid="{6E72B505-24D7-4338-9A65-D70EFDFFC57B}"
-    name="Kind:src"
-    dataDxfId="361"/<tableColumn
-    id="3"
-    xr3:uid="{00000000-0010-0000-0400-000003000000}"
-    name="Kind"
-    dataDxfId="360"<calculatedColumnFormula
-    xml:space="preserve"
-    =
-    INDEX( meta_Classifiers[Display Qualified], MATCH( meta_Columns[[#This Row],[Kind:src]], meta_Classifiers[ID], 0 ) ) )</calculatedColumnFormula></tableColumn><tableColumn id="4" xr3:uid="{00000000-0010-0000-0400-000004000000}" name="Package" dataDxfId="359"><calculatedColumnFormula>IF(meta_Columns[[#This Row],[Owning Table:src]]="","",INDEX(meta_Classifiers[Package],MATCH(meta_Columns[[#This Row],[Owning Table Instances Class]],meta_Classifiers[ID],0)))</calculatedColumnFormula></tableColumn><tableColumn id="5" xr3:uid="{00000000-0010-0000-0400-000005000000}" name="Sub Package" dataDxfId="358"/><tableColumn id="14" xr3:uid="{00000000-0010-0000-0400-00000E000000}" name="_Tables" dataDxfId="357"><calculatedColumnFormula>INDEX(meta_Tables[Excel Table - Excel Name],MATCH(meta_Columns[[#This Row],[Owning Table:src]],meta_Tables[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="10" xr3:uid="{00000000-0010-0000-0400-00000A000000}" name="Owning Table Instances Class" dataDxfId="356"><calculatedColumnFormula>INDEX(meta_Tables[Instances Class:src],MATCH(meta_Columns[[#This Row],[Owning Table:src]],meta_Tables[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="40" xr3:uid="{C54BA0C1-D44D-4CFE-B1CA-3F830A4C1A66}" name="Owning Table:src" dataDxfId="355"/><tableColumn id="9" xr3:uid="{00000000-0010-0000-0400-000009000000}" name="Owning Table" dataDxfId="354"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Columns[[#This Row],[Owning Table:src]] ) = "", "",
-    INDEX( meta_Tables[Display Qualified], MATCH( meta_Columns[[#This Row],[Owning Table:src]], meta_Tables[ID], 0 ) ) )</calculatedColumnFormula></tableColumn><tableColumn id="48" xr3:uid="{3D7A0EDF-AF51-40A8-8A98-34751314A8CC}" name="Referenced Table:src" dataDxfId="353"/><tableColumn id="45" xr3:uid="{B2BC55F0-4617-47EF-A1AE-AA473E4D6E63}" name="Referenced Table" dataDxfId="352"><calculatedColumnFormula>IF(TRIM(meta_Columns[[#This Row],[Referenced Table:src]])="","",
-    INDEX(meta_Tables[Display Qualified],MATCH(meta_Columns[[#This Row],[Referenced Table:src]],meta_Tables[ID],0)))</calculatedColumnFormula></tableColumn><tableColumn id="50" xr3:uid="{26D77C09-C15A-4576-B795-02A30483B8C0}" name="Referenced Table Display and Select Column:src" dataDxfId="351"/><tableColumn id="41" xr3:uid="{B2C65460-A4E0-A340-BFA4-E6287331A5B3}" name="Referenced Table Display and Select Column" dataDxfId="350"/><tableColumn id="52" xr3:uid="{2BF52C4F-C41A-48F9-A0B1-82565B174F58}" name="Changeable" dataDxfId="349"><calculatedColumnFormula>IF(meta_Columns[[#This Row],[Excel Column - Excel Formula]]="","x","")</calculatedColumnFormula></tableColumn><tableColumn id="55" xr3:uid="{2BE28D52-EA0C-469A-B592-F2C9E6B6F804}" name="Excel Column - Name Prefix" dataDxfId="348"/><tableColumn id="56" xr3:uid="{A1AFBA24-E5F8-4960-925A-492F12DA3C5C}" name="Referenced Table Instance Class Name" dataDxfId="347"><calculatedColumnFormula>IF(meta_Columns[[#This Row],[Referenced Table:src]]="","",INDEX(meta_Tables[Instances Class],MATCH(meta_Columns[[#This Row],[Referenced Table:src]],meta_Tables[ID],0)))</calculatedColumnFormula></tableColumn><tableColumn id="42" xr3:uid="{4ACD9FB3-716D-41F9-B56B-10D55CF2D047}" name="Property ID from Actual Column Label" dataDxfId="346"><calculatedColumnFormula>IF(meta_Columns[[#This Row],[Property]]<>"","",
-    IF(meta_Columns[[#This Row],[Excel Column - Label Actual Subtype]]="",
-    INDEX(meta_Classifiers[Display Allways Qualified],MATCH(meta_Columns[[#This Row],[Owning Table Instances Class]],meta_Classifiers[ID],0)),
-    INDEX(meta_Classifiers[Display Allways Qualified],MATCH(camelCaseUpper(meta_Columns[[#This Row],[Excel Column - Label Actual Subtype]]),meta_Classifiers[Display],0)))
-
-    &"."&camelCaseLower(meta_Columns[[#This Row],[Excel Column - Label Actual Property Name]]))</calculatedColumnFormula></tableColumn><tableColumn id="51" xr3:uid="{D3240530-5921-4FC7-8CFA-08C30FAB1469}" name="Property:src" dataDxfId="345"/><tableColumn id="22" xr3:uid="{00000000-0010-0000-0400-000016000000}" name="Property" dataDxfId="344"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Columns[[#This Row],[Property:src]] ) = "", "",
-    INDEX( meta_TypedModelElements[Display Qualified], MATCH( meta_Columns[[#This Row],[Property:src]], meta_TypedModelElements[ID], 0 ) ) )</calculatedColumnFormula></tableColumn><tableColumn id="26" xr3:uid="{00000000-0010-0000-0400-00001A000000}" name="Semantics Case" dataDxfId="343"/><tableColumn id="13" xr3:uid="{00000000-0010-0000-0400-00000D000000}" name="Generalization 6" dataDxfId="342"><calculatedColumnFormula>INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 5]],meta_Classifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="29" xr3:uid="{00000000-0010-0000-0400-00001D000000}" name="Generalization 5" dataDxfId="341"><calculatedColumnFormula>INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 4]],meta_Classifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="28" xr3:uid="{00000000-0010-0000-0400-00001C000000}" name="Generalization 4" dataDxfId="340"><calculatedColumnFormula>INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 3]],meta_Classifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="21" xr3:uid="{00000000-0010-0000-0400-000015000000}" name="Generalization 3" dataDxfId="339"><calculatedColumnFormula>INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 2]],meta_Classifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="20" xr3:uid="{00000000-0010-0000-0400-000014000000}" name="Generalization 2" dataDxfId="338"><calculatedColumnFormula>INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 1]],meta_Classifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="16" xr3:uid="{00000000-0010-0000-0400-000010000000}" name="Generalization 1" dataDxfId="337"><calculatedColumnFormula>INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Owning Table Instances Class]],meta_Classifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="25" xr3:uid="{00000000-0010-0000-0400-000019000000}" name="Property Owning Class is Instance Class or Generalization" dataDxfId="336"><calculatedColumnFormula>_xlfn.IFNA(IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Owning Table Instances Class]],"x",
-    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 1]],TRUE,
-    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 2]],TRUE,
-    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 3]],TRUE,
-    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 4]],TRUE,
-    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 5]],TRUE,
-    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 6]],TRUE,FALSE
-    ))))))),FALSE)</calculatedColumnFormula></tableColumn><tableColumn id="35" xr3:uid="{00000000-0010-0000-0400-000023000000}" name="Is From Specialization 6" dataDxfId="335"><calculatedColumnFormula>_xlfn.IFNA(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
-    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)</calculatedColumnFormula></tableColumn><tableColumn id="34" xr3:uid="{00000000-0010-0000-0400-000022000000}" name="Is From Specialization 5" dataDxfId="334"><calculatedColumnFormula>_xlfn.IFNA(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
-    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)</calculatedColumnFormula></tableColumn><tableColumn id="33" xr3:uid="{00000000-0010-0000-0400-000021000000}" name="Is From Specialization 4" dataDxfId="333"><calculatedColumnFormula>_xlfn.IFNA(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
-    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)</calculatedColumnFormula></tableColumn><tableColumn id="32" xr3:uid="{00000000-0010-0000-0400-000020000000}" name="Is From Specialization 3" dataDxfId="332"><calculatedColumnFormula>_xlfn.IFNA(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
-    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)</calculatedColumnFormula></tableColumn><tableColumn id="31" xr3:uid="{00000000-0010-0000-0400-00001F000000}" name="Is From Specialization 2" dataDxfId="331"><calculatedColumnFormula>_xlfn.IFNA(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
-    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
-    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)</calculatedColumnFormula></tableColumn><tableColumn id="30" xr3:uid="{00000000-0010-0000-0400-00001E000000}" name="Is From Specialization 1" dataDxfId="330"><calculatedColumnFormula>_xlfn.IFNA(INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0))=meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)</calculatedColumnFormula></tableColumn><tableColumn id="24" xr3:uid="{00000000-0010-0000-0400-000018000000}" name="Property Owning Class is Specialization of Instance Class" dataDxfId="329"><calculatedColumnFormula>OR(meta_Columns[[#This Row],[Is From Specialization 1]],meta_Columns[[#This Row],[Is From Specialization 2]],meta_Columns[[#This Row],[Is From Specialization 3]],meta_Columns[[#This Row],[Is From Specialization 4]],meta_Columns[[#This Row],[Is From Specialization 5]],meta_Columns[[#This Row],[Is From Specialization 6]])</calculatedColumnFormula></tableColumn><tableColumn id="36" xr3:uid="{00000000-0010-0000-0400-000024000000}" name="Property Owning Class Name" dataDxfId="328"><calculatedColumnFormula>INDEX(meta_Classifiers[Name],MATCH(INDEX(meta_TypedModelElements[Property - Owning Class:src],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0)),meta_Classifiers[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="23" xr3:uid="{00000000-0010-0000-0400-000017000000}" name="Property Owning Class" dataDxfId="327"><calculatedColumnFormula>INDEX(meta_TypedModelElements[Property - Owning Class:src],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="12" xr3:uid="{00000000-0010-0000-0400-00000C000000}" name="Property Kind" dataDxfId="326"><calculatedColumnFormula>INDEX(meta_TypedModelElements[Kind:src],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="19" xr3:uid="{00000000-0010-0000-0400-000013000000}" name="Property Name" dataDxfId="325"><calculatedColumnFormula>INDEX(meta_TypedModelElements[Name or Type],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="27" xr3:uid="{00000000-0010-0000-0400-00001B000000}" name="Property Changeable" dataDxfId="324"><calculatedColumnFormula>INDEX(meta_TypedModelElements[Property - Changeable],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0))</calculatedColumnFormula></tableColumn><tableColumn id="7" xr3:uid="{00000000-0010-0000-0400-000007000000}" name="Position" dataDxfId="323"/><tableColumn id="37" xr3:uid="{00000000-0010-0000-0400-000025000000}" name="Stored Column Position" dataDxfId="322"/><tableColumn id="18" xr3:uid="{00000000-0010-0000-0400-000012000000}" name="Excel Column - Label from Property or Referenced Table" dataDxfId="321"><calculatedColumnFormula>meta_Columns[[#This Row],[Excel Column - Label Subtype Prefix]]&
-    IF(meta_Columns[[#This Row],[Property Name]]<>"",meta_Columns[[#This Row],[Property Name]],
-    IF(meta_Columns[[#This Row],[Excel Column - Name Prefix]]<>"", meta_Columns[[#This Row],[Excel Column - Name Prefix]]&" ","")  &
-    meta_Columns[[#This Row],[Referenced Table Instance Class Name]]) &
-    IF(AND(meta_Columns[[#This Row],[Referenced Table:src]]<>"",meta_Columns[[#This Row],[Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="display"),"",
-    IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="display"),"",
-    IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x"),IF(meta_Columns[[#This Row],[Semantics Case]]="","",":"&meta_Columns[[#This Row],[Semantics Case]]),
-    IF(AND(OR(meta_Columns[[#This Row],[Changeable]]="x",meta_Columns[[#This Row],[Property Changeable]]="x"),meta_Columns[[#This Row],[Semantics Case]]="src"),"",
-    IF(OR(meta_Columns[[#This Row],[Changeable]]="x",meta_Columns[[#This Row],[Property Changeable]]="x"),IF(meta_Columns[[#This Row],[Semantics Case]]="","",":"&meta_Columns[[#This Row],[Semantics Case]]),
-    IF(AND(meta_Columns[[#This Row],[Changeable]]<>"x",meta_Columns[[#This Row],[Property Changeable]]<>"x",meta_Columns[[#This Row],[Semantics Case]]="derive"),"",
-    IF(AND(meta_Columns[[#This Row],[Changeable]]<>"x",meta_Columns[[#This Row],[Property Changeable]]<>"x"),IF(meta_Columns[[#This Row],[Semantics Case]]="","",":"&meta_Columns[[#This Row],[Semantics Case]]),"TODO")))))))</calculatedColumnFormula></tableColumn><tableColumn id="54" xr3:uid="{BEAE76B9-3FBA-194A-AEE7-293AB8666AE4}" name="Excel Column - Label Subtype Prefix" dataDxfId="320"><calculatedColumnFormula xml:space="preserve"> IF(meta_Columns[[#This Row],[Property Owning Class is Specialization of Instance Class]],meta_Columns[[#This Row],[Property Owning Class Name]]&" - ","")</calculatedColumnFormula></tableColumn><tableColumn id="53" xr3:uid="{5F392C7A-6704-204E-878F-DECAEFC93B72}" name="Excel Column - Label from Property OLD Formula" dataDxfId="319"><calculatedColumnFormula>IF(meta_Columns[[#This Row],[Property Owning Class is Specialization of Instance Class]],meta_Columns[[#This Row],[Property Owning Class Name]]&" - ","")&meta_Columns[[#This Row],[Property Name]]&
-    IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="src"),":src",
-    IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="display"),"",
-    IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x"),":"&meta_Columns[[#This Row],[Semantics Case]],
-    IF(AND(meta_Columns[[#This Row],[Property Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="src"),"",
-    IF(AND(meta_Columns[[#This Row],[Property Changeable]]="x"),":"&meta_Columns[[#This Row],[Semantics Case]],
-    IF(AND(meta_Columns[[#This Row],[Property Changeable]]<>"x",meta_Columns[[#This Row],[Semantics Case]]="derive"),"",
-    IF(AND(meta_Columns[[#This Row],[Property Changeable]]<>"x"),":"&meta_Columns[[#This Row],[Semantics Case]],"TODO")))))))</calculatedColumnFormula></tableColumn><tableColumn id="47" xr3:uid="{F09CD71B-D776-49DF-9801-D7E8E7B50956}" name="Excel Column - Label Actual Property Name" dataDxfId="318"><calculatedColumnFormula>IFERROR(RIGHT(meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]],LEN(meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]])-FIND("-",
-    meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]])),meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]])</calculatedColumnFormula></tableColumn><tableColumn id="44" xr3:uid="{D7A0038E-47AF-42B7-BA9E-078DB4BC6DA2}" name="Excel Column - Label Actual Subtype" dataDxfId="317"><calculatedColumnFormula>IFERROR(LEFT(meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]],FIND("-",
-    meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]])-2),"")</calculatedColumnFormula></tableColumn><tableColumn id="43" xr3:uid="{5BC61B25-8F0A-4B96-8B32-00EBCB1C4C0B}" name="Excel Column - Label Actual without Semantic Case" dataDxfId="316"><calculatedColumnFormula>IFERROR(LEFT(meta_Columns[[#This Row],[Excel Column - Label Actual
-    (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]],FIND(":",meta_Columns[[#This Row],[Excel Column - Label Actual
-    (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]])-1),meta_Columns[[#This Row],[Excel Column - Label Actual
-    (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]])</calculatedColumnFormula></tableColumn><tableColumn id="6" xr3:uid="{3057A0C6-62FA-445B-B0A0-6B042E6FF7A9}" name="Excel Column - Label Actual Semantic Case" dataDxfId="315"><calculatedColumnFormula>IFERROR(RIGHT(meta_Columns[[#This Row],[Excel Column - Label Actual
-    (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]],LEN(meta_Columns[[#This Row],[Excel Column - Label Actual
-    (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]])-FIND(":",meta_Columns[[#This Row],[Excel Column - Label Actual
-    (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]])),"")</calculatedColumnFormula></tableColumn><tableColumn id="15" xr3:uid="{00000000-0010-0000-0400-00000F000000}" name="Excel Column - Label Actual_x000a_(formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)" dataDxfId="314"><calculatedColumnFormula>IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Classifiers",INDEX(meta_Classifiers[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::CodeTemplates",INDEX(meta_CodeTemplates[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Columns",INDEX(meta_Columns[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::DocumentVersions",INDEX(meta_DocumentVersions[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Literals",INDEX(meta_Literals[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::NonCapitalizedTitleWords",INDEX(#REF!,meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::PackageDocumentation",INDEX(meta_PackageDocumentation[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Rules",INDEX(meta_Rules[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::SimpleTestPattern",INDEX(meta_SimpleTestPattern[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Snippets",INDEX(#REF!,meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::TablePatterns",INDEX(meta_TablePatterns[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Tables",INDEX(meta_Tables[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::TypedModelElements",INDEX(meta_TypedModelElements[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="belowred::Table1Rows",INDEX(belowred_Table1Rows[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="belowred::Table2Rows",INDEX(belowred_Table2Rows[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="finance::Portfolios",INDEX(finance_Portfolios[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="finance::Positions",INDEX(finance_Positions[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="finance::Securities",INDEX(finance_Securities[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="myxyzpackage::MyXYZObjects",INDEX(myxyzpackage_MyXYZ_Objects[#Headers],meta_Columns[[#This Row],[Position]]),
-    IF(meta_Columns[[#This Row],[Owning Table:src]]="test::NewTable",INDEX(test_NewTable[#Headers],meta_Columns[[#This Row],[Position]]),
-    "TODO"))))))))))))))))))))</calculatedColumnFormula></tableColumn><tableColumn id="11" xr3:uid="{00000000-0010-0000-0400-00000B000000}" name="Label:backup:previous" dataDxfId="313"/><tableColumn id="46" xr3:uid="{72F9B8E6-EC9A-4F83-89CF-8F88F28F6218}" name="Display Qualified" dataDxfId="312"><calculatedColumnFormula>meta_Columns[[#This Row],[Owning Table]]&"."&meta_Columns[[#This Row],[Excel Column - Label]]</calculatedColumnFormula></tableColumn><tableColumn id="8" xr3:uid="{00000000-0010-0000-0400-000008000000}" name="Excel Column - Label Overwrite" dataDxfId="311"/><tableColumn id="17" xr3:uid="{00000000-0010-0000-0400-000011000000}" name="Excel Column - Label" dataDxfId="310"><calculatedColumnFormula>IF(TRIM(meta_Columns[[#This Row],[Excel Column - Label Overwrite]])<>"",meta_Columns[[#This Row],[Excel Column - Label Overwrite]],meta_Columns[[#This Row],[Excel Column - Label from Property or Referenced Table]])</calculatedColumnFormula></tableColumn><tableColumn id="38" xr3:uid="{00000000-0010-0000-0400-000026000000}" name="Excel Column - Explicit Excel Formula" dataDxfId="309"/><tableColumn id="39" xr3:uid="{00000000-0010-0000-0400-000027000000}" name="Excel Column - Excel Formula" dataDxfId="308"><calculatedColumnFormula>IF(meta_Columns[[#This Row],[Excel Column - Explicit Excel Formula]]="","",meta_Columns[[#This Row],[Excel Column - Explicit Excel Formula]])</calculatedColumnFormula></tableColumn><tableColumn id="57" xr3:uid="{C2776EE3-610F-C044-84D9-D4ECD4E36C59}" name="Excel Column - Validation Formula" dataDxfId="307"/><tableColumn id="2" xr3:uid="{C6EC425D-35C3-094D-B676-8DF67F65D351}" name="Excel Column - String Type" dataDxfId="306"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
+<table xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="xr xr3" xmlns:xr="http://schemas.microsoft.com/office/spreadsheetml/2014/revision" xmlns:xr3="http://schemas.microsoft.com/office/spreadsheetml/2016/revision3" id="14" xr:uid="{00000000-000C-0000-FFFF-FFFF04000000}" name="meta_Columns" displayName="meta_Columns" ref="A1:BE422" totalsRowShown="0" headerRowDxfId="367" dataDxfId="365" headerRowBorderDxfId="366" tableBorderDxfId="364" totalsRowBorderDxfId="363"><autoFilter ref="A1:BE422" xr:uid="{00000000-0009-0000-0100-00000E000000}"/>
+<tableColumns count="57">
+    <tableColumn id="1" xr3:uid="{00000000-0010-0000-0400-000001000000}" name="ID" dataDxfId="362"/>
+    <tableColumn id="49" xr3:uid="{6E72B505-24D7-4338-9A65-D70EFDFFC57B}" name="Kind:src" dataDxfId="361"/>
+    <tableColumn id="3" xr3:uid="{00000000-0010-0000-0400-000003000000}" name="Kind" dataDxfId="360"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Columns[[#This Row],[Kind:src]] ) = "", "",
+        INDEX( meta_Classifiers[Display Qualified], MATCH( meta_Columns[[#This Row],[Kind:src]], meta_Classifiers[ID], 0 ) ) )</calculatedColumnFormula></tableColumn>
+        <tableColumn id="4" xr3:uid="{00000000-0010-0000-0400-000004000000}" name="Package" dataDxfId="359"><calculatedColumnFormula>
+            IF(meta_Columns[[#This Row],[Owning Table:src]]="","",INDEX(meta_Classifiers[Package],MATCH(meta_Columns[[#This Row],[Owning Table Instances Class]],meta_Classifiers[ID],0)))
+        </calculatedColumnFormula></tableColumn>
+        <tableColumn id="5" xr3:uid="{00000000-0010-0000-0400-000005000000}" name="Sub Package" dataDxfId="358"/>
+        <tableColumn id="14" xr3:uid="{00000000-0010-0000-0400-00000E000000}" name="_Tables" dataDxfId="357"><calculatedColumnFormula>
+            INDEX(meta_Tables[Excel Table - Excel Name],MATCH(meta_Columns[[#This Row],[Owning Table:src]],meta_Tables[ID],0))
+        </calculatedColumnFormula></tableColumn>
+        <tableColumn id="10" xr3:uid="{00000000-0010-0000-0400-00000A000000}" name="Owning Table Instances Class" dataDxfId="356"><calculatedColumnFormula>
+            INDEX(meta_Tables[Instances Class:src],MATCH(meta_Columns[[#This Row],[Owning Table:src]],meta_Tables[ID],0))
+        </calculatedColumnFormula></tableColumn>
+        <tableColumn id="40" xr3:uid="{C54BA0C1-D44D-4CFE-B1CA-3F830A4C1A66}" name="Owning Table:src" dataDxfId="355"/>
+        <tableColumn id="9" xr3:uid="{00000000-0010-0000-0400-000009000000}" name="Owning Table" dataDxfId="354"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Columns[[#This Row],[Owning Table:src]] ) = "", "",
+        INDEX( meta_Tables[Display Qualified], MATCH( meta_Columns[[#This Row],[Owning Table:src]], meta_Tables[ID], 0 ) ) )</calculatedColumnFormula></tableColumn>
+            <tableColumn id="48" xr3:uid="{3D7A0EDF-AF51-40A8-8A98-34751314A8CC}" name="Referenced Table:src" dataDxfId="353"/>
+            <tableColumn id="45" xr3:uid="{B2BC55F0-4617-47EF-A1AE-AA473E4D6E63}" name="Referenced Table" dataDxfId="352"><calculatedColumnFormula>
+                IF(TRIM(meta_Columns[[#This Row],[Referenced Table:src]])="","",
+                INDEX(meta_Tables[Display Qualified],MATCH(meta_Columns[[#This Row],[Referenced Table:src]],meta_Tables[ID],0)))
+            </calculatedColumnFormula></tableColumn>
+            <tableColumn id="50" xr3:uid="{26D77C09-C15A-4576-B795-02A30483B8C0}" name="Referenced Table Display and Select Column:src" dataDxfId="351"/>
+            <tableColumn id="41" xr3:uid="{B2C65460-A4E0-A340-BFA4-E6287331A5B3}" name="Referenced Table Display and Select Column" dataDxfId="350"/>
+            <tableColumn id="52" xr3:uid="{2BF52C4F-C41A-48F9-A0B1-82565B174F58}" name="Changeable" dataDxfId="349"><calculatedColumnFormula>
+                IF(meta_Columns[[#This Row],[Excel Column - Excel Formula]]="","x","")
+            </calculatedColumnFormula></tableColumn>
+            <tableColumn id="55" xr3:uid="{2BE28D52-EA0C-469A-B592-F2C9E6B6F804}" name="Excel Column - Name Prefix" dataDxfId="348"/>
+            <tableColumn id="56" xr3:uid="{A1AFBA24-E5F8-4960-925A-492F12DA3C5C}" name="Referenced Table Instance Class Name" dataDxfId="347"><calculatedColumnFormula>
+                IF(meta_Columns[[#This Row],[Referenced Table:src]]="","",INDEX(meta_Tables[Instances Class],MATCH(meta_Columns[[#This Row],[Referenced Table:src]],meta_Tables[ID],0)))
+            </calculatedColumnFormula></tableColumn>
+            <tableColumn id="42" xr3:uid="{4ACD9FB3-716D-41F9-B56B-10D55CF2D047}" name="Property ID from Actual Column Label" dataDxfId="346"><calculatedColumnFormula>
+                IF(meta_Columns[[#This Row],[Property]]<>"","",
+                IF(meta_Columns[[#This Row],[Excel Column - Label Actual Subtype]]="",
+                INDEX(meta_Classifiers[Display Allways Qualified],MATCH(meta_Columns[[#This Row],[Owning Table Instances Class]],meta_Classifiers[ID],0)),
+                INDEX(meta_Classifiers[Display Allways Qualified],MATCH(camelCaseUpper(meta_Columns[[#This Row],[Excel Column - Label Actual Subtype]]),meta_Classifiers[Display],0)))
+                &"."&camelCaseLower(meta_Columns[[#This Row],[Excel Column - Label Actual Property Name]]))
+            </calculatedColumnFormula></tableColumn>
+            <tableColumn id="51" xr3:uid="{D3240530-5921-4FC7-8CFA-08C30FAB1469}" name="Property:src" dataDxfId="345"/>
+            <tableColumn id="22" xr3:uid="{00000000-0010-0000-0400-000016000000}" name="Property" dataDxfId="344"><calculatedColumnFormula xml:space="preserve"> IF( TRIM( meta_Columns[[#This Row],[Property:src]] ) = "", "",
+        INDEX( meta_TypedModelElements[Display Qualified], MATCH( meta_Columns[[#This Row],[Property:src]], meta_TypedModelElements[ID], 0 ) ) )</calculatedColumnFormula></tableColumn>
+                <tableColumn id="26" xr3:uid="{00000000-0010-0000-0400-00001A000000}" name="Semantics Case" dataDxfId="343"/>
+                <tableColumn id="13" xr3:uid="{00000000-0010-0000-0400-00000D000000}" name="Generalization 6" dataDxfId="342"><calculatedColumnFormula>
+                    INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 5]],meta_Classifiers[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="29" xr3:uid="{00000000-0010-0000-0400-00001D000000}" name="Generalization 5" dataDxfId="341"><calculatedColumnFormula>
+                    INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 4]],meta_Classifiers[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="28" xr3:uid="{00000000-0010-0000-0400-00001C000000}" name="Generalization 4" dataDxfId="340"><calculatedColumnFormula>
+                    INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 3]],meta_Classifiers[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="21" xr3:uid="{00000000-0010-0000-0400-000015000000}" name="Generalization 3" dataDxfId="339"><calculatedColumnFormula>
+                    INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 2]],meta_Classifiers[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="20" xr3:uid="{00000000-0010-0000-0400-000014000000}" name="Generalization 2" dataDxfId="338"><calculatedColumnFormula>
+                    INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Generalization 1]],meta_Classifiers[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="16" xr3:uid="{00000000-0010-0000-0400-000010000000}" name="Generalization 1" dataDxfId="337"><calculatedColumnFormula>
+                    INDEX(meta_Classifiers[Class - Generalization:src], MATCH(meta_Columns[[#This Row],[Owning Table Instances Class]],meta_Classifiers[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="25" xr3:uid="{00000000-0010-0000-0400-000019000000}" name="Property Owning Class is Instance Class or Generalization" dataDxfId="336"><calculatedColumnFormula>
+                    _xlfn.IFNA(IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Owning Table Instances Class]],"x",
+                    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 1]],TRUE,
+                    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 2]],TRUE,
+                    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 3]],TRUE,
+                    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 4]],TRUE,
+                    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 5]],TRUE,
+                    IF(meta_Columns[[#This Row],[Property Owning Class]]=meta_Columns[[#This Row],[Generalization 6]],TRUE,FALSE
+                    ))))))),FALSE)
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="35" xr3:uid="{00000000-0010-0000-0400-000023000000}" name="Is From Specialization 6" dataDxfId="335"><calculatedColumnFormula>
+                    _xlfn.IFNA(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
+                    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="34" xr3:uid="{00000000-0010-0000-0400-000022000000}" name="Is From Specialization 5" dataDxfId="334"><calculatedColumnFormula>
+                    _xlfn.IFNA(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
+                    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="33" xr3:uid="{00000000-0010-0000-0400-000021000000}" name="Is From Specialization 4" dataDxfId="333"><calculatedColumnFormula>
+                    _xlfn.IFNA(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
+                    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="32" xr3:uid="{00000000-0010-0000-0400-000020000000}" name="Is From Specialization 3" dataDxfId="332"><calculatedColumnFormula>
+                    _xlfn.IFNA(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
+                    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="31" xr3:uid="{00000000-0010-0000-0400-00001F000000}" name="Is From Specialization 2" dataDxfId="331"><calculatedColumnFormula>
+                    _xlfn.IFNA(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(
+                    INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0)),meta_Classifiers[ID],0))
+                    =meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="30" xr3:uid="{00000000-0010-0000-0400-00001E000000}" name="Is From Specialization 1" dataDxfId="330"><calculatedColumnFormula>
+                    _xlfn.IFNA(INDEX(meta_Classifiers[Class - Generalization:src],MATCH(meta_Columns[[#This Row],[Property Owning Class]],meta_Classifiers[ID],0))=meta_Columns[[#This Row],[Owning Table Instances Class]],FALSE)
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="24" xr3:uid="{00000000-0010-0000-0400-000018000000}" name="Property Owning Class is Specialization of Instance Class" dataDxfId="329"><calculatedColumnFormula>
+                    OR(meta_Columns[[#This Row],[Is From Specialization 1]],meta_Columns[[#This Row],[Is From Specialization 2]],meta_Columns[[#This Row],[Is From Specialization 3]],meta_Columns[[#This Row],[Is From Specialization 4]],meta_Columns[[#This Row],[Is From Specialization 5]],meta_Columns[[#This Row],[Is From Specialization 6]])
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="36" xr3:uid="{00000000-0010-0000-0400-000024000000}" name="Property Owning Class Name" dataDxfId="328"><calculatedColumnFormula>
+                    INDEX(meta_Classifiers[Name],MATCH(INDEX(meta_TypedModelElements[Property - Owning Class:src],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0)),meta_Classifiers[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="23" xr3:uid="{00000000-0010-0000-0400-000017000000}" name="Property Owning Class" dataDxfId="327"><calculatedColumnFormula>
+                    INDEX(meta_TypedModelElements[Property - Owning Class:src],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="12" xr3:uid="{00000000-0010-0000-0400-00000C000000}" name="Property Kind" dataDxfId="326"><calculatedColumnFormula>
+                    INDEX(meta_TypedModelElements[Kind:src],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="19" xr3:uid="{00000000-0010-0000-0400-000013000000}" name="Property Name" dataDxfId="325"><calculatedColumnFormula>
+                    INDEX(meta_TypedModelElements[Name or Type],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="27" xr3:uid="{00000000-0010-0000-0400-00001B000000}" name="Property Changeable" dataDxfId="324"><calculatedColumnFormula>
+                    INDEX(meta_TypedModelElements[Property - Changeable],MATCH(meta_Columns[[#This Row],[Property]],meta_TypedModelElements[ID],0))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="7" xr3:uid="{00000000-0010-0000-0400-000007000000}" name="Position" dataDxfId="323"/>
+                <tableColumn id="37" xr3:uid="{00000000-0010-0000-0400-000025000000}" name="Stored Column Position" dataDxfId="322"/>
+                <tableColumn id="18" xr3:uid="{00000000-0010-0000-0400-000012000000}" name="Excel Column - Label from Property or Referenced Table" dataDxfId="321"><calculatedColumnFormula>
+                    meta_Columns[[#This Row],[Excel Column - Label Subtype Prefix]]&
+                    IF(meta_Columns[[#This Row],[Property Name]]<>"",meta_Columns[[#This Row],[Property Name]],
+                    IF(meta_Columns[[#This Row],[Excel Column - Name Prefix]]<>"", meta_Columns[[#This Row],[Excel Column - Name Prefix]]&" ","")  &
+                    meta_Columns[[#This Row],[Referenced Table Instance Class Name]]) &
+                    IF(AND(meta_Columns[[#This Row],[Referenced Table:src]]<>"",meta_Columns[[#This Row],[Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="display"),"",
+                    IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="display"),"",
+                    IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x"),IF(meta_Columns[[#This Row],[Semantics Case]]="","",":"&meta_Columns[[#This Row],[Semantics Case]]),
+                    IF(AND(OR(meta_Columns[[#This Row],[Changeable]]="x",meta_Columns[[#This Row],[Property Changeable]]="x"),meta_Columns[[#This Row],[Semantics Case]]="src"),"",
+                    IF(OR(meta_Columns[[#This Row],[Changeable]]="x",meta_Columns[[#This Row],[Property Changeable]]="x"),IF(meta_Columns[[#This Row],[Semantics Case]]="","",":"&meta_Columns[[#This Row],[Semantics Case]]),
+                    IF(AND(meta_Columns[[#This Row],[Changeable]]<>"x",meta_Columns[[#This Row],[Property Changeable]]<>"x",meta_Columns[[#This Row],[Semantics Case]]="derive"),"",
+                    IF(AND(meta_Columns[[#This Row],[Changeable]]<>"x",meta_Columns[[#This Row],[Property Changeable]]<>"x"),IF(meta_Columns[[#This Row],[Semantics Case]]="","",":"&meta_Columns[[#This Row],[Semantics Case]]),"TODO")))))))
+                </calculatedColumnFormula></tableColumn>
+                <tableColumn id="54" xr3:uid="{BEAE76B9-3FBA-194A-AEE7-293AB8666AE4}" name="Excel Column - Label Subtype Prefix" dataDxfId="320"><calculatedColumnFormula xml:space="preserve"> IF(meta_Columns[[#This Row],[Property Owning Class is Specialization of Instance Class]],meta_Columns[[#This Row],[Property Owning Class Name]]&" - ","")</calculatedColumnFormula></tableColumn>
+                    <tableColumn id="53" xr3:uid="{5F392C7A-6704-204E-878F-DECAEFC93B72}" name="Excel Column - Label from Property OLD Formula" dataDxfId="319"><calculatedColumnFormula>
+                        IF(meta_Columns[[#This Row],[Property Owning Class is Specialization of Instance Class]],meta_Columns[[#This Row],[Property Owning Class Name]]&" - ","")&meta_Columns[[#This Row],[Property Name]]&
+                        IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="src"),":src",
+                        IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="display"),"",
+                        IF(AND(meta_Columns[[#This Row],[Property Kind]]="_Reference",meta_Columns[[#This Row],[Property Changeable]]="x"),":"&meta_Columns[[#This Row],[Semantics Case]],
+                        IF(AND(meta_Columns[[#This Row],[Property Changeable]]="x",meta_Columns[[#This Row],[Semantics Case]]="src"),"",
+                        IF(AND(meta_Columns[[#This Row],[Property Changeable]]="x"),":"&meta_Columns[[#This Row],[Semantics Case]],
+                        IF(AND(meta_Columns[[#This Row],[Property Changeable]]<>"x",meta_Columns[[#This Row],[Semantics Case]]="derive"),"",
+                        IF(AND(meta_Columns[[#This Row],[Property Changeable]]<>"x"),":"&meta_Columns[[#This Row],[Semantics Case]],"TODO")))))))
+                    </calculatedColumnFormula></tableColumn>
+                    <tableColumn id="47" xr3:uid="{F09CD71B-D776-49DF-9801-D7E8E7B50956}" name="Excel Column - Label Actual Property Name" dataDxfId="318"><calculatedColumnFormula>
+                        IFERROR(RIGHT(meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]],LEN(meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]])-FIND("-",
+                        meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]])),meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]])
+                    </calculatedColumnFormula></tableColumn>
+                    <tableColumn id="44" xr3:uid="{D7A0038E-47AF-42B7-BA9E-078DB4BC6DA2}" name="Excel Column - Label Actual Subtype" dataDxfId="317"><calculatedColumnFormula>
+                        IFERROR(LEFT(meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]],FIND("-",
+                        meta_Columns[[#This Row],[Excel Column - Label Actual without Semantic Case]])-2),"")
+                    </calculatedColumnFormula></tableColumn>
+                    <tableColumn id="43" xr3:uid="{5BC61B25-8F0A-4B96-8B32-00EBCB1C4C0B}" name="Excel Column - Label Actual without Semantic Case" dataDxfId="316"><calculatedColumnFormula>
+                        IFERROR(LEFT(meta_Columns[[#This Row],[Excel Column - Label Actual
+                        (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]],FIND(":",meta_Columns[[#This Row],[Excel Column - Label Actual
+                        (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]])-1),meta_Columns[[#This Row],[Excel Column - Label Actual
+                        (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]])
+                    </calculatedColumnFormula></tableColumn>
+                    <tableColumn id="6" xr3:uid="{3057A0C6-62FA-445B-B0A0-6B042E6FF7A9}" name="Excel Column - Label Actual Semantic Case" dataDxfId="315"><calculatedColumnFormula>
+                        IFERROR(RIGHT(meta_Columns[[#This Row],[Excel Column - Label Actual
+                        (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]],LEN(meta_Columns[[#This Row],[Excel Column - Label Actual
+                        (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]])-FIND(":",meta_Columns[[#This Row],[Excel Column - Label Actual
+                        (formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)]])),"")
+                    </calculatedColumnFormula></tableColumn>
+                    <tableColumn id="15" xr3:uid="{00000000-0010-0000-0400-00000F000000}" name="Excel Column - Label Actual_x000a_(formula calculated in meta_Tables "Excel Formula for Column Label Actual Calculation" column)" dataDxfId="314"><calculatedColumnFormula>
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Classifiers",INDEX(meta_Classifiers[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::CodeTemplates",INDEX(meta_CodeTemplates[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Columns",INDEX(meta_Columns[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::DocumentVersions",INDEX(meta_DocumentVersions[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Literals",INDEX(meta_Literals[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::NonCapitalizedTitleWords",INDEX(#REF!,meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::PackageDocumentation",INDEX(meta_PackageDocumentation[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Rules",INDEX(meta_Rules[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::SimpleTestPattern",INDEX(meta_SimpleTestPattern[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Snippets",INDEX(#REF!,meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::TablePatterns",INDEX(meta_TablePatterns[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::Tables",INDEX(meta_Tables[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="_meta::TypedModelElements",INDEX(meta_TypedModelElements[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="belowred::Table1Rows",INDEX(belowred_Table1Rows[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="belowred::Table2Rows",INDEX(belowred_Table2Rows[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="finance::Portfolios",INDEX(finance_Portfolios[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="finance::Positions",INDEX(finance_Positions[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="finance::Securities",INDEX(finance_Securities[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="myxyzpackage::MyXYZObjects",INDEX(myxyzpackage_MyXYZ_Objects[#Headers],meta_Columns[[#This Row],[Position]]),
+                        IF(meta_Columns[[#This Row],[Owning Table:src]]="test::NewTable",INDEX(test_NewTable[#Headers],meta_Columns[[#This Row],[Position]]),
+                        "TODO"))))))))))))))))))))
+                    </calculatedColumnFormula></tableColumn>
+                    <tableColumn id="11" xr3:uid="{00000000-0010-0000-0400-00000B000000}" name="Label:backup:previous" dataDxfId="313"/>
+                    <tableColumn id="46" xr3:uid="{72F9B8E6-EC9A-4F83-89CF-8F88F28F6218}" name="Display Qualified" dataDxfId="312"><calculatedColumnFormula>
+                        meta_Columns[[#This Row],[Owning Table]]&"."&meta_Columns[[#This Row],[Excel Column - Label]]
+                    </calculatedColumnFormula></tableColumn>
+                    <tableColumn id="8" xr3:uid="{00000000-0010-0000-0400-000008000000}" name="Excel Column - Label Overwrite" dataDxfId="311"/>
+                    <tableColumn id="17" xr3:uid="{00000000-0010-0000-0400-000011000000}" name="Excel Column - Label" dataDxfId="310"><calculatedColumnFormula>
+                        IF(TRIM(meta_Columns[[#This Row],[Excel Column - Label Overwrite]])<>"",meta_Columns[[#This Row],[Excel Column - Label Overwrite]],meta_Columns[[#This Row],[Excel Column - Label from Property or Referenced Table]])
+                    </calculatedColumnFormula></tableColumn>
+                    <tableColumn id="38" xr3:uid="{00000000-0010-0000-0400-000026000000}" name="Excel Column - Explicit Excel Formula" dataDxfId="309"/>
+                    <tableColumn id="39" xr3:uid="{00000000-0010-0000-0400-000027000000}" name="Excel Column - Excel Formula" dataDxfId="308"><calculatedColumnFormula>
+                        IF(meta_Columns[[#This Row],[Excel Column - Explicit Excel Formula]]="","",meta_Columns[[#This Row],[Excel Column - Explicit Excel Formula]])
+                    </calculatedColumnFormula></tableColumn>
+                    <tableColumn id="57" xr3:uid="{C2776EE3-610F-C044-84D9-D4ECD4E36C59}" name="Excel Column - Validation Formula" dataDxfId="307"/>
+                    <tableColumn id="2" xr3:uid="{C6EC425D-35C3-094D-B676-8DF67F65D351}" name="Excel Column - String Type" dataDxfId="306"/></tableColumns><tableStyleInfo name="TableStyleLight9" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0"/></table>
\ No newline at end of file
```
