select
f.nombre as finca,
count(l.id) * 4 as hectareas
from fincas f
    join lotes l
        on l.id_finca = f.id
group by f.nombre