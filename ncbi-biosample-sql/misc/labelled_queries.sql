-- attribute names per harmonized names
select
	hn,
	count(1) as count
from
	(
	select
		distinct harmonized_name hn,
		attribute_name
	from
		all_attribs aa
	where
		harmonized_name is not null
		and harmonized_name != '') as raw
group by
	hn
order by
	count(1) desc
;

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
