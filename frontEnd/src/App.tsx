import { useState, useEffect } from 'react';
import axios from 'axios';

// 백엔드 배포 주소 (아까 성공한 그 주소!)
const API_URL = "https://deployment-testing-phase.onrender.com";

function App() {
  const [users, setUsers] = useState<{name: string, email: string}[]>([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  // 1. 데이터 가져오기 (GET)
  const fetchUsers = async () => {
    try {
      const response = await axios.get(`${API_URL}/users`);
      setUsers(response.data);
    } catch (error) {
      console.error("데이터 로딩 실패:", error);
    }
  };

  // 2. 데이터 넣기 (POST)
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post(`${API_URL}/users`, { name, email });
      alert("등록되었습니다!");
      setName(""); setEmail("");
      fetchUsers(); // 목록 새로고침
    } catch (error) {
      alert("등록 실패!");
    }
  };

  useEffect(() => { fetchUsers(); }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Semicolon 팀 테스트</h1>
      
      {/* 데이터 입력 폼 */}
      <form onSubmit={handleSubmit}>
        <input value={name} onChange={e => setName(e.target.value)} placeholder="이름" />
        <input value={email} onChange={e => setEmail(e.target.value)} placeholder="이메일" />
        <button type="submit">등록하기</button>
      </form>

      <hr />

      {/* 데이터 출력 목록 */}
      <h3>등록된 유저 목록</h3>
      <ul>
        {users.map((user, idx) => (
          <li key={idx}>{user.name} ({user.email})</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
