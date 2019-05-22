ELECT DISTINCT Customer.FirstName || ' ' || 
	Customer.LastName as FullName, Customer.Phone
FROM Customer
INNER JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
WHERE Customer.City in 
	(SELECT Customer.City
	FROM Customer
	GROUP by Customer.City
	HAVING count(Customer.City) > 1)
ORDER BY Customer.City;

SELECT City
FROM Customer, Invoice
WHERE Customer.CustomerId = Invoice.CustomerId
GROUP BY City
ORDER BY SUM(Total) DESC
LIMIT 3;

SELECT T1.Name Genre, Track.Name Track, Album.Title, Artist.Name Artist
FROM Track, Album, Artist, (SELECT Genre.GenreId, Genre.Name
	FROM Track
	INNER JOIN Genre ON Genre.GenreId = Track.GenreId
	INNER JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
	GROUP BY Track.GenreId
	ORDER BY count(Track.GenreId) DESC
	LIMIT 1) T1
WHERE Track.AlbumId = Album.AlbumId
AND Album.ArtistId = Artist.ArtistId
AND Track.GenreId = T1.GenreId
ORDER BY Artist.Name
