import { useState } from "react";
import PRForm from "./components/PRForm";
import ReviewResult from "./components/ReviewResult";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ maxWidth: "800px", margin: "40px auto" }}>
      <h1>AI Pull Request Reviewer</h1>

      <PRForm onResult={setResult} />

      <ReviewResult result={result} />
    </div>
  );
}

export default App;
