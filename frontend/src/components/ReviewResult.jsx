function ReviewResult({ result }) {
  if (!result) {
    return null;
  }

  return (
    <div
      style={{
        background: "white",
        padding: "16px",
        borderRadius: "6px",
        marginTop: "20px",
      }}
    >
      <h2>AI Review Result</h2>

      <p>
        <strong>Recommendation:</strong>{" "}
        <span
          style={{
            color:
              result.recommendation === "SAFE TO MERGE" ? "green" : "red",
          }}
        >
          {result.recommendation}
        </span>
      </p>

      <h3>Issues Found</h3>

      {result.issues.length === 0 ? (
        <p>No issues detected 🎉</p>
      ) : (
        <ul>
          {result.issues.map((issue, index) => (
            <li key={index}>{issue}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ReviewResult;

