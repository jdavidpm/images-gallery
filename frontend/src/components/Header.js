import React from 'react';
import { Navbar, Container } from 'react-bootstrap';
import { ReactComponent as Logo } from '../images/logo.svg';
const navbarStyle = {
	backgroundColor: 'lightblue'
};

const Header = (props) =>{
	return (<>
				<Navbar style={navbarStyle} /*data-bs-theme="dark"*/>
					<Container> <Logo alt={props.title} style={{ maxWidth: '20rem', maxHeight: '20rm'}}/> </Container>
				</Navbar>
	</>)
};

export default Header;