create table recogidas_por_finca as
select
f.nombre as finca,
sum(r.cantidad) as cantidad_total
from recogida r
    join lote l on r.id_lote = l.id
    join finca f on l.id_finca = f.id
group by f.nombre;

create table tamano_finca as
select 
f.nombre as finca,
count(l.id)  * 4 as hectareas
from finca f
    join lote l on l.id_finca = f.id
group by f.nombre;

create table out_recogidas_por_hectarea as
select 
rf.finca,
rf.cantidad_total / tf.hectareas as cantidad_por_hectarea
from recogidas_por_finca rf
    join tamano_finca tf
        on tf.finca = rf.finca;