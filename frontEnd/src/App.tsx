import { useEffect, useState } from "react";

type User = {
  id: number;
  name: string;
};

function App() {
  const [users, setUsers] = useState<User[]>([]); //오류 수정: 타입 지정

  useEffect(() => {
    fetch("http://127.0.0.1:8000/users")
      .then(res => res.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div>
      <h1>유저 목록</h1>
      {users.map(u => (
        <div key={u.id}>{u.name}</div>
      ))}
    </div>
  );
}

export default App;
