-- usage counts of harmonized names
select
	harmonized_name ,
	count(1) as count
from
	all_attribs aa
group by
	harmonized_name
order by
	count(1) desc;