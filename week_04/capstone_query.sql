/* Name: Kidus Tesema 
Category/Vendor of Choice: Pernod Ricard
*/
SELECT DISTINCT vendor
FROM sales
WHERE vendor ILIKE '%Pernod%';

-- 1. Create a list of all transactions for your chosen [Category/Vendor] that took place in
-- the last quarter of 2014, sorted by the total sale amount from highest to lowest.
-- (Strength: Identifying high-volume peak periods).

SELECT *
FROM sales
WHERE vendor = 'Pernod Ricard USA/Austin Nichols'
  AND date BETWEEN '2014-10-01' AND '2014-12-31'
ORDER BY total DESC;

-- 2. Which transactions for your [Category/Vendor] had a bottle quantity greater than 12?
-- Display the date, store number, item description, and total amount.
-- (Strength: Identifying bulk buyers or wholesale-style transactions).

SELECT *
FROM sales
WHERE vendor = 'Pernod Ricard USA/Austin Nichols'
  AND bottle_qty > 12
ORDER BY bottle_qty DESC, total DESC;


-- 3. Find all products in the products_table whose item_description contains a specific
-- keyword (e.g., 'Limited', 'Spiced'). What categories do they belong to?
-- (Opportunity: Identifying niche product variants).

SELECT *
FROM products
WHERE vendor_name ILIKE '%Pernod%'
  AND item_description ILIKE '%Limited%'
ORDER BY category_name, item_description;

-- Aggregation--
-- 4. What is the total sales revenue and the average bottle price (btl_price) for
-- your chosen [Category/Vendor]?
-- (Strength/Baseline: Establishing the financial footprint).

SELECT
    vendor,
    SUM(total) AS total_sales_revenue,
    AVG(btl_price) AS average_bottle_price
FROM sales
WHERE vendor = 'Pernod Ricard USA/Austin Nichols'
GROUP BY vendor;

---els teqnique

SELECT
    SUM(total::numeric) AS total_sales_revenue,
    AVG(btl_price::numeric) AS average_bottle_price
FROM sales
WHERE vendor ILIKE 'Pernod Ricard USA/Austin Nichols';

-- 5. How many transactions were recorded for each specific item description within your
-- chosen [Category]? Which specific product is the most frequently purchased?
-- (Strength: Identifying your "hero" product).

SELECT
    description AS item_description,
    COUNT(*) AS transaction_count,
    SUM(bottle_qty) AS total_bottles_sold
FROM sales
WHERE vendor = 'Pernod Ricard USA/Austin Nichols'
GROUP BY description
ORDER BY transaction_count DESC;

-- 6. Which store generated the highest total revenue for your [Category/Vendor]?
-- Which generated the lowest (but still greater than zero)?
-- (Strength vs. Weakness: Identifying your best and worst retail partners).

SELECT
    store,
    SUM(REPLACE(REPLACE(total::text, '$', ''), ',', '')::numeric) AS total_revenue
FROM sales
WHERE vendor = 'Pernod Ricard USA/Austin Nichols'
GROUP BY store
ORDER BY total_revenue DESC
LIMIT 1;


-- 7. What is the total revenue for every vendor within your chosen [Category],
-- sorted from highest to lowest?
-- (Threat: Identifying your top competitors in that space).

SELECT
    vendor,
    SUM(REPLACE(REPLACE(total::text, '$', ''), ',', '')::numeric) AS total_revenue
FROM sales
WHERE category_name = 'IMPORTED VODKA'
GROUP BY vendor
ORDER BY total_revenue DESC;


