(: Name- Sarvesh Sadhoo :)
(: UTA ID- 1000980763 :)

for $x in doc("auction.xml")/site/regions
return <ItemSum>{count($x//item)}</ItemSum>