select
cultivo,
sum(ingreso) as total_ingreso    
from ingreso_mes_cultivo_finca
group by cultivo