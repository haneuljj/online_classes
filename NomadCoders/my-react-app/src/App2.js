import { useState, useEffect } from "react";

function Hello(){
    useEffect(() => {
        console.log("hi :)");
        return () => console.log("bye :(");
    }, []);
    // useEffect(() => {
        
    //     return () => console.log("destroyed :(");  // 컴포넌트가 사라질 때 코드 실행 
    // }, []);
    return <h1>Hello</h1>;
}

function App2() {
    const [showing, setShowing] = useState(false);
    const onClick = () => setShowing((prev) => !prev);

    return (
        <div>
            {showing ? <Hello /> : null}
            <button onClick={onClick}>{showing ? "Hide" : "Show"}</button>
        </div>
    );
}

export default App2;