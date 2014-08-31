(: Name- Sarvesh Sadhoo :)
(: UTA ID- 1000980763 :)

for $item at $i in doc("auction.xml")/site/regions/europe/item
return (<ItemName>{$item/name/text()}</ItemName> , {$item/description},'&#10;')

