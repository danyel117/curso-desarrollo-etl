select 
tr.finca,
tr.cultivo,
tr.mes,
tr.cantidad_recogida,
ppm.precio_promedio,
ppm.precio_promedio * tr.cantidad_recogida as ingreso
from precios_por_mes ppm
    join total_recogido tr
        on ppm.cultivo = tr.cultivo and ppm.mes = tr.mes