-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
use hbtn_0d_tvshows;
select s.title,g.genre_id from tv_shows as s inner join tv_show_genres as g on s.id=g.show_id 
order by s.title asc,g.genre_id asc;

