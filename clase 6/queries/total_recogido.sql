select 
f.nombre as finca,
c.nombre as cultivo,
strftime('%Y-%m', r.fecha) as mes,
sum(r.cantidad) as cantidad_recogida
from recogidas r
    join lotes l
        on r.id_lote = l.id
    join fincas f
        on l.id_finca = f.id
    join cultivos c
        on l.id_cultivo = c.id
group by f.nombre, c.nombre, strftime('%Y-%m', r.fecha)