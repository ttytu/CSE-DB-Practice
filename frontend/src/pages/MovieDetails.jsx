import React from 'react';
import { useState, useEffect } from 'react';

import Banner from '../components/Banner';
import MovieSlider from '../components/MovieSlider';


const MovieDetails = ({ movieId }) => {
	const baseurl = "https://image.tmdb.org/t/p/original";
	const [movie, setMovie] = useState({});

	useEffect(() => {
		const fetchMovie = async () => {
			try {
				const response = await fetch(`http://localhost:8000/v1/movie/${movieId}`);
				const movie = await response.json();
				setMovie(movie);
				console.log('movie:', movie);
				// TODO: Handle movie data
			} catch (error) {
				console.error('Error fetching movie:', error);
			}
		};
		console.log('movieId:', movieId);
		fetchMovie();
	}, [movieId]);

	const [relatedMovies, setrelatedMovies] = useState([]);
	useEffect(() => {
		async function fetchMovies() {
			try {
				const response = await fetch('http://localhost:8000/v1/movie');
				const data = await response.json();
				setrelatedMovies(data);
				// Process the movie list data here
			} catch (error) {
				// Handle any errors that occur during the fetch request
			}
		}

		fetchMovies();
	}, []);

	return (
		<div className="">
			<Banner imgsrc={baseurl + movie.backdrop_path} />

			<div className='max-w-screen-lg mx-auto grid grid-cols-1 gap-10 px-4 lg:px-0'>
				<div className='grid grid-cols-1 gap-4'>
					<h1 className="text-2xl font-bold">{movie.movieTitle}</h1>
					<img src={baseurl + movie.poster_path} alt={movie.movieTitle} className="h-[300px] w-[200px]" />
				</div>

				<div className='grid grid-cols-1 gap-4'>
					<h2 className="text-xl font-bold">Related Movies</h2>
					<MovieSlider movies={relatedMovies} />
				</div>
			</div>
		</div>
	);
};

export default MovieDetails;