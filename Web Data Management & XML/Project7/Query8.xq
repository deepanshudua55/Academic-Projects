(: Name- Sarvesh Sadhoo :)
(: UTA ID- 1000980763 :)

for $auction in doc("auction.xml")/site/open_auctions/open_auction
let $date3 := $auction/bidder[personref/@person="person3"]/date
let $time3 := $auction/bidder[personref/@person="person3"]/time
let $date6 := $auction/bidder[personref/@person="person3"]/date
let $time6 := $auction/bidder[personref/@person="person3"]/time


return if($date3 < $date6)
then {$auction/reserve}

else if($date3 = $date6)
	then(if($time3 < $time6)
	then {$auction/reserve}
	else()
	)

else()