import { useEffect, useState } from "react";
import ArticleCard from "../components/ArticleCard";

function Article() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [next, setNext] = useState(null);
  const [prev, setPrev] = useState(null);
  const [url, setUrl] = useState('http://127.0.0.1:8000/article/');

  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then((res) => res.json())
      .then((json) => {
        setArticles(json.results || json); // support both paginated and non-paginated
        setNext(json.next);
        setPrev(json.previous);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Fetch error:", err);
        setLoading(false);
      });
  }, [url]);

  return (
    <div>
      <h1>This is article page</h1>

      {loading ? (
        <p>Loading articles...</p>
      ) : (
        <>
          {articles.map((article) => (
            <ArticleCard key={article.id} article={article} />
          ))}

          <div style={{ display: 'flex', justifyContent: 'center', gap: '10px', marginTop: '20px' }}>
            {prev && <button onClick={() => setUrl(prev)}>Previous</button>}
            {next && <button onClick={() => setUrl(next)}>Next</button>}
          </div>
        </>
      )}
    </div>
  );
}

export default Article;
