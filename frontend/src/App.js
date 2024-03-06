import './App.css';
import React, { useEffect, useState } from 'react';
import { Route, Routes, useLocation } from 'react-router-dom';

import Home from './pages/Home';

import Nav from './components/Nav';
import Footer from './components/Footer';


function App() {
	const location = useLocation();

	return (
		<div className="App text-slate-50 bg-slate-950 min-w-fit">
			<Nav />

			<div className='max-w-screen-lg mx-auto pt-24'>
				<Routes location={location}>
					<Route key={location.pathname} path='/' element={<Home />} />
				</Routes>
			</div>

			<Footer />
		</div>
	);
}

export default App;
