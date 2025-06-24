import { useEffect, useState } from "react";

function Article() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/article/')
      .then((res) => res.json())
      .then((json) => setArticles(json))
      .catch((err) => console.error("Fetch error:", err));
    console.log(articles)
  }, []);
  return (
    <div>
      <h1>This is article page</h1>
      <ul>
        {articles.map((each) => (
          <li key={each.title}>{each.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default Article;
