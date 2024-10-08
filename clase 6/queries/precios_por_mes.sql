select 
c.nombre as cultivo,
strftime('%Y-%m', p.fecha) as mes,
avg(p.valor) as precio_promedio
from precios p
    join cultivos c
        on p.id_cultivo = c.id
group by c.nombre, strftime('%Y-%m', p.fecha)