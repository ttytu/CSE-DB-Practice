import React from 'react';
import { Link } from 'react-router-dom';


const MovieCard = ({ movie }) => {
	const baseurl = "https://image.tmdb.org/t/p/w500";

	return (
		<Link to={"/movie/" + movie.movieId} className="snap-start shrink-0 relative group pb-8">
			<div className='h-full flex transition-all ease-in-out overflow-hidden'>
				<img src={baseurl + movie.poster_path} alt={movie.movieTitle} className="h-full object-cover group-hover:scale-105 transition-all ease-in-out" />
			</div>
			<h2 className="font-bold group-hover:text-slate-300 transition-colors">{movie.movieTitle}</h2>
		</Link>
	);
};

export default MovieCard;