import React from 'react';
import MovieCard from './MovieCard';


const MovieGrid = ({ movies }) => {
	return (
		<div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2">
			{movies.map((movie) => (
				<MovieCard key={movie.movieId} movie={movie} />
			))}
		</div>
	);
};

export default MovieGrid;