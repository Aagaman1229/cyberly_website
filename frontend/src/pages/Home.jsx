import intro from '../assets/bg_transparent.png';
import '../styles/Home.css';

function Home(){
    return (
        <div className="home-container">
            <img src={intro} alt="Intro" className="intro-image" />
            <h1>Welcome to the Home Page</h1>
            <p>This is the home page of our application.</p>
            <p>Feel free to explore the articles, researches, and about sections.</p>
        </div>

    )
}
export default Home