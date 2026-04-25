use ankur;

CREATE TABLE t_shirts (
    brand VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    color VARCHAR(50) NOT NULL,
    size VARCHAR(10) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (brand, color, size)
);

INSERT INTO t_shirts (brand, name, color, size, price, quantity) VALUES
('Nike', 'Dri-Fit Classic', 'Black', 'S', 29.99, 50),
('Nike', 'Dri-Fit Classic', 'Black', 'M', 29.99, 45),
('Nike', 'Dri-Fit Classic', 'White', 'L', 29.99, 35),
('Nike', 'Dri-Fit Classic', 'Blue', 'XL', 29.99, 25),
('Adidas', 'Essential Tee', 'Black', 'S', 24.99, 60),
('Adidas', 'Essential Tee', 'Red', 'M', 24.99, 55),
('Adidas', 'Essential Tee', 'Blue', 'L', 24.99, 40),
('Adidas', 'Essential Tee', 'White', 'XL', 24.99, 30),
('Puma', 'Essentials', 'Black', 'S', 22.99, 70),
('Puma', 'Essentials', 'Gray', 'M', 22.99, 65),
('Puma', 'Essentials', 'Green', 'L', 22.99, 50),
('Puma', 'Essentials', 'Navy', 'XL', 22.99, 35),
('Calvin Klein', 'Cotton Stretch', 'Black', 'M', 39.99, 40),
('Calvin Klein', 'Cotton Stretch', 'White', 'L', 39.99, 38),
('Calvin Klein', 'Cotton Stretch', 'Gray', 'XL', 39.99, 32),
('Tommy Hilfiger', 'Classic Fit', 'Blue', 'S', 34.99, 45),
('Tommy Hilfiger', 'Classic Fit', 'Red', 'M', 34.99, 42),
('Tommy Hilfiger', 'Classic Fit', 'White', 'L', 34.99, 38);

INSERT INTO t_shirts (brand, name, color, size, price, quantity) VALUES
('Levi', 'Graphic Tee', 'Black', 'M', 27.99, 55),
('Levi', 'Graphic Tee', 'Navy', 'L', 27.99, 48);

ALTER TABLE t_shirts ADD COLUMN shirt_id INT AUTO_INCREMENT UNIQUE FIRST;

CREATE TABLE discount (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    t_shirt_id INT NOT NULL,
    discount_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (t_shirt_id) REFERENCES t_shirts(shirt_id)
);

INSERT INTO discount (t_shirt_id, discount_amount) VALUES
(1, 5.00),
(2, 3.50),
(3, 4.00),
(4, 6.00),
(5, 2.50),
(6, 3.00),
(7, 2.00),
(8, 4.50),
(9, 2.00),
(10, 3.50),
(11, 2.50),
(12, 4.00),
(13, 8.00),
(14, 7.50),
(15, 9.00),
(16, 5.50),
(17, 6.00),
(18, 4.50),
(19, 3.50),
(20, 5.00);

select * from ankur.t_shirts;

select * from ankur.discount;
