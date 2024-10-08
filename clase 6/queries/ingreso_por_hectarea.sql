select 
i.finca,
i.total_ingreso / h.hectareas as ingreso_por_hectarea
from ingreso_por_finca i
    join hectareas_por_finca h
        on h.finca = i.finca
