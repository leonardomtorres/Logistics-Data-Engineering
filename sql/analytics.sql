-- 1. Lucro total por tipo de veículo
-- Mostra qual meio de transporte é mais rentável
SELECT 
    vehicle, 
    SUM(lucro) AS lucro_total
FROM fato_entrega
GROUP BY vehicle
ORDER BY lucro_total DESC;

-- 2. Média de tempo de entrega por condição climática
-- Ajuda a entender o impacto do clima na operação
SELECT 
    weather, 
    AVG(delivery_time) AS tempo_medio
FROM fato_entrega
GROUP BY weather
ORDER BY tempo_medio ASC;

-- 3. Performance dos agentes (Rating) por tipo de tráfego
SELECT 
    traffic, 
    AVG(agent_rating) AS avaliacao_media
FROM fato_entrega
GROUP BY traffic;

-- 4. Volume de entregas por categoria de produto
SELECT 
    category, 
    COUNT(*) AS total_pedidos
FROM fato_entrega
GROUP BY category
ORDER BY total_pedidos DESC;