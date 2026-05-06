import { useEffect, useState } from "react";

type User = {
  id: number;
  name: string;
};

function App() {
  const [users, setUsers] = useState<User[]>([]);
  // 1. 클라이언트 마운트 상태 추가
  const [isMounted, setIsMounted] = useState(false);
  
  const API_BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

  useEffect(() => {
    // 2. 컴포넌트가 마운트되면 true로 변경
    setIsMounted(true);

    fetch(`${API_BASE_URL}/users`)
      .then((res) => res.json())
      .then((data) => setUsers(data))
      .catch((err) => console.error("Fetch error:", err));
  }, []);

  // 3. 마운트되기 전(서버 렌더링 시점)에는 아무것도 렌더링하지 않음
  if (!isMounted) {
    return null; 
  }

  return (
    <div>
      <h1>유저 목록</h1>
      {users.length > 0 ? (
        users.map((u) => <div key={u.id}>{u.name}</div>)
      ) : (
        <p>사용자를 불러오는 중...</p>
      )}
    </div>
  );
}

export default App;
