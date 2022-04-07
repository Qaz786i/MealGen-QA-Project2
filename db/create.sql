CREATE TABLE IF NOT EXISTS make_meal (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    main VARCHAR(30) NOT NULL,
    side VARCHAR(30) NOT NULL,
    price_main INT NOT NULL,
    price_side INT NOT NULL,
    total_price INT NOT NULL
);