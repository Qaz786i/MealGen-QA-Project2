CREATE TABLE IF NOT EXISTS results (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    main_dish VARCHAR(30) NOT NULL,
    side_dish VARCHAR(30) NOT NULL,
    price_main INT NOT NULL,
    price_side INT NOT NULL,
    total_price INT NOT NULL
);