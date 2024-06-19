import { useEffect, useState } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]); // default value : [] => undefined 방지
  const [budget, setBudget] = useState(0);
  const [price, setPrice] = useState(0);
  const [symbol, setSymbol] = useState("");
  const [selected, setSelected] = useState(false);

  const onChangeBudget = (evenet) => setBudget(evenet.target.value);

  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
    .then((response) => response.json())
    .then((json) => {
        setCoins(json);
        setLoading(false);
    });
  }, []);

  const onChangeCoin = (event) => {
    setPrice(coins[event.target.value].quotes.USD.price);
    setSymbol(coins[event.target.value].symbol);
    setSelected(true);
  }

  return (
    <div>
      <h1>The Coins! {loading ? "" : `(${coins.length})` }</h1>
  
      {loading ? (
        <strong>Loading...</strong>
      ) : (
        <div>
          <input 
            type="number"
            placeholder="Type your budget .."
            value={budget}
            onChange={onChangeBudget}
          /> $
          <br />

          <select onChange={onChangeCoin}>
            {coins.map((coin, index) => (
              <option key={coin.id} value={index}>{coin.name} ({coin.symbol}) : ${coin.quotes.USD.price} USD</option>
            ))}
          </select>
          <button>Calculate</button>

          <br />
          {selected ? <strong>You can buy {budget / price} ({symbol})</strong> : null}
        </div>
      )}
    </div>

    
  );
}

export default App;
