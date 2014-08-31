(: Name- Sarvesh Sadhoo :)
(: UTA ID- 1000980763 :)

for $z in doc("auction.xml")/site/regions
let $item := $z/europe/item/@id

for $x in doc("auction.xml")/site/closed_auctions
let $xml := $x

for $c in $xml/closed_auction
let $itemid := $c/itemref/@item
where $item = $itemid
let $person := $c/buyer
let $pername := doc("auction.xml")/site/people/person[@id=$person/@person]/name
let $itemname := doc("auction.xml")/site/regions/europe/item[@id = $itemid]/name
return {$pername/text(), ': ', <ItemName>{$itemname/text()}</ItemName>, '&#xa;'}


