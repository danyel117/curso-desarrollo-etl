create table gasto_por_cc as
select
cc.codigo as centro_de_costos,
sum(oc.total) as total
from orden_de_compra oc
    join centro_de_costos cc
        on oc.centroDeCostosId = cc.id
group by cc.codigo;

create table out_gasto_por_cc as
select * from gasto_por_cc
order by total desc;