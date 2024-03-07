import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';


const Nav = ({ user, setUser, isloggedIn, setIsLoggedIn }) => {
	const [isOpen, setIsOpen] = useState(false);
	const location = useLocation();

	const fetchUser = async (userId) => {
		try {
			const response = await fetch(`http://localhost:8000/v1/user/${userId}`);
			const data = await response.json();

			if (response.ok) {
				setUser(data);
				setIsLoggedIn(true);

				localStorage.setItem('user', JSON.stringify(data));
				localStorage.setItem('isloggedIn', true);

				console.log('user:', data);
			} else {
				console.error('Error fetching user:', data);
				alert('User not found');
			}
		} catch (error) {
			console.error('Error fetching user:', error);
		}
	};

	const loginhandler = (userId) => {
		if (isloggedIn) {
			setUser(null);
			setIsLoggedIn(false);

			localStorage.removeItem('user');
			localStorage.removeItem('isloggedIn');
		} else if (userId > 0) {
			fetchUser(userId);
		}
		else {
			alert('Please enter a valid User ID');
		}
	};

	return (
		<nav className="fixed bg-opacity-30 p-4 bg-slate-950 backdrop-blur-xl z-50 w-full border-b-[1px] border-b-slate-800">
			<div className="max-w-screen-lg mx-auto flex justify-between">
				<Link to="/" className="flex gap-1 hover:text-slate-300">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
						<path strokeLinecap="round" strokeLinejoin="round" d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75C20.25 16.153 16.556 18 12 18s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125" />
					</svg>
					<span className="font-bold">
						DBRS
					</span>
				</Link>

				<div className={`flex flex-col overflow-hidden`}>
					<button
						className={`group transition ease-in-out self-end`}
						onClick={() => setIsOpen(!isOpen)}
					>
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className={`group-hover:text-slate-300 w-6 h-6`}>
							<path
								key={isOpen ? "open" : "closed"}
								strokeLinecap="round" strokeLinejoin="round"
								d={isOpen ?
									"M3.75 6.75h16.5M3.75 12h16.5M12 17.25h8.25" :
									"M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"}
							/>
						</svg>
					</button>

					<div className={`${isOpen ? "h-[40px] pt-2" : "h-0"} gap-[1px] transition-all flex`}>
						<input
							id='selectUser'
							type="text"
							placeholder={isloggedIn ? user.userId : "Enter User ID"}
							className={`bg-slate-500 text-slate-50 rounded-s-full transition-all px-4 w-32 ${isloggedIn ? 'pointer-events-none opacity-50' : ''}`}
							disabled={isloggedIn ? true : false}
						/>
						<button
							onClick={() => loginhandler(document.querySelector('#selectUser').value)}
							className={`bg-slate-500 text-slate-50 px-4 rounded-e-full transition-all ${isloggedIn ? '' : ''}`}
						>
							{isloggedIn ? "Logout" : "Login"}
						</button>
					</div>
				</div>
			</div>
		</nav >
	);
};

export default Nav;