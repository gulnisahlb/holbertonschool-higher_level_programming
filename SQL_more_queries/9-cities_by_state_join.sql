-- hello
SELECT cities.id,cities.name,states.name
FROM cities,states
WHERE cities.states_id = states_id
ORDER BY cities_id ASC;
