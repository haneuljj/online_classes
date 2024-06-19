import { useState, useEffect } from "react";

function App() {
  const [count, setValue] = useState(0);
  const [keyword, setKeyword] = useState("");

  const onClick = () => setValue((prev) => prev + 1)
  const onChange = (event) => setKeyword(event.target.value);

  // state가 변해도 처음에 한번만 실행됨
  useEffect(() => {
    console.log("i run only once.")
  }, []);
  // keyword가 변하면 앞의 함수 실행
  useEffect(() => {
    console.log("i run when 'keyword' changes.")
  }, [keyword]);
  useEffect(() => {
    console.log("i run when 'count' changes.")
  }, [count]);
  useEffect(() => {
    console.log("i run when 'keyword' & 'count' changes.")
  }, [keyword, count]);

  return (
    <div>
      <input type="text" placeholder="Search herer..." value={keyword} onChange={onChange} />
      <h1>{count}</h1>
      <button onClick={onClick}>Click me</button>
    </div>
  );
}

export default App;
