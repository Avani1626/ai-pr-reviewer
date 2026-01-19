import { useState } from "react";

function App() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [diff, setDiff] = useState("");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const submitForReview = async () => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8001/review", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: title,
          description: description,
          diff: diff,
        }),
      });

      if (!response.ok) {
        throw new Error("Review failed");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError("Error while reviewing PR");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "800px" }}>
      <h2>AI PR Reviewer</h2>

      <input
        type="text"
        placeholder="PR Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <textarea
        placeholder="PR Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        rows={4}
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <textarea
        placeholder="Code Changes (Diff)"
        value={diff}
        onChange={(e) => setDiff(e.target.value)}
        rows={8}
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <button onClick={submitForReview} disabled={loading}>
        {loading ? "Reviewing..." : "Review PR"}
      </button>

      {error && (
        <p style={{ color: "red", marginTop: "10px" }}>{error}</p>
      )}

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>AI Review Result</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
