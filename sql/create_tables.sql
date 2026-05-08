CREATE TABLE fato_entrega (
    order_id VARCHAR(50) PRIMARY KEY,
    agent_age INTEGER,
    agent_rating NUMERIC,
    order_date DATE,
    weather VARCHAR(50),
    traffic VARCHAR(50),
    vehicle VARCHAR(50),
    area VARCHAR(50),
    delivery_time_min INTEGER, -- Tempo que levou a entrega
    category VARCHAR(50)
);