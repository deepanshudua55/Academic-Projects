(: Name- Sarvesh Sadhoo :)
(: UTA ID- 1000980763 :)

for $person in doc("auction.xml")/site/people/person
let $category := $person/profile/interest/@category

for $cat in doc("auction.xml")/site/categories/category
let $xml := $cat

for $c in $xml/@id
where $category = $c
return {$person/name/text(),': ', <Category>{$cat/name/text()}</Category>, '&#xa;'}