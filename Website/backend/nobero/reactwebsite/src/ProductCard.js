// src/ProductCard.js
import React from 'react';
import './ProductCard.css';

const ProductCard = ({ product }) => {
  return (
    <div className="product-card">
      
      <a href ={product.url}><h2>{product.title}</h2> </a>
      <p>Category: {product.category}</p>
      <p>Price: ₹{product.price}</p>
      <p>MRP: ₹{product.MRP}</p>
      {product.last_7_day_sale && <p>Last 7 Days Sale: ₹{product.last_7_day_sale}</p>}
      <p>Fit: {product.fit}</p>
      <p>Fabric: {product.fabric}</p>
      <p>Neck: {product.neck}</p>
      <p>Sleeve: {product.sleeve}</p>
      <p>Pattern: {product.pattern}</p>
      <p>Length: {product.length}</p>
      <p>Description: {product.description}</p>
    </div>
  );
};

export default ProductCard;
