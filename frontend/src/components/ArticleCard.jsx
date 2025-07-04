// components/ArticleCard.jsx
import '../styles/ArticleCard.css';

const SUPABASE_IMAGE_BASE = "https://apjsodlrgldcwebdghuy.supabase.co/storage/v1/object/public/";


function ArticleCard({ article }) {
    console.log(SUPABASE_IMAGE_BASE + article.cover_image.replace(/^\/?media\//, ''));

  return (
    <div className="article-card">

      <img
        src={SUPABASE_IMAGE_BASE + article.cover_image}
        alt={article.title}
        className="cover-image"
      />
      <h2>{article.title}</h2>
    </div>
  );
}
export default ArticleCard;
