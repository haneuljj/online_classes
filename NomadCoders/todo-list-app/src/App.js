import { useState } from "react";

function App() {
  const [toDo, setTodo] = useState("");
  const [toDos, setTodos] = useState([]);

  const onChange = (event) => setTodo(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault();
    
    if(toDo === "") {
      return;
    }
    
    setTodos((currentArray) => [toDo, ...currentArray]); // 현재 배열에 입력된 투두 내용 합치기
    setTodo("");
  } 
  
  // 단순히 부모 태그를 없애는 게 아니라 toDos 배열에서 삭제하는 방법 -> filter함수 사용
  // toDos의 인덱스값이 전달받은 인덱스값과 같이 않을 경우에는 삭제 안됨
  const deleteBtn = index => {
    setTodos(toDos.filter((item, todoIndex) => index !== todoIndex));
  }
  
  console.log(toDos);

  return (
    <div>
      <h1>My To Dos ({toDos.length})</h1>
      <form onSubmit={onSubmit}>
        <input value={toDo} onChange={onChange} type="text" placeholder="Write your todo ... " />
        <button>ADD TODO</button>
      </form>

      <hr />

      <ul>
        {toDos.map((item, index) => (
          <li key={index}>
            {item}
            <button onClick={() => deleteBtn(index)}>Delete</button> {/**익명함수로 바로 실행되지 않고 클릭 기다리도록 */}
            </li>
      ))}
      </ul>
    </div>
  );
}

export default App;
