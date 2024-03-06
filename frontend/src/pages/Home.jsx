import React from 'react';
import { useEffect, useState } from 'react';

import MovieCarousel from '../components/MovieCarousel';


const Home = () => {
	const [movies, setMovies] = useState([]);
	useEffect(() => {
		async function fetchMovies() {
			try {
				const response = await fetch('http://localhost:8000/v1/movie');
				const data = await response.json();
				setMovies(data);
				// Process the movie list data here
			} catch (error) {
				// Handle any errors that occur during the fetch request
			}
		}

		fetchMovies();
	}, []);

	return (
		<div className="w-full grid grid-cols-1 gap-4">
			<h1 className="text-2xl font-bold">Welcome to the Home Page!</h1>
			<MovieCarousel movies={movies} />
			<MovieCarousel movies={movies} />
			<MovieCarousel movies={movies} />
		</div>
	);
};

export default Home;