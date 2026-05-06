import { useEffect, useState } from "react";

// 유저 타입 정의
type User = {
  id: number;
  name: string;
};

function App() {
  const [users, setUsers] = useState<User[]>([]);
  // 하이드레이션 에러 방지를 위한 마운트 상태 관리
  const [isMounted, setIsMounted] = useState(false);

  // 환경 변수에서 API 주소 가져오기 (없으면 로컬 주소 사용)
  const API_BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

  useEffect(() => {
    setIsMounted(true); // 컴포넌트가 브라우저에 마운트됨을 표시

    // 데이터 페칭
    fetch(`${API_BASE_URL}/users`)
      .then((res) => {
        if (!res.ok) throw new Error("Network response was not ok");
        return res.json();
      })
      .then((data) => setUsers(data))
      .catch((err) => console.error("데이터 로딩 실패:", err));
  }, [API_BASE_URL]);

  // 마운트되기 전(서버 렌더링 시점)에는 아무것도 그리지 않음 (에러 방지 핵심)
  if (!isMounted) {
    return null;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>유저 목록</h1>
      {users.length > 0 ? (
        <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
          {users.map((u) => (
            <div key={u.id} style={{ padding: "10px", border: "1px solid #ccc", borderRadius: "5px" }}>
              <strong>ID: {u.id}</strong> - {u.name}
            </div>
          ))}
        </div>
      ) : (
        <p>사용자 정보를 불러오는 중이거나 데이터가 없습니다.</p>
      )}
    </div>
  );
}

export default App;