-- 8. Which stores had total sales revenue for your [Category/Vendor] exceeding $2,000?
-- (Hint: Use HAVING to filter aggregated store totals).
-- (Strength: Pinpointing high-performing retail locations.

SELECT
    store,
    SUM(total::numeric) AS total_sales_revenue
FROM sales
WHERE vendor = 'Pernod Ricard USA/Austin Nichols'
GROUP BY store
HAVING SUM(total::numeric) > 2000
ORDER BY total_sales_revenue DESC;


-- Joins
-- 9. Find all sales records where the category_name is either your chosen category
-- or a closely related competitor category (e.g., 'VODKA 80 PROOF' vs 'IMPORTED VODKA').
-- (Threat: Comparing performance against direct substitutes).

SELECT
    s.date,
    s.store,
    st.name AS store_name,
    s.vendor,
    p.item_description,
    p.category_name,
    s.bottle_qty,
    s.btl_price,
    s.total
FROM sales s
JOIN products p
    ON s.item = p.item_no
JOIN stores st
    ON s.store = st.store
WHERE s.vendor = 'Pernod Ricard USA/Austin Nichols'
  AND p.category_name IN ('IMPORTED VODKA', 'VODKA 80 PROOF')
ORDER BY p.category_name, s.total DESC;


-- 10. List all transactions where the state bottle cost was between $10 and $20 for
-- your [Category/Vendor].
-- (Opportunity: Analyzing performance in the "mid-tier" price bracket).

SELECT *
FROM sales s
JOIN products p
    ON s.item = p.item_no
JOIN stores st
    ON s.store = st.store
WHERE s.vendor = 'Pernod Ricard USA/Austin Nichols'
  AND s.state_btl_cost BETWEEN 10 AND 20
ORDER BY s.state_btl_cost, s.total DESC;


--eroor 
SELECT *
FROM sales s
JOIN products p
    ON s.item = p.item_no
JOIN stores st
    ON s.store = st.store
WHERE s.vendor = 'Pernod Ricard USA/Austin Nichols'
  AND CASE
        WHEN s.state_btl_cost BETWEEN '$10.00' AND '$20.00' THEN TRUE
        ELSE FALSE
      END
ORDER BY s.state_btl_cost, s.total DESC;
-- 11. Write a query that displays each store's total sales for your [Category/Vendor]
-- along with the store's name and address from the stores_table.
-- (Strength: Mapping your physical sales footprint).

SELECT
    st.name AS store_name,
    st.store_address,
    SUM(s.total) AS total_sales
FROM sales s
JOIN stores st
    ON s.store = st.store
WHERE s.vendor = 'Pernod Ricard USA/Austin Nichols'
GROUP BY
    st.name,
    st.store_address
ORDER BY total_sales DESC;


-- 12. For each sale in your [Category], display the transaction date, total amount,
-- and the population of the county where the sale occurred by joining with counties_table.
-- (Opportunity: Correlating sales volume with population density).

SELECT
    s.date,
    s.total,
    s.county,
    c.population
FROM sales s
JOIN counties c
    ON s.county = c.county
WHERE s.vendor = 'Pernod Ricard USA/Austin Nichols'
ORDER BY s.date;


-- 13. Write a query that shows total sales for your [Category/Vendor] by county.
-- Which county generates the most revenue for you?
-- (Strength: Identifying your geographic stronghold).


SELECT
    s.county,
    c.population,
    SUM(s.total) AS total_sales
FROM sales s
JOIN counties c
    ON s.county = c.county
WHERE s.vendor = 'Pernod Ricard USA/Austin Nichols'
GROUP BY
    s.county,
    c.population
ORDER BY total_sales DESC
LIMIT 1;

-- 14. Join the sales_table and products_table to show total revenue for your [Vendor]
-- alongside the proof and pack size of the items.
-- (Strength: Determining if higher proof or larger packs drive more revenue).

SELECT
    p.proof,
    p.pack,
    SUM(s.total) AS total_revenue
FROM sales s
JOIN products p
    ON s.item = p.item_no
WHERE s.vendor = 'Pernod Ricard USA/Austin Nichols'
GROUP BY
    p.proof,
    p.pack
ORDER BY total_revenue DESC;


-- 15. Are there any counties in the counties_table that have a population over 10,000
-- but zero sales for your [Category/Vendor]?
-- (Opportunity: Identifying untapped markets).

SELECT
    c.county,
    c.population,
    COUNT(s.*) AS sales_count
FROM counties c
LEFT JOIN sales s
    ON c.county = s.county
   AND s.vendor = 'Pernod Ricard USA/Austin Nichols'
WHERE c.population > 10000
GROUP BY
    c.county,
    c.population
HAVING COUNT(s.*) = 0
ORDER BY c.population DESC;
--check 
SELECT
    c.county,
    c.population,
    COUNT(s.store) AS sales_count
FROM counties c
LEFT JOIN sales s
    ON c.county = s.county
   AND s.vendor = 'Pernod Ricard USA/Austin Nichols'
WHERE c.population > 10000
GROUP BY c.county, c.population
ORDER BY sales_count ASC;


-- 16. Display total revenue for your [Category/Vendor] grouped by the store_status
-- (from stores_table). Are active stores ('A') performing significantly better than others?
-- (Threat: Assessing the risk of sales tied to inactive or closed locations).

SELECT
    st.store_status,
    COUNT(DISTINCT s.store) AS number_of_stores,
    COUNT(*) AS transaction_count,
    SUM(s.total) AS total_revenue
FROM sales s
JOIN stores st
    ON s.store = st.store
WHERE s.vendor = 'Pernod Ricard USA/Austin Nichols'
GROUP BY st.store_status
ORDER BY total_revenue DESC;



-- Subqueries
-- 17. Using a subquery, find all transactions for your [Category/Vendor] from stores
-- located in a specific high-growth city (e.g., 'Des Moines') found in the stores_table.
-- (Opportunity: Drilling down into urban market performance).
SELECT *
FROM sales
WHERE vendor = 'Pernod Ricard USA/Austin Nichols'
  AND store IN (
      SELECT store
      FROM stores
      WHERE store_address::text ILIKE '%Des Moines%'
         OR address_info::text ILIKE '%Des Moines%'
  )
ORDER BY total DESC;



-- 18. Which stores had total sales for your [Category/Vendor] that were above the
-- average store revenue for that same group? (Hint: Use a subquery for the average).
-- (Strength: Identifying stores that are over-performing).




-- 19. Find the top 5 highest-grossing items for your [Vendor], then use a subquery
-- to look up their full details (like case_cost and proof) from the products_table.
-- (Strength: Deep-dive into the specs of your most profitable inventory).




-- 20. Write a query using a subquery to find all sales records for your [Category]
-- from stores that have an 'A' (Active) status in the stores_table.
-- (Strength: Filtering for reliable, ongoing revenue streams).
