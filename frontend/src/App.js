import './App.css';
import React, { useEffect, useState } from 'react';
import { Route, Routes, useLocation } from 'react-router-dom';

import Home from './pages/Home';
import MovieDetails from './pages/MovieDetails';

import Nav from './components/Nav';
import Footer from './components/Footer';


function App() {
	const location = useLocation();
	const [userId, setUserId] = useState(null);
	const [user, setUser] = useState(null);

	useEffect(() => {
		const fetchUser = async () => {
			try {
				const response = await fetch(`http://localhost:8000/v1/user/${userId}`);
				const data = await response.json();
				setUser(data);
				console.log('user:', data);
			} catch (error) {
				console.error('Error fetching user:', error);
			}
		};

		fetchUser();
	}, [userId]);

	return (
		<div className="App text-slate-50 bg-slate-950 min-w-fit">
			<Nav user={userId} setUser={setUserId} />

			<div className='mx-auto'>
				<Routes location={location}>
					<Route key={location.pathname} path='/' element={<Home user={user} />} />
					<Route key={location.pathname} path='/movie/:id' element={<MovieDetails movieId={location.pathname.split('/')[2]} />} />
				</Routes>
			</div>

			<Footer />
		</div>
	);
}

export default App;
