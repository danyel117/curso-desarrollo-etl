create table recogidas_por_cultivo as
select
c.nombre,
sum(r.cantidad) as total
from recogida r
    join lote l on r.id_lote = l.id
    join cultivo c on l.id_cultivo = c.id
group by c.nombre;


create table out_top5_cultivos as
select * from recogidas_por_cultivo
order by total desc
limit 5;