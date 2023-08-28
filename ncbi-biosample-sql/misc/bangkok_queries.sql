select
	attribute_name ,
	count(1) as row_count
from
	all_attribs aa
where
	attribute_name like '%16%'
group by
	attribute_name
order by
	count(1) desc ;

select
	value,
	count(1) as val_count
from
	all_attribs aa
where
	attribute_name = '16S recovered'
group by
	value
order by
	count(1) desc ;

select
	*
from
	all_attribs aa
where
	attribute_name = '16S recovered' ;





select
	attribute_name,
	count(1) as count
from
	all_attribs aa
where
	harmonized_name = 'geo_loc_name'
group by
	attribute_name
order by
	count(1) desc ;

select
	value ,
	count(1)
from
	all_attribs aa
where
	harmonized_name = 'geo_loc_name'
group by
	value
order by
	count(1) desc;

select
	package_name ,
	count(1)
from
	non_attribute_metadata nam
group by
	package_name
order by
	count(1) desc;

select
	count(1)
from
	harmonized_wide hw ;

select
	aa.attribute_name ,
	count(1)
from
	non_attribute_metadata nam
join all_attribs aa on
	aa.raw_id = nam.raw_id
where
	nam.package = 'MIMS.me.host-associated.6.0'
	and aa.harmonized_name = 'geo_loc_name'
group by
	aa.attribute_name
order by
	count(1) desc;

select
	value,
	count(1)
from
	non_attribute_metadata nam
join all_attribs aa on
	aa.raw_id = nam.raw_id
where
	package = 'MIMS.me.host-associated.6.0'
	and aa.harmonized_name = 'collection_date'
	and value not like '____-__-__'
group by
	value
order by
	count(1) desc ;


--group by
--	package 
--order by
--	count(1);

select
	count(1)
from
	all_attribs aa
where
	attribute_name = 'PAR';

