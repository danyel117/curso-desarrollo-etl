create table recogidas_por_usuario as
select 
u.nombre,
sum(r.cantidad) as total
from recogida r
    join usuario u on r.id_usuario = u.id
group by u.nombre;


create table out_top5_usuarios as
select * from recogidas_por_usuario
order by total desc
limit 5;