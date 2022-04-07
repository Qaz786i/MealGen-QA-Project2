CREATE TABLE IF NOT EXISTS make_meal (
    id INT PRIMARY KEY AUTO_INCREMENT,
    main VARCHAR(500) NOT NULL,
    side VARCHAR(200) NOT NULL,
    price_main INT NOT NULL,
    price_side INT NOT NULL,
    total_price INT NOT NULL
);