import React from 'react';
import { Link } from 'react-router-dom';


const Nav = () => {
	return (
		<nav className="fixed bg-opacity-30 p-4 bg-slate-950 backdrop-blur-xl z-50 w-full border-b-[1px] border-b-slate-800">
			<div className="max-w-screen-lg mx-auto flex">
				<Link to="/" className="">Home</Link>
			</div>
		</nav>
	);
};

export default Nav;