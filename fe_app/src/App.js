import './App.css';
import React, { useState } from 'react';



function App() {
  const [searchResults, setSearchResults] = useState([]);
  function searchProducts() {
    fetch('https://search-engine.onrender.com/search_products?search_sentence=' + document.getElementById('searchTerm').value)
    .then(response => response.json())
    .then(data => setSearchResults(data['data']))
  }

  function renderSearchResults() {
    return searchResults.map((product) => {
      var product = JSON.parse(product)
        return <div class="productCard">
            <p>Title: {product['product_title']}</p>
            <p>Description: {product['product_description']}</p>
          </div>
      }
    )
  }

  return (
    <div className="App">
      <div class="wrap">
        <div class="search">
          <input id="searchTerm" type="text" class="searchTerm" placeholder="What are you looking for?"></input>
          <button type="submit" class="searchButton" onClick={searchProducts}> GO </button>
        </div>
      </div>
      <div class="resultsWrap">
        {renderSearchResults()}
      </div>
    </div>
  );
}

export default App;
