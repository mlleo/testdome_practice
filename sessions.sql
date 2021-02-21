SELECT userID, avg(duration)
FROM sessions
GROUP BY userid
having count(userId) >1
