import React from 'react';


const MovieCard = ({ movie }) => {
	const baseurl = "https://image.tmdb.org/t/p/w500";

	return (
		<div className="snap-start shrink-0 h-[350px] relative group pb-2">
			<div className='h-full flex flex-col'>
				<img src={baseurl + movie.poster_path} alt={movie.movieTitle} className="h-4/5 object-cover" />
				<h2 className="font-bold">{movie.movieTitle}</h2>
			</div>
		</div>
	);
};

export default MovieCard;