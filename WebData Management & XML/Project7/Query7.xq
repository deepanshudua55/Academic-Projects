(: Name- Sarvesh Sadhoo :)
(: UTA ID- 1000980763 :)

for $item at $i in doc("auction.xml")/site/regions/*/item
order by $item/name
return (<Name>{$item/name/text()}</Name> | <Location>{$item/location/text()}</Location>, '&#xa;')
