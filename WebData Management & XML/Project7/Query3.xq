(: Name- Sarvesh Sadhoo :)
(: UTA ID- 1000980763 :)
(: Reference:-> http://my.zorba-xquery.com/doc/zorba-0.9.8/zorba/html/groupby.html :)

for $buyer in doc("auction.xml")/site/closed_auctions/closed_auction
let $personname := $buyer/buyer/@person

group by $personname
let $person := doc("auction.xml")/site/people/person[@id=$personname]/name
let $quantity := sum($buyer/quantity)
return(<PersonName>{$person/text()}</PersonName>, ':', $quantity, '&#xa;')
