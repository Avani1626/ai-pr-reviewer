import { useState } from "react";
import { reviewPR } from "../services/api";

function PRForm({ onResult }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [code, setCode] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);

    const result = await reviewPR({
      title,
      description,
      code,
    });

    onResult(result);
    setLoading(false);
  };

  return (
    <div style={{ background: "white", padding: "16px", borderRadius: "6px" }}>
      <h2>Enter Pull Request Details</h2>

      <input
        placeholder="Pull Request Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <textarea
        placeholder="Pull Request Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        rows="4"
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <textarea
        placeholder="Code Changes"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        rows="6"
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Reviewing..." : "Review Pull Request"}
      </button>
    </div>
  );
}

export default PRForm;
