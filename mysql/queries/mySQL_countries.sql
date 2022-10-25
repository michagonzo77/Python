-- 1 
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON languages.country_id = countries.id
WHERE language = "Slovene"
ORDER BY languages.percentage DESC;

-- 2 
SELECT countries.name, COUNT(cities.name) AS cities FROM cities
JOIN countries ON cities.country_id = countries.id
GROUP by countries.id
ORDER BY COUNT(cities.name) DESC;

-- 3  
SELECT cities.name, cities.population, cities.country_id FROM countries
JOIN cities ON cities.country_id = countries.id
WHERE cities.population > 500000 AND countries.name = "Mexico";

-- 4
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON languages.country_id = countries.id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

-- 5
SELECT countries.name, countries.surface_area, countries.population from countries
WHERE surface_area < 501 AND population > 100000; 

-- 6
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy from countries
WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75;

-- 7
SELECT countries.name, cities.name, cities.district, cities.population FROM countries
JOIN cities ON cities.country_id = countries.id
WHERE countries.name = "Argentina" AND cities.population > 500000;

-- 8
SELECT countries.region, COUNT(countries.name) AS number_of_countries FROM countries
GROUP by countries.region
ORDER BY COUNT(countries.name) DESC;