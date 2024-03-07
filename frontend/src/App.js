import './App.css';
import React, { useEffect, useState } from 'react';
import { Route, Routes, useLocation } from 'react-router-dom';

import Home from './pages/Home';
import MovieDetails from './pages/MovieDetails';

import Nav from './components/Nav';
import Footer from './components/Footer';


function App() {
	const location = useLocation();
	const [isloggedIn, setIsLoggedIn] = useState(localStorage.getItem('isloggedIn') || false);
	const [user, setUser] = useState(JSON.parse(localStorage.getItem('user')));

	return (
		<div className="App text-slate-50 bg-slate-950 min-w-fit">
			<Nav user={user} setUser={setUser} isloggedIn={isloggedIn} setIsLoggedIn={setIsLoggedIn} />

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
