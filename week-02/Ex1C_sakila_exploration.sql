/*
a) The actor table contains information about actors, including actor_id, first_name, last_name, and last_update.

b) The film table contains information about movies, including film_id, title, description, release_year, rental_rate, length, rating, and last_update.

c) The table that contains both actor_id and film_id is the film_actor table.

d) The rental table contains information about movie rentals, including rental_id, rental_date, inventory_id, customer_id, return_date, and staff_id. The information is somewhat hard to read because it uses IDs instead of descriptive names, requiring joins with other tables.

e) The inventory table contains information about copies of films available in stores, including inventory_id, film_id, store_id, and last_update.

f) To find the names of all films rented on a specific date, we need to use the rental, inventory, and film tables. The rental table links to inventory through inventory_id, and inventory links to film through film_id. This relationship allows us to retrieve film titles based on rental activity.
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;
