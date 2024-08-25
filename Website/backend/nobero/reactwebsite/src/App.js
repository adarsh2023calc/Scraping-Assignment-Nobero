import React, { useEffect, useState } from 'react';
import './App.css';
import ProductCard from './ProductCard';
import 'react-bootstrap'

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/products/')
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  return (
    <div className="App">
      
      <h1>Nobero Website</h1>
      <nav class="navbar-nav mr-auto mt-2 mt-lg-0">
        <li class="nav-item">Men</li>
        <li class="nav-item" >Women</li>
      </nav>
      <div className="product-container">
        {products.map((product, index) => (
          <ProductCard key={index} product={product} />
        ))}
      </div>
    </div>
  );
}

export default App;
