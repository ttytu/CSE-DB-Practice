import React from 'react';
import MovieCard from './MovieCard';


const MovieCarousel = ({ movies }) => {
	return (
		<div className="flex flex-nowrap gap-2 overflow-x-scroll shrink-0 snap-x">
			{movies.map((movie) => (
				<MovieCard key={movie.movieId} movie={movie} />
			))}
		</div>
	);
};

export default MovieCarousel;